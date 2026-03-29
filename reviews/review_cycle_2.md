# Review Cycle 2: Controllable Skill Forgetting in LLMs

**Review Cycle:** 2  
**Target Venue:** Top-tier ML/NLP Conference (NeurIPS/ICML/ACL)  
**Overall Assessment:** Weak Reject - Requires Substantial Work

---

## EXECUTIVE SUMMARY

The paper has improved significantly in layout, typography, and structure following Cycle 1 refactoring. The visual presentation is now publication-quality with proper academic styling. However, the fundamental content issues identified in Cycle 1 have not been adequately addressed. The paper remains weak in statistical rigor, reproducibility, missing citations, and missing baselines. These are major concerns for top-tier venue acceptance.

**Verdict:** Weak Reject (requires substantial revisions)

---

## 1. PROGRESS SINCE CYCLE 1

### 1.1 Improvements Successfully Made

| Aspect | Status | Notes |
|--------|--------|-------|
| Layout/Typography | **Excellent** | Clean academic design, KaTeX math, proper fonts |
| Section Organization | **Improved** | Clear flow, good use of visual elements |
| Contribution Clarity | **Improved** | Now 3 clear contributions in abstract and intro |
| Visual Abstracts | **Added** | Figure 0 provides good overview |
| Figures | **Improved** | Proper captions, SVG support |
| Skill Independence Analysis | **Added** | Correlation matrices in Figure 4 |
| Limitations Section | **Expanded** | Now explicitly lists key limitations |

### 1.2 Issues NOT Addressed from Cycle 1

The following critical issues from Cycle 1 remain unaddressed:

1. **Statistical Rigor** - Still no p-values, effect sizes, confidence intervals
2. **Reproducibility** - Still no exact model versions, prompt templates not provided
3. **Missing Citations** - Still only ~10 references, missing key works
4. **Dataset Details** - No dataset size, annotation methodology, QC numbers
5. **Missing Baselines** - No random forgetting, alternative prompting comparisons
6. **Results Precision** - Still reported as ranges (~0.08-0.12)
7. **Educational Validation** - Still no user study or pilot validation
8. **Model Diversity** - Still only 3 models, no open-source

---

## 2. DETAILED ASSESSMENT

### 2.1 Statistical Rigor - CRITICAL GAP

**Issue:** The paper lacks statistical rigor throughout results.

- Results reported as ranges: "RMSE ~0.08-0.12", "~85-92%", "5-15%"
- No standard deviations reported
- No p-values or statistical tests comparing models
- No confidence intervals
- No effect sizes

**Severity:** Major  
**Impact:** This is a fundamental requirement for top-tier venues. The paper cannot claim "statistical significance" without proper tests.

**Required Fix:**
- Report exact means with standard deviations for all metrics
- Add paired t-tests or Wilcoxon tests comparing model performances
- Add Cohen's d effect sizes for key comparisons
- Add 95% confidence intervals

---

### 2.2 Reproducibility - CRITICAL GAP

**Issue:** Paper lacks sufficient detail for reproducibility.

- Line 432: "Claude" - which version? (3.0, 3.5 Sonnet, 3.7?)
- Line 434: "DeepSeek" - which variant? (DeepSeek-Coder, DeepSeek-LLM?)
- Line 434: "GPT-4o" - which dated version? (May 2024, August 2024?)
- Line 651: "Temperature = 0" - but what about other API parameters (top_p, max_tokens)?
- No exact prompt templates provided
- "Available upon request" is insufficient for top venues

**Severity:** Major  
**Impact:** Other researchers cannot reproduce findings.

**Required Fix:**
- Specify exact model versions (e.g., "Claude 3.5 Sonnet", "GPT-4o-2024-05-13")
- Provide complete prompt templates in appendix
- Document all API parameters used
- Consider releasing code (even if not required)

---

### 2.3 Missing Citations - CRITICAL GAP

**Issue:** References section is severely limited (~10 citations).

**Missing critical works:**
| Work | Relevance | Why Important |
|------|-----------|---------------|
| Liu et al. (2024) Steering Language Models | Direct method for behavior control | Main alternative approach |
| Rao et al. (2024) Persona Consistency | Evaluation methodology | Related framework |
| Kadavath et al. (2022) LLM Self-Evaluation | LLM knowledge/uncertainty | Theoretical foundation |
| Wei et al. (2023) Jailbreak | Making models ignore knowledge | Related phenomenon |
| EdNet Knowledge Tracing | Alternative datasets | Benchmark comparison |
| DKT variants (Piech et al.) | Deep knowledge tracing | Foundational work |

**Severity:** Major  
**Impact:** Paper appears unaware of directly relevant work.

**Required Fix:** Add 5+ key citations to Related Work section.

---

### 2.4 Dataset Details - CRITICAL GAP

**Issue:** Dataset described but key details missing.

- Line 579: "100 multiple-choice questions" per grade - what are total sizes across grades?
- Line 575: "MathCAMPS" - what is the full dataset size?
- Line 583: "Cross-model error detection" - which models? What threshold?
- No inter-annotator agreement for skill mapping
- No exact numbers of filtered/replaced questions

**Severity:** Major  
**Impact:** Reproducibility concerns, cannot assess data quality.

**Required Fix:**
- Add total dataset size
- Document skill mapping methodology
- Report annotation agreement statistics
- Provide exact numbers of quality-controlled items

---

### 2.5 Missing Baselines - CRITICAL GAP

**Issue:** No comparison to alternative approaches.

The paper compares three prompting strategies but lacks:
- **Random forgetting baseline**: What if skills are forgotten randomly?
- **Universal forgetting baseline**: What if all skills are forgotten?
- **Alternative prompting**: "Pretend you are a student who didn't learn..."
- **Fine-tuning comparison**: Not even acknowledged as future direction

**Severity:** Major  
**Impact:** Cannot assess whether the proposed approach is actually good.

**Required Fix:**
- Add random forgetting control condition
- Add alternative prompting baselines
- Discuss fine-tuning as alternative (even if not implemented)

---

### 2.6 Results Precision - MAJOR GAP

**Issue:** Results reported as imprecise ranges throughout.

Examples from paper:
- Line 667: "RMSE ~0.08-0.12"
- Line 730: "~85-92%"
- Lines 684-698: Table 2 uses ranges like "5-15%", "30-40%"

**Severity:** Major  
**Impact:** Impossible to assess statistical significance.

**Required Fix:**
- Report exact means with standard deviations
- Remove "~" approximations
- Provide full numerical results (can be in appendix)

---

### 2.7 Educational Validation - MAJOR GAP

**Issue:** No validation that this helps teacher training.

The paper's motivation (Section 1.1) centers on teacher training simulators, but:
- No pilot user study with teachers
- No evaluation of whether "imperfect students" feel realistic
- No comparison to actual student error patterns

**Severity:** Major (but acknowledged as limitation)  
**Impact:** Application claim is unvalidated.

**Required Fix:**
- Conduct pilot user study with teacher trainees, OR
- More prominently acknowledge this as required future work
- Add comparison to real student error data if available

---

### 2.8 Writing Quality Assessment

**Positive:**
- Good overall organization and flow
- Clear section headings
- Appropriate use of visual elements
- Professional typography

**Remaining Issues:**
- Some sentences still long/complex
- Minor inconsistencies in terminology
- Some claims lack appropriate hedging

---

## 3. CONTENT GAPS FROM CYCLE 1

### 3.1 Fully Addressed
- Contribution clarity (now 3 clear items)
- Visual abstract added
- Figure quality improved
- Skill independence analysis added

### 3.2 Partially Addressed
- Limitations section expanded but still missing skill difficulty analysis
- Some terminology clarified

### 3.3 Not Addressed
All major content issues remain:
- Statistical rigor
- Reproducibility details
- Citations
- Baselines
- Dataset details
- Results precision

---

## 4. PUBLICATION QUALITY ASSESSMENT

### 4.1 Is the paper at publication quality?

**No.** While the visual presentation is excellent, the content lacks the rigor required for top-tier venues. The paper reads more like a technical report than a conference paper.

### 4.2 Specific Content Gaps

1. **Cannot verify claims** - No statistical tests means cannot verify "substantial controllability variation"
2. **Cannot reproduce** - Missing model versions and prompts
3. **Incomplete context** - Missing relevant citations
4. **Weak comparison** - No baselines to judge if approach is good

### 4.3 Figures Assessment

- **Figure 0**: Good overview visual
- **Figure 1**: Architecture diagram - caption is minimal
- **Figure 2**: Experiment pipeline - adequate
- **Figure 3**: Results summary - but what does SVG show?
- **Figures 4-6**: Statistical visualizations - need data labels

The figures reference SVG files that may not render in HTML. Need to ensure all figures are viewable.

---

## 5. RECOMMENDED FIXES

### Priority 1 (Required for Acceptance)

| # | Issue | Fix |
|---|-------|-----|
| 1 | Statistical rigor | Add means, std devs, p-values, effect sizes |
| 2 | Reproducibility | Specify exact model versions, add prompt templates |
| 3 | Missing citations | Add 5+ key citations (Liu, Rao, Kadavath, etc.) |
| 4 | Baselines | Add random forgetting, alternative prompting |
| 5 | Results precision | Report exact numbers, not ranges |
| 6 | Dataset details | Add size, annotation methodology, QC numbers |

### Priority 2 (Strongly Recommended)

| # | Issue | Fix |
|---|-------|-----|
| 7 | Educational validation | Pilot user study or strengthen future work section |
| 8 | Model diversity | Add open-source models (Llama, Mistral) |
| 9 | Error analysis | Analyze why some skills resist forgetting |
| 10 | Continuous mastery | Implement/test continuous representation |

---

## 6. FINAL VERDICT

**Overall Quality Rating: Weak Reject**

The paper makes a conceptually valuable contribution with the skill-vs-fact forgetting distinction and controllability metrics. The refactoring has produced a visually excellent manuscript. However, the fundamental content gaps around statistical rigor, reproducibility, citations, and baselines remain unaddressed from Cycle 1. These are not minor issues but rather fundamental requirements for top-tier venue acceptance.

**Summary:**
- **Strengths**: Novel problem framing, good presentation, clear contributions
- **Weaknesses**: No statistical tests, unreproducible, missing citations, no baselines, imprecise results

**Recommendation:** Major revisions required. Address all Priority 1 issues before resubmission.

---

## 7. COMPARISON TO CYCLE 1

| Aspect | Cycle 1 | Cycle 2 | Change |
|--------|---------|---------|--------|
| Visual Quality | Poor | Excellent | +++ |
| Organization | Good | Excellent | + |
| Statistical Rigor | Major Gap | Major Gap | = |
| Reproducibility | Major Gap | Major Gap | = |
| Citations | Major Gap | Major Gap | = |
| Baselines | Major Gap | Major Gap | = |
| Results Precision | Major Gap | Major Gap | = |

The refactoring successfully addressed presentation issues but failed to address the core content deficiencies.

---

*Review prepared for NeurIPS/ICML/ACL/AAAI venue consideration*  
*Reviewer Confidence: 4/5*
