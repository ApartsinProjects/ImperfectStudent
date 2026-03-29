# 4. Methods

This section describes the benchmark framework, experimental setup, and evaluation methodology for measuring controllable skill forgetting in large language models. We begin by describing the dataset construction and quality control procedures, followed by the specification of the Controllable Generative Student Framework. We then detail the model selection criteria, prompting strategies, and experimental protocol. Finally, we present the evaluation metrics used to assess controllability performance.

---

## 4.1 Dataset Description

### 4.1.1 MathCAMPS Dataset and Skill Annotation

We constructed our benchmark using the MathCAMPS dataset, a curriculum-aligned collection of mathematics problems mapped to U.S. Common Core standards. The dataset provides a principled skill taxonomy where educational standards correspond to distinct skill domains, enabling precise evaluation of domain-specific performance. This alignment ensures that questions within each skill category share underlying conceptual dependencies, making it possible to assess whether skill forgetting generalizes appropriately within domains.

The MathCAMPS dataset spans elementary and middle school mathematics, covering Grades 1 through 8. Each question is annotated with its corresponding skill domain (Knowledge Component), allowing us to compute per-skill accuracy metrics and evaluate the degree to which skill suppression affects performance on questions requiring the targeted competency. The granularity of domain-level skill assignment provides a balanced testbed for controllable forgetting experiments, as each grade level contains multiple distinct skill domains with sufficient question volume for statistical analysis.

All questions were converted to a standardized four-option multiple-choice format (options A through D) with numerically close or conceptually plausible distractors designed to challenge students who lack complete mastery of the target skill. This format ensures consistent evaluation across all questions and facilitates automated scoring.

### 4.1.2 Dataset Preparation and Quality Control

We constructed grade-specific datasets containing 100 questions each, selected to achieve balanced distribution across skill domains within each grade level. This stratification ensures that each skill domain contributes equally to the evaluation, preventing bias from uneven skill representation.

To ensure benchmark quality, we implemented a multi-stage filtering procedure. First, we identified and removed systematically ambiguous or poorly constructed items through manual inspection by experienced educators. Second, we conducted cross-model error detection, flagging items that produced consistent errors across multiple model architectures. This procedure catches questions with unclear solution paths or defective distractors. Third, problematic items were replaced with alternative questions drawn from the same educational standard, and skill distribution balance was verified after each replacement. This conservative replacement strategy maintains the statistical properties of the original dataset while eliminating unreliable evaluation items.

The primary test grades for our experiments were Grade 4 and Grade 5. These grades were selected because they exhibit well-defined, fixed skill domains with balanced distributions and strong internal consistency, providing an ideal testbed for controllable forgetting evaluation.

---

## 4.2 Controllable Generative Student Framework

### 4.2.1 Problem Formulation and Notation

We formalize controllable skill forgetting through a mathematical framework that models student knowledge states as binary mastery vectors. Let **S** denote the set of skill domains:

$$S = \{s_1, s_2, \ldots, s_K\}$$

where **K** represents the total number of distinct skill domains under consideration. Each skill domain corresponds to a specific mathematical competency within the curriculum.

The mastery vector **K** is a K-dimensional binary vector:

$$K = \{k_1, k_2, \ldots, k_K\}, \quad k_i \in \{0, 1\}$$

where $k_i = 1$ indicates that the student has **retained** (mastered) skill $s_i$, and $k_i = 0$ indicates that the student has **forgotten** (not mastered) skill $s_i$. This formulation allows us to represent arbitrary combinations of retained and forgotten competencies.

A **perfect student** is represented by a fully activated mastery vector $K_{perfect} = \{1, 1, \ldots, 1\}$, implying full mastery across all skills. An **imperfect student** with realistic learning gaps is represented by a partially deactivated vector such as $K_{imperfect} = \{1, 0, 1, \ldots, 1\}$, where specific skills are intentionally suppressed to simulate knowledge deficiencies.

For each skill $s_i$, we denote $A_{base}(s_i)$ as the **baseline accuracy** without forgetting constraints and $A_{ctrl}(s_i)$ as the **accuracy under controlled prompt**. The objective is not to reduce global performance, but to induce structured, domain-specific deficiencies that accurately reflect the specified mastery vector.

### 4.2.2 Architecture and Prompt Design

The Controllable Generative Student (CGS) Framework operationalizes skill forgetting through a structured prompting pipeline. The framework comprises five sequential components:

1. **Binary Skill Vector Input**: The mastery vector **K** is provided as a K-dimensional binary vector specifying which skills are retained ($k_i = 1$) and which are forgotten ($k_i = 0$).

2. **Vector-to-Text Translation**: The binary mastery vector is translated into explicit skill category descriptions that can be incorporated into natural language prompts. This translation maps the abstract mathematical representation to human-readable descriptions of student capabilities.

3. **Student Profile Prompt**: A structured prompt is constructed that encodes the student's knowledge state, including descriptions of mastered skills, descriptions of missing or forgotten skills, and behavioral instructions or demonstration examples that guide the model's responses.

4. **LLM Generation**: The large language model generates responses conditioned on the skill profile prompt, answering questions while attempting to exhibit the specified knowledge state.

5. **Output Collection**: Responses are parsed to extract standardized answer selections (single option from A-D), enabling automated scoring.

The prompt template follows a consistent structure across all experiments:

- Mastered skills description: Explicit statement of which competencies the student possesses
- Missing/forgotten skills description: Explicit statement of which competencies the student lacks
- Behavioral instructions (for rule-based prompting): Direct commands specifying desired response patterns
- Demonstration examples (for few-shot prompting): Worked examples showing correct and incorrect responses
- Target question: The multiple-choice mathematics problem to be answered
- Output instruction: Direction to provide a single answer without explanation

---

## 4.3 Model Selection

### 4.3.1 Evaluated Models

We selected three state-of-the-art large language models representing diverse architectural characteristics and training methodologies:

| Model | Provider | Characteristics | Selection Rationale |
|-------|----------|-----------------|---------------------|
| Claude | Anthropic | Safety-aligned, strong instruction-following | Known compliance with behavioral constraints |
| DeepSeek | DeepSeek | High-performance, reasoning-optimized | Strong mathematical reasoning capabilities |
| GPT-4o | OpenAI | General-purpose, widely used | Baseline comparison and generalizability |

### 4.3.2 Selection Criteria

Models were selected based on three criteria. First, **baseline performance**: all candidate models were evaluated on the MathCAMPS benchmark, and only models achieving high overall accuracy were retained. This ensures that observed performance degradation results from skill suppression rather than underlying incapability. Second, **capability assurance**: selected models must demonstrate accurate task completion when no forgetting constraints are applied, validating that they possess the target skills before attempting suppression. Third, **architectural diversity**: the chosen models represent different training regimes and alignment characteristics, enabling analysis of how model architecture affects controllability.

### 4.3.3 Inference Configuration

All experiments used deterministic decoding with temperature set to 0 to ensure reproducible behavior. Standard API endpoints were used for all models with fixed decoding parameters across experiments to prevent confounding variation from generation settings.

---

## 4.4 Prompting Strategies

### 4.4.1 Rule-Based Strategy

The rule-based prompting strategy relies on explicit behavioral constraints encoded as direct instructions. The prompt components include:

- An instruction directing the model to answer correctly for mastered skills
- An instruction directing the model to produce consistent mistakes for forgotten skills

This approach operates through direct specification of desired behavior, leveraging the model's instruction-following capabilities to enforce the skill forgetting constraints.

### 4.4.2 Few-Shot Strategy

The few-shot prompting strategy employs demonstration examples that illustrate the desired response patterns. The prompt components include:

- Skill-aligned examples showing correct responses for mastered skills
- Skill-aligned examples showing incorrect responses for forgotten skills
- External file retrieval for example selection to prevent data leakage from evaluation questions

This approach relies on pattern matching through examples, allowing the model to infer the appropriate response behavior from demonstrated instances.

### 4.4.3 Combined Strategy (Hybrid)

The combined strategy integrates both explicit behavioral rules and concrete demonstration examples. The prompt components include:

- Explicit behavioral rules defining desired response patterns
- Concrete demonstrations reinforcing the specified rules

This approach exploits the complementary effects of rules and examples: rules provide explicit behavioral definitions while examples demonstrate how those rules apply to specific cases.

### 4.4.4 Unified Prompt Architecture

All prompting strategies follow a consistent structural architecture:

1. Student mastery profile: Explicit description of mastered versus missing skills
2. Behavioral instructions and/or examples: Rules and demonstrations encoding the desired response patterns
3. Target multiple-choice question: The mathematics problem requiring a response
4. Output instruction: Direction to provide a single answer selection with no explanation

This unified architecture ensures fair comparison across prompting strategies by controlling for structural variability.

---

## 4.5 Experimental Protocol

### 4.5.1 Experiment Stages

We conducted experiments across four sequential stages:

**Stage 1: Perfect Student Baseline.** We established the upper-bound performance by evaluating each model on all questions without applying forgetting constraints. This stage validates that models can solve the tasks correctly when no skill suppression is attempted, ensuring that any subsequent performance degradation results from controllable forgetting rather than model incapability.

**Stage 2: Controlled Skill Forgetting.** We systematically deactivated selected skills by specifying mastery vectors with $k_i = 0$ for targeted competencies. We then evaluated selective suppression versus retention by measuring per-skill accuracy against the specified mastery vector. This stage directly tests the core hypothesis that models can be directed to forget specific skills.

**Stage 3: Prompt Ablation.** We compared rule-based, few-shot, and combined prompting strategies under identical student profiles. This stage isolates the effect of prompt design on controllability, identifying which strategy most effectively enforces skill-level control.

**Stage 4: Variance Analysis.** We assessed stability across repeated executions to determine reproducibility of controllable forgetting effects. This stage ensures that observed results are reliable rather than artifacts of particular generation instances.

### 4.5.2 Student Profile Enumeration

For a system with K skills, there exist $2^K$ possible distinct mastery vectors. We conducted exhaustive enumeration of all possible skill configurations, evaluating each configuration separately. This approach provides complete coverage of the configuration space, enabling analysis of all possible imperfect student profiles and ensuring that controllability generalizes across the full range of skill combinations.

### 4.5.3 Experimental Dimensions

Our experiments span three orthogonal dimensions:

- **Student profiles** ($2^K$ configurations): All possible mastery vectors representing different learning-gap profiles
- **Skill-tagged questions** (m questions per grade): Question sets annotated with their corresponding skill domains
- **Language models** (i models): Claude, DeepSeek, and GPT-4o

The complete experimental grid examines every combination of these dimensions, enabling comprehensive analysis of controllable forgetting across all factors.

---

## 4.6 Evaluation Metrics

### 4.6.1 Per-Skill Accuracy

Per-skill accuracy is computed as the proportion of correct responses within each skill domain:

$$\text{Accuracy}(s_i) = \frac{\text{correct\_responses}_{s_i}}{\text{total\_items}_{s_i}}$$

This metric enables direct comparison between observed performance and the mastery vector specification, forming the foundation for all higher-level controllability assessments.

### 4.6.2 Root Mean Squared Error (RMSE)

RMSE measures the overall deviation between the intended skill vector and observed accuracy:

$$RMSE = \sqrt{\frac{1}{K} \sum_{i=1}^{K} (k_i - A_{ctrl}(s_i))^2}$$

Lower RMSE indicates better alignment between intended and observed behavior. This metric captures deviation from the ideal binary mastery pattern, where forgotten skills should yield zero accuracy and retained skills should yield perfect accuracy.

### 4.6.3 Relative Loss

Relative loss quantifies selective forgetting independent of baseline capability. For a forgotten skill ($k = 0$):

$$RL(s_i) = \frac{A_{base}(s_i) - A_{ctrl}(s_i)}{A_{base}(s_i)}$$

For a retained skill ($k = 1$):

$$RL(s_i) = \frac{A_{ctrl}(s_i) - A_{base}(s_i)}{A_{base}(s_i)}$$

Interpretation: For forgotten skills ($k=0$), $RL \rightarrow 1$ is desirable, indicating maximal forgetting. For retained skills ($k=1$), $RL \rightarrow 0$ is desirable, indicating no degradation. This metric separates compliance with the forgetting specification from underlying model capability.

### 4.6.4 Controllability Score

The controllability score measures overall adherence to the mastery vector:

$$CS = \frac{1}{K} \sum_{i=1}^{K} f(k_i, A_{ctrl}(s_i))$$

where the alignment function $f$ penalizes deviation from intended behavior:

$$f(k_i, A_{ctrl}) = \begin{cases} 1 - A_{ctrl} & \text{if } k_i = 0 \text{ (forgotten)} \\ A_{ctrl} & \text{if } k_i = 1 \text{ (retailed)} \end{cases}$$

Properties: The score rewards correct forgetting ($k=0 \rightarrow$ low accuracy) and penalizes unintended degradation of retained skills. It is independent of absolute baseline performance, enabling fair comparison across models with different underlying capabilities. CS = 1 indicates perfect simulation of the intended student profile; CS = 0 indicates no controllable behavior.

### 4.6.5 Cross-Skill Influence Matrix

The cross-skill influence matrix detects unintended interference between skills. Structure: A K $\times$ K matrix **M** where:

$$M_{ij} = \text{Performance change on skill } s_j \text{ when skill } s_i \text{ is forgotten}$$

The diagonal elements ($M_{ii}$) represent direct forgetting effectiveness for skill $s_i$. The off-diagonal elements ($M_{ij}, i \neq j$) represent the impact on skill $s_j$ when skill $s_i$ is forgotten. Under weak correlations, the expected retained performance should approximate baseline performance:

$$E[\text{Acc}_{retained} \mid \text{forget } s_i] \approx E[\text{Acc}_{retained}]$$

The ideal configuration exhibits high diagonal values (effective forgetting) with near-zero off-diagonal values (no interference). This metric characterizes whether skills can be manipulated independently.

### 4.6.6 Prediction Score

The prediction score quantifies alignment between expected and observed retained-skill accuracy:

$$PS = A_{actual} - A_{expected}$$

Interpretation: PS $\approx$ 0 indicates accurate alignment with theoretical expectations. PS $>$ 0 indicates better-than-expected retention. PS $<$ 0 indicates under-performance due to unintended degradation.

### 4.6.7 Skill Correlation Analysis

We additionally characterize dependencies between skill performances through Pearson correlation analysis over simulated student populations. Each simulated student is represented by a performance vector $[acc_{s_1}, acc_{s_2}, \ldots, acc_{s_K}]$, and correlation coefficients are computed between all skill pairs. Interpretation: Correlation coefficients near zero indicate independent skills; positive correlations indicate potential interference effects where performance on one skill affects another.

---

## 4.7 Aggregation and Analysis

### 4.7.1 Multi-Level Aggregation

We aggregate results at multiple levels to enable comprehensive analysis:

- **Per skill**: Individual skill behavior analysis examining each domain's response to forgetting manipulations
- **Per student profile**: Configuration-level evaluation examining the effectiveness of each mastery vector specification
- **Per model**: Cross-profile model comparison assessing which architectures best support controllable forgetting
- **Per prompt strategy**: Ablation comparison identifying which prompting approach most effectively enforces skill-level control

### 4.7.2 Statistical Analysis

We conduct variance analysis across repeated experimental runs to assess reproducibility. Significance testing using appropriate statistical tests (e.g., paired t-tests, Wilcoxon signed-rank tests) enables rigorous comparison between models and prompting strategies. Effect size calculations quantify the magnitude of differences between conditions, providing practical significance beyond statistical significance alone.
