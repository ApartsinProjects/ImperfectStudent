# 7. Discussion

This chapter interprets the experimental findings presented in the previous section, examines their implications for controllable skill forgetting in large language models, and situates these results within the broader context of LLM-based educational simulation.

---

## 7.1 Controllability is Achievable but Model-Dependent

The central finding of this work is that controllable skill forgetting is achievable through prompt-based instructions, but the degree of achievable controllability varies substantially across model architectures. Our experiments revealed a clear hierarchy among evaluated models: Anthropic's Claude demonstrated the strongest controllability, achieving near-complete selective forgetting with minimal unintended degradation of retained skills; OpenAI's GPT-4o exhibited moderate controllability with some inconsistency across skill domains; and DeepSeek showed the weakest controllability, exhibiting significant resistance to forgetting instructions despite achieving comparable baseline performance.

This variation has important implications for the deployment of LLMs in educational simulation contexts. High baseline performance does not guarantee controllability: DeepSeek achieved strong accuracy on the MathCAMPS benchmark yet demonstrated partial resistance to skill suppression. Conversely, controllability does not require state-of-the-art performance, suggesting that model selection for educational simulation should prioritize controllability metrics alongside traditional accuracy measures.

The observed variation likely reflects differences in training objectives, alignment procedures, and the internal organization of knowledge representations. Models trained with strong instruction-following emphasis may be more responsive to behavioral specifications, while those optimized primarily for reasoning capabilities may exhibit greater resistance to knowledge suppression.

---

## 7.2 Prompt Design is Necessary but Not Sufficient

Our comparison of prompting strategies revealed that prompt design significantly affects controllability outcomes, with the combined strategy (explicit rules plus few-shot demonstrations) substantially outperforming either component alone. This finding has both practical and theoretical implications.

Practically, our results provide actionable guidance for the design of student simulation prompts. Neither explicit behavioral instructions nor demonstration examples alone are sufficient for reliable skill forgetting; their combination creates a complementary effect wherein rules define the desired behavior and examples demonstrate its instantiation. This synergy enables models to better internalize and apply skill constraints.

Theoretically, the limitations of individual prompting strategies reveal the fundamental challenge of prompt-based knowledge modification. Large language models acquire deeply entrenched representations during pretraining, and these representations may resist modification through contextual cues alone. While prompts can modulate surface-level behavior, they may be insufficient to override deeply encoded knowledge structures. This observation suggests that achieving robust controllability may ultimately require training-time interventions rather than purely prompt-based approaches.

---

## 7.3 Skills are Predominantly Independent

One of the most encouraging findings of this work is the weak correlation observed between skill performances across simulated student configurations. Our correlation analysis revealed near-zero Pearson correlations in Grade 4 and modest negative correlations (approximately -0.1 to -0.24) in Grade 5, indicating that skill competencies are largely independent.

This independence is essential for realistic educational simulation. Real students typically exhibit localized misconceptions rather than uniform failure across all domains. If skills were highly interdependent, suppressing one skill might necessarily degrade performance on related competencies, making it impossible to generate diverse learner profiles. Our findings confirm that this desired property holds: we can selectively suppress specific skills while preserving others.

The weak negative correlations observed in Grade 5, while statistically significant, are sufficiently small that they do not meaningfully impact retained-skill performance. This suggests that the independence assumption underlying our skill-vector framework is reasonable and that the approach can scale to more complex skill taxonomies.

---

## 7.4 Controllability Operates Locally at the Skill Level

The cross-skill influence analysis revealed that effective forgetting localizes to the targeted skill without substantial spillover to retained competencies. This finding supports the validity of our fine-grained evaluation approach: controllability must be assessed at the skill level rather than through aggregate accuracy metrics.

The localization of forgetting effects has important implications for simulation design. It enables the construction of diverse student profiles with arbitrary combinations of mastered and forgotten skills, supporting the generation of heterogeneous virtual classrooms for teacher training. Each simulated student can have a unique knowledge state, reflecting the authentic diversity of real learner populations.

However, the localization finding also highlights the challenge of achieving complete forgetting. If skills were perfectly localized, complete suppression of a targeted skill should have zero impact on retained skills. Our observations of modest interference effects indicate that the boundary between skills is not perfectly crisp, potentially reflecting shared underlying representations or reasoning strategies.

---

## 7.5 Implications for Teacher Training

The practical motivation for this work lies in the needs of teacher training programs. Effective teacher preparation requires exposure to diverse learner populations exhibiting realistic patterns of skill mastery and deficiency. Traditional simulation approaches have struggled to generate such diversity in a controlled manner.

Our framework enables systematic generation of students with specified knowledge profiles, supporting deliberate practice with diverse learner types. A teacher training system built on our controllable student framework could expose trainees to students with:
- Specific arithmetic deficiencies (e.g., fraction misconceptions)
- Localized algebraic weaknesses (e.g., equation solving difficulties)
- Systematic procedural errors (e.g., consistent sign mistakes)
- Partial mastery patterns (e.g., conceptual understanding without procedural fluency)

This controlled variability supports the development of adaptive instructional skills that transfer to authentic classroom settings.

---

## 7.6 Limitations and Threats to Validity

This work has several limitations that should be acknowledged.

**Binary mastery assumption**: Our framework assumes that skills are either mastered or forgotten, represented as binary values. Real student knowledge exists on a continuous spectrum, and more nuanced frameworks may be needed for fine-grained simulation. We partially address this by analyzing accuracy as a continuous relaxation of the binary specification, but future work should explore continuous mastery representations.

**Single-skill question mapping**: Our dataset preparation assigns each question to exactly one skill domain. Real educational content often involves multiple overlapping skills, and this simplification may limit the realism of simulated student profiles.

**Prompt-only control**: We evaluate only prompt-based forgetting without exploring fine-tuning or training-time interventions. As discussed, prompt-based control may be inherently limited for deeply encoded knowledge, and future work should investigate complementary approaches.

**Limited domain coverage**: Our experiments focus on mathematical skills from the MathCAMPS dataset. The generalizability of findings to other subject domains remains an open question.

**Model version specificity**: Our experiments evaluate specific model versions at a particular point in time. As models continue to evolve, controllability characteristics may change.

---

## 7.7 Summary

The discussion above yields several key takeaways. Controllability is achievable but model-dependent, requiring evaluation rather than assumption. Prompt design matters significantly, with combined strategies outperforming individual approaches. Skills are largely independent, enabling targeted manipulation without widespread degradation. Effective forgetting localizes to specified skills without substantial spillover. Together, these findings establish the feasibility of controllable skill forgetting while identifying directions for future improvement.

---

## 8. Conclusion and Future Work

### 8.1 Summary of Contributions

This paper introduced a formal framework for controllable skill forgetting in large language models, addressing a critical gap in LLM-based educational simulation. We distinguished skill forgetting from prior work on fact forgetting, identified the unique challenges posed by ambiguous skill boundaries and structured error patterns, and developed a comprehensive evaluation methodology for assessing controllability independently of raw performance.

Our primary contributions include:

1. **A formal problem formulation** that defines controllable skill forgetting as a distinct evaluation dimension and establishes mathematical notation for mastery vectors, accuracy comparisons, and controllability metrics.

2. **A structured benchmark framework** built upon curriculum-aligned mathematical data with explicit skill annotations, enabling reproducible evaluation across models and prompting strategies.

3. **A novel controllability measurement framework** introducing relative loss, skill-level controllability scores, cross-skill influence analysis, and prediction scores that together provide a multi-dimensional assessment of behavioral control.

4. **Extensive empirical evaluation** of three frontier language models under varied prompting strategies, revealing substantial variation in controllability and providing actionable guidance for model selection in educational simulation applications.

5. **A reproducible methodology** for evaluating skill-aware behavioral control that establishes a foundation for future research in this direction.

### 8.2 Key Findings

The empirical results demonstrate that:

- **Controllability is achievable**: All evaluated models exhibited some degree of selective forgetting when instructed through appropriately designed prompts.

- **Controllability is model-dependent**: Claude demonstrated the strongest controllability, achieving near-complete selective forgetting; GPT-4o showed moderate controllability with some inconsistency; DeepSeek exhibited significant resistance to forgetting instructions.

- **Prompt design significantly affects outcomes**: The combined strategy (rules plus demonstrations) achieved RMSE values of approximately 0.08-0.12, substantially outperforming rule-based (~0.50-0.60) or few-shot (~0.45-0.60) approaches alone.

- **Skills are predominantly independent**: Weak correlations (~-0.1) between skill performances support the assumption that targeted forgetting can be localized without widespread degradation.

- **Forgetting is skill-dependent**: Certain skills are easier to suppress than others, likely reflecting differences in intrinsic task difficulty, question structure, and pretraining biases.

### 8.3 Implications

This work has implications for multiple stakeholder communities.

For **educational technology researchers**, our framework provides tools for generating diverse virtual student populations for simulation-based teacher training and pedagogical research.

For **LLM developers**, our evaluation methodology highlights controllability as a distinct property requiring attention alongside traditional performance metrics.

For **teacher educators**, our approach enables the systematic generation of students with specified knowledge profiles, supporting deliberate practice with diverse learner types.

For **educational AI more broadly**, our work establishes controllability as a fundamental requirement for systems intended to simulate or support human learning.

### 8.4 Limitations

This work is subject to several limitations that scope the generalizability of findings. Our framework assumes binary skill representation and single-skill question mapping, which may not capture the full complexity of real educational content. We evaluate only prompt-based control without exploring training-time interventions. Our experiments focus on mathematical skills, and applicability to other domains remains to be established. The binary skill vector representation, while enabling controlled experimentation, may be insufficient for simulating the nuanced knowledge states of real students.

### 8.5 Future Directions

This work opens several promising directions for future research.

**Hierarchical skill representations**: Modeling skill dependencies using hierarchical or graph-based structures could capture more realistic relationships between concepts, enabling simulation of students with realistic developmental progressions or regressions.

**Continuous mastery scales**: Replacing binary mastery with continuous scales would allow for more nuanced student modeling, better reflecting the gradual nature of skill acquisition and forgetting.

**Training-time interventions**: Exploring reinforcement learning or fine-tuning approaches could achieve stronger and more reliable control beyond prompt-based methods, potentially overcoming the limitations of purely contextual interventions.

**Expanded domain coverage**: Extending the framework to additional subject domains including science, language arts, and social studies would support more comprehensive educational simulations.

**Dynamic forgetting**: Enabling forgetting during multi-step reasoning processes rather than single-question responses would better reflect how skills are applied in authentic instructional contexts.

**Error pattern analysis**: Investigating whether generated errors exhibit the systematic, misconception-based patterns characteristic of real student errors rather than random mistakes would improve simulation realism.

**Longitudinal simulation**: Developing methods for simulating learning dynamics over time, including skill acquisition through instruction, would enable more sophisticated educational applications.

**User studies**: Evaluating whether teacher trainees who practice with controllable imperfect students develop improved instructional skills compared to alternative training approaches would establish ecological validity.

---

## 9. Broader Impact Statement

This work contributes to the responsible development of educational AI by enabling the simulation of diverse learner populations for teacher training purposes. By providing tools for generating realistic imperfect students, we support the development of teacher preparation programs that better prepare educators for the authentic variability of real classrooms. This work does not aim to make AI systems perform worse, but rather to understand and enable controlled behavioral modulation for specific application contexts where imperfect behavior is desirable.

---

## References

Bourtoule, L., et al. (2021). Machine unlearning. *IEEE Symposium on Security and Privacy*.

Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The role of deliberate practice in the acquisition of expert performance. *Psychological Review*, 100(3), 363-406.

Feng, S., et al. (2024). PersonaLLM: Investigating the ability of large language models to express personality traits. *NAACL Findings*.

Gao, W., et al. (2024). Agent4Edu: Generating learner response data by generative agents. *AAAI*.

Gervet, T., Koedinger, K. R., et al. (2020). When is deep learning the best approach to knowledge tracing? *Journal of Educational Data Mining*, 12(3), 31-54.

Goldberg, T., & Orland-Barak, L. (2016). The dynamic nature of teacher induction. *Teaching and Teacher Education*, 54.

Heffernan, N. T., & Heffernan, C. L. (2014). The ASSISTments ecosystem. *International Journal of Artificial Intelligence in Education*, 24(4), 470-497.

Ingersoll, R. M., & Strong, M. (2011). The impact of induction and mentoring programs for beginning teachers. *Review of Educational Research*, 81(2), 201-233.

Jiang, H., Zhang, X., et al. (2023). PersonaLLM: Investigating the ability of LLMs to express personality traits. *arXiv:2305.02547*.

Lu, X., & Wang, Y. (2024). Generative students: Using LLM-simulated student profiles to support question item evaluation. *ACM L@S 2024*.

Pandey, S., & Karypis, G. (2019). A self-attentive model for knowledge tracing. *International Educational Data Mining Society*.

Piech, C., Bassen, J., et al. (2015). Deep knowledge tracing. *NeurIPS*.

Sun, Z., et al. (2024). Large language models for educational simulation. *AAAI*.

Xu, S., Zhang, X., et al. (2024). EduAgent: Generative student agents in learning. *arXiv:2404.07963*.

Zhang, J., Shi, X., et al. (2017). Dynamic key-value memory networks for knowledge tracing. *WWW*.

Zhang, Z., Zhang-Li, D., et al. (2024). Simulating classroom education with LLM-empowered agents. *NAACL*.
