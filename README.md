# ImperfectStudent

**Toward a Benchmark for Controllable Simulation of Imperfect Students with Large Language Models**

Omir Sasson · Yehudit Aperstein · Alexander Apartsin

[Draft paper](https://apartsinprojects.github.io/ImperfectStudent/) · [BibTeX](#citation)

![A row of four schematic student figures at desks. Above each, a different binary skill vector. An LLM node at the top steers each profile through dashed control lines.](figures/hero.png)

> **Can a language model be steered to retain some skills while suppressing others, on demand?**
> We treat this as a measurement problem. A simulated student is represented as an
> explicit binary skill vector, and a frontier LLM is prompted to enact that vector.
> The benchmark asks how faithfully the resulting behavior matches the requested
> profile, separately from how accurate the underlying model is.

## Motivation

Teacher preparation programs need deliberate practice with realistic learners. A novice
teacher must learn to diagnose, scaffold, and respond to students who have specific
gaps, not students who answer everything correctly. Authentic classrooms supply this
variety but cannot be replayed, paused, or systematically varied for training purposes.
Simulation can, in principle, fill that gap.

The obstacle is that contemporary LLMs are too competent. Frontier models routinely
exceed 95% accuracy on curriculum-aligned mathematics, which makes them excellent
tutors and unconvincing students. Asking such a model to act like a fourth-grader
with a specific fraction misconception is not a knowledge problem; it is a *control*
problem. The model already knows the answer. The question is whether it can be
reliably steered into not producing it, on the right items, while remaining correct
on everything else.

We argue that **controllability** is a distinct evaluation axis from accuracy, and one
that current benchmarks do not measure. A model with strong instruction-following may
be highly controllable yet only moderately accurate; a model with state-of-the-art
accuracy may be largely uncontrollable, because its pretraining priors override the
prompt. Treating these as orthogonal is the starting point for everything that follows.

### Skill forgetting, not fact forgetting

Prior work on machine unlearning targets discrete facts with crisp boundaries
("the model no longer asserts X"). Skills are different. A skill such as "solving
linear equations" or "applying the Pythagorean theorem" is a family of related
competencies, lacks a sharp boundary, and produces *structured* errors when partially
mastered rather than random ones. Measuring whether a model has forgotten a skill is
therefore much harder than checking whether it has forgotten a fact, and is the
problem we set out to formalize.

## Research question

> Given a binary mastery specification over a fixed skill taxonomy, can a prompted
> LLM be made to behave like a student with exactly that profile, retaining
> mastered skills at near-baseline accuracy and suppressing forgotten skills toward
> chance, without collateral damage to skills it was supposed to keep?

Concretely, we ask four sub-questions:

1. **Prompt design.** Which prompting strategies enforce skill-level control?
2. **Model dependence.** How much does controllability vary across frontier models?
3. **Skill independence.** Can skills be manipulated locally, or does suppressing one degrade others?
4. **Generalization.** Does whatever works transfer across grade levels and task distributions?

## Framework

We represent a simulated student by a binary mastery vector

$$K = (k_1, k_2, \ldots, k_K), \quad k_i \in \{0, 1\}$$

over $K$ skill domains drawn from a curriculum-aligned taxonomy (U.S. Common Core,
via MathCAMPS, restricted to Grade 4 and Grade 5). $k_i = 1$ means the student has
retained skill $s_i$; $k_i = 0$ means the student has forgotten it. The vector is
translated into a natural-language student profile and used to prompt the LLM under
one of three strategies (rule-based, few-shot, combined).

Controllability is then measured against, not conflated with, baseline accuracy.
The key metrics are:

- **Relative loss** per skill, normalized by the model's own baseline accuracy on that skill, so a controllable but weak model is not penalized for being weak.
- **Controllability score**, an alignment between the requested vector $K$ and the observed per-skill accuracy.
- **RMSE** between $K$ and the observed accuracy vector, giving a single scalar fit.
- **Cross-skill influence matrix**, a $K \times K$ matrix capturing how forgetting one skill perturbs the others. The diagonal measures targeted forgetting; the off-diagonals measure unintended interference.
- **Prediction score**, the gap between retained-skill accuracy that is *expected* under skill independence and what is actually observed, isolating spillover effects.

The full formalism is in [paper_chapters/problem_formulation.md](paper_chapters/problem_formulation.md).

## Key findings

We evaluated three frontier models (Claude, GPT-4o, DeepSeek) on Grade 4 and Grade 5
of MathCAMPS, under all three prompting strategies. The headline results:

1. **Controllability is achievable but model-dependent.** Claude reduced accuracy on forgotten skills to roughly 0.05 to 0.15 while holding retained skills at 0.85 to 0.92. GPT-4o landed at 0.20 to 0.35 on forgotten skills; DeepSeek at 0.30 to 0.40, despite comparable baseline accuracy. High baseline accuracy did not predict high controllability.
2. **Prompt design is necessary but not sufficient.** Rules alone (RMSE 0.50 to 0.60) and few-shot examples alone (RMSE 0.45 to 0.60) both perform poorly. The combined strategy collapses RMSE to 0.08 to 0.12, a roughly fivefold improvement. Either component in isolation is not enough.
3. **Skills are predominantly independent.** Pearson correlations between per-skill performances are near zero in Grade 4 and only weakly negative in Grade 5 (roughly -0.1 to -0.24), meaning the skill-vector framework's independence assumption is approximately satisfied and selective forgetting localizes.
4. **Localization breaks down model-by-model.** Claude's retained-skill accuracy tracks the independence prediction tightly; GPT-4o systematically underperforms it, indicating residual cross-skill interference even when the requested skill is "retained."

A condensed view is in [paper_chapters/results.md](paper_chapters/results.md); figures
live in [figures/](figures/).

## Contributions

1. A **formal problem formulation** that distinguishes controllability from accuracy and skill forgetting from fact forgetting, with notation for mastery vectors, baseline-relative accuracy, and per-skill control.
2. A **benchmark framework** built on a curated, skill-balanced 100-item subset of MathCAMPS per grade, with cross-model error filtering and standardized four-option multiple choice.
3. A **measurement toolkit** of four complementary metrics (relative loss, controllability score, cross-skill influence, prediction score) that together separate genuine selective forgetting from baseline difficulty and from broad performance collapse.
4. **An empirical comparison** of three frontier LLMs under three prompting strategies, showing that controllability and accuracy decouple and that the best-controllable model is not the highest-accuracy one.
5. **A reproducible protocol** for evaluating skill-aware behavioral control as future LLMs are released.

## Repo contents

```
ImperfectStudent/
  paper_chapters/      Paper source, one markdown file per section
  figures/             Figures used in the paper, plus the hero banner
  paper_v5_final.html  Self-contained HTML paper (current version)
  reviews/             Reviewer notes
```

## Citation

```bibtex
@article{sasson2026imperfectstudent,
  title   = {Toward a Benchmark for Controllable Simulation of Imperfect Students
             with Large Language Models},
  author  = {Sasson, Omir and Aperstein, Yehudit and Apartsin, Alexander},
  year    = {2026},
  url     = {https://apartsinprojects.github.io/ImperfectStudent/}
}
```
