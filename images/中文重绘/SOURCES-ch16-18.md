# 第16、18章论文配图来源

以下8张中文图参考原论文对应图制作，用于解释模型结构和综述分类。中文标注与必要的排版调整不代表原作者提供了中文版；来源同时在教材相关图页的脚注中列出。

| 中文图 | 作者与论文 | 采用版本、图号与PDF物理页 | 来源 |
| --- | --- | --- | --- |
| `graph-tasks-cn.png` | Khemani et al., *A review of graph neural networks: concepts, architectures, techniques, challenges, datasets, applications, and future directions* | 2024，Figure 16 | [期刊论文](https://doi.org/10.1186/s40537-023-00876-4) |
| `graphsage-cn.png` | Hamilton et al., *Inductive Representation Learning on Large Graphs* | arXiv:1706.02216v4，Figure 1，p.2 | [原论文](https://arxiv.org/abs/1706.02216v4) |
| `gat-cn.png` | Veličković et al., *Graph Attention Networks* | arXiv:1710.10903v3，Figure 1，p.4 | [原论文](https://arxiv.org/abs/1710.10903v3) |
| `clip-cn.png` | Radford et al., *Learning Transferable Visual Models From Natural Language Supervision* | arXiv:2103.00020v1，Figure 1，p.2 | [原论文](https://arxiv.org/abs/2103.00020v1) |
| `blip2-cn.png` | Li et al., *BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models* | arXiv:2301.12597v3，Figure 1，p.1 | [原论文](https://arxiv.org/abs/2301.12597v3) |
| `llava-cn.png` | Liu et al., *Visual Instruction Tuning* | arXiv:2304.08485v2，Figure 1，p.4 | [原论文](https://arxiv.org/abs/2304.08485v2) |
| `alignment-survey-cn.png` | Liang et al., *Foundations & Trends in Multimodal Machine Learning: Principles, Challenges, and Open Questions* | arXiv:2209.03430v2，Figure 9，p.11；期刊版本2024年 | [原论文](https://arxiv.org/abs/2209.03430v2) |
| `fusion-survey-cn.png` | Gaw et al., *Multimodal data fusion for systems improvement: A review* | 2022，Figure 1，p.4 | [期刊论文](https://doi.org/10.1080/24725854.2021.1987593)、[作者公开PDF](https://www.afit.edu/BIOS/publications/Gawetal.2022_MultimodaldatafusionforsystemsimprovementAreview.pdf) |

## 图文对应与解释边界

- GAT原图的 $W$、$\alpha$ 对应正文的 $B$、$\beta$。
- GraphSAGE第三栏展示不同监督设定的训练目标，不表示每次都同时训练两个目标。
- BLIP-2雪花表示冻结；两个训练阶段不同时接入所有模块。
- LLaVA原图的 $Z_v$、$H_v$ 对应正文的 $H_v$、$B_v$；图中连接投影与正文采用的行向量表示对应。
- Liang对齐综述图的三栏是分类示意，不等同于本章讨论的五类工业对应问题；图中“分段与连续扭曲”同时容纳不同类型的对齐对象。
- Gaw融合综述图中的A、B、C泛指不同模态，虚线框说明分开或联合训练的范围，不表示某种融合方式普遍更优。
