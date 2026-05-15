"""One-shot hero image generation for the ImperfectStudent README."""
from pathlib import Path
import json
import sys
import time

from google import genai
from google.genai import types

CONFIG = json.loads(Path.home().joinpath(".gemini-imagegen.json").read_text())
OUT = Path(r"E:\Claude\ImperfectStudent\interesting-gauss-1432cd\figures\hero.png")

PROMPT = """An editorial-quality scientific illustration for the cover of an academic research paper on "controllable simulation of imperfect students with large language models."

Composition: a horizontal 16:9 banner. Centered, a row of FOUR abstract, schematic "simulated student" figures seated at small wooden desks. Each figure is a clean, stylized silhouette, half human, half circuit-board (faint board traces visible inside the torso). The figures are calm, neutral, and identical in posture (slightly leaning forward, hands on desk), so the only thing distinguishing them is the skill state shown above.

Above each figure floats a horizontal "skill vector": a row of 6 small square cells. Some cells are FILLED with a single warm accent color (muted terracotta), and others are OUTLINED and dimmed (empty). Each of the four students shows a DIFFERENT pattern of filled / empty cells, conveying that each has been configured with a different selective skill profile (one with mostly filled, one with mostly empty, two mixed).

Above and slightly behind the row, near the top center, a small compact "LLM" glyph: an abstract neural-graph node with about 8 connected dots, drawn in the same flat style. Thin DASHED control-signal lines descend from this LLM glyph to each of the four skill vectors, suggesting that a single prompt is steering the imperfection of each student.

In the soft, far background: a large chalkboard wall, faintly visible, with sparse hand-drawn elementary math motifs gently drifting out of focus, fractions, a simple equation, a triangle with a right-angle mark, a small times-table fragment. Very low contrast, almost ghostly.

Palette: deep navy background, warm cream foreground figures and desks, a single muted terracotta accent for the lit skill cells and dashed control lines. Flat shapes with subtle paper texture, no photoreal humans, no children's faces, no clutter, NO text, NO captions, NO labels, NO logos. Generous negative space at top and sides. Academic, didactic, calm. Aspect ratio strictly 16:9, wide horizontal."""

def main() -> int:
    client = genai.Client(api_key=CONFIG["api_key"])
    model = "gemini-3-pro-image-preview"
    print(f"Generating hero image with {model} ...")

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=model,
                contents=PROMPT,
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE"],
                    image_config=types.ImageConfig(aspect_ratio="16:9", image_size="2K"),
                ),
            )
            break
        except Exception as exc:
            print(f"Attempt {attempt + 1} failed: {exc}")
            if attempt == 2:
                raise
            time.sleep(5 * (2 ** attempt))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    saved = False
    for part in response.parts:
        if getattr(part, "inline_data", None):
            part.as_image().save(OUT)
            print(f"Saved: {OUT}")
            saved = True
            break
    if not saved:
        print("No image returned by model.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
