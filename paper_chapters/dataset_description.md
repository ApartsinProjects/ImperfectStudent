# Dataset Description

This section describes the construction, preparation, and quality control procedures for the MathCAMPS benchmark dataset used to evaluate controllable skill forgetting in large language models. The dataset serves as the foundational resource for assessing whether LLM-based student simulations can be directed to exhibit predefined patterns of selective knowledge retention and forgetting aligned with authentic learner profiles.

## Data Source: MathCAMPS Dataset

The MathCAMPS (Mathematics Curriculum-Aligned Mathematical Problem Set) dataset comprises a comprehensive collection of mathematics problems sourced from curriculum-aligned educational materials mapped to United States Common Core State Standards. This dataset was selected as the primary data source for our benchmark for several interconnected reasons that align with the pedagogical objectives of controllable student simulation.

First, the Common Core standards provide a well-established and widely adopted educational framework that defines mathematical competencies across grade levels with explicit skill domains and learning progressions. This standardization enables precise skill annotation and ensures that the benchmark captures authentic mathematical competencies rather than idiosyncratic problem types. Second, the curriculum-aligned nature of MathCAMPS ensures that problems reflect developmentally appropriate content for each grade level, incorporating progressive complexity and scaffolding that mirrors authentic student learning trajectories. Third, the mathematical domain offers well-defined skill boundaries compared to more ambiguous educational domains, facilitating precise specification of mastery vectors and enabling clear evaluation criteria for skill forgetting.

The dataset encompasses mathematical competencies spanning grades 1 through 8, covering skill domains including but not limited to operations and algebraic thinking, number and operations in base ten, number and operations with fractions, measurement and data, geometry, and ratio and proportional relationships. Each problem within MathCAMPS is associated with a specific standard identifier that maps unambiguously to a skill domain, enabling systematic evaluation of model behavior across different competency areas.

## Skill Annotation: Mapping Educational Standards to Skills

The skill annotation framework adopted in this study operationalizes educational standards as discrete skill units that can be selectively activated or deactivated in student simulations. This annotation scheme transforms the hierarchical structure of Common Core standards into a flat representation of skill domains suitable for controllable generation.

Each question within the dataset carries a explicit skill tag corresponding to its associated Knowledge Component (KC), defined at the domain level of the standard hierarchy. For instance, a problem assessing "Solve word problems involving dollar bills, quarters, dimes, nickels, and pennies" (CCSS.MATH.CONTENT.2.MD.C.8) receives the skill annotation "money" within the broader Measurement and Data domain. This domain-level granularity balances specificity with practical manageability: finer-grained skill definitions would introduce excessive complexity in skill vector specification, while coarser definitions would obscure meaningful distinctions in competency areas.

The mapping from standards to skills follows a systematic aggregation protocol wherein related standards within a domain are consolidated into unified skill categories. This aggregation preserves the pedagogical structure of the curriculum while creating a tractable space of skill dimensions for experimental evaluation. The resulting annotation schema comprises a set of skills S = {s₁, s₂, ..., sₖ} where each sᵢ represents a distinct competency domain relevant to the corresponding grade level.

Mastery computation within this framework operates at the skill level, with accuracy calculated as the proportion of correctly answered questions within each skill domain. Formally, for a given skill sᵢ with associated question set Q(sᵢ), the per-skill accuracy A(sᵢ) is computed as:

A(sᵢ) = (1 / |Q(sᵢ)|) × Σ_{q∈Q(sᵢ)} [correct(q)]

where correct(q) equals 1 if the model produces the correct answer for question q and 0 otherwise. This per-skill accuracy metric serves as the primary outcome variable for evaluating alignment between intended mastery vectors and observed model behavior.

## Dataset Preparation: Grade-Level Splitting and Question Formatting

The dataset preparation procedure transforms the raw MathCAMPS collection into a structured benchmark suitable for systematic evaluation. This preparation involves grade-level stratification, question format standardization, and skill-balanced sampling to ensure robust and reproducible assessment.

### Grade-Level Stratification

The dataset is organized into eight grade-specific subsets corresponding to the elementary and middle school grade levels (grades 1-8) represented in the Common Core standards. Each grade-specific subset contains exactly 100 questions, creating a fixed experimental corpus that enables controlled comparison across grade levels while maintaining manageable computational requirements for large-scale evaluation with multiple models and prompting strategies.

The grade-level stratification serves multiple methodological purposes. First, it ensures developmental appropriateness of problems, as skills at different grade levels reflect distinct cognitive demands and prerequisite knowledge. Second, it enables analysis of controllability as a function of grade-level complexity, addressing whether skill forgetting becomes more or less controllable as mathematical content becomes more sophisticated. Third, it provides natural variation in skill domain composition across grades, as different mathematical topics become salient at different points in the curriculum.

### Question Format Standardization

All questions within the benchmark are converted to a standardized four-option multiple-choice format (options A through D) with precisely one correct answer. This standardization serves several practical and methodological functions. From a practical standpoint, multiple-choice format enables automated scoring without requiring sophisticated answer parsing or natural language inference, facilitating large-scale evaluation across hundreds of experimental conditions. From a methodological standpoint, the fixed response space enables direct comparison of model behavior across conditions and models, as the same question always presents identical response options.

The distractor options (incorrect answers) in each multiple-choice item are designed to be numerically close to the correct answer or conceptually plausible alternatives that reflect common student misconceptions. This distractor design ensures that incorrect responses represent meaningful cognitive errors rather than arbitrary guesses, which is essential for evaluating whether model errors under skill-forgetting conditions exhibit the systematic patterns characteristic of authentic learner behavior.

### Skill Balance Requirements

Within each grade-specific subset, questions are distributed to ensure approximately equal representation across skill domains. This balanced design prevents skill-level analyses from being confounded by uneven question distribution and ensures that per-skill accuracy metrics are computed over comparable sample sizes. The balance requirement means that for a grade with n skill domains, each domain contains approximately 100/n questions, with minor variations due to integer constraints and original dataset composition.

## Quality Control: Filtering, Detection, and Replacement

Quality control procedures ensure that the benchmark dataset exhibits the reliability and validity necessary for meaningful experimental conclusions. These procedures address multiple potential sources of measurement error and artifact that could compromise the interpretability of controllability assessments.

### Ambiguity Filtering

The ambiguity filtering stage identifies and removes questions that exhibit systematic ambiguity, poor construction, or content that does not cleanly map to a single skill domain. Questions are flagged as ambiguous when they meet any of the following criteria: the problem statement admits multiple reasonable interpretations that could lead to different correct answers; the correct answer depends on unstated assumptions about context or convention; the problem requires knowledge of material outside the indicated grade level or skill domain; or the distractors do not represent plausible student errors.

Ambiguity filtering employs both automated statistical analysis and manual expert review. Automated analysis identifies questions with unusual response patterns, such as those where the distribution of model responses across options significantly diverges from the expected pattern or where multiple models consistently select different answers. Questions flagged by automated analysis undergo manual review by experienced educators who assess whether the ambiguity reflects genuine problem quality issues or represents expected variation in problem-solving approaches.

### Cross-Model Error Detection

The cross-model error detection procedure identifies questions that cause systematic errors across multiple language models, as these errors may reflect problem quality issues rather than genuine differences in model controllability. When a question is answered incorrectly by the majority of evaluated models under baseline (full-mastery) conditions, it is flagged for review because such consistent failure suggests the question may be poorly constructed, require specialized knowledge not captured in standard curricula, or contain errors in the answer key.

Questions identified through cross-model error detection undergo the same dual review process as ambiguously flagged items, with automated statistical flags serving as indicators requiring expert adjudication rather than automatic exclusion. This approach recognizes that some questions may be genuinely difficult (and thus appropriately answered incorrectly by most models) while others may reflect dataset errors requiring correction.

### Replacement Strategy

Questions that fail quality control review are replaced using a stratified replacement strategy that preserves the original skill distribution and difficulty characteristics of the dataset. Replacement questions are selected from the broader MathCAMPS corpus based on the following criteria: the replacement must map to the same skill domain and grade level as the original question; the replacement must have demonstrated adequate performance in pilot testing (indicating clear correct answer and plausible distractors); and the replacement must maintain the overall balance of question counts across skill domains within the grade level.

This replacement strategy ensures that quality control procedures do not introduce systematic differences between grade-level subsets that could confound experimental comparisons. When sufficient replacement questions cannot be identified within the same skill domain and grade level, the affected skill domain receives reduced representation with documented justification, and this reduction is noted in dataset documentation.

### Final Dataset Characteristics

Following quality control procedures, the benchmark dataset comprises eight grade-specific subsets, each containing 100 questions distributed across skill domains. The total corpus encompasses 800 questions spanning grades 1-8, with comprehensive coverage of mathematical competency areas defined by the Common Core standards. Each question carries explicit skill annotations enabling per-skill accuracy computation, and all questions employ standardized four-option multiple-choice format with validated distractors.

## Per-Skill Mastery Computation

The computation of per-skill mastery enables evaluation of alignment between intended skill vectors and observed model behavior. Given a predefined mastery vector K = {k₁, k₂, ..., kₖ} where kᵢ ∈ {0, 1} indicates whether skill sᵢ should be retained (kᵢ = 1) or forgotten (kᵢ = 0), the per-skill accuracy computation provides the empirical foundation for assessing controllability.

For each experimental condition defined by a particular mastery vector K, each evaluated model produces responses to all questions in the grade-specific subset. These responses are then aggregated to compute per-skill accuracy values A(sᵢ) using the formula:

A(sᵢ) = (1 / |Q(sᵢ)|) × Σ_{q∈Q(sᵢ)} [correct(q)]

where Q(sᵢ) denotes the subset of questions tagged with skill sᵢ and correct(q) is the binary indicator for correct response as defined above.

The resulting accuracy vector A = {A(s₁), A(s₂), ..., A(sₖ)} constitutes the observed behavior that can be compared against the intended mastery vector K. Perfect controllability would manifest as A(sᵢ) ≈ 1 for all skills where kᵢ = 1 and A(sᵢ) ≈ 0 for all skills where kᵢ = 0. Deviations from this pattern indicate imperfect controllability, with the magnitude and structure of deviations providing insight into the nature and extent of control failures.

This per-skill accuracy computation serves as the basis for all subsequent evaluation metrics in our controllability assessment framework, including the relative loss formulation, controllability score, root mean squared error, and cross-skill influence matrix detailed in the Evaluation Metrics section.
