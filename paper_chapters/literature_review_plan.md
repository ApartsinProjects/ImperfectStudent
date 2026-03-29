# Literature Review Plan

## Overview
This literature review establishes the theoretical and empirical foundations for controllable skill forgetting in LLM-based educational simulation. The review is organized into six thematic sections, progressing from educational applications to technical foundations.

---

## Theme 1: Teacher Professional Development & Simulation-Based Training

### 1.1 Novice Teacher Challenges
- Transition from academic preparation to classroom practice
- Induction programs and mentorship
- Emotional support and professional identity formation
- Burnout and attrition rates among beginning teachers

### 1.2 Deliberate Practice Framework
- Ericsson's expertise acquisition theory
- Need for repeated, structured engagement with targeted challenges
- Constraints of authentic classroom environments
- Role of feedback in skill development

### 1.3 Computational Simulation in Teacher Training
- Historical development of educational simulations
- Virtual standardized patients (medicine)
- Intelligent tutoring systems
- **Gap**: Need for imperfect student simulation specifically

---

## Theme 2: LLM-Based Educational Simulation

### 2.1 Generative Agents in Education
- Zhang et al. (2024): LLM-empowered classroom agents
- Sun et al. (2024): Scalable, personalized learning environments
- Differentiated student behavior simulation
- Intentional error generation

### 2.2 Generative Students
- Lu & Wang (2024): Binary mastery vectors for learner simulation
- Skill profile conditioning
- **Gap**: Focus on control mechanisms and measurement of forgetting

### 2.3 Current Limitations
- Qualitative alignment studies
- Lack of quantitative behavioral adherence metrics
- No systematic evaluation of controllability

---

## Theme 3: Behavioral Control in Large Language Models

### 3.1 Persona Conditioning
- PersonaLLM (Feng et al., 2023): Stylistic and personality consistency
- Maintaining traits across interactions
- Perfect coherence challenges

### 3.2 Instruction Following
- Model alignment techniques
- Reward modeling and RLHF
- Susceptibility to behavioral modification
- **Key tension**: Alignment strength vs. controllability flexibility

### 3.3 Prompt Engineering for Behavior
- Few-shot learning mechanisms
- Chain-of-thought prompting
- Constraint satisfaction approaches
- **Gap**: Systematic comparison of prompting strategies for forgetting

---

## Theme 4: Machine Unlearning & Knowledge Removal

### 4.1 Fact Forgetting
- Machine unlearning algorithms
- Gradient-based forgetting
- SISA training
- Knowledge deletion for privacy

### 4.2 Distinction from Skill Forgetting
| Fact Forgetting | Skill Forgetting |
|-----------------|------------------|
| Discrete assertions | Generalizable competencies |
| Clear boundaries | Ambiguous edges |
| Binary (known/unknown) | Continuous (mastery levels) |
| Random errors when forgotten | Systematic errors reflecting misconceptions |
| Easy measurement | Requires pattern analysis |

### 4.3 Conceptual Challenges
- Definition of skill boundaries
- Skill hierarchies and dependencies
- Transfer and interference effects
- **Gap**: No prior work on prompt-based skill forgetting

---

## Theme 5: Knowledge Tracing & Learner Modeling

### 5.1 Classical Approaches
- Bayesian Knowledge Tracing (BKT)
- Item Response Theory
- Frog溜ler Learning Factors
- Extensions and hybrid models

### 5.2 Deep Learning Approaches
- Deep Knowledge Tracing (Piech et al., 2015)
- Dynamic Key-Value Memory Networks (Zhang et al., 2017)
- Self-Attentive Knowledge Tracing (Pandey & Karypis, 2019)
- Comparative evaluation (Gervet et al., 2020)

### 5.3 LLM-Based Skill Gap Identification
- SkillGapGPT (2025): LLM annotation alignment
- Strengths and limitations of current approaches
- **Connection**: Detection vs. Induction of knowledge gaps

---

## Theme 6: Evaluation Methodologies in Educational AI

### 6.1 Traditional Metrics
- Accuracy, RMSE, AUC, precision, recall, F1
- Designed for prediction, not control
- Limitation: Cannot distinguish forgetting from difficulty

### 6.2 Controllability Evaluation
- Emerging concept in LLM research
- Behavioral alignment metrics
- Profile adherence measurement
- **Gap**: No standardized controllability benchmarks

### 6.3 Benchmark Design Principles
- Reproducibility requirements
- Standardized test conditions
- Curated datasets with skill annotations
- Multi-dimensional evaluation

---

## Synthesis: Research Gaps

Based on the literature review, we identify the following gaps that motivate this work:

1. **No framework for controllable skill forgetting** in LLMs
2. **No distinction** between fact forgetting and skill forgetting methodologies
3. **No measurement framework** for evaluating controllability (vs. accuracy)
4. **No benchmark** for standardized controllability assessment
5. **Limited understanding** of how different models respond to forgetting instructions
6. **Gap between detection and induction** of knowledge gaps (knowledge tracing vs. simulation)

---

## Key Citations to Include

### Foundational
- Ericsson, K. A., et al. (1993). The role of deliberate practice. *Psychological Review*
- Ingersoll, R. M., & Strong, M. (2011). Impact of induction programs. *Review of Educational Research*

### LLM Simulation
- Zhang, X., et al. (2024). LLM-powered classroom simulation agents
- Sun, Z., et al. (2024). LLM-driven educational simulations
- Lu, X., & Wang, Y. (2024). Generative students

### Behavioral Control
- Feng, S., et al. (2023). PersonaLLM: Persona consistency in LLMs

### Knowledge Tracing
- Piech, C., et al. (2015). Deep knowledge tracing. *NeurIPS*
- Zhang, J., et al. (2017). Dynamic key-value memory networks
- Gervet, T., et al. (2020). Deep learning for knowledge tracing

### Machine Unlearning
- Bourtoule, L., et al. (2021). Machine unlearning. *IEEE S&P*
- Nguyen, H., et al. (2022). Adapting membership disclosure tests

---

## Structure Recommendation

```
2. Literature Review (2500-3000 words)
   2.1 Teacher Training and Simulation-Based Learning (400 words)
   2.2 LLM-Based Educational Simulation (400 words)
   2.3 Behavioral Control in Large Language Models (400 words)
   2.4 Machine Unlearning and Knowledge Removal (400 words)
   2.5 Knowledge Tracing and Learner Modeling (400 words)
   2.6 Evaluation Methodologies in Educational AI (300 words)
   2.7 Synthesis and Research Gaps (200 words)
```
