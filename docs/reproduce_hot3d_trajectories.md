# Reproducing HOT3D Trajectories

This note explains how to reproduce HOT3D trajectories using the official
toolkit, then export them into TRACE-friendly files.

## What "Trajectory" Means In HOT3D

HOT3D contains several trajectory types:

- Device/headset trajectory: `headset_trajectory.csv`
- Object pose trajectories: `dynamic_objects.csv`
- Hand wrist pose trajectories: `umetrack_hand_pose_trajectory.jsonl` and
  `mano_hand_pose_trajectory.jsonl`
- SLAM trajectories: `mps/slam/open_loop_trajectory.csv` and
  `mps/slam/closed_loop_trajectory.csv`
- Eye gaze trajectory-like stream: `mps/eye_gaze/*.csv`

The official tutorial states that device, hand, and object poses are shared in
world coordinates and measured in meters.

## Official Viewer Path

The official README reproduces trajectories with `viewer.py`, which uses
Rerun for visualization.

Run:

```bash
source /home/yifu/miniconda3/etc/profile.d/conda.sh
conda activate hot3d
cd /home/yifu/hot3d/hot3d

python3 viewer.py \
  --sequence_folder /home/yifu/TRACE/data/hot3d/P0003_c701bd11 \
  --object_library_folder /home/yifu/TRACE/data/hot3d/assets \
  --hand_type UMETRACK
```

If the GUI viewer does not open in WSL, save a Rerun file instead:

```bash
python3 viewer.py \
  --sequence_folder /home/yifu/TRACE/data/hot3d/P0003_c701bd11 \
  --object_library_folder /home/yifu/TRACE/data/hot3d/assets \
  --hand_type UMETRACK \
  --rrd_output_path /home/yifu/TRACE/outputs/hot3d/P0003_c701bd11_viewer.rrd
```

For a faster preview, our local HOT3D checkout has a small compatibility patch
that adds `--max_frames` and adapts the Rerun time API for `rerun-sdk==0.16.1`:

```bash
python3 viewer.py \
  --sequence_folder /home/yifu/TRACE/data/hot3d/P0003_c701bd11 \
  --object_library_folder /home/yifu/TRACE/data/hot3d/assets \
  --hand_type UMETRACK \
  --rrd_output_path /home/yifu/TRACE/outputs/hot3d/P0003_c701bd11_viewer_300.rrd \
  --max_frames 300
```

Current quick-preview output:

`/home/yifu/TRACE/outputs/hot3d/P0003_c701bd11_viewer_300.rrd`

Note: the local patch modifies `/home/yifu/hot3d/hot3d/viewer.py`. It changes
`rr.set_time(...)` to `rr.set_time_nanos(...)` / `rr.set_time_sequence(...)`,
matching the official notebook style.

## Official Tutorial Logic

The official notebook `HOT3D_Tutorial.ipynb` shows the key logic:

- Initialize `Hot3dDataProvider`.
- Use `device_pose_data_provider.get_pose_at_timestamp(...)`.
- Extract `T_world_device`.
- Append `T_world_device.translation()[0]` to a list.
- Log the trajectory with `rr.LineStrips3D`.

For hands, the tutorial uses:

- `umetrack_hand_data_provider` or `mano_hand_data_provider`
- `hand_data_provider.get_pose_at_timestamp(...)`
- each hand pose's `wrist_pose`
- `rr.LineStrips3D` for left/right wrist trajectories

## TRACE Export Path

We added a simple exporter that mirrors the official logic but writes CSV files:

```bash
source /home/yifu/miniconda3/etc/profile.d/conda.sh
conda activate hot3d

python /home/yifu/TRACE/scripts/export_hot3d_trajectories.py
```

Outputs:

- `/home/yifu/TRACE/outputs/hot3d/trajectories/P0003_c701bd11_headset.csv`
- `/home/yifu/TRACE/outputs/hot3d/trajectories/P0003_c701bd11_objects.csv`

Current result:

```text
headset trajectory rows: 7200
object trajectory rows: 42332
```

## Plot Exported Trajectories

Generate a static 3D plot:

```bash
source /home/yifu/miniconda3/etc/profile.d/conda.sh
conda activate hot3d

python /home/yifu/TRACE/scripts/plot_hot3d_trajectories.py
```

Output:

`/home/yifu/TRACE/outputs/hot3d/P0003_c701bd11_trajectories.png`

## Notes

- The official viewer is the best way to reproduce the full visual experience:
  RGB streams, hands, objects, and trajectories.
- The TRACE exporter is better for research code because it produces simple CSV
  files that can be plotted, scored, and converted into a trajectory schema.
- For the first TRACE milestone, use the exported headset/object trajectories
  plus mask-based quality metrics.
