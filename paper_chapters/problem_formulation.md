# 3. Problem Formulation

This chapter formalizes the problem of controllable skill forgetting in large language models. We establish mathematical notation, define the key concepts, and introduce the evaluation metrics that underpin our framework.

---

## 3.1 Formal Definitions

### Definition 1: Skill Domains

Let **S** denote the set of skill domains:

$$S = \{s_1, s_2, \ldots, s_K\}$$

where **K** represents the total number of distinct skill domains under consideration.

### Definition 2: Mastery Vector

Let **K** denote the mastery vector, a K-dimensional binary vector:

$$K = \{k_1, k_2, \ldots, k_K\}, \quad k_i \in \{0, 1\}$$

where:
- $k_i = 1$: The student has **retained** (mastered) skill $s_i$
- $k_i = 0$: The student has **forgotten** (not mastered) skill $s_i$

### Definition 3: Perfect Student

A **perfect student** is represented by a fully activated mastery vector:

$$K_{perfect} = \{1, 1, \ldots, 1\}$$

This configuration implies full mastery across all skills.

### Definition 4: Imperfect Student

An **imperfect student** with learning gaps is represented by a partially deactivated vector:

$$K_{imperfect} = \{1, 0, 1, \ldots, 1\}$$

where specific skills are intentionally suppressed to simulate realistic knowledge gaps.

---

## 3.2 Objective

The objective is **not** to reduce global performance, but to induce **structured, domain-specific deficiencies** that reflect realistic student profiles.

For each skill $s_i$:
- Let $A_{base}(s_i)$ denote the **baseline accuracy** without forgetting constraints
- Let $A_{ctrl}(s_i)$ denote the **accuracy under controlled prompt**

---

## 3.3 Relative Loss Metric

### Purpose
Quantify selective forgetting independent of baseline capability.

### Formulation

For a **forgotten skill** ($k = 0$):

$$RL(s_i) = \frac{A_{base}(s_i) - A_{ctrl}(s_i)}{A_{base}(s_i)}$$

For a **retained skill** ($k = 1$):

$$RL(s_i) = \frac{A_{ctrl}(s_i) - A_{base}(s_i)}{A_{base}(s_i)}$$

### Interpretation

| Condition | Formula | Desirability |
|-----------|---------|--------------|
| Forgotten skill ($k=0$) | $RL \rightarrow 1$ | **Desirable** (maximal forgetting) |
| Retained skill ($k=1$) | $RL \rightarrow 0$ | **Desirable** (no degradation) |

### Intuition
- When $k=0$ and $RL=1$: $A_{ctrl}=0$ (complete forgetting)
- When $k=1$ and $RL=0$: $A_{ctrl}=A_{base}$ (perfect retention)

---

## 3.4 Controllability Score

### Purpose
Overall adherence to the mastery vector across all skills.

### Formulation

$$CS = \frac{1}{K} \sum_{i=1}^{K} f(k_i, A_{ctrl}(s_i))$$

where $f$ is an alignment function penalizing deviation from intended behavior:

$$f(k_i, A_{ctrl}) = \begin{cases} 1 - A_{ctrl} & \text{if } k_i = 0 \text{ (forgotten)} \\ A_{ctrl} & \text{if } k_i = 1 \text{ (retained)} \end{cases}$$

### Properties
- **Rewards**: Correct forgetting ($k=0 \rightarrow$ low accuracy)
- **Penalizes**: Unintended degradation of retained skills
- **Independence**: From absolute baseline performance

### Interpretation
- Higher CS indicates better controllability
- CS = 1: Perfect simulation of intended student profile
- CS = 0: No controllable behavior

---

## 3.5 Root Mean Squared Error (RMSE)

### Purpose
Measure overall deviation between intended skill vector and observed accuracy.

### Formulation

$$RMSE = \sqrt{\frac{1}{K} \sum_{i=1}^{K} (k_i - A_{ctrl}(s_i))^2}$$

### Interpretation
- **RMSE = 0**: Perfect alignment (binary accuracy matches skill vector)
- **Lower RMSE**: Better controllability
- Captures deviation from ideal binary pattern

---

## 3.6 Cross-Skill Influence Matrix

### Purpose
Detect unintended interference between skills.

### Structure
A K × K matrix **M** where:

$$M_{ij} = \text{Performance change on skill } s_j \text{ when skill } s_i \text{ is forgotten}$$

### Elements

| Element | Description |
|---------|-------------|
| **Diagonal** ($M_{ii}$) | Direct forgetting effectiveness for skill $s_i$ |
| **Off-diagonal** ($M_{ij}, i \neq j$) | Impact on skill $s_j$ when $s_i$ is forgotten |

### Ideal Behavior
- Diagonal elements: High (effective forgetting)
- Off-diagonal elements: Near zero (no interference)

### Mathematical Formulation

Under weak correlations, the expected retained performance is:

$$E[\text{Acc}_{retained} \mid \text{forget } s_i] \approx E[\text{Acc}_{retained}]$$

This validates that skills can be controlled independently.

---

## 3.7 Prediction Score

### Purpose
Quantify alignment between expected and observed retained-skill accuracy.

### Formulation

$$PS = A_{actual} - A_{expected}$$

### Interpretation

| Score | Meaning |
|-------|---------|
| PS ≈ 0 | Accurate alignment with theoretical expectation |
| PS > 0 | Better-than-expected retention |
| PS < 0 | Under-performance, unintended degradation |

---

## 3.8 Relationship Between Metrics

The metrics form a coherent evaluation framework:

```
┌─────────────────────────────────────────────────────────────┐
│                    CONTROLLABILITY                         │
│                                                              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐      │
│  │   RMSE      │    │  Relative   │    │  Cross-Skill │      │
│  │ (Alignment) │    │    Loss     │    │   Influence  │      │
│  └─────────────┘    └─────────────┘    └─────────────┘      │
│         │                  │                  │              │
│         └──────────────────┼──────────────────┘              │
│                            │                                 │
│                            ▼                                 │
│                   ┌─────────────┐                          │
│                   │  Skill-Level │                          │
│                   │   Accuracy   │                          │
│                   └─────────────┘                          │
│                            │                                 │
│         ┌─────────────────┼─────────────────┐               │
│         │                 │                 │               │
│         ▼                 ▼                 ▼               │
│  ┌────────────┐    ┌────────────┐    ┌────────────┐        │
│  │  Retained  │    │ Forgoten   │    │ Prediction │        │
│  │  Skills    │    │  Skills    │    │   Score    │        │
│  └────────────┘    └────────────┘    └────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

---

## 3.9 Key Research Question

**Central Question:**
> Can we configure a prompted LLM to selectively forget certain skills and knowledge while reliably retaining others?

### Sub-Questions

1. **Prompt Effectiveness**: Which prompting strategies best enforce skill-level control?
2. **Model Variation**: How do different model architectures affect controllability?
3. **Skill Independence**: Can skills be manipulated independently without interference?
4. **Generalization**: Does controllability transfer across grade levels and task distributions?

---

## 3.10 Experimental Hypotheses

Based on the theoretical framework, we hypothesize:

### H1: Controllability Achievability
> LLMs can be directed to selectively forget specified skills through appropriately designed prompts.

### H2: Prompt Strategy Impact
> Combined prompting strategies (rules + demonstrations) will achieve better controllability than either approach alone.

### H3: Skill Independence
> Skills can be controlled independently, with weak inter-skill correlations enabling localized forgetting.

### H4: Model Dependence
> Controllability will vary significantly across model architectures due to differences in training and alignment.

### H5: Localization
> Forgetting effects will localize to targeted skills without substantial degradation of retained competencies.
