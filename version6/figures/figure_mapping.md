# Figure Mapping

## Overview
This document maps each extracted figure from Final Report.docx to its corresponding paper section based on the original paper structure.

---

## Methodology Figures (from Section 5)

### Figure 01: Controllable Generative Student Architecture
- **Filename:** figure_01.png
- **Description:** Pipeline diagram showing the architecture for controllable student behavior generation. Binary skill vector k = {1,0,...,1} transforms into structured student profile prompt that conditions the LLM to produce responses aligned with intended skill retention/forgetting patterns.
- **Type:** Architecture Diagram / Pipeline
- **Paper Section:** 5.1 Generative Student Definition
- **Caption:** "Figure 1. Controllable Generative Student Architecture."

### Figure 02: Main Experiment Pipeline
- **Filename:** figure_02.png
- **Description:** Full experimental workflow showing multiple simulated students defined by different skill vectors, answering skill-tagged questions via multiple LLMs, with answers aggregated and analyzed for controllability evaluation.
- **Type:** Flowchart / Workflow Diagram
- **Paper Section:** 5.4 Experimental Protocol
- **Caption:** "Figure 2. Main Experiment Pipeline."

---

## Results Figures (from Section 7)

### Figure 03: Prompting Strategy Comparison (RMSE)
- **Filename:** figure_03.png
- **Description:** Bar chart comparing RMSE values across prompting strategies (Combined vs Few-Shot vs Rule-Based) for Grades 4 and 5. Shows combined strategy achieving RMSE ~0.08-0.12 vs ~0.45-0.60 for others.
- **Type:** Bar Chart
- **Paper Section:** 7.1 Prompt Strategy Comparison
- **Caption:** "Figure showing RMSE comparison between prompting strategies."

### Figure 04: Retained vs. Forgotten Skills Comparison
- **Filename:** figure_04.png
- **Description:** Grouped bar chart comparing accuracy between imperfect students (IS) and perfect students (PS) across retained and forgotten skills, aggregated over models and grades. Percentage values show relative accuracy (IS/PS).
- **Type:** Grouped Bar Chart
- **Paper Section:** 7.3 Retained vs. Forgotten
- **Caption:** "This figure compares accuracy between imperfect students (IS) and perfect students (PS) across retained and forgotten skills."

### Figure 05: Correlation Matrix - Grade 4
- **Filename:** figure_05.png
- **Description:** Pearson correlation matrix between skills for Grade 4, computed over simulated students using per-skill accuracy vectors. Values near zero (~-0.1) indicate independence between skills.
- **Type:** Correlation Matrix Heatmap
- **Paper Section:** 7.4 Skill Correlation Analysis
- **Caption:** "Pearson correlation matrices between skills for Grades 4 and 5."

### Figure 06: Correlation Matrix - Grade 5
- **Filename:** figure_06.png
- **Description:** Pearson correlation matrix between skills for Grade 5. Shows slightly stronger negative correlations (~-0.1 to -0.24) indicating weak interference effects.
- **Type:** Correlation Matrix Heatmap
- **Paper Section:** 7.4 Skill Correlation Analysis
- **Caption:** "Correlation matrices between skills for Grades 4 and 5."

### Figure 07: Expected vs. Actual Accuracy - Grade 4
- **Filename:** figure_07.png
- **Description:** Scatter plot comparing expected retained-skill accuracy (derived from correlation analysis) with actual accuracy measured from LLM outputs for Grade 4. Diagonal = perfect agreement.
- **Type:** Scatter Plot
- **Paper Section:** 7.5 Expected vs. Actual Accuracy
- **Caption:** "Figure compares expected retained-skill accuracy with actual accuracy across simulated students for Grades 4 and 5."

### Figure 08: Expected vs. Actual Accuracy - Grade 5
- **Filename:** figure_08.png
- **Description:** Scatter plot for Grade 5 showing differences between models. Claude and DeepSeek cluster near diagonal; GPT-4o deviates below diagonal.
- **Type:** Scatter Plot
- **Paper Section:** 7.5 Expected vs. Actual Accuracy
- **Caption:** "Diagonal represents perfect agreement. Points close to diagonal indicate accurate preservation of retained skills."

### Figure 09: Per-Skill Accuracy Grid - Combined View
- **Filename:** figure_09.png
- **Description:** Grid view of per-skill accuracy showing how well models adhere to imposed student profiles at individual skill level. Demonstrates near-zero accuracy on forgotten skills and high accuracy on retained skills.
- **Type:** Heatmap / Grid
- **Paper Section:** 7.2 Per-Skill Behavior
- **Caption:** "Per-skill accuracy grids provide detailed view of model adherence to student profile."

### Figure 10: Prediction Score Comparison
- **Filename:** figure_10.png
- **Description:** Bar chart presenting mean prediction score (actual minus expected retained-skill accuracy) for each model, aggregated over simulated students, with error bars indicating variance.
- **Type:** Bar Chart with Error Bars
- **Paper Section:** 7.6 Prediction Score
- **Caption:** "Mean prediction score for each model, aggregated over simulated students, with error bars indicating variance."

### Figure 11: Forgotten Skill Heatmap - Grade 4
- **Filename:** figure_11.png
- **Description:** Heatmap of imperfect-student (IS) accuracy on forgotten skills (K=0) across models and skill domains for Grade 4. Lower values = more effective forgetting. Shows Claude consistently achieves low accuracy.
- **Type:** Heatmap
- **Paper Section:** 7.7 Forgotten Skill Heatmaps
- **Caption:** "Heatmaps of imperfect-student (IS) accuracy on forgotten skills (K=0) across models and skill domains."

### Figure 12: Forgotten Skill Heatmap - Grade 5
- **Filename:** figure_12.png
- **Description:** Heatmap for Grade 5 showing model behavior on forgotten skills. Claude: 0.09-0.20, DeepSeek: 0.31-0.34, GPT-4o: variable (0.10-0.38).
- **Type:** Heatmap
- **Paper Section:** 7.7 Forgotten Skill Heatmaps
- **Caption:** "Each cell represents accuracy of a model on a specific skill when designated as forgotten."

### Figure 13: Per-Skill Controllability Grid - Extended
- **Filename:** figure_13.png
- **Description:** Extended view of per-skill controllability showing accuracy distribution across different student configurations and skill domains.
- **Type:** Heatmap / Grid
- **Paper Section:** 7.2 Per-Skill Behavior
- **Caption:** "Per-skill accuracy showing fine-grained control analysis."

### Figure 14: Model Comparison Summary
- **Filename:** figure_14.png
- **Description:** Summary comparison across models showing controllability metrics, forgotten skill accuracy, and retained skill accuracy for all three models.
- **Type:** Multi-panel Comparison
- **Paper Section:** 7.8 Key Empirical Findings
- **Caption:** "Model comparison showing controllability differences."

### Figure 15: Key Findings Dashboard
- **Filename:** figure_15.png
- **Description:** Summary dashboard with key empirical findings: (1) Selective forgetting achievable, (2) Retention stable under skill removal, (3) Skills mostly independent, (4) Model architecture affects controllability, (5) Claude most reliable.
- **Type:** Summary Dashboard
- **Paper Section:** 7.8 Key Empirical Findings
- **Caption:** "Key Empirical Findings summary."

---

## Summary Table

| Figure # | Filename | Type | Section |
|----------|----------|------|---------|
| 1 | figure_01.png | Architecture Diagram | 5.1 |
| 2 | figure_02.png | Flowchart | 5.4 |
| 3 | figure_03.png | Bar Chart (RMSE) | 7.1 |
| 4 | figure_04.png | Grouped Bar Chart | 7.3 |
| 5 | figure_05.png | Correlation Matrix | 7.4 |
| 6 | figure_06.png | Correlation Matrix | 7.4 |
| 7 | figure_07.png | Scatter Plot | 7.5 |
| 8 | figure_08.png | Scatter Plot | 7.5 |
| 9 | figure_09.png | Heatmap/Grid | 7.2 |
| 10 | figure_10.png | Bar Chart + Error Bars | 7.6 |
| 11 | figure_11.png | Heatmap | 7.7 |
| 12 | figure_12.png | Heatmap | 7.7 |
| 13 | figure_13.png | Heatmap/Grid | 7.2 |
| 14 | figure_14.png | Multi-panel | 7.8 |
| 15 | figure_15.png | Dashboard | 7.8 |

---

## Figure Count by Type

| Type | Count |
|------|-------|
| Architecture/Flowchart | 2 |
| Bar Chart | 2 |
| Scatter Plot | 2 |
| Correlation Matrix | 2 |
| Heatmap | 4 |
| Grid/Multi-panel | 2 |
| Dashboard | 1 |
| **Total** | **15** |
