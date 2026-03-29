# Technical Review: paper_v5_final.html

## Overview
This review examines the technical rigor of the paper on controllable skill forgetting in LLMs. Four focus areas are addressed: math notation, metrics, statistical analysis, and experimental design.

---

## 1. Math Notation Issues

### 1.1 Relative Loss Formula (Lines 620-625)
**Issue:** Division by zero vulnerability and unbounded output.

The formula:
$$\text{RL}(s_i) = \frac{A_{\text{base}}(s_i) - A_{\text{ctrl}}(s_i)}{A_{\text{base}}(s_i)}$$

- **Division by zero** if $A_{\text{base}} = 0$ (though unlikely in practice, this should be handled)
- **No upper bound**: If $A_{\text{ctrl}} > A_{\text{base}}$ (counterintuitive retention), RL becomes negative
- **Asymmetry**: The retained skill formula uses different structure, making cross-comparison problematic

**Fix:** Add epsilon smoothing and clamp:
$$\text{RL}(s_i) = \min\left(1, \frac{A_{\text{base}} - A_{\text{ctrl}}}{\max(A_{\text{base}}, \epsilon)}\right)$$

### 1.2 RMSE Formula (Line 631)
**Issue:** Dimensional mismatch.

$$\text{RMSE} = \sqrt{\frac{1}{K} \sum_{i=1}^{K} (k_i - A_{\text{ctrl}}(s_i))^2}$$

Comparing binary $k_i \in \{0,1\}$ with continuous $A_{\text{ctrl}} \in [0,1]$ is problematic. A 50% accuracy on forgotten skills ($A=0.5$) yields $(0-0.5)^2 = 0.25$, while 100% accuracy yields $(0-1)^2 = 1$. This scale is inverted.

**Fix:** Consider normalization or alternative metric like Brier score adaptation.

### 1.3 Prediction Score (Line 645)
**Issue:** Undefined variable.

$$\text{PS} = A_{\text{actual}} - A_{\text{expected}}$$

The term $A_{\text{expected}}$ is never formally defined. What does "expected" mean here? The intended mastery vector? A theoretical baseline?

**Fix:** Define explicitly: $A_{\text{expected}} = k_i$ (the target accuracy from the skill vector).

---

## 2. Metrics Issues

### 2.1 Controllability Score (Lines 637-641)
**Issue:** Ad hoc definition without theoretical justification.

The function $f(k_i, A_{\text{ctrl}})$ produces values in [0,1] but has no derivation or justification. Why this specific formulation? What properties should an ideal controllability metric have, and does this satisfy them?

**Recommendation:** Provide explicit rationale for metric design.

### 2.2 Missing Metric Definitions
- **$A_{\text{base}}$**: Is this single-prompt baseline or ensemble? Never specified.
- **$A_{\text{ctrl}}$**: Defined as "controlled" but unclear if this is mean accuracy across prompts or single evaluation.
- **Bootstrapped CI**: Line 752-753 mentions bootstrap but methodology is unclear—what is being resampled?

### 2.3 Acc_skill Formula (Line 676)
Minor: Should specify if this is per-question or per-dataset aggregation.

---

## 3. Statistical Analysis Issues

### 3.1 Significance Claims Without Details (Line 670)
> "significantly outperforms both baselines (p < 0.01)"

**Issues:**
- No statistical test specified (t-test, Wilcoxon, bootstrap?)
- No effect size reported
- No multiple comparison correction applied
- Sample sizes unclear

### 3.2 Confidence Interval Method (Lines 750-754)
**Issue:** Inconsistent application.

The paper uses:
- "Exact performance values" for deterministic outputs
- "Bootstrapped CI" for forgotten skills

This inconsistency is confusing. What specifically is being bootstrapped? Question variants? If temperature=0 is deterministic, bootstrap across what?

### 3.3 Variance Reporting
- Line 754: "SD = 4.2%" and "SD = 11.3%" reported but unclear what these standard deviations represent (across models? questions? skill configurations?)
- No confidence intervals on main effect sizes

### 3.4 Correlation Claims (Line 836)
> "correlation |ρ| < 0.15"

- No p-values or confidence intervals on correlation
- Sample size (n) not reported
- Which correlation coefficient? (Pearson specified in Fig 4 caption but not in text)

---

## 4. Experimental Design Issues

### 4.1 Baseline Definition (Lines 668-672)
Two baseline conditions are described but:
- How many trials per baseline?
- Random forgetting: how is "random" implemented?
- What is the exact comparison methodology?

### 4.2 Skill Enumeration (Line 744)
> "All $2^K$ skill vector configurations are enumerated."

With K = 8-12 skills per grade:
- $2^8 = 256$ to $2^{12} = 4096$ configurations
- How many questions per configuration?
- Total sample size unclear

### 4.3 Missing Information

| Missing Element | Location | Impact |
|-----------------|----------|--------|
| Sample sizes | Throughout | Reproducibility |
| Exact prompts | Lines 731-735 | Replication |
| Question counts per skill | Section 4 | Evaluation robustness |
| Multiple comparison correction | Line 670 | Validity of significance claims |
| Effect sizes | Section 6 | Practical significance |
| Power analysis | N/A | Study adequacy |

### 4.4 Temperature Justification
Line 741: Temperature = 0 for "deterministic decoding." While this ensures reproducibility, it limits generalizability since users typically employ non-zero temperature. Consider reporting results at temperature > 0.

### 4.5 Single Prompt per Condition
The paper evaluates single prompt instances rather than multiple variations. This misses prompt sensitivity analysis—crucial since prompt wording significantly affects LLM behavior.

---

## Summary of Critical Issues

| Priority | Issue | Location |
|----------|-------|----------|
| High | Relative Loss unbounded/division by zero | Eq. 2, 3 |
| High | Undefined $A_{\text{expected}}$ | Eq. 5 |
| High | p-value without test details | Line 670 |
| Medium | RMSE dimensional mismatch | Eq. 4 |
| Medium | No correlation CIs or n | Line 836 |
| Medium | Bootstrap methodology unclear | Line 752 |
| Low | CS justification missing | Eq. 4 |

---

## Recommendations

1. **Math notation**: Add bounds checking, define all variables explicitly, provide unified Relative Loss formula
2. **Metrics**: Justify Controllability Score theoretically, define all terms before use
3. Statistics: Specify exact tests, report effect sizes, correct for multiple comparisons
4. Experimental design: Report sample sizes, include temperature ablation, add prompt variation analysis
