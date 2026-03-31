#!/usr/bin/env python3
"""
Generate the revised camera-ready figure set for the version6 manuscript.

The data below is taken from:
- Final Report.docx
- extracted_experimental_results.md

The goal is to keep each figure focused on one claim and to avoid repeating
the same evidence in both a table and a figure.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyBboxPatch, Patch, Rectangle


ROOT = Path(__file__).resolve().parent


RMSE_DATA = {
    "Grade 4": {"Hybrid": 0.08, "Example-only": 0.46, "Instruction-only": 0.49, "Reference": 0.25},
    "Grade 5": {"Hybrid": 0.12, "Example-only": 0.58, "Instruction-only": 0.59, "Reference": 0.25},
}

PROFILE_CASE_STUDY = {
    "S4.1": [0.88, 0.04, 0.04, 0.85, 0.88, 0.85],
    "S4.2": [0.92, 0.12, 0.04, 0.04, 0.12, 0.92],
    "S4.3": [1.00, 0.00, 0.00, 0.00, 1.00, 0.00],
    "S4.4": [0.79, 0.12, 0.79, 0.79, 0.17, 0.12],
}

PROFILE_LABELS = [
    "Perfect\n[1,1,1,1]",
    "All forgotten\n[0,0,0,0]",
    "Profile A\n[0,0,0,1]",
    "Profile B\n[1,0,0,1]",
    "Profile C\n[1,0,1,0]",
    "Profile D\n[1,1,0,0]",
]

PROFILE_TARGETS = np.array(
    [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
    ]
)

TARGET_STRIP_LABELS = list(PROFILE_CASE_STUDY.keys())

RETAINED_FORGOTTEN = {
    "Grade 4": {
        "Claude": {"Retained": 98.2, "Forgotten": 7.6},
        "DeepSeek": {"Retained": 93.8, "Forgotten": 22.0},
        "GPT-4o": {"Retained": 84.9, "Forgotten": 32.2},
    },
    "Grade 5": {
        "Claude": {"Retained": 98.2, "Forgotten": 16.2},
        "DeepSeek": {"Retained": 103.7, "Forgotten": 38.4},
        "GPT-4o": {"Retained": 98.7, "Forgotten": 36.4},
    },
}

FORGOTTEN_HEATMAP = {
    "Grade 4": {
        "rows": ["Claude", "DeepSeek", "GPT-4o"],
        "cols": [
            "S4.1",
            "S4.2",
            "S4.3",
            "S4.4",
        ],
        "values": np.array(
            [
                [0.04, 0.07, 0.00, 0.16],
                [0.17, 0.39, 0.10, 0.11],
                [0.25, 0.20, 0.38, 0.10],
            ]
        ),
    },
    "Grade 5": {
        "rows": ["Claude", "DeepSeek", "GPT-4o"],
        "cols": [
            "S5.1",
            "S5.2",
            "S5.3",
        ],
        "values": np.array(
            [
                [0.09, 0.09, 0.20],
                [0.34, 0.31, 0.32],
                [0.11, 0.31, 0.23],
            ]
        ),
    },
}

CORRELATIONS = {
    "Grade 4": {
        "labels": [
            "S4.1",
            "S4.2",
            "S4.3",
            "S4.4",
        ],
        "values": np.array(
            [
                [1.00, -0.10, -0.10, -0.10],
                [-0.10, 1.00, -0.10, -0.10],
                [-0.10, -0.10, 1.00, -0.10],
                [-0.10, -0.10, -0.10, 1.00],
            ]
        ),
    },
    "Grade 5": {
        "labels": [
            "S5.1",
            "S5.2",
            "S5.3",
        ],
        "values": np.array(
            [
                [1.00, -0.16, -0.24],
                [-0.16, 1.00, -0.10],
                [-0.24, -0.10, 1.00],
            ]
        ),
    },
}


PALETTE = {
    "ink": "#14324a",
    "ink_soft": "#426378",
    "accent": "#0f766e",
    "accent_soft": "#8bd3c7",
    "warm": "#d97745",
    "warm_soft": "#f3c4a8",
    "muted": "#d9e2ea",
    "grid": "#e8eef3",
    "border": "#cbd6df",
    "gold": "#c59b2a",
}


def set_style() -> None:
    sns.set_theme(style="whitegrid")
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.spines.left": False,
            "axes.spines.bottom": False,
            "axes.facecolor": "white",
            "figure.facecolor": "white",
            "axes.edgecolor": PALETTE["border"],
            "grid.color": PALETTE["grid"],
            "grid.linewidth": 0.8,
            "axes.titleweight": "bold",
            "axes.labelcolor": PALETTE["ink"],
            "text.color": PALETTE["ink"],
            "xtick.color": PALETTE["ink_soft"],
            "ytick.color": PALETTE["ink_soft"],
            "axes.titlesize": 14,
            "axes.labelsize": 11,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "legend.frameon": False,
        }
    )


def save_figure(fig: plt.Figure, stem: str) -> None:
    png_path = ROOT / f"{stem}.png"
    svg_path = ROOT / f"{stem}.svg"
    fig.savefig(png_path, dpi=300, bbox_inches="tight")
    fig.savefig(svg_path, bbox_inches="tight")
    plt.close(fig)


def annotation_color(value: float, threshold: float) -> str:
    return "white" if value >= threshold else PALETTE["ink"]


def build_pipeline_figure() -> None:
    fig, ax = plt.subplots(figsize=(12.0, 4.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    def box(x: float, y: float, w: float, h: float, title: str, body: str, face: str) -> None:
        patch = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.02,rounding_size=0.025",
            linewidth=1.4,
            edgecolor=PALETTE["border"],
            facecolor=face,
        )
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h - 0.055, title, ha="center", va="top", fontsize=12, fontweight="bold")
        ax.text(x + 0.02, y + h - 0.12, body, ha="left", va="top", fontsize=10, linespacing=1.35)

    box(
        0.03,
        0.53,
        0.18,
        0.28,
        "Student Profiles",
        "Enumerate binary mastery vectors\nacross retained and suppressed\nskills for each grade.",
        "#eef6fb",
    )
    box(
        0.28,
        0.53,
        0.22,
        0.28,
        "Prompt Conditions",
        "Instruction-only\nExample-only\nHybrid",
        "#f3fbf8",
    )
    box(
        0.57,
        0.53,
        0.16,
        0.28,
        "LLM Inference",
        "Claude\nDeepSeek\nGPT-4o",
        "#fbf7ef",
    )
    box(
        0.79,
        0.53,
        0.18,
        0.28,
        "Scored Outputs",
        "One answer per item,\naggregated by skill,\nprofile, and model.",
        "#f9f3f2",
    )

    box(
        0.20,
        0.12,
        0.22,
        0.20,
        "Benchmark Items",
        "Skill-tagged multiple-choice\nquestions reused across\nprofiles within each grade.",
        "#f7fafc",
    )
    box(
        0.55,
        0.12,
        0.28,
        0.20,
        "Evaluation",
        "RMSE to target profile\nCalibration and prediction score\nRetained vs forgotten summaries",
        "#f7fafc",
    )

    arrow = dict(arrowstyle="-|>", lw=1.6, color=PALETTE["ink_soft"], shrinkA=6, shrinkB=6)
    ax.annotate("", xy=(0.28, 0.67), xytext=(0.21, 0.67), arrowprops=arrow)
    ax.annotate("", xy=(0.57, 0.67), xytext=(0.50, 0.67), arrowprops=arrow)
    ax.annotate("", xy=(0.79, 0.67), xytext=(0.73, 0.67), arrowprops=arrow)
    ax.annotate("", xy=(0.68, 0.32), xytext=(0.88, 0.53), arrowprops=arrow)
    ax.annotate("", xy=(0.39, 0.53), xytext=(0.31, 0.32), arrowprops=arrow)
    ax.annotate("", xy=(0.55, 0.22), xytext=(0.42, 0.22), arrowprops=arrow)

    ax.text(
        0.5,
        0.93,
        "Main Experiment Pipeline",
        ha="center",
        va="center",
        fontsize=15,
        fontweight="bold",
    )
    save_figure(fig, "figure_02")


def build_rmse_figure() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.4), sharex=True, sharey=True)

    strategy_order = ["Hybrid", "Example-only", "Instruction-only"]
    strategy_colors = {
        "Hybrid": PALETTE["accent"],
        "Example-only": PALETTE["warm_soft"],
        "Instruction-only": PALETTE["warm"],
    }

    for ax, (grade, values) in zip(axes, RMSE_DATA.items()):
        y = np.arange(len(strategy_order))
        x = [values[name] for name in strategy_order]
        bars = ax.barh(y, x, color=[strategy_colors[name] for name in strategy_order], height=0.55)
        ax.axvline(values["Reference"], color=PALETTE["ink_soft"], lw=1.4, ls=(0, (4, 3)))
        ax.set_xlim(0, 0.65)
        ax.set_xlabel("RMSE (lower is better)")
        ax.set_yticks(y, labels=strategy_order)
        ax.invert_yaxis()
        ax.set_title(grade, pad=10)

        for bar, val in zip(bars, x):
            ax.text(val + 0.015, bar.get_y() + bar.get_height() / 2, f"{val:.2f}", va="center", fontsize=10)

    fig.subplots_adjust(top=0.80, bottom=0.18, wspace=0.18)
    save_figure(fig, "fig03_prompt_rmse")


def build_profile_case_figure() -> None:
    fig = plt.figure(figsize=(11.0, 5.6))
    gs = fig.add_gridspec(2, 1, height_ratios=[0.62, 3.7], hspace=0.08)
    ax_top = fig.add_subplot(gs[0])
    ax = fig.add_subplot(gs[1])

    target_cmap = LinearSegmentedColormap.from_list("target", ["#f1f5f9", PALETTE["accent"]])
    sns.heatmap(
        PROFILE_TARGETS,
        ax=ax_top,
        cmap=target_cmap,
        cbar=False,
        linewidths=1,
        linecolor="white",
        vmin=0,
        vmax=1,
        xticklabels=PROFILE_LABELS,
        yticklabels=TARGET_STRIP_LABELS,
    )
    ax_top.set_xlabel("")
    ax_top.set_ylabel("Target\nmastery", rotation=0, labelpad=36, va="center")
    ax_top.tick_params(axis="x", labelbottom=False, bottom=False)
    ax_top.tick_params(axis="y", rotation=0)

    accuracy = np.array(list(PROFILE_CASE_STUDY.values()))
    acc_cmap = LinearSegmentedColormap.from_list("accuracy", ["#f8fbff", "#b8d5ea", PALETTE["ink"]])
    sns.heatmap(
        accuracy,
        ax=ax,
        cmap=acc_cmap,
        linewidths=1,
        linecolor="white",
        vmin=0,
        vmax=1,
        cbar_kws={"label": "Observed accuracy"},
        xticklabels=PROFILE_LABELS,
        yticklabels=list(PROFILE_CASE_STUDY.keys()),
    )
    ax.set_xlabel("Student profile")
    ax.set_ylabel("Skill")
    ax.tick_params(axis="x", rotation=0)
    ax.tick_params(axis="y", rotation=0)

    for row in range(accuracy.shape[0]):
        for col in range(accuracy.shape[1]):
            value = accuracy[row, col]
            ax.text(
                col + 0.5,
                row + 0.5,
                f"{value:.2f}",
                ha="center",
                va="center",
                fontsize=10,
                color=annotation_color(value, 0.55),
                fontweight="bold",
            )
            ax_top.text(
                col + 0.5,
                row + 0.5,
                str(int(PROFILE_TARGETS[row, col])),
                ha="center",
                va="center",
                fontsize=10,
                color=annotation_color(PROFILE_TARGETS[row, col], 0.5),
                fontweight="bold",
            )

    legend_handles = [
        Patch(facecolor=PALETTE["accent"], label="target retained (1)"),
        Patch(facecolor="#f1f5f9", label="target forgotten (0)"),
    ]
    ax.legend(handles=legend_handles, loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=2)
    save_figure(fig, "fig04_profile_case_study")


def build_retained_vs_forgotten_figure() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.8), sharex=True, sharey=True)
    model_order = ["Claude", "DeepSeek", "GPT-4o"]
    percent_formatter = FuncFormatter(lambda x, pos: f"{int(x)}%")

    for ax, (grade, values) in zip(axes, RETAINED_FORGOTTEN.items()):
        y = np.arange(len(model_order))[::-1]
        retained = [values[model]["Retained"] for model in model_order]
        forgotten = [values[model]["Forgotten"] for model in model_order]

        for idx, model in enumerate(model_order):
            ax.plot(
                [forgotten[idx], retained[idx]],
                [y[idx], y[idx]],
                color=PALETTE["muted"],
                lw=3,
                solid_capstyle="round",
                zorder=1,
            )
            ax.scatter(retained[idx], y[idx], s=90, color=PALETTE["ink"], zorder=3)
            ax.scatter(forgotten[idx], y[idx], s=90, color=PALETTE["warm"], zorder=3)
            ax.annotate(
                f"{retained[idx]:.1f}%",
                xy=(retained[idx], y[idx]),
                xytext=(6, 8),
                textcoords="offset points",
                fontsize=10,
                color=PALETTE["ink"],
            )
            ax.annotate(
                f"{forgotten[idx]:.1f}%",
                xy=(forgotten[idx], y[idx]),
                xytext=(6, -18),
                textcoords="offset points",
                fontsize=10,
                color=PALETTE["warm"],
            )

        ax.axvline(100, color=PALETTE["ink_soft"], lw=1.2, ls=(0, (4, 3)))
        ax.set_title(grade)
        ax.set_yticks(y, labels=model_order)
        ax.set_xlim(0, 112)
        ax.set_xticks(np.arange(0, 101, 20))
        ax.xaxis.set_major_formatter(percent_formatter)
        ax.grid(axis="x", alpha=0.8)
        ax.grid(axis="y", visible=False)

    legend_handles = [
        Patch(facecolor=PALETTE["ink"], label="Retained"),
        Patch(facecolor=PALETTE["warm"], label="Forgotten"),
    ]
    fig.legend(handles=legend_handles, loc="lower center", bbox_to_anchor=(0.5, 0.02), ncol=2)
    fig.subplots_adjust(top=0.82, bottom=0.18, wspace=0.15)
    save_figure(fig, "fig05_retained_vs_forgotten")


def build_forgotten_heatmap_figure() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.8))
    cmap = LinearSegmentedColormap.from_list(
        "suppression",
        ["#0f766e", "#8fd1c1", "#f8f4ec", "#edb38f", "#c55a2d"],
    )

    for idx, (ax, (grade, spec)) in enumerate(zip(axes, FORGOTTEN_HEATMAP.items())):
        sns.heatmap(
            spec["values"],
            ax=ax,
            cmap=cmap,
            vmin=0,
            vmax=0.40,
            linewidths=1,
            linecolor="white",
            cbar=ax is axes[-1],
            cbar_kws={"label": "Forgotten-skill accuracy"} if ax is axes[-1] else None,
            xticklabels=spec["cols"],
            yticklabels=spec["rows"] if idx == 0 else False,
        )
        ax.set_title(grade)
        ax.tick_params(axis="x", rotation=0)
        ax.tick_params(axis="y", rotation=0, length=0)
        ax.set_xlabel("")
        ax.set_ylabel("")

        if idx > 0:
            ax.tick_params(axis="y", left=False, labelleft=False)

        for row in range(spec["values"].shape[0]):
            for col in range(spec["values"].shape[1]):
                value = spec["values"][row, col]
                ax.text(
                    col + 0.5,
                    row + 0.5,
                    f"{value:.2f}",
                    ha="center",
                    va="center",
                    fontsize=10,
                    color=annotation_color(value / 0.40, 0.55),
                    fontweight="bold",
                )

    fig.subplots_adjust(wspace=0.22)
    save_figure(fig, "fig06_forgotten_heatmap")


def draw_correlation_panel(ax: plt.Axes, title: str, labels: list[str], values: np.ndarray) -> None:
    mask = np.eye(values.shape[0], dtype=bool)
    off_diag = values.copy()
    off_diag[mask] = np.nan

    cmap = LinearSegmentedColormap.from_list("corr", ["#cf6a32", "#f7efe8", "#eef5f9", PALETTE["ink"]])
    sns.heatmap(
        off_diag,
        ax=ax,
        cmap=cmap,
        vmin=-0.30,
        vmax=0.10,
        center=0,
        linewidths=1,
        linecolor="white",
        cbar=False,
        xticklabels=labels,
        yticklabels=labels,
    )

    for idx in range(values.shape[0]):
        ax.add_patch(Rectangle((idx, idx), 1, 1, facecolor="#dfe7ee", edgecolor="white", lw=1))
        ax.text(idx + 0.5, idx + 0.5, "1.00", ha="center", va="center", fontsize=10, color=PALETTE["ink"], fontweight="bold")

    for row in range(values.shape[0]):
        for col in range(values.shape[1]):
            if row == col:
                continue
            ax.text(
                col + 0.5,
                row + 0.5,
                f"{values[row, col]:.2f}",
                ha="center",
                va="center",
                fontsize=10,
                color=PALETTE["ink"],
                fontweight="bold",
            )

    ax.set_title(title)
    ax.tick_params(axis="x", rotation=0)
    ax.tick_params(axis="y", rotation=0)
    ax.set_xlabel("")
    ax.set_ylabel("")


def build_correlation_figure() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.0))
    for idx, (ax, (grade, spec)) in enumerate(zip(axes, CORRELATIONS.items())):
        draw_correlation_panel(ax, grade, spec["labels"], spec["values"])
        if idx == 1:
            ax.set_yticklabels([])
            ax.tick_params(axis="y", left=False)

    norm = mpl.colors.Normalize(vmin=-0.30, vmax=0.10)
    cmap = LinearSegmentedColormap.from_list("corr_bar", ["#cf6a32", "#f7efe8", "#eef5f9", PALETTE["ink"]])
    sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([])
    fig.subplots_adjust(top=0.80, bottom=0.16, wspace=0.24, right=0.88)
    cbar = fig.colorbar(sm, ax=axes, shrink=0.78, pad=0.02)
    cbar.set_label("Off-diagonal Pearson correlation")
    save_figure(fig, "fig07_skill_correlation")


def main() -> None:
    set_style()
    build_pipeline_figure()
    build_rmse_figure()
    build_profile_case_figure()
    build_retained_vs_forgotten_figure()
    build_forgotten_heatmap_figure()
    build_correlation_figure()


if __name__ == "__main__":
    main()
