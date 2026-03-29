# Content Review: paper_v5_final.html

**Reviewer:** Senior Content Review  
**Focus:** Content completeness and clarity

---

## 1. Introduction

### Strengths
- Motivation is compelling and well-grounded in teacher training challenges
- Skill vs. fact distinction (Section 1.3) is clearly articulated with good examples
- Four key challenges (deep knowledge entrenchment, interference effects, evaluation methodology, model resistance) are well-identified

### Issues & Suggestions

| Issue | Location | Suggestion |
|-------|----------|------------|
| **Binary skill-vector lacks operationalization** | Section 1.5, 3.1 | Define how skills are identified/extracted. What makes something a "skill" vs. a sub-skill? How granular should the decomposition be? |
| **Transition from motivation to framework is abrupt** | Lines 509-517 | Add a bridging sentence connecting the challenges (1.1-1.4) to the three innovations (1.5) |
| **Research questions lack specificity** | Lines 526-527 | "(1) How effective are different prompting strategies" — specify which strategies; "(2) How does controllability vary" — specify which architectures; "(3) Can skills be controlled independently" — add expected outcome |
| **"Controlled imperfection" is used but not defined** | Line 473 | Add a brief operational definition |

---

## 2. Related Work

### Strengths
- Covers all five key areas: teacher development, LLM simulation, persona control, machine unlearning, knowledge tracing
- Clear gap identification (Section 2.6)
- Good positioning of skill forgetting vs. fact forgetting

### Issues & Suggestions

| Issue | Location | Suggestion |
|-------|----------|------------|
| **Missing bibliography entries** | References | Several papers cited in text do not appear in References: Chen et al. (2025) - SimInstruct, Liu et al. (2025) - SocraticLM, Taylor et al. (2025) - social skills tutoring, Scarlatos et al. (2025), Dong et al. (2025), Peng et al. (2024) |
| **Reference formatting inconsistent** | Lines 885-900 | Some entries lack venue/citation details; standardize format (author, year, title, venue) |
| **Limited coverage of student modeling literature** | Section 2.5 | Could mention cognitive tutoring systems (e.g., Andes, Cognitive Tutor) as predecessors |
| **Missing connection to "imperfect student" literature** | - | The term "imperfect student" appears in title but no prior work cited on this exact concept |

---

## 3. Problem Formulation

### Strengths
- Clear formal notation in Section 3.1
- Four well-chosen metrics covering different aspects of controllability
- Mathematical definitions are correct

### Issues & Suggestions

| Issue | Location | Suggestion |
|-------|----------|------------|
| **Prediction Score equation is unclear** | Line 645 | Define what "expected" accuracy means. Is it baseline? Random chance? Ideal forgetting? Add explicit definition: $A_{expected}(s_i) = k_i$ (perfect control) or $A_{expected} = A_{base}$? |
| **Metrics lack interpretation guidance** | Section 3.2 | Add brief paragraphs explaining what "good" vs. "bad" values look like in practice. E.g., "CS > 0.8 indicates strong controllability" |
| **RMSE formula needs clarification** | Line 631 | Confirm that $A_{ctrl}$ values are scaled 0-1, not percentages. If percentages, adjust formula |
| **No metric for "realistic errors"** | Section 3.2 | Skills require not just low accuracy but *systematic* errors. Consider adding a metric for error pattern consistency |

---

## 4. Results

### Strengths
- Five key findings are clearly summarized (Section 6.6)
- Visual figures provide good overview
- Quantitative results are specific (RMSE ranges, accuracy percentages)

### Issues & Suggestions

| Issue | Location | Suggestion |
|-------|----------|------------|
| **Figure references may break** | Lines 764, 808, 817 | SVG files (fig_results_summary.svg, fig06_correlation_matrix.svg) may not render in all browsers; consider providing PNG fallbacks |
| **Insufficient quantitative detail** | Table 1, Section 6.2 | Add standard deviations, confidence intervals, or exact n-sizes. "5-15%" is a wide range |
| **No statistical significance testing** | Section 6 | Report p-values or effect sizes for model comparisons |
| **Figure 5 caption is unclear** | Line 819 | "Points below diagonal" - clarify what this means (under-performing expectations) |
| **Bootstrapping claim is unclear** | Line 750 | "temperature=0 produces deterministic outputs" contradicts need for bootstrapping. Clarify: is there stochasticity in question selection, prompt variations, or something else? |

---

## Additional Observations

### Minor Issues
- Abstract is well-written but could explicitly state the benchmark name earlier (currently "MathCAMPS" appears without definition until Section 4.1)
- Section 4.3 "Baseline Comparison" text is fragmented and could be integrated better
- "Cross-skill influence analysis" mentioned in contributions (line 533) but not formally defined in metrics section

### Missing Elements
- No ethical considerations section (relevant for educational technology with minors)
- No discussion of computational costs beyond brief mention in Limitations
- No comparison to random/baseline in Results (only mentioned in Section 4.3)

---

## Summary

The paper provides a solid foundation with clear motivation, good theoretical framing, and reasonable methodology. Key improvements needed:

1. **Complete bibliography** — add missing references
2. **Clarify metrics** — define "expected" accuracy and add interpretation guidelines
3. **Strengthen Results** — add statistical details and clarify figure captions
4. **Operationalize skills** — explain how skills are identified/decomposed
5. **Add ethical considerations** — relevant for educational applications
