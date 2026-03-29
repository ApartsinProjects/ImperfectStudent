# Methods Section Plan

## Overview
The methods section describes the benchmark framework, experimental setup, and evaluation methodology for measuring controllable skill forgetting in LLMs.

---

## 4. Dataset Creation

### 4.1 Data Source: MathCAMPS Dataset
- **Description**: Curriculum-aligned mathematics problems mapped to U.S. Common Core standards
- **Structure**: Educational standards mapped to Domains = Skills
- **Grade Coverage**: Grades 1-8
- **Question Format**: Multiple-choice (A-D) with balanced distractors

### 4.2 Dataset Preparation
- **Grade-level splitting**: 8 separate grade-specific datasets (100 questions each)
- **Question conversion**: All items converted to 4-option multiple-choice format
- **Distractor design**: Numerically close or conceptually plausible alternatives
- **Skill balance**: Equal distribution across skill domains per grade

### 4.3 Quality Control
- **Ambiguity filtering**: Identify systematically ambiguous/poorly constructed items
- **Cross-model error detection**: Items causing repeated errors across models flagged
- **Replacement strategy**: Replace problematic items from same educational standard
- **Balance preservation**: Maintain skill distribution after replacement

### 4.4 Skill Annotation
- **Annotation scheme**: Each question tagged with corresponding skill/Knowledge Component (KC)
- **Granularity**: Domain-level skill assignment
- **Mastery computation**: Per-skill accuracy = correct responses / total items for skill

---

## 5. Controllable Generative Student Framework

### 5.1 Problem Formulation

#### Skill Vector Representation
```
S = {s₁, s₂, ..., sₖ}  : Set of skill domains
K = {k₁, k₂, ..., kₖ}  : Mastery vector where kᵢ ∈ {0, 1}
                          kᵢ = 1 → retained skill
                          kᵢ = 0 → forgotten skill
```

#### Student Configurations
- **Perfect Student**: K = {1,1,...,1} (full mastery)
- **Imperfect Student**: K = {1,0,...,1} (selective forgetting)

#### Notation
- **A_base**: Baseline accuracy without forgetting constraints
- **A_ctrl**: Accuracy under controlled prompt

### 5.2 Architecture: Controllable Generative Student

**Pipeline Components:**
1. **Binary Skill Vector Input**: k = {1,0,...,1}
2. **Vector-to-Text Translation**: Convert mastery vector to explicit skill categories
3. **Student Profile Prompt**: Structured prompt encoding knowledge state
4. **LLM Generation**: Answer prediction conditioned on skill profile
5. **Output Collection**: Standardized answer format (single option)

**Prompt Template Structure:**
- Mastered skills description
- Missing/forgotten skills description
- Behavioral instructions (for rule-based)
- Demonstration examples (for few-shot)
- Target question

---

## 6. Model Selection

### 6.1 Evaluated Models

| Model | Provider | Characteristics | Selection Rationale |
|-------|----------|-----------------|---------------------|
| Claude | Anthropic | Safety-aligned, strong instruction-following | Known compliance with behavioral constraints |
| DeepSeek | DeepSeek | High-performance, reasoning-optimized | Strong math capabilities |
| GPT-4o | OpenAI | General-purpose, widely used | Baseline comparison |

### 6.2 Selection Criteria
- **Baseline performance**: All models evaluated on MathCAMPS; only high-performing models selected
- **Capability assurance**: Models must accurately solve tasks before skill suppression
- **Architectural diversity**: Different training regimes and alignment characteristics

### 6.3 Inference Configuration
- **Temperature**: 0 (deterministic behavior)
- **Decoding**: Fixed parameters across experiments
- **API access**: Standardized endpoints

---

## 7. Prompting Strategies

### 7.1 Rule-Based Strategy
**Approach**: Explicit behavioral constraints
**Components**:
- Instruction to answer correctly for mastered skills
- Instruction to produce consistent mistakes for forgotten skills
**Rationale**: Direct specification of desired behavior

### 7.2 Few-Shot Strategy
**Approach**: Demonstration examples
**Components**:
- Skill-aligned examples showing correct responses (mastered)
- Skill-aligned examples showing incorrect responses (forgotten)
- External file retrieval (no data leakage)
**Rationale**: Pattern matching through examples

### 7.3 Combined Strategy (Hybrid)
**Approach**: Rules + Examples
**Components**:
- Explicit behavioral rules
- Concrete demonstrations reinforcing rules
**Rationale**: Complementary effect - rules define, examples demonstrate

### 7.4 Prompt Architecture (Unified)
All prompts follow consistent structure:
1. Student mastery profile (mastered vs. missing skills)
2. Behavioral instructions and/or examples
3. Target multiple-choice question
4. Output instruction (single answer, no explanation)

---

## 8. Experimental Protocol

### 8.1 Experiment Stages

**Stage 1: Perfect Student Baseline**
- Establish upper-bound performance
- Validate models can solve tasks correctly
- Ensure later degradation from skill suppression, not incapacity

**Stage 2: Controlled Skill Forgetting**
- Systematically deactivate selected skills
- Evaluate selective suppression vs. retention
- Measure per-skill accuracy against mastery vector

**Stage 3: Prompt Ablation**
- Compare rule-based, few-shot, and combined strategies
- Isolate effect of prompt design on controllability
- Under identical student profiles

**Stage 4: Variance Analysis**
- Stability across repeated executions
- Reproducibility assessment

### 8.2 Student Profile Enumeration
- **Exhaustive enumeration**: All 2^K possible skill vectors for K skills
- **Configuration space**: Each vector represents distinct learning-gap profile
- **Coverage**: Full space of imperfect student configurations

### 8.3 Experimental Dimensions
```
Dimensions:
- Student profiles (1...n): 2^K distinct configurations
- Skill-tagged questions (1...m): Per-grade question sets
- Language models (1...i): Claude, DeepSeek, GPT-4o
```

### 8.4 Test Grades
- **Primary**: Grade 4 and Grade 5
- **Rationale**: Fixed skill domains, balanced distributions, internal consistency

---

## 9. Evaluation Metrics

### 9.1 Per-Skill Accuracy
**Definition**: Accuracy computed per skill domain
**Formula**: correct_responses_skill / total_items_skill
**Use**: Direct comparison with mastery vector

### 9.2 Relative Loss (Novel Metric)

**Purpose**: Quantify selective forgetting independent of baseline

**Formula**:
```
For forgotten skill (k=0):  RL = A_base - A_ctrl / A_base
For retained skill (k=1):  RL = A_ctrl - A_base / A_base
```

**Interpretation**:
- Forgotten skill (k=0): RL → 1 is desirable (maximal forgetting)
- Retained skill (k=1): RL → 0 is desirable (no degradation)

**Advantage**: Separates compliance from baseline capability

### 9.3 Controllability Score (Novel Metric)

**Purpose**: Overall adherence to mastery vector

**Formula**:
```
CS = (1/K) * Σᵢ f(kᵢ, A_skill_i)

Where:
- K = number of skills
- kᵢ = mastery indicator (0=forgotten, 1=retained)
- A_skill_i = accuracy on skill i
- f = alignment function penalizing deviation
```

**Properties**:
- Rewards correct forgetting (k=0 → low accuracy)
- Penalizes unintended degradation (k=1 → high accuracy required)
- Independent of absolute baseline performance

### 9.4 RMSE (Root Mean Squared Error)

**Purpose**: Alignment between intended skill vector and observed accuracy

**Formula**:
```
RMSE = sqrt(1/K * Σᵢ (kᵢ - A_skill_i)²)
```

**Interpretation**:
- Lower RMSE = better alignment
- Captures deviation from binary mastery pattern

### 9.5 Cross-Skill Influence Matrix (Novel Metric)

**Purpose**: Detect unintended interference between skills

**Structure**: K×K matrix where:
- **Diagonal**: Direct forgetting effectiveness for skill i
- **Off-diagonal**: Impact on skill j when skill i is forgotten

**Interpretation**:
- Ideal: Localized degradation (diagonal effects only)
- Realistic: Some off-diagonal interference acceptable
- **Goal**: Minimize collateral impact on retained skills

**Mathematical formulation**:
```
P_ret | forget_i ≈ P_ret  (if skills are truly independent)
```

Conditional expectation under weak correlations:
```
E[performance_on_ret | forget_i] ≈ E[performance_on_ret]
```

### 9.6 Prediction Score (Novel Metric)

**Purpose**: Quantify alignment between expected and observed retained-skill accuracy

**Formula**:
```
PS = A_actual - A_expected
```

**Interpretation**:
- PS ≈ 0: Accurate alignment with theoretical expectation
- PS > 0: Better-than-expected retention
- PS < 0: Under-performance, unintended degradation

### 9.7 Skill Correlation Analysis

**Purpose**: Characterize dependencies between skill performances

**Method**: Pearson correlation matrix over n simulated students
- Each student: performance vector [acc_skill1, acc_skill2, ...]
- Compute correlation between skill performances

**Interpretation**:
- |ρ| ≈ 0: Independent skills
- |ρ| > 0: Potential interference

---

## 10. Aggregation and Analysis

### 10.1 Multi-Level Aggregation
- **Per skill**: Individual skill behavior analysis
- **Per student profile**: Configuration-level evaluation
- **Per model**: Cross-profile model comparison
- **Per prompt strategy**: Ablation comparison

### 10.2 Visualization
- Per-skill accuracy heatmaps
- Retained vs. forgotten comparison plots
- Expected vs. actual scatter plots
- Correlation matrices
- RMSE bar charts

### 10.3 Statistical Analysis
- Variance across runs
- Significance testing for model comparisons
- Effect size for prompt strategy differences

---

## Structure Summary

```
4. Dataset Description
   4.1 MathCAMPS Dataset and Skill Annotation
   4.2 Dataset Preparation and Quality Control

5. Controllable Generative Student Framework
   5.1 Problem Formulation and Notation
   5.2 Architecture and Prompt Design

6. Experimental Setup
   6.1 Model Selection
   6.2 Prompting Strategies
   6.3 Experimental Protocol

7. Evaluation Metrics
   7.1 Per-Skill Accuracy and RMSE
   7.2 Relative Loss and Controllability Score
   7.3 Cross-Skill Influence Analysis
   7.4 Prediction Score
```
