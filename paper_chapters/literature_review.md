# 2. Related Work

This chapter reviews the foundational literature across six interconnected domains that collectively establish the theoretical and empirical basis for controllable skill forgetting in large language models. We begin with the educational context that motivates this research, examine prior work on LLM-based educational simulation, survey approaches to behavioral control in language models, contrast our work with machine unlearning research, review knowledge tracing methodologies, and conclude with evaluation frameworks relevant to our proposed benchmark.

---

## 2.1 Teacher Professional Development and Simulation-Based Training

### 2.1.1 The Novice Teacher Transition Problem

The transition from formal academic preparation to authentic classroom practice represents one of the most challenging phases in a teacher's professional development. Research consistently demonstrates that beginning teachers face substantial difficulties in managing classroom diversity, adapting instruction to individual learner needs, and developing the adaptive expertise necessary for effective teaching. Ingersoll and Strong (2011) conducted a comprehensive meta-analysis of teacher induction and mentoring programs, finding that structured support during the first years of teaching has measurable positive effects on teacher retention, instructional effectiveness, and student achievement outcomes. Their review identified key components of effective induction programs including structured mentorship, opportunities for reflection, peer collaboration, and sustained emotional and practical support.

Building on this foundation, Goldberg and Orland-Barak (2016) examined the dynamic, iterative nature of teacher induction, arguing that effective support must adapt to the evolving needs of beginning teachers across different stages of their development. Their work highlighted the importance of exposing novice teachers to diverse instructional contexts, including classrooms with heterogeneous learner populations exhibiting varied skill levels and learning needs. This heterogeneity presents particular challenges that cannot be adequately addressed through training experiences focused solely on high-performing or idealized student populations.

### 2.1.2 Deliberate Practice and Expert Performance

The theoretical framework for expertise development in teaching draws upon the deliberate practice paradigm established by Ericsson, Krampe, and Tesch-Romer (1993) in their seminal Psychological Review article. Through extensive analysis of expert performance across domains including chess, music, sports, and medicine, these researchers established that superior performance is not merely a product of innate talent or accumulated experience, but rather emerges from focused, structured practice with targeted feedback on specific weaknesses. The theory posits that deliberate practice involves engagement with tasks specifically designed to improve performance, sustained effort directed at areas of deficiency, and iterative cycles of performance and feedback.

Applied to teacher development, deliberate practice theory suggests that effective professional preparation requires repeated exposure to instructional challenges calibrated to the learner's current developmental level, with immediate feedback and opportunities for modification. However, Heffernan and Heffernan (2014) identified a fundamental constraint: authentic classroom environments are inherently variable and unpredictable, making it difficult to systematically recreate identical instructional scenarios for repeated practice. Their work on the ASSISTments ecosystem demonstrated how computational platforms can bridge this gap by enabling controlled, reproducible instructional interactions suitable for deliberate practice frameworks.

### 2.1.3 The Simulation Solution

Computational simulation offers a principled approach to addressing the limitations of authentic classroom exposure for teacher training. By generating virtual students with predefined characteristics, simulation systems enable teacher trainees to practice instructional responses to diverse learner profiles under conditions that support systematic reflection and controlled experimentation. Critically, effective teacher training requires exposure not only to idealized high-performing students but also to learners exhibiting partial mastery, systematic misconceptions, and realistic error patterns. A simulation system that generates only uniformly expert-level responses fails to prepare teachers for the authentic variability they will encounter in actual classrooms, making the development of controllable imperfect student models a critical research priority.

---

## 2.2 LLM-Based Educational Simulation

### 2.2.1 Generative Agents in Education

Recent advances in large language models have enabled a new generation of educational simulation systems leveraging generative agents. Zhang, Zhang-Li, et al. (2024) introduced a comprehensive framework for simulating classroom education with LLM-empowered agents, demonstrating that language models can effectively simulate differentiated student behavior including intentional errors, varying engagement levels, and diverse response patterns. Their work at NAACL 2024 showed qualitative alignment between predefined student profiles and generated behaviors, establishing the feasibility of LLM-based classroom simulation while noting the need for more rigorous quantitative evaluation of behavioral adherence.

Sun, Zhang, et al. (2024) extended this research direction by highlighting the potential of LLM-driven educational simulations for scalable and personalized learning environments. Their work emphasized the importance of generating learner behaviors that reflect authentic patterns of human learning and forgetting, including the systematic misconceptions that characterize real student populations. However, these prior studies focused primarily on demonstrating feasibility rather than systematically quantifying the degree of behavioral adherence to formally specified mastery structures.

### 2.2.2 Generative Students

The concept of generative students was formalized by Lu and Wang (2024) in their paper "Generative Students: Using LLM-Simulated Student Profiles to Support Question Item Evaluation," presented at ACM L@S 2024. Their framework introduced the use of binary mastery vectors for representing learner knowledge states, demonstrating that LLMs can condition their responses on predefined skill profiles. Crucially, they showed that LLMs can generate responses consistent with specified patterns of skill mastery and deficiency, establishing a proof-of-concept for controllable learner simulation.

Building on this foundation, subsequent work has explored variations of this approach. EduAgent (Xu et al., 2024) introduced a framework for generative student agents focusing on learning dynamics simulation. Agent4Edu (Gao et al., 2024) proposed methods for generating learner response data using generative agents for intelligent education systems. These efforts collectively demonstrate growing interest in LLM-based learner simulation while highlighting the need for more rigorous controllability evaluation.

### 2.2.3 Limitations of Prior Work

Despite promising demonstrations of feasibility, prior work on LLM-based educational simulation suffers from several significant limitations. First, existing studies predominantly employ qualitative evaluation methods, relying on human judgment to assess alignment between generated behaviors and intended profiles. Second, there is no standardized framework for measuring controllability independently of raw performance. Third, prior work has not systematically investigated the conditions under which models resist or comply with forgetting instructions. This paper addresses these gaps by introducing a formal controllability measurement framework and a reproducible benchmark for evaluating skill-level forgetting.

---

## 2.3 Behavioral Control in Large Language Models

### 2.3.1 Persona Conditioning

A substantial body of research has examined the extent to which large language models can be directed to adopt predefined behavioral traits through prompt design. PersonaLLM, introduced by Jiang, Zhang, et al. (2023) in their NAACL findings paper, conducted systematic investigations into whether LLMs can express specified personality traits in a consistent manner. Their work demonstrated that models can maintain stylistic and personality consistency across interactions when provided with appropriate persona descriptions, though perfect coherence remains challenging particularly for nuanced traits.

The PersonaLLM study revealed several important findings relevant to our work. First, the fidelity of persona expression varies substantially across models and trait dimensions. Second, models tend to revert to default behaviors when facing ambiguous or unspecified situations. Third, providing explicit behavioral guidelines improves consistency but does not guarantee perfect adherence. These observations suggest that controllability is a model-dependent property that must be empirically evaluated rather than assumed.

### 2.3.2 Instruction Following and Alignment

Contemporary large language models undergo extensive alignment training to improve their ability to follow user instructions and exhibit helpful, harmless, and honest behaviors. This alignment process, typically involving reinforcement learning from human feedback (RLHF) and related techniques, creates models that are generally responsive to behavioral specifications provided through prompts. However, alignment primarily targets generic instruction-following rather than domain-specific controllability.

Prior research on instruction-following has established that models vary in their susceptibility to different types of prompts and constraints. Strongly aligned models may resist behavioral modifications that conflict with their internalized representations, even when explicitly instructed to behave differently. Understanding this tension between alignment and controllability is essential for educational simulation applications where intentionally imperfect behavior is required.

### 2.3.3 Prompt Engineering for Behavioral Modification

A significant body of work has investigated methods for guiding LLM behavior through prompt design. Few-shot prompting, wherein examples of desired behavior are provided in the context, has demonstrated effectiveness for eliciting specific response patterns. Chain-of-thought prompting has been shown to improve reasoning performance by encouraging explicit step-by-step reasoning. Constraint satisfaction approaches have been explored for enforcing specific output formats or content requirements.

However, prior prompt engineering research has focused predominantly on eliciting correct or desired behaviors rather than inducing specific types of errors or deficiencies. The challenge of prompt-based forgetting presents qualitatively different requirements: the model must not only produce a different output but must fundamentally modify its underlying knowledge application in a structured, predictable manner.

---

## 2.4 Machine Unlearning and Knowledge Removal

### 2.4.1 Approaches to Machine Unlearning

Machine unlearning research addresses the challenge of removing specific knowledge from trained models, motivated by privacy concerns, regulatory requirements (such as GDPR's right to be forgotten), and the desire to eliminate harmful or outdated information. Bourtoule et al. (2021) introduced the SISA (Sharding, Indexing, Slices, and Aggregation) framework for efficient machine unlearning, enabling models to forget training data instances without complete retraining. This line of work has produced various algorithms for gradient-based forgetting, influence function-based methods, and retraining with data exclusion.

### 2.4.2 Fact Forgetting Versus Skill Forgetting

A critical conceptual distinction separates our work from machine unlearning research: the difference between fact forgetting and skill forgetting. Fact forgetting concerns the removal of specific, discrete factual assertions from model behavior. A fact such as "the capital of France is Paris" has clear boundaries and unambiguous truth conditions. Evaluating fact forgetting is correspondingly straightforward: a model either correctly declines to state the targeted fact or it does not.

Skill forgetting, by contrast, operates at a substantially higher level of abstraction. Skills represent generalizable competencies that enable correct performance across families of related tasks. A skill such as "solving quadratic equations" encompasses numerous specific problem types, each requiring appropriate application of underlying principles to different contexts and numerical values. Unlike facts, skills lack crisp definitional boundaries. The question "At what point does forgetting begin?" admits no simple answer, as skill mastery exists along a continuum and manifests differently across varied problem types.

This distinction has profound implications for evaluation methodology. Fact forgetting can be assessed through direct queries to the model. Skill forgetting requires analysis of response patterns across families of problems, with careful attention to the structured nature of errors. When a student forgets a mathematical skill, their errors are not random but systematic, reflecting specific misconceptions about underlying principles. A simulation system that merely injects random errors fails to capture this structured nature of skill forgetting.

### 2.4.3 Measurement Challenges

The ambiguous boundaries of skills introduce fundamental measurement challenges that distinguish skill forgetting from fact forgetting. When evaluating whether a model has successfully forgotten a skill, we must consider not only aggregate accuracy but also error patterns. A model achieving 50% accuracy on a skill domain might be exhibiting genuine forgetting, might simply find the material challenging, or might be demonstrating a systematic misconception that differs from the intended error pattern. Disentangling these possibilities requires careful comparison against baselines and qualitative analysis of response patterns.

Furthermore, skills exhibit hierarchical relationships and dependencies. A skill such as "algebraic fraction manipulation" builds upon more fundamental skills such as basic arithmetic and equation solving. "Forgetting" fraction operations may have differential effects on different underlying competencies, and understanding these relationships is essential for designing effective forgetting instructions.

---

## 2.5 Knowledge Tracing and Learner Modeling

### 2.5.1 Classical Knowledge Tracing Approaches

Knowledge tracing, the task of modeling student knowledge states over time, has been a central problem in educational data mining for decades. Classical approaches include Bayesian Knowledge Tracing (BKT), which uses dynamic Bayesian networks to model transitions between known and unknown knowledge component states, and Item Response Theory (IRT), which provides probabilistic models of student performance as a function of ability and item difficulty.

These classical approaches assume that knowledge states are binary or discretized, enabling straightforward representation of mastery and non-mastery. While effective for prediction tasks, they were not designed to support the deliberate induction of specific knowledge states required for controllable simulation.

### 2.5.2 Deep Learning Approaches

Recent advances in deep learning have produced increasingly sophisticated knowledge tracing models. Deep Knowledge Tracing (DKT), introduced by Piech, Bassen, et al. (2015) at NeurIPS, applied recurrent neural networks to model student knowledge states from sequential interaction data. DKT demonstrated improved predictive performance compared to classical approaches while enabling capture of complex temporal dependencies in learning.

Building on this foundation, Zhang, Shi, et al. (2017) introduced Dynamic Key-Value Memory Networks (DKVMN), which used dedicated memory structures to separately track knowledge component concepts and their associated mastery levels. The key-value architecture enabled direct interpretation of learned knowledge states while achieving strong predictive performance. Pandey and Karypis (2019) proposed Self-Attentive Knowledge Tracing (SAKT), which applied self-attention mechanisms to model dependencies between exercise sequences, further advancing the state of the art in knowledge prediction.

### 2.5.3 When Deep Models Outperform Classical Approaches

Gervet, Koedinger, et al. (2020) conducted a comprehensive evaluation of when deep learning approaches to knowledge tracing outperform classical methods, finding that the answer depends critically on the characteristics of the available data. Deep models excel when large amounts of interaction data are available and when complex temporal dependencies exist between learning events. However, classical approaches remain competitive or superior in low-data regimes and when interpretability is paramount.

### 2.5.4 LLM-Based Skill Gap Identification

Most recently, research has explored the application of large language models to skill gap identification. SkillGapGPT (2025) demonstrated that LLMs can identify skill gaps directly from student responses, reporting strong alignment with expert annotations. These approaches leverage the semantic understanding capabilities of LLMs to provide fine-grained diagnosis of student misconceptions.

Notably, all existing knowledge tracing approaches focus on the detection or prediction of existing knowledge states. The present work addresses a complementary problem: the deliberate induction of predefined knowledge gaps for simulation purposes. Rather than inferring what a student knows, we investigate how to make a model forget what it knows, establishing the foundations for controllable educational simulation.

---

## 2.6 Evaluation Methodologies in Educational AI

### 2.6.1 Traditional Performance Metrics

Evaluation in educational modeling has traditionally relied on quantitative performance metrics including accuracy, root mean squared error (RMSE), area under the curve (AUC), precision, recall, and F1 score. These metrics, developed for predictive modeling tasks, assess how well a model's outputs align with ground truth labels or expected values. Gervet et al. (2020) and subsequent work have applied these metrics extensively to knowledge tracing evaluation.

While these metrics effectively capture predictive performance, they are insufficient for evaluating controllability. A model that achieves 80% accuracy on a skill domain may be performing well because it genuinely knows the material, because the questions are easy, or because it is applying a flawed strategy that coincidentally produces correct answers. Traditional metrics cannot distinguish between these possibilities, making them inadequate for evaluating whether a model is exhibiting intended forgetting behavior.

### 2.6.2 Controllability as a Distinct Evaluation Dimension

This paper introduces controllability as a distinct evaluation dimension orthogonal to traditional performance metrics. Controllability measures not what a model knows, but the extent to which that knowledge can be selectively modulated in response to external specifications. An ideally controllable model demonstrates perfect accuracy when instructed to retain a skill and zero accuracy when instructed to forget the same skill, enabling precise simulation of any desired learner profile.

The distinction between controllability and raw performance has important implications for model selection and evaluation. A model may achieve high performance while remaining largely uncontrollable, and conversely, a controllable model need not achieve state-of-the-art accuracy. Educational simulation applications require both properties, but they must be evaluated independently.

### 2.6.3 Benchmark Design Principles

Reproducible evaluation of controllability requires standardized benchmark conditions. Key design principles include curated test datasets with explicit skill annotations, standardized prompting protocols, controlled experimental conditions, and multi-dimensional evaluation metrics. The MathCAMPS dataset, which provides curriculum-aligned mathematics problems tagged according to educational standards, offers an appropriate foundation for skill-level controllability evaluation.

---

## 2.7 Synthesis and Research Gaps

The literature review reveals several critical gaps that motivate the present research:

**Gap 1: No framework for controllable skill forgetting.** While prior work has demonstrated feasibility of LLM-based student simulation, no systematic framework exists for inducing specific patterns of skill forgetting through prompting. Existing approaches rely on informal persona descriptions without formal evaluation of behavioral adherence.

**Gap 2: No distinction between fact and skill forgetting.** Machine unlearning research addresses forgetting of discrete facts but provides no guidance for skill-level forgetting where boundaries are ambiguous and errors are structured rather than random.

**Gap 3: No controllability measurement framework.** Traditional evaluation metrics capture predictive performance but cannot distinguish between a model that has genuinely forgotten a skill and one that is simply performing poorly due to inherent difficulty.

**Gap 4: No benchmark for standardized controllability assessment.** The absence of standardized benchmarks impedes systematic comparison across models and prompting strategies, limiting scientific progress in this domain.

**Gap 5: Limited understanding of model-specific controllability variation.** Prior work has not systematically investigated which model architectures and training paradigms facilitate or impede controllable skill forgetting.

**Gap 6: Gap between knowledge tracing and knowledge induction.** Existing knowledge tracing research focuses on detecting existing knowledge states. The complementary problem of deliberately inducing specific knowledge gaps for simulation purposes remains largely unexplored.

This paper addresses these gaps by introducing a formal framework for controllable skill forgetting, including a mathematical formulation, a novel measurement framework, and a reproducible benchmark for evaluating frontier language models.

---

## References

- Bourtoule, L., et al. (2021). Machine unlearning. *IEEE Symposium on Security and Privacy (S&P)*.
- Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The role of deliberate practice in the acquisition of expert performance. *Psychological Review*, 100(3), 363-406.
- Feng, S., et al. (2023/2024). PersonaLLM: Investigating the ability of large language models to express personality traits. *NAACL Findings*.
- Gao, W., et al. (2024). Agent4Edu: Generating learner response data by generative agents. *AAAI*.
- Gervet, T., Koedinger, K. R., et al. (2020). When is deep learning the best approach to knowledge tracing? *Journal of Educational Data Mining*, 12(3), 31-54.
- Goldberg, T., & Orland-Barak, L. (2016). The dynamic nature of teacher induction. *Teaching and Teacher Education*, 54.
- Heffernan, N. T., & Heffernan, C. L. (2014). The ASSISTments ecosystem. *International Journal of Artificial Intelligence in Education*, 24(4), 470-497.
- Ingersoll, R. M., & Strong, M. (2011). The impact of induction and mentoring programs for beginning teachers. *Review of Educational Research*, 81(2), 201-233.
- Jiang, H., Zhang, X., et al. (2023). PersonaLLM: Investigating the ability of LLMs to express personality traits. *arXiv:2305.02547*.
- Lu, X., & Wang, Y. (2024). Generative students: Using LLM-simulated student profiles to support question item evaluation. *ACM L@S 2024*.
- Pandey, S., & Karypis, G. (2019). A self-attentive model for knowledge tracing. *International Educational Data Mining Society*.
- Piech, C., Bassen, J., et al. (2015). Deep knowledge tracing. *NeurIPS*.
- Sun, Z., et al. (2024). Large language models for educational simulation. *AAAI*.
- Xu, S., Zhang, X., et al. (2024). EduAgent: Generative student agents in learning. *arXiv:2404.07963*.
- Zhang, J., Shi, X., et al. (2017). Dynamic key-value memory networks for knowledge tracing. *WWW*.
- Zhang, Z., Zhang-Li, D., et al. (2024). Simulating classroom education with LLM-empowered agents. *NAACL*.
