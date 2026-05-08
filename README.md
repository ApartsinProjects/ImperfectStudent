# ImperfectStudent

**Toward a Benchmark for Controllable Simulation of Imperfect Students with Large Language Models**

Omri Sason · Alexander Apartsin · Yehudit Aperstein

[Draft paper](https://apartsinprojects.github.io/ImperfectStudent/) · [BibTeX](#citation)

> Can a language model be steered to retain some skills while suppressing others?
> We introduce a benchmark-oriented framework for controllable learner simulation,
> representing a student as an explicit skill vector and evaluating selective partial
> mastery in a structured mathematics setting.

## What is this?

Teacher education requires deliberate practice with learners who exhibit identifiable
strengths, weaknesses, and partial mastery. This project investigates whether prompted
language models can simulate such students in a controllable, measurable way.

The framework represents a simulated student as an explicit skill vector. Prompt-based
control specifies which competencies are retained and which are suppressed. Results show
that selective partial mastery can be induced and measured in a structured mathematics
setting, though the degree of controllability remains model-dependent.

## Repo contents

```
ImperfectStudent/
  paper_chapters/     Paper source (Markdown per section)
  figures/            Figures used in the paper
  paper_v5_final.html Self-contained paper (HTML)
  reviews/            Reviewer notes
```

## Citation

```bibtex
@article{sason2026imperfectstudent,
  title   = {Toward a Benchmark for Controllable Simulation of Imperfect Students
             with Large Language Models},
  author  = {Sason, Omri and Apartsin, Alexander and Aperstein, Yehudit},
  year    = {2026},
  url     = {https://apartsinprojects.github.io/ImperfectStudent/}
}
```
