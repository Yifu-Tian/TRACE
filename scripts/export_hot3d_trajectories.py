#!/usr/bin/env python3
"""Export HOT3D headset and object trajectories to simple CSV files.

This mirrors the official HOT3D tutorial's trajectory reproduction logic, but
stores the points so TRACE can plot and score them later.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


HOT3D_REPO = Path("/home/yifu/hot3d/hot3d")
if str(HOT3D_REPO) not in sys.path:
    sys.path.insert(0, str(HOT3D_REPO))

from data_loaders.HeadsetPose3dProvider import (  # noqa: E402
    load_headset_pose_provider_from_csv,
)
from data_loaders.ObjectPose3dProvider import load_pose_provider_from_csv  # noqa: E402


def translation_xyz(se3_pose) -> tuple[float, float, float]:
    xyz = se3_pose.translation()[0]
    return float(xyz[0]), float(xyz[1]), float(xyz[2])


def export_headset_trajectory(sequence_folder: Path, output_path: Path) -> int:
    provider = load_headset_pose_provider_from_csv(
        str(sequence_folder / "headset_trajectory.csv")
    )

    with output_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp_ns", "x_m", "y_m", "z_m"])
        for timestamp_ns in provider.timestamp_ns_list:
            pose_with_dt = provider.get_pose_at_timestamp(
                timestamp_ns=timestamp_ns,
                time_query_options=__import__(
                    "projectaria_tools.core.sensor_data",
                    fromlist=["TimeQueryOptions"],
                ).TimeQueryOptions.CLOSEST,
                time_domain=__import__(
                    "projectaria_tools.core.sensor_data",
                    fromlist=["TimeDomain"],
                ).TimeDomain.TIME_CODE,
            )
            if pose_with_dt is None:
                continue
            x, y, z = translation_xyz(pose_with_dt.pose3d.T_world_device)
            writer.writerow([timestamp_ns, x, y, z])

    return len(provider.timestamp_ns_list)


def export_object_trajectories(sequence_folder: Path, output_path: Path) -> int:
    provider = load_pose_provider_from_csv(str(sequence_folder / "dynamic_objects.csv"))
    row_count = 0

    with output_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp_ns", "object_uid", "x_m", "y_m", "z_m"])
        for timestamp_ns in provider.timestamp_ns_list:
            collection = provider.get_pose_at_timestamp(
                timestamp_ns=timestamp_ns,
                time_query_options=__import__(
                    "projectaria_tools.core.sensor_data",
                    fromlist=["TimeQueryOptions"],
                ).TimeQueryOptions.CLOSEST,
                time_domain=__import__(
                    "projectaria_tools.core.sensor_data",
                    fromlist=["TimeDomain"],
                ).TimeDomain.TIME_CODE,
            )
            if collection is None:
                continue
            for object_uid, object_pose in collection.pose3d_collection.poses.items():
                x, y, z = translation_xyz(object_pose.T_world_object)
                writer.writerow([timestamp_ns, object_uid, x, y, z])
                row_count += 1

    return row_count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sequence-folder",
        type=Path,
        default=Path("/home/yifu/TRACE/data/hot3d/P0003_c701bd11"),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("/home/yifu/TRACE/outputs/hot3d/trajectories"),
    )
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    headset_output = args.output_dir / f"{args.sequence_folder.name}_headset.csv"
    object_output = args.output_dir / f"{args.sequence_folder.name}_objects.csv"

    headset_rows = export_headset_trajectory(args.sequence_folder, headset_output)
    object_rows = export_object_trajectories(args.sequence_folder, object_output)

    print(f"headset trajectory rows: {headset_rows}")
    print(f"wrote: {headset_output}")
    print(f"object trajectory rows: {object_rows}")
    print(f"wrote: {object_output}")


if __name__ == "__main__":
    main()
