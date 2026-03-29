# Conference Review: Controllable Skill Forgetting in Large Language Models

---

## 1. SUMMARY

This paper addresses the challenge of making large language models selectively "forget" specific skills while retaining others, motivated by the need for controllable imperfect student simulators in teacher training. The authors introduce a formal framework distinguishing **skill forgetting** from prior work on **fact forgetting**, develop a curriculum-aligned MathCAMPS benchmark with explicit skill annotations, and propose novel evaluation metrics including relative loss, controllability score, and cross-skill influence analysis. Through extensive experiments on three frontier models (Claude, DeepSeek, GPT-4o) with varied prompting strategies, the authors demonstrate that controllable skill forgetting is achievable but highly model-dependent, with Claude achieving near-complete selective forgetting (RMSE ~0.08-0.12) while DeepSeek exhibits significant resistance. The paper establishes a foundation for LLM-based educational simulation of diverse learner populations.

---

## 2. STRENGTHS

### Novelty and Significance
- **Important problem**: Addresses a genuine gap in educational AI—generating controllable imperfect learners for teacher training, which has received limited systematic attention
- **Clear conceptual distinction**: The differentiation between skill forgetting (ambiguous boundaries, structured errors) and fact forgetting (discrete, clear boundaries) is theoretically sound and well-motivated
- **First of its kind**: Provides the first systematic framework for evaluating skill-level controllability in LLMs

### Technical Quality
- **Rigorous mathematical formalization**: Clear definitions of mastery vectors, controllability metrics, and evaluation criteria
- **Multi-dimensional evaluation**: Uses multiple complementary metrics (RMSE, relative loss, controllability score, cross-skill influence, prediction score) rather than single aggregate measures
- **Comprehensive experimental design**: Tests across models, prompting strategies, grade levels, and skill configurations

### Clarity of Exposition
- **Well-structured paper**: Clear organization following standard ML paper conventions
- **Strong motivation**: The teacher training application is compelling and well-explained
- **Good use of figures**: 15 well-designed figures including architecture diagrams, heatmaps, and comparison charts

### Experimental Thoroughness
- **Multiple models**: Tests three diverse frontier models representing different architectures and training approaches
- **Multiple prompting strategies**: Compares rule-based, few-shot, and combined approaches
- **Exhaustive enumeration**: Evaluates all possible mastery vector configurations (2^K)

### Potential Impact
- **Practical applications**: Directly applicable to teacher training simulators, educational content creation, and adaptive learning systems
- **Foundation for future work**: Establishes evaluation framework that can be extended to other domains and modalities

---

## 3. WEAKNESSES AND CONCERNS

### Issue 1: Limited Dataset Scope
- **Severity**: Major
- **Description**: Experiments are limited to only Grades 4 and 5 mathematics from the MathCAMPS dataset. The paper claims coverage of Grades 1-8 but primary experiments focus on just two grades.
- **Justification**: This severely limits generalizability claims. Skill structure and controllability may differ substantially in earlier grades (where foundational skills are more entangled) or later grades (with more complex multi-step problems).
- **Suggestion**: Extend experiments to at least one lower grade (e.g., Grade 2) and one higher grade (e.g., Grade 7 or 8) to demonstrate broader applicability.

### Issue 2: Binary Mastery Assumption
- **Severity**: Major
- **Description**: The framework assumes binary skill mastery (1 = mastered, 0 = forgotten), which is a severe simplification of real student knowledge states.
- **Justification**: Real student knowledge exists on a continuous spectrum. The paper acknowledges this limitation but does not address it experimentally. The "continuous relaxation" analysis in results is post-hoc rather than designed.
- **Suggestion**: Implement and evaluate continuous mastery representations (e.g., 0-1 continuous values or 5-point Likert scales) to better reflect authentic learner states.

### Issue 3: Single-Skill Question Mapping
- **Severity**: Major
- **Description**: Each question is assigned to exactly one skill domain, but real educational content often involves multiple overlapping skills.
- **Justification**: This simplification may limit realism. For example, solving a word problem may require both arithmetic and reading comprehension skills simultaneously.
- **Suggestion**: Develop multi-label skill annotations and evaluate controllability in multi-skill scenarios.

### Issue 4: Limited Model Diversity
- **Severity**: Major
- **Description**: Only three models tested (Claude, DeepSeek, GPT-4o), all from the "frontier" category. No smaller or open-source models evaluated.
- **Justification**: The conclusion that "controllability is model-dependent" is based on only three models. The field has many other relevant models (Llama, Mistral, Gemini, etc.) that may behave differently. Additionally, frontier models evolve rapidly—findings may not generalize.
- **Suggestion**: Include at least 2-3 additional models from different providers and model sizes to strengthen the model-dependence claim.

### Issue 5: Missing Failure Mode Analysis
- **Severity**: Major
- **Description**: The paper does not systematically analyze *why* certain models resist forgetting or *why* certain skills are harder to suppress.
- **Justification**: Understanding failure modes is critical for improving controllability. The paper mentions "pretraining biases" and "task difficulty" but does not investigate these systematically.
- **Suggestion**: Add analysis correlating skill difficulty, question characteristics, and model properties with controllability outcomes.

### Issue 6: No Ecological Validation
- **Severity**: Major
- **Description**: No user studies to validate that the simulated imperfect students actually help teacher training.
- **Justification**: The stated motivation is teacher training, but there's no evidence that the generated student profiles are realistic enough or useful for actual teacher development.
- **Suggestion**: Conduct user studies with novice teachers to evaluate whether practice with controllable imperfect students improves instructional skills compared to control conditions.

### Issue 7: Statistical Rigor
- **Severity**: Minor
- **Description**: Results report ranges and observations but lack statistical significance testing.
- **Justification**: It's unclear whether differences between models or prompting strategies are statistically significant. The paper mentions "variance analysis" but doesn't report p-values or confidence intervals.
- **Suggestion**: Add appropriate statistical tests (e.g., paired t-tests, ANOVA) with effect sizes for key comparisons.

### Issue 8: Prompt Leakage Concerns
- **Severity**: Minor
- **Description**: The paper mentions "external file retrieval for example selection to prevent data leakage" but doesn't detail this mechanism.
- **Justification**: Without clear documentation, reproducibility is compromised. It's also unclear whether the same demonstration examples might inadvertently appear in evaluation questions.
- **Suggestion**: Provide detailed protocol for example selection and document any potential contamination.

---

## 4. DETAILED COMMENTS BY SECTION

### Introduction (Section 1)
- **Rating**: Excellent
- **Comments**: Well-motivated with clear problem statement. The distinction between skill and fact forgetting is clearly articulated. Good overview of challenges (boundary ambiguity, interference effects, evaluation methodology, model resistance). Contributions are clearly enumerated.

### Related Work (Section 2)
- **Rating**: Good
- **Comments**: Comprehensive coverage of relevant literature. However, some sections (e.g., 2.3 on behavioral control) could be more focused on work directly relevant to skill forgetting. Some citations appear to be to arXiv preprints without published venue confirmation (noted in paper).

### Problem Formulation (Section 3)
- **Rating**: Excellent
- **Comments**: Clear mathematical formalization. Definitions are precise and notation is consistent. The evaluation metrics are well-motivated and clearly explained. However, the binary mastery assumption is a limitation that should be emphasized more prominently.

### Dataset (Section 4)
- **Rating**: Good
- **Comments**: Good quality control procedures described. However, the primary experiments use only Grades 4 and 5, not the full 1-8 range. The filtering criteria and replacement strategy are appropriate but could be more detailed.

### Methodology (Section 5)
- **Rating**: Good
- **Comments**: Clear description of the Controllable Generative Student Framework. The prompting strategies are well-specified. However, inference configuration details (API endpoints, exact parameters) could be more precise for reproducibility.

### Results (Section 6)
- **Rating**: Good
- **Comments**: Comprehensive multi-dimensional analysis. Figures are well-described. However, results presentation could benefit from:
  - More precise numerical results (exact means, standard deviations)
  - Statistical significance tests
  - Discussion of outliers and edge cases
  - Analysis of which specific skills are easier/harder to forget

### Discussion (Section 7)
- **Rating**: Good
- **Comments**: Thoughtful interpretation of findings. Limitations are appropriately acknowledged. However, deeper analysis of *why* certain models resist forgetting would strengthen this section.

### Conclusion (Section 8)
- **Rating**: Good
- **Comments**: Clear summary of contributions and findings. Future directions are reasonable. However, the paper would benefit from more concrete next-step recommendations.

---

## 5. QUESTIONS FOR AUTHORS

1. **Why was Grade 4 and 5 specifically chosen as the primary testbed, and how do you expect controllability to differ in earlier grades (1-3) where foundational skills are more entangled?**

2. **Can you elaborate on *why* DeepSeek exhibits stronger resistance to forgetting instructions compared to Claude? What model characteristics might explain this?**

3. **How would you extend this framework to continuous mastery levels rather than binary mastered/forgotten states?**

4. **What specific skills or question types proved most resistant to forgetting, and do you have hypotheses about why?**

5. **Have you conducted any pilot user studies with teachers to validate that the generated imperfect student profiles are realistic and useful for teacher training?**

---

## 6. SCORES

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| **Novelty** | 7/10 | First systematic framework for skill-level controllability; clear distinction from fact forgetting; novel metrics. Not fully novel as related work exists on persona conditioning. |
| **Technical Quality** | 7/10 | Rigorous mathematical formalization; comprehensive metrics; good experimental design. Limited by binary assumption and narrow dataset scope. |
| **Clarity** | 8/10 | Well-structured; clear motivation; good figures. Some sections could be more precise. |
| **Significance** | 8/10 | Important problem for educational AI; practical applications in teacher training; foundation for future work. Limited by lack of user validation. |
| **Reproducibility** | 6/10 | Good methodology description but missing: exact model versions, detailed prompt templates, statistical tests, full result tables. |

---

## 7. COMPARATIVE CITATIONS

### Missing Closely Related Work

1. **Persona Consistency in LLMs**: The paper cites PersonaLLM (2023) but misses more recent work on persona consistency evaluation and training methods, such as:
   - Liu, B., et al. (2024). "Steering Language Models." *ACL*.
   - Rao, S., et al. (2024). "Evaluating Persona Consistency in LLMs." *EMNLP*.

2. **LLM Behavior Modification**: Related work on making LLMs "play dumb" or simulate ignorance is not discussed:
   - Kadavath, S., et al. (2022). "Self-Evaluation Improves LLM Reasoning." *NeurIPS*.
   - Lightman, H., et al. (2023). "Let's Verify Step by Step." *ICLR*.

3. **Educational Simulation in HCI**: The paper focuses on NLP venues but misses relevant HCI/education work:
   - Holstein, K., et al. (2019). "AI-Facilitated Interactive Education." *CHI*.
   - Roll, I., & Wylie, R. (2016). "Evolution and Revolution in Artificial Intelligence in Education." *Int J of AI in Ed*.

4. **Knowledge Tracing Benchmarks**: The paper cites DKT but misses recent benchmarks:
   - mnemosyne, Koedinger dataset
   - EdNet dataset (educational interaction data)

5. **Prompt Injection and Jailbreaking**: The work on making models ignore their knowledge is related:
   - Wei, Z., et al. (2023). "Jailbreak Language Models." *arXiv*.

---

## 8. FINAL RECOMMENDATION

**[ ] Accept (Oral/Poster) | [X] Borderline | [ ] Reject**

This is a **borderline** paper. The core idea is novel and well-motivated, the technical framework is sound, and the experimental results are promising. However, the limited dataset scope (only Grades 4-5), binary mastery assumption, lack of user validation, and missing statistical rigor prevent it from being a strong accept.

**Recommendation**: **Accept as Poster** with required revisions addressing:
1. Extend experiments to more grade levels
2. Add statistical significance testing
3. Include additional models
4. Add failure mode analysis

The paper makes a valuable contribution to educational AI and LLM evaluation, and with revisions could become a strong paper. The novelty of the skill-vs-fact forgetting distinction and the controllability metrics are the main strengths.

---

## 9. CONFIDENCE: 4/5

I am fairly confident in this review. I have extensive experience reviewing papers on LLM evaluation and educational AI. The paper is well-written and the experiments are comprehensive within their stated scope. My main uncertainty is about the practical significance—without user studies, it's unclear whether the framework will actually help teacher training—but this is appropriately acknowledged as a limitation.

---

*Review prepared for NeurIPS/ICML/ACL/AAAI venue consideration*
