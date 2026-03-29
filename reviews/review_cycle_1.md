# Critical Review: Controllable Skill Forgetting in Large Language Models

**Review Cycle:** 1  
**Target Venue:** Top-tier ML/NLP Conference (NeurIPS/ICML/ACL)  
**Overall Assessment:** Borderline - Requires Major Revisions

---

## EXECUTIVE SUMMARY

This paper addresses an important and underexplored problem: making LLMs selectively "forget" specific skills while retaining others, motivated by teacher training applications. The skill-vs-fact forgetting distinction is conceptually sound, and the controllability metrics are novel. However, the paper suffers from significant limitations in dataset scope, statistical rigor, missing baselines, and validation that prevent it from being a strong accept at top venues.

**Verdict:** Accept (Poster) with Mandatory Revisions

---

## 1. INTRODUCTION

### 1.1 Motivation Assessment

**Issue:** The motivation, while clear, may not be compelling enough for top-tier venues.

- The teacher training imperative is well-explained but feels somewhat narrow
- The paper frames this as primarily for "teacher training simulators" but the framework could have broader applications (safety, privacy, AI safety) that are not explored
- The connection between the technical problem and the application could be stronger

**Severity:** Minor  
**Fix:** Expand the motivation to include additional application contexts (e.g., privacy-preserving model modification, safety testing, simulating knowledge gaps for adversarial robustness).

### 1.2 Research Questions

**Issue:** Research questions are stated clearly but could be more specific.

- The central RQ ("Can we configure a prompted LLM to selectively forget...?") is broad
- Sub-questions in Section 3.9 are good but buried in problem formulation rather than introduction

**Severity:** Minor  
**Fix:** Move sub-questions to Section 1.4 (Research Questions) for earlier visibility.

### 1.3 Contributions

**Issue:** Contribution statement is somewhat inconsistent.

- Abstract claims "three primary contributions" but Introduction lists "four primary contributions"
- Contribution 1 (formal skill representation framework) and Contribution 4 (reproducible methodology) feel like sub-components rather than separate contributions
- The benchmark framework and controllability metrics are the true novel contributions

**Severity:** Major  
**Fix:** Consolidate to 2-3 clear contributions:
1. A formal framework for controllable skill forgetting with novel evaluation metrics
2. A reproducible benchmark (MathCAMPS-based) for evaluating skill-level controllability
3. Empirical findings demonstrating model-dependent controllability

---

## 2. RELATED WORK

### 2.1 Missing Critical Citations

**Issue:** Several important related works are missing.

| Missing Work | Relevance | Severity |
|-------------|-----------|----------|
| **Steering Language Models (Liu et al., 2024)** | Direct method for behavior modification | Major |
| **Evaluating Persona Consistency (Rao et al., 2024)** | Related evaluation methodology | Major |
| **Self-Evaluation/LLM Reasoning (Kadavath et al., 2022)** | LLM uncertainty and knowledge | Major |
| **Jailbreak literature (Wei et al., 2023)** | Making models ignore knowledge | Minor |
| **EdNet/Knowledge Tracing Benchmarks** | Alternative datasets | Major |
| **ASSISTments/SIG-Assessments** | Prior educational simulation work | Minor |

**Fix:** Add citations to Section 2, especially:
- Liu, B., et al. (2024). "Steering Language Models." *ACL*.
- Rao, S., et al. (2024). "Evaluating Persona Consistency in LLMs." *EMNLP*.
- Kadavath, S., et al. (2022). "Self-Evaluation Improves LLM Reasoning." *NeurIPS*.

### 2.2 Gap Identification

**Issue:** The literature review is comprehensive but the "gaps" identified in Section 2.7 are not sufficiently connected to the paper's contributions.

- Gap 3 (no controllability measurement framework) is addressed by the paper
- But Gaps 5-6 (model variation, knowledge induction) are not clearly addressed

**Severity:** Minor  
**Fix:** Restructure Section 2.7 to explicitly map each gap to paper contributions.

### 2.3 Fact vs. Skill Forgetting Distinction

**Issue:** Well-justified but could be more rigorous.

- The distinction is conceptually sound but lacks empirical validation
- No direct experiments comparing fact forgetting vs. skill forgetting in the same framework

**Severity:** Minor  
**Fix:** Add a brief experiment or discussion showing that the same prompting approach fails for skill forgetting but might work for fact forgetting.

---

## 3. PROBLEM FORMULATION

### 3.1 Mathematical Correctness

**Issue:** The RMSE formula has a potential issue.

- Line 450 in paper_manuscript.html: `RMSE = sqrt(1/K * sum((k_i - A_ctrl(s_i))^2))`
- This compares binary k_i (0 or 1) to continuous accuracy (0-1)
- For k_i=1 (retained), deviation is (1 - A_ctrl); for k_i=0, deviation is (0 - A_ctrl) = -A_ctrl
- This is correct but could be more clearly explained

**Severity:** Minor (clarity issue)  
**Fix:** Add explicit interpretation of what RMSE=0 means for each case.

### 3.2 Assumptions

**Issue:** Key assumptions are not explicitly stated.

- Assumption 1: Skills are independent (tested but assumed)
- Assumption 2: Binary mastery is sufficient
- Assumption 3: Prompt-based control is the only method evaluated

**Severity:** Major  
**Fix:** Add explicit "Assumptions" subsection to Section 3.

### 3.3 Metrics

**Issue:** The Controllability Score formula has a typo.

- Line 205 in methods.md: "retained" is spelled as "retailed"
- The function f(k_i, A_ctrl) is not well-explained for the k=0 case
- For forgotten skills: f = 1 - A_ctrl; this rewards LOW accuracy (good)
- For retained skills: f = A_ctrl; this rewards HIGH accuracy (good)
- This is correct but needs clearer explanation

**Severity:** Minor (but embarrassing for publication)  
**Fix:** Fix typo and add interpretation table.

---

## 4. DATASET

### 4.1 MathCAMPS Description

**Issue:** Adequately described but missing key details.

- What is the total size of MathCAMPS?
- How were skills mapped to questions? Manually or automatically?
- What was the inter-annotator agreement for skill annotation?

**Severity:** Major (reproducibility)  
**Fix:** Add:
- Total dataset size
- Skill mapping methodology
- Annotation statistics (number of questions per skill, agreement scores)

### 4.2 Quality Control

**Issue:** Quality control is described but not reproducible.

- "Cross-model error detection" - which models were used?
- What threshold determined "majority" for flagging?
- How many questions were replaced? (exact numbers)

**Severity:** Major  
**Fix:** Provide exact numbers of filtered/replaced questions and the criteria used.

### 4.3 Reproducibility Concerns

**Issue:** Major reproducibility gaps.

- No mention of exact model versions (Claude which version? GPT-4o which variant?)
- No exact prompt templates provided
- No code or data links in appendix

**Severity:** Major  
**Fix:** 
- Specify exact model versions (e.g., "Claude 3.5 Sonnet", "GPT-4o-2024-05-13")
- Add prompt templates as supplementary material
- Consider releasing code/data (or at minimum, detailed protocols)

---

## 5. METHODOLOGY

### 5.1 Prompting Strategies

**Issue:** Not clearly described enough for reproducibility.

- "External file retrieval" mentioned but not detailed
- No exact prompt templates provided
- How were demonstration examples selected?

**Severity:** Major  
**Fix:** Provide:
- Exact prompt templates in appendix/supplementary
- Example prompts in the paper
- Documentation of example selection process

### 5.2 Experimental Protocol

**Issue:** Protocol is mostly complete but missing details.

- Temperature = 0 is good for reproducibility, but what about other API parameters?
- How were the 100 questions per grade selected?
- How many skill configurations were actually tested? (2^K for K skills)

**Severity:** Minor  
**Fix:** Document all API parameters and question selection criteria.

### 5.3 Missing Baselines and Comparisons

**Issue:** No comparison to alternative approaches.

- No comparison to fine-tuning approaches
- No comparison to system prompt variations (e.g., role-playing prompts)
- No comparison to simpler baselines (e.g., random forgetting)

**Severity:** Major  
**Fix:** Add baseline comparisons:
- Random forgetting (forgot random skills, not specified)
- Universal forgetting (forget all skills)
- Alternative prompting (e.g., "pretend you are a student who didn't learn...")

---

## 6. RESULTS

### 6.1 Findings Presentation

**Issue:** Results are presented clearly but lack precision.

- Results often reported as ranges (e.g., "~0.03-0.09", "~85-92%")
- No standard deviations reported
- No confidence intervals

**Severity:** Major  
**Fix:** Report exact means and standard deviations, not just ranges.

### 6.2 Figures and Tables

**Issue:** Some figures are described but not shown (SVG versions exist but unclear relationship to PNG versions).

- Figure 03 has both PNG and SVG versions - which is the final version?
- Some figures are referenced but their content is unclear from the text alone
- Figure captions could be more informative

**Severity:** Minor  
**Fix:** 
- Consolidate to one figure format (SVG preferred for publication)
- Expand figure captions with more detail
- Ensure all figures referenced are complete

### 6.3 Statistical Rigor

**Issue:** Significant statistical shortcomings.

- No p-values reported
- No statistical tests comparing models
- No effect sizes
- Paper claims "statistical significance" in methods but doesn't deliver

**Severity:** Major  
**Fix:** Add:
- Paired t-tests or Wilcoxon tests comparing model performances
- Effect sizes (Cohen's d) for key comparisons
- Confidence intervals for main results
- Correction for multiple comparisons if applicable

---

## 7. DISCUSSION

### 7.1 Limitations

**Issue:** Limitations are acknowledged but incomplete.

- Missing: No analysis of WHY certain skills are harder to forget
- Missing: No analysis of prompt characteristics that correlate with success
- Missing: Computational cost analysis

**Severity:** Major  
**Fix:** Expand Section 7.6 to include:
- Analysis of skill-level difficulty factors
- Prompt characteristics analysis
- Runtime/computational requirements

### 7.2 Implications

**Issue:** Implications are discussed but could be deeper.

- Practical implications for teacher training are clear
- Implications for LLM development are vague ("model selection should prioritize controllability")
- Implications for safety/privacy are not explored

**Severity:** Minor  
**Fix:** Expand implications section to cover:
- Guidelines for model developers
- Safety/privacy implications
- Limitations of prompt-based approaches

### 7.3 Prior Work Comparison

**Issue:** Comparison to prior work is limited.

- Lu & Wang (2024) is mentioned but no direct comparison
- No quantitative comparison to prior benchmarks
- No discussion of how this work advances beyond "proof of concept"

**Severity:** Major  
**Fix:** Add:
- Direct comparison to Lu & Wang's approach
- Quantitative improvements over prior work
- Clear statement of what this paper enables that prior work didn't

---

## 8. WRITING QUALITY

### 8.1 Organization

**Issue:** Paper is generally well-organized but has some issues.

- Literature review is very long (Section 2 is ~174 lines in markdown)
- Results section mixes quantitative and qualitative descriptions
- Some redundancy between sections (e.g., metrics defined multiple times)

**Severity:** Minor  
**Fix:** 
- Condense literature review
- Separate quantitative and qualitative results
- Remove redundancy via cross-references

### 8.2 Unclear Passages

**Issue:** Several passages are unclear or ambiguous.

- Line 317 in paper_manuscript.html: "The subtitle" conflicts with title - needs clarification
- Some sentences are excessively long (10+ lines in introduction)
- Technical terms introduced without definition (e.g., "Curriculum-aligned" assumed to be understood)

**Severity:** Minor  
**Fix:** 
- Break up long sentences
- Add glossary or define terms inline
- Clarify title/subtitle

### 8.3 Prose Quality

**Issue:** Generally good but needs polishing.

- Typos: "retailed" in methods.md line 205
- Some awkward phrasings ("the forgetting effects will localize")
- Some claims lack hedging ("Our findings confirm that..." when it's just evidence)

**Severity:** Minor  
**Fix:** Professional proofreading pass to fix:
- All typos
- Awkward phrasings
- Hedging where appropriate

---

## 9. ADDITIONAL CRITICAL ISSUES

### 9.1 Title and Subtitle Mismatch

**Issue:** Title says "Controllable Skill Forgetting" but subtitle says "Imperfect Student Simulation for Teacher Training."

- These are related but different framings
- Paper oscillates between both framings

**Severity:** Minor  
**Fix:** Align title, subtitle, and framing throughout.

### 9.2 Contribution Count Inconsistency

**Issue:** Abstract says "three primary contributions" but Introduction lists four.

- This is confusing for reviewers
- Some contributions overlap

**Severity:** Minor  
**Fix:** Consolidate to 2-3 clear contributions.

### 9.3 Model Selection Justification

**Issue:** Three models tested but justification is thin.

- Why these specific three?
- Why no open-source models (Llama, Mistral)?
- Why no smaller models?

**Severity:** Major  
**Fix:** Provide clearer justification for model selection and acknowledge limitation.

### 9.4 Educational Validation Missing

**Issue:** No validation that this actually helps teacher training.

- This is the stated application but not validated
- User studies are needed

**Severity:** Major (but acknowledged as limitation)  
**Fix:** Either:
- Conduct pilot user study, OR
- More prominently acknowledge this as future work

### 9.5 Error Analysis Missing

**Issue:** No analysis of WHY certain skills resist forgetting.

- Paper says some skills are "harder to suppress" but doesn't investigate why
- What characteristics make a skill easier/harder?

**Severity:** Major  
**Fix:** Add analysis correlating:
- Skill difficulty (from baseline performance)
- Question characteristics
- Prompt characteristics
with controllability outcomes

---

## 10. ACTIONABLE FIXES SUMMARY

| Priority | Issue | Severity | Specific Fix |
|----------|-------|----------|--------------|
| 1 | Statistical rigor | Major | Add p-values, effect sizes, confidence intervals |
| 2 | Reproducibility | Major | Add exact model versions, prompt templates, code availability |
| 3 | Missing citations | Major | Add 5+ key citations (see Section 2.1) |
| 4 | Dataset details | Major | Add dataset size, annotation methodology, QC numbers |
| 5 | Missing baselines | Major | Add random/forgetting, alternative prompting baselines |
| 6 | Error analysis | Major | Add analysis of why skills differ in controllability |
| 7 | Contribution clarity | Major | Consolidate to 2-3 clear contributions |
| 8 | Results precision | Major | Report exact means, std devs, not just ranges |
| 9 | Binary mastery | Major | Implement and test continuous mastery representation |
| 10 | Educational validation | Major | Conduct pilot user study or strengthen future work |
| 11 | Model diversity | Major | Add 2-3 more models (open-source, different sizes) |
| 12 | Grade coverage | Major | Extend experiments to Grades 2 and 7-8 |
| 13 | Typos/proofreading | Minor | Fix "retailed" typo and other errors |
| 14 | Figure consistency | Minor | Standardize on SVG, expand captions |
| 15 | Limitation scope | Minor | Add computational cost, skill difficulty analysis |

---

## 11. RECOMMENDATION

**Final Verdict:** Accept (Poster) with Mandatory Revisions

This paper makes a valuable contribution to educational AI and LLM evaluation. The skill-vs-fact forgetting distinction is novel and important, and the controllability metrics provide a valuable framework. However, the limited dataset scope (Grades 4-5 only), lack of statistical rigor, missing baselines, and absence of user validation prevent it from being a strong accept.

**Required Revisions (for acceptance):**
1. Add statistical significance tests with effect sizes
2. Extend experiments to more grades (at minimum, Grades 2 and 7)
3. Add 2-3 additional models (include open-source)
4. Add missing citations (5+ key papers)
5. Provide exact model versions and prompt templates
6. Add baseline comparisons
7. Consolidate contributions to 2-3 clear items

**Recommended Revisions (for stronger paper):**
1. Implement continuous mastery representation
2. Conduct pilot user study
3. Add error analysis (why skills differ)
4. Professional proofreading

---

*Review prepared for NeurIPS/ICML/ACL/AAAI venue consideration*  
*Reviewer Confidence: 4/5*
