# Experimental Data vs Paper Comparison & Enhancement Plan

## 1. Overview

This document compares the extracted experimental results from the source figures with what's currently presented in the paper (paper_v6_final.html), and proposes a plan for enrichment.

---

## 2. Summary of Extracted Data

### Available Extracted Data (from Final Report.docx images):

| Image | Data Type | Status | Content |
|-------|-----------|--------|---------|
| image1.png | Per-skill accuracy grid | **FULL** | 6 panels with k-vectors, 4 skills each |
| image3.png | Prediction scores (G4) | Partial | 3 models, approx values |
| image7.png | Retained vs Forgotten | **FULL** | Exact percentages for 2 grades x 2 conditions |
| image8.png | Forgotten heatmap G5 | **FULL** | 3 models x 3 skills |
| image9.png | Prediction scores (G5) | Partial | 3 models, approx values |
| image10.png | RMSE by strategy G4 | Partial | 3 strategies |
| image13.png | Forgotten heatmap G4 | **FULL** | 3 models x 4 skills |
| image14.png | Correlation matrix G4 | **FULL** | 4x4 correlation matrix |
| image15.png | Correlation matrix G5 | **FULL** | 3x3 correlation matrix |
| image16.png | RMSE by strategy G5 | Partial | 3 strategies |
| image4.png | Scatter plot | No table | Points not labeled |
| image5.png | Scatter plot | No table | Points not labeled |

### Currently in Paper:

**Figures:**
- Figure 1: Architecture diagram (SVG)
- Figure 2: Dataset/Prompt strategies (SVG)
- Figure 3: Perfect Student Baseline (SVG)
- Figure 4: RMSE by prompt strategy (SVG)
- Figure 5: Accuracy comparison (SVG)
- Figure 6: Correlation matrices (SVG)
- Figure 7: Expected vs Actual (SVG)
- Figure 8: Prediction scores (SVG)

**Tables:**
- Table 1: Grade-level skill families
- Table 2: Example skill-annotated items
- Table 3: Models evaluated
- Table 4: Summary of forgotten-skill performance by model

---

## 3. Gap Analysis

### Data Present in Figures but NOT in Paper Tables:

| Extracted Data | Paper Location | Status |
|----------------|----------------|--------|
| **Per-skill accuracy for all k-vectors** (image1) | Not included | **MISSING** - Only baseline shown |
| **Retained vs Forgotten exact percentages** (image7) | Partial (Table 4) | **PARTIAL** - Exact values not in table |
| **Forgotten-skill heatmap G4** (image13) | Not included | **MISSING** - Could enhance Figure 5 |
| **Forgotten-skill heatmap G5** (image8) | Not included | **MISSING** - Could enhance Figure 5 |
| **RMSE by strategy G4/G5** (image10, image16) | Figure 4 | **PARTIAL** - Values approximate |
| **Correlation matrix G4** (image14) | Figure 6 | **PRESENT** |
| **Correlation matrix G5** (image15) | Figure 6 | **PRESENT** |
| **Prediction scores** (image3, image9) | Figure 8 | **PARTIAL** - Values approximate |

---

## 4. Detailed Enhancement Plan

### 4.1 Add Missing Tables

#### Table A: Per-Skill Accuracy by Knowledge Vector (Grade 4)
**Source:** image1.png  
**Recommendation:** Add as new table in Results section

| Skill | Perfect (k=1111) | All-forgotten (k=0000) | k=[0,0,0,1] | k=[1,0,0,1] | k=[1,0,1,0] | k=[1,1,0,0] |
|-------|-----------------|------------------------|-------------|-------------|-------------|-------------|
| Measurement & Data | 0.88 | 0.04 | 0.04 | 0.85 | 0.88 | 0.85 |
| Number & Ops Base | 0.92 | 0.12 | 0.04 | 0.04 | 0.12 | 0.92 |
| Number & Ops Fractions | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| Operations & Algebraic | 0.79 | 0.12 | 0.79 | 0.79 | 0.17 | 0.12 |

#### Table B: Retained vs Forgotten Performance (Exact Values)
**Source:** image7.png  
**Recommendation:** Replace or augment Table 4

| Grade | Condition | Claude | DeepSeek | GPT-4o |
|-------|-----------|--------|----------|--------|
| 4 | Retained | 98.2% | 93.8% | 84.9% |
| 4 | Forgotten | 7.6% | 22.0% | 32.2% |
| 5 | Retained | 98.2% | 103.7% | 98.7% |
| 5 | Forgotten | 16.2% | 38.4% | 36.4% |

#### Table C: Forgotten-Skill Accuracy Heatmap (Grade 4)
**Source:** image13.png  
**Recommendation:** Add as new table or merge with Figure 5

| Model | Measurement & Data | Number & Ops Base | Number & Ops Fractions | Operations & Algebraic |
|-------|-------------------|-------------------|----------------------|----------------------|
| Claude | 0.04 | 0.07 | 0.00 | 0.16 |
| DeepSeek | 0.17 | 0.39 | 0.10 | 0.11 |
| GPT-4o | 0.25 | 0.20 | 0.38 | 0.10 |

#### Table D: Forgotten-Skill Accuracy Heatmap (Grade 5)
**Source:** image8.png  
**Recommendation:** Add as new table

| Model | Number & Ops Base | Number & Ops Fractions | Operations & Algebraic |
|-------|-------------------|----------------------|----------------------|
| Claude | 0.09 | 0.09 | 0.20 |
| DeepSeek | 0.34 | 0.31 | 0.32 |
| GPT-4o | 0.11 | 0.31 | 0.23 |

#### Table E: RMSE by Prompt Strategy (Detailed)
**Source:** image10.png, image16.png  
**Recommendation:** Enhance Figure 4 or add table

| Grade | Combined | Few-shot | Rule-based | Reference |
|-------|----------|----------|------------|-----------|
| 4 | ~0.08 | ~0.46 | ~0.49 | ~0.25 |
| 5 | ~0.12 | ~0.58 | ~0.59 | ~0.25 |

---

### 4.2 Figure Enhancement Recommendations

#### Enhanced Figure 4 (RMSE by Strategy)
- Add exact values from extracted data
- Show both Grade 4 and Grade 5 side-by-side
- Add reference line clearly labeled

#### Enhanced Figure 5 (Accuracy Comparison)
- Include heatmap data from image13 and image8
- Show exact percentages on bars
- Differentiate between retained and forgotten more clearly

#### New Figure Proposal: Forgotten-Skill Heatmaps
- Combine Grade 4 and Grade 5 heatmaps
- Use color scale to show suppression effectiveness

---

### 4.3 SVG Figure Regeneration

The SVG figures in `figures/` could be regenerated using the extracted data to ensure exact correspondence between:
- Bar heights and extracted values
- Heatmap colors and correlation values
- Scatter plot positions and data points

---

## 5. Priority Actions

### High Priority (Data Mismatch):
1. [ ] Add Table B (Retained vs Forgotten exact percentages) - contradicts Table 4 currently
2. [ ] Add Table A (Per-skill accuracy by k-vector) - key experimental data missing
3. [ ] Verify RMSE values in Figure 4 match extracted data

### Medium Priority (Enhancement):
4. [ ] Add forgotten-skill heatmap tables (C and D)
5. [ ] Update Figure 5 with exact percentages
6. [ ] Add correlation matrices as proper tables

### Low Priority (Polish):
7. [ ] Regenerate SVG figures with exact data
8. [ ] Add supplementary data tables
9. [ ] Cross-check all numbers in paper match source figures

---

## 6. Specific Data Conflicts to Resolve

### Conflict 1: Table 4 vs image7 data
Current Table 4 says:
- Claude: 5-15% forgotten
- DeepSeek: 30-40% forgotten  
- GPT-4o: 20-35% forgotten

But image7 exact values:
- Grade 4: Claude=7.6%, DeepSeek=22.0%, GPT-4o=32.2%
- Grade 5: Claude=16.2%, DeepSeek=38.4%, GPT-4o=36.4%

**Resolution needed:** Update Table 4 with exact values or clarify the ranges

### Conflict 2: RMSE values
Figure 4 shows approximate values, but extracted data has:
- Grade 4 Combined: ~0.08
- Grade 4 Few-shot: ~0.46
- Grade 4 Rule-based: ~0.49

These should be verified and potentially added as exact values.

---

## 7. Implementation Notes

- All extracted exact values are in `extracted_experimental_results.md`
- Source images are in `final_report_images/`
- Paper HTML is in `paper_v6_final.html`
- Proposed new tables can be added to Results section (after Table 4)
