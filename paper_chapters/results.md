# 6. Experimental Results

This chapter presents the experimental findings from our evaluation of controllable skill forgetting across multiple frontier language models. The results are organized into seven subsections, progressing from prompting strategy comparisons to fine-grained skill-level analyses.

---

## 6.1 Prompting Strategy Comparison

### Research Question
How effective are different prompting strategies at enforcing skill-level behavioral control?

### Methodology
We measured Root Mean Squared Error (RMSE) between the intended binary skill vector and observed per-skill accuracy. Lower RMSE indicates better alignment with the desired student profile.

### Key Finding: Combined Strategy Dominance

| Prompting Strategy | RMSE Range | Performance |
|-------------------|------------|-------------|
| **Combined (Rules + Few-Shot)** | 0.08 - 0.12 | Excellent |
| Few-Shot Only | 0.45 - 0.60 | Poor |
| Rule-Based Only | 0.50 - 0.60 | Poor |

### Interpretation
The combined prompting strategy significantly outperforms both individual approaches across both Grade 4 and Grade 5 datasets. This synergy occurs because:
- **Rules** explicitly define desired behavior
- **Examples** demonstrate how behavior manifests in practice
- Together, they enable better internalization of skill constraints

### Implications
- Neither explicit instructions nor examples alone are sufficient
- Prompt design is a necessary but not sufficient condition for controllability
- All subsequent experiments use the combined prompting strategy

---

## 6.2 Per-Skill Accuracy Analysis

### Fine-Grained Behavioral Adherence

The per-skill accuracy grids reveal how well models adhere to imposed student profiles at the individual skill level.

### Quantitative Results

| Condition | Accuracy Range | Interpretation |
|-----------|----------------|----------------|
| Forgotten Skills (K=0) | ~0.03 - 0.09 | Near-complete suppression (best cases) |
| Retained Skills (K=1) | ~0.85 - 0.94 | High preservation |

### Key Observations

1. **Clear Separation**: Strong models demonstrate near-zero accuracy on forgotten skills while maintaining high accuracy on retained skills

2. **Skill-Dependent Variability**: Controllability is not uniform across skills:
   - Certain skills are easier to suppress
   - Residual performance observed on some "forgotten" skills
   - Variation likely stems from task difficulty and pretraining biases

3. **Continuous Relaxation**: The accuracy vector approximates a continuous relaxation of the binary skill profile:
   - Skills marked as 1 (mastered) → high accuracy values
   - Skills marked as 0 (forgotten) → low accuracy values

### Figure Description: Per-Skill Accuracy Heatmaps
*(For inclusion: heatmaps showing per-skill accuracy across models and skill domains for Grades 4 and 5)*

- Rows: Different models (Claude, DeepSeek, GPT-4o)
- Columns: Skill domains
- Color intensity: Accuracy level
- Lower values (darker) indicate effective forgetting

---

## 6.3 Retained vs. Forgotten Skills Comparison

### Research Question
Do models exhibit differential behavior between retained and forgotten skills, and how does this vary across model architectures?

### Quantitative Results

| Model | Retained Skills | Forgotten Skills | Gap |
|-------|-----------------|------------------|-----|
| **Claude** | ~0.85-0.92 | ~0.05-0.15 | Strong separation |
| **DeepSeek** | ~0.85-0.92 | ~0.30-0.40 | Moderate separation |
| **GPT-4o** | ~0.85-0.92 | ~0.20-0.35 | Moderate separation |

### Model-Specific Analysis

#### Claude (Anthropic)
- **Forgotten Skills**: ~5-15% accuracy
- **Behavior**: Near-complete suppression of targeted skills
- **Controllability**: Strongest among evaluated models

#### DeepSeek
- **Forgotten Skills**: ~30-40% accuracy
- **Behavior**: Partial resistance to forgetting instructions
- **Controllability**: Weaker - retains substantial knowledge

#### GPT-4o (OpenAI)
- **Forgotten Skills**: ~20-35% accuracy
- **Behavior**: Clear forgetting but not to same extent as Claude
- **Controllability**: Moderate, variable across skill domains

### Key Finding: Localized Degradation
The performance degradation is **not global** but **highly localized** to specified skills, confirming:
- Controlled, selective forgetting behavior
- Not general performance decline
- Structured, reproducible response to skill constraints

### Figure Description: Retained vs. Forgotten Comparison
*(For inclusion: bar chart comparing imperfect student (IS) vs. perfect student (PS) accuracy across retained and forgotten skills)*
- Grouped bars by model
- Percentage annotations showing relative accuracy (IS/PS)
- Clear visual separation between retained and forgotten conditions

---

## 6.4 Skill Correlation Analysis

### Research Question
Are skill performances independent, or does suppressing one skill affect others?

### Methodology
- Computed Pearson correlation matrix over n simulated students
- Each student represented by performance vector [acc_skill1, acc_skill2, ...]
- Analyzed correlations between skill performances

### Quantitative Results

| Grade | Correlation Range | Interpretation |
|-------|------------------|---------------|
| Grade 4 | ~-0.1 (near zero) | Strong independence |
| Grade 5 | ~-0.1 to -0.24 | Weak negative correlation |

### Interpretation

#### Grade 4: Strong Independence
- Correlations approximately uniform and near zero
- Skills operate independently
- Supports localized controllability

#### Grade 5: Mild Interference
- Slightly stronger negative correlations observed
- Suggests weak interference effects
- Performance in one skill may weakly decrease as another increases
- **However**: Magnitude remains small, indicating limited practical impact

### Mathematical Formalization

We model skill performance as a multivariate Gaussian distribution. Under weak correlations:

```
E[performance_on_ret | forget_i] ≈ E[performance_on_ret]
```

This confirms: suppressing one skill does **not** significantly affect performance on others.

### Implication for Simulation Design
- Skills can be controlled independently
- Enables construction of diverse student profiles with arbitrary skill combinations
- Validates core assumption of the skill-vector framework

### Figure Description: Correlation Matrices
*(For inclusion: heatmaps showing Pearson correlation matrices between skills for Grades 4 and 5)*
- Diagonal: Self-correlation (=1)
- Off-diagonal: Cross-skill correlations
- Color scale: Correlation strength
- Near-zero values indicate independence

---

## 6.5 Expected vs. Actual Retained-Skill Accuracy

### Research Question
Do models preserve retained skills at predicted levels when other skills are suppressed?

### Methodology
- Derived theoretical expectation for retained-skill accuracy from correlation analysis
- Compared expected vs. actual accuracy across simulated students
- Scatter plots for Grades 4 and 5

### Quantitative Results

| Model | Alignment with Expectation | Deviation Pattern |
|-------|---------------------------|-------------------|
| **Claude** | Strong | Clusters near diagonal |
| **DeepSeek** | Moderate | Near diagonal |
| **GPT-4o** | Weak | Consistent deviation below diagonal |

### Model-Specific Findings

#### Claude & DeepSeek
- Points cluster closely around the diagonal
- Strong agreement between expected and observed performance
- Successfully preserve retained skills as predicted

#### GPT-4o
- Consistently deviates **below** the diagonal
- Actual performance lower than expected
- Exhibits unintended degradation in retained domains
- Suggests incomplete skill independence

### Interpretation
Weak skill correlations enable localized controllability, but **realization depends on model**:
- Claude: Highest fidelity to expected behavior
- DeepSeek: Moderate alignment
- GPT-4o: Weaker controllability due to residual cross-skill interference

### Figure Description: Expected vs. Actual Scatter Plots
*(For inclusion: scatter plots comparing expected retained-skill accuracy with actual accuracy)*
- Diagonal line: Perfect agreement
- Points: Individual simulated students
- Color/shape: Different models
- Deviation below diagonal indicates under-performance

---

## 6.6 Prediction Score Analysis

### Metric Definition
```
Prediction Score = Actual Retained Accuracy - Expected Retained Accuracy
```

### Interpretation Framework

| Score Value | Interpretation |
|-------------|----------------|
| PS ≈ 0 | Accurate alignment with expectation |
| PS > 0 | Better-than-expected retention |
| PS < 0 | Under-performance, unintended degradation |

### Quantitative Results

| Model | Grade 4 | Grade 5 | Overall |
|-------|---------|---------|---------|
| **Claude** | Positive | Positive | High alignment |
| **DeepSeek** | Moderate Positive | Moderate Positive | Partial alignment |
| **GPT-4o** | **Negative** | Marginal Positive | Inconsistent |

### Key Findings

#### Claude
- Consistently positive prediction scores
- Strong alignment with expected retained-skill performance
- Confirms high controllability

#### DeepSeek
- Moderate positive scores
- Partial alignment with theoretical model
- Some variability across runs

#### GPT-4o
- **Negative scores in Grade 4**
- Only marginal improvement in Grade 5
- Systematic under-performance relative to expectations
- Weaker controllability due to consistent degradation

### Figure Description: Prediction Score Bar Chart
*(For inclusion: mean prediction score per model with error bars indicating variance)*
- Horizontal axis: Models
- Vertical axis: Prediction score
- Error bars: Variance across runs
- Zero line: Perfect alignment reference

---

## 6.7 Forgotten Skill Heatmaps

### Research Question
How effective is forgetting suppression at the individual skill level across different models and domains?

### Methodology
- Examined per-skill accuracy on forgotten skills (K=0) across all domains
- Heatmaps for Grades 4 and 5

### Quantitative Results

| Model | Grade 4 | Grade 5 | Consistency |
|-------|---------|---------|-------------|
| **Claude** | 0.00 - 0.16 | 0.09 - 0.20 | Consistent low |
| **DeepSeek** | 0.10 - 0.39 | 0.31 - 0.34 | Consistently high |
| **GPT-4o** | 0.10 - 0.38 | Variable | Highly variable |

### Model-Specific Findings

#### Claude: Effective Suppression
- Consistently low accuracy across all forgotten skills
- Strong, stable forgetting behavior
- Minimal cross-skill interference

#### DeepSeek: Residual Knowledge
- Significantly higher residual accuracy
- Retains substantial knowledge despite instructions
- Partial resistance to constraints

#### GPT-4o: Variable Behavior
- Sometimes achieves low accuracy (0.10-0.11)
- Other cases show high residual performance (up to 0.38)
- Inconsistent suppression across skill domains

### Figure Description: Forgotten Skill Heatmaps
*(For inclusion: heatmaps showing imperfect-student accuracy on forgotten skills)*
- Rows: Models (Claude, DeepSeek, GPT-4o)
- Columns: Skill domains
- Cell values: Accuracy when skill is designated forgotten
- Color intensity: Lower = more effective forgetting

---

## 6.8 Summary of Key Empirical Findings

Based on the comprehensive experimental evaluation, we identify five key empirical findings:

### Finding 1: Selective Forgetting is Achievable and Measurable
All evaluated models demonstrated some degree of selective forgetting when instructed through appropriately designed prompts. The controllability metrics successfully quantify this behavior.

### Finding 2: Retention Remains Stable Under Skill Removal
For retained skills, imperfect students maintained accuracy levels close to perfect student baselines (~85-92%), confirming that knowledge is largely preserved when required.

### Finding 3: Skills Are Predominantly Independent
Weak correlations (~-0.1 to -0.24) between skill performances support the assumption that targeted forgetting can be localized without widespread degradation.

### Finding 4: Model Architecture Strongly Affects Controllability
Substantial variation in controllability observed across models:
- **Best**: Claude (Anthropic)
- **Moderate**: GPT-4o (OpenAI)
- **Weakest**: DeepSeek

### Finding 5: Claude Provides the Most Reliable Controllable Student Simulation
Across all evaluation dimensions, Claude demonstrated:
- Near-complete skill suppression
- Minimal cross-skill interference
- Highest prediction score alignment
- Most consistent forgetting behavior

---

## 6.9 Results Tables Summary

### Table 1: Prompting Strategy Comparison

| Strategy | Grade 4 RMSE | Grade 5 RMSE | Recommendation |
|----------|--------------|--------------|----------------|
| Combined | 0.08-0.10 | 0.10-0.12 | **Best** |
| Few-Shot | 0.45-0.55 | 0.50-0.60 | Insufficient |
| Rule-Based | 0.50-0.55 | 0.55-0.60 | Insufficient |

### Table 2: Model Controllability Summary

| Model | Forgotten Skill Accuracy | Retained Skill Accuracy | Prediction Score | Overall |
|-------|-------------------------|------------------------|------------------|---------|
| Claude | 0.05-0.15 | 0.85-0.92 | Positive | **Best** |
| DeepSeek | 0.30-0.40 | 0.85-0.92 | Moderate Positive | Moderate |
| GPT-4o | 0.20-0.35 | 0.85-0.92 | Negative (G4) | Weak |

### Table 3: Skill Independence Analysis

| Grade | Correlation Range | Independence Level |
|-------|-------------------|-------------------|
| Grade 4 | ~-0.1 | Strong |
| Grade 5 | -0.1 to -0.24 | Moderate |
| Both | Sufficiently weak for independent control |

---

## 6.10 Figures for Inclusion

The following figures should be included in the final manuscript:

1. **Figure 1**: Controllable Generative Student Architecture (pipeline diagram)
2. **Figure 2**: Main Experiment Pipeline (workflow diagram)
3. **Figure 3**: Prompting Strategy Comparison (RMSE bar chart)
4. **Figure 4**: Retained vs. Forgotten Skills Comparison (grouped bar chart)
5. **Figure 5**: Skill Correlation Matrices (heatmap for Grades 4 and 5)
6. **Figure 6**: Expected vs. Actual Accuracy Scatter Plots
7. **Figure 7**: Prediction Score Comparison (bar chart with error bars)
8. **Figure 8**: Forgotten Skill Heatmaps (Grades 4 and 5)
9. **Figure 9**: Per-Skill Accuracy Grids
