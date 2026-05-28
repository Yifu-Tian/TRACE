#!/usr/bin/env python3
"""Compute a first TRACE quality report from HOT3D mask files."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from statistics import mean


MASK_FILES = {
    "headset_pose_validity": "mask_headset_pose_available.csv",
    "object_pose_validity": "mask_object_pose_available.csv",
    "hand_pose_validity": "mask_hand_pose_available.csv",
    "object_visibility": "mask_object_visible.csv",
    "hand_visibility": "mask_hand_visible.csv",
    "good_exposure": "mask_good_exposure.csv",
    "qa_pass_rate": "mask_qa_pass.csv",
}

TRACE_WEIGHTS = {
    "headset_pose_validity": 0.20,
    "object_pose_validity": 0.15,
    "hand_pose_validity": 0.15,
    "object_visibility": 0.15,
    "hand_visibility": 0.15,
    "good_exposure": 0.10,
    "qa_pass_rate": 0.10,
}


def parse_bool(value: str) -> bool:
    return value.strip().lower() in {"true", "1", "yes", "y"}


def load_mask_rates(mask_path: Path) -> dict[str, float]:
    counts: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    with mask_path.open("r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            stream_id = row["stream_id"]
            counts[stream_id][0] += int(parse_bool(row["mask"]))
            counts[stream_id][1] += 1

    return {
        stream_id: true_count / total_count
        for stream_id, (true_count, total_count) in counts.items()
        if total_count > 0
    }


def aggregate_metric(stream_rates: dict[str, float]) -> float | None:
    if not stream_rates:
        return None
    return mean(stream_rates.values())


def compute_quality_report(sequence_folder: Path) -> dict:
    masks_folder = sequence_folder / "masks"
    if not masks_folder.exists():
        raise FileNotFoundError(f"Missing masks folder: {masks_folder}")

    metrics = {}
    per_stream = {}
    missing_masks = []

    for metric_name, filename in MASK_FILES.items():
        mask_path = masks_folder / filename
        if not mask_path.exists():
            missing_masks.append(filename)
            metrics[metric_name] = None
            per_stream[metric_name] = {}
            continue

        stream_rates = load_mask_rates(mask_path)
        per_stream[metric_name] = stream_rates
        metrics[metric_name] = aggregate_metric(stream_rates)

    weighted_terms = [
        value * TRACE_WEIGHTS[name]
        for name, value in metrics.items()
        if value is not None
    ]
    used_weight = sum(
        TRACE_WEIGHTS[name] for name, value in metrics.items() if value is not None
    )
    trace_score_v0 = sum(weighted_terms) / used_weight if used_weight else None

    ranked_failures = sorted(
        (
            {
                "metric": name,
                "score": value,
                "weight": TRACE_WEIGHTS[name],
            }
            for name, value in metrics.items()
            if value is not None
        ),
        key=lambda item: item["score"],
    )

    return {
        "trajectory_id": sequence_folder.name,
        "sequence_folder": str(sequence_folder),
        "metrics": metrics,
        "per_stream": per_stream,
        "trace_score_v0": trace_score_v0,
        "lowest_scoring_metrics": ranked_failures[:3],
        "missing_masks": missing_masks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sequence-folder",
        type=Path,
        default=Path("/home/yifu/TRACE/data/hot3d/P0003_c701bd11"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("/home/yifu/TRACE/outputs/hot3d/P0003_c701bd11_quality.json"),
    )
    args = parser.parse_args()

    report = compute_quality_report(args.sequence_folder)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"trajectory_id: {report['trajectory_id']}")
    print(f"trace_score_v0: {report['trace_score_v0']:.4f}")
    print("metrics:")
    for name, value in report["metrics"].items():
        if value is None:
            print(f"  {name}: missing")
        else:
            print(f"  {name}: {value:.4f}")
    print("lowest_scoring_metrics:")
    for item in report["lowest_scoring_metrics"]:
        print(f"  {item['metric']}: {item['score']:.4f}")
    print(f"wrote: {args.output}")


if __name__ == "__main__":
    main()
