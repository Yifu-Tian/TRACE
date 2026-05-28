#!/usr/bin/env python3
"""Plot exported HOT3D trajectories as a simple 3D figure."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt


def load_headset_points(path: Path) -> list[tuple[float, float, float]]:
    points = []
    with path.open("r", newline="") as f:
        for row in csv.DictReader(f):
            points.append((float(row["x_m"]), float(row["y_m"]), float(row["z_m"])))
    return points


def load_object_points(path: Path) -> dict[str, list[tuple[float, float, float]]]:
    points = defaultdict(list)
    with path.open("r", newline="") as f:
        for row in csv.DictReader(f):
            points[row["object_uid"]].append(
                (float(row["x_m"]), float(row["y_m"]), float(row["z_m"]))
            )
    return dict(points)


def downsample(points: list[tuple[float, float, float]], max_points: int):
    if len(points) <= max_points:
        return points
    stride = max(1, len(points) // max_points)
    return points[::stride]


def plot_line(ax, points, label, linewidth=1.5):
    if not points:
        return
    xs, ys, zs = zip(*points)
    ax.plot(xs, ys, zs, label=label, linewidth=linewidth)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--trajectory-dir",
        type=Path,
        default=Path("/home/yifu/TRACE/outputs/hot3d/trajectories"),
    )
    parser.add_argument("--sequence-name", default="P0003_c701bd11")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("/home/yifu/TRACE/outputs/hot3d/P0003_c701bd11_trajectories.png"),
    )
    args = parser.parse_args()

    headset_csv = args.trajectory_dir / f"{args.sequence_name}_headset.csv"
    objects_csv = args.trajectory_dir / f"{args.sequence_name}_objects.csv"

    headset_points = load_headset_points(headset_csv)
    object_points = load_object_points(objects_csv)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")
    plot_line(ax, downsample(headset_points, 1000), "headset/device", linewidth=2.0)

    for object_uid, points in sorted(object_points.items()):
        plot_line(ax, downsample(points, 500), f"object {object_uid}", linewidth=1.0)

    ax.set_title(f"HOT3D Trajectories: {args.sequence_name}")
    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")
    ax.set_zlabel("z [m]")
    ax.legend(loc="best", fontsize=8)
    fig.tight_layout()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, dpi=200)
    print(f"wrote: {args.output}")


if __name__ == "__main__":
    main()
