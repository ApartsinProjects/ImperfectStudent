**Authors:** Omer Sasson, Alexander Apartsin, Yehuda Aperstein

# Abstract

Large language models achieve near-expert performance on structured mathematical benchmarks, frequently exceeding 95% accuracy across diverse assessments. While advantageous for reasoning applications, this capability poses a fundamental challenge for teacher training simulators, which require controllable, imperfect learners reflecting differentiated skill profiles rather than uniformly high accuracy.

This paper introduces a formal framework for controllable skill forgetting in LLMs, addressing the question: can a model be directed to selectively forget specified skills while reliably retaining others? We distinguish this from prior work on fact forgetting by focusing on skill-level forgetting at the level of generalizable competencies, where boundaries are inherently ambiguous and measurement challenges are substantially greater.

We present three primary contributions. First, we introduce a structured benchmark framework built upon curriculum-aligned mathematical data with explicit skill annotations, enabling reproducible evaluation across models and prompting strategies. Second, we develop a controllability measurement framework that introduces novel metrics including a relative loss formulation, skill-level controllability scores, and cross-skill influence analysis, thereby distinguishing controllability from raw performance. Third, we conduct extensive experiments across three frontier models under varied prompting strategies, revealing substantial variation in controllability: some models achieve near-complete selective forgetting with minimal interference, while others exhibit significant resistance or unintended degradation of retained skills.

Our findings demonstrate that controllability is achievable but model-dependent, highlighting the importance of both prompt design and model selection for educational simulation applications. We provide a reproducible methodology for evaluating skill-aware behavioral control, establishing a foundation for LLM-based systems that can reliably simulate the imperfect learners teachers encounter in authentic classroom settings.
