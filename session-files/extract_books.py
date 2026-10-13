"""Extract local reference books as UTF-8 text with PDF page markers."""

import argparse
import importlib
import json
from pathlib import Path


BOOKS = (
    ("机器学习：贝叶斯和优化方法（英文文字）.pdf", "machine-learning-book"),
    ("mml-book.pdf", "mml-book"),
)


def select_backend():
    for module_name in ("pymupdf", "pypdf"):
        try:
            return module_name, importlib.import_module(module_name)
        except ModuleNotFoundError as exc:
            if exc.name != module_name:
                raise
    raise SystemExit(
        "Missing PDF reader. Install PyMuPDF with the same interpreter:\n"
        "python -m pip install pymupdf"
    )


def read_pages(source, backend_name, backend):
    if backend_name == "pymupdf":
        with backend.open(str(source)) as document:
            if document.needs_pass:
                raise ValueError(f"Password required: {source.name}")
            for page in document:
                yield page.get_text("text", sort=True)
    else:
        with source.open("rb") as stream:
            reader = backend.PdfReader(stream)
            if reader.is_encrypted and not reader.decrypt(""):
                raise ValueError(f"Password required: {source.name}")
            for page in reader.pages:
                yield page.extract_text() or ""


def extract_book(source, stem, output_dir, backend_name, backend):
    text_path = output_dir / f"{stem}.txt"
    pages_path = output_dir / f"{stem}.pages.jsonl"
    page_count = 0
    character_count = 0
    low_text_pages = []
    with text_path.open("w", encoding="utf-8", newline="\n") as text_file, \
            pages_path.open("w", encoding="utf-8", newline="\n") as pages_file:
        for page_count, text in enumerate(
            read_pages(source, backend_name, backend), start=1
        ):
            text = text.replace("\r\n", "\n").replace("\r", "\n")
            character_count += len(text)
            if len(text.strip()) < 40:
                low_text_pages.append(page_count)
            text_file.write(f"\n===== PDF PAGE {page_count} =====\n\n{text}\n")
            pages_file.write(json.dumps(
                {"pdf_page": page_count, "text": text}, ensure_ascii=False
            ) + "\n")
            if page_count % 100 == 0:
                print(f"{source.name}: {page_count} pages", flush=True)
    if page_count == 0 or character_count == 0:
        raise ValueError(f"No text extracted from {source.name}; OCR may be required.")
    return {
        "source": str(source),
        "backend": backend_name,
        "text_file": str(text_path),
        "pages_file": str(pages_path),
        "page_count": page_count,
        "character_count": character_count,
        "low_text_pdf_pages": low_text_pages,
        "note": "PDF page numbers are 1-based, not printed book page numbers. "
                "Math symbols and reading order require checking against the PDF. "
                "Low-text pages may be blank, figures, or scans; no OCR was performed.",
    }


def main():
    project_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=project_root)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output_dir = (args.output or root / "session-files" / "book-text").resolve()
    for filename, _ in BOOKS:
        if not (root / filename).is_file():
            parser.error(f"Missing source: {root / filename}")
    if output_dir.exists():
        parser.error(f"Output directory already exists; choose a new --output: {output_dir}")
    backend_name, backend = select_backend()
    output_dir.mkdir(parents=True)
    summaries = []
    try:
        for filename, stem in BOOKS:
            summary = extract_book(root / filename, stem, output_dir, backend_name, backend)
            summaries.append(summary)
            print(f"{filename}: {summary['page_count']} pages, "
                  f"{summary['character_count']} characters, "
                  f"{len(summary['low_text_pdf_pages'])} low-text pages", flush=True)
        (output_dir / "manifest.json").write_text(
            json.dumps(summaries, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    except Exception:
        for filename in ("machine-learning-book.txt", "machine-learning-book.pages.jsonl",
                         "mml-book.txt", "mml-book.pages.jsonl", "manifest.json"):
            (output_dir / filename).unlink(missing_ok=True)
        output_dir.rmdir()
        raise
    print(f"Completed: {output_dir}")


if __name__ == "__main__":
    main()
