# HOT3D Next Steps

The HOT3D repository has already been cloned to:

`/home/yifu/hot3d`

Use HOT3D as the first public dataset for TRACE V0 because it contains
egocentric hand-object interaction data and useful masks for visibility,
tracking availability, and QA.

## Immediate Goal

Download the smallest useful HOT3D subset and verify that we can read one Aria
sequence.

Recommended sequence:

`P0003_c701bd11`

Reason:

- It is listed in the HOT3D README as an example Aria training sequence.
- It should include ground-truth annotations.
- It is enough for a first TRACE smoke test.

## Step 1: Create The HOT3D Environment

The README supports Pixi and Conda. Conda is usually simpler if conda is already
installed.

From `/home/yifu/hot3d`:

```bash
conda create --name hot3d python=3.10 -y
conda activate hot3d
python3 -m ensurepip
python3 -m pip install projectaria_tools==1.5.1 torch requests rerun-sdk==0.16.0
python3 -m pip install vrs matplotlib
```

Optional hand rendering dependencies:

```bash
python3 -m pip install 'git+https://github.com/vchoutas/smplx.git'
python3 -m pip install 'git+https://github.com/mattloper/chumpy'
```

Skip the optional dependencies for the first smoke test unless the viewer or
hand rendering requires them.

## Step 2: Get HOT3D Download URL JSON Files

Manual web step:

1. Open the HOT3D website: `https://www.projectaria.com/datasets/hot3D/`
2. Review the license.
3. Sign up with email.
4. Keep the refreshed page open because the download view is ephemeral.
5. Download these JSON files:
   - `Hot3DAria_download_urls.json`
   - `Hot3DAssets_download_urls.json`

Place the JSON files in:

`/home/yifu/hot3d/hot3d/data_downloader/`

## Step 3: Download Minimal Data

Use TRACE's data directory as the output folder:

```bash
cd /home/yifu/hot3d/hot3d/data_downloader
mkdir -p /home/yifu/TRACE/data/hot3d

python3 dataset_downloader_base_main.py \
  -c Hot3DAssets_download_urls.json \
  -o /home/yifu/TRACE/data/hot3d \
  --sequence_name all

python3 dataset_downloader_base_main.py \
  -c Hot3DAria_download_urls.json \
  -o /home/yifu/TRACE/data/hot3d \
  --sequence_name P0003_c701bd11 \
  --data_types all
```

When prompted, type `y`.

## Step 4: Run The Official Viewer

After download, inspect the sequence:

```bash
cd /home/yifu/hot3d/hot3d
python3 viewer.py \
  --sequence_folder /home/yifu/TRACE/data/hot3d/P0003_c701bd11 \
  --object_library_folder /home/yifu/TRACE/data/hot3d/assets
```

If the viewer works, the official toolkit and data are healthy.

## Step 5: Run A Mask-Based Smoke Test

HOT3D provides useful masks that are almost perfect for TRACE V0:

- `mask_object_pose_available.csv`
- `mask_hand_pose_available.csv`
- `mask_headset_pose_available.csv`
- `mask_object_visibility.csv`
- `mask_hand_visible.csv`
- `mask_good_exposure.csv`
- `mask_qa_pass.csv`

First TRACE metric idea:

```text
sensor_validity = fraction(mask_headset_pose_available == True)
object_visibility = fraction(mask_object_visibility == True)
hand_visibility = fraction(mask_hand_visible == True)
hand_object_evidence = fraction(mask_hand_visible AND mask_object_visibility)
qa_pass_rate = fraction(mask_qa_pass == True)
```

This is enough to generate the first per-trajectory quality report before we
touch any deep learning.

## Step 6: Build TRACE Loader Outside HOT3D

Do not edit the official HOT3D repo for TRACE-specific logic.

Implement our code under:

`/home/yifu/TRACE/src/trace/`

First target script:

`/home/yifu/TRACE/scripts/hot3d_quality_smoke_test.py`

Expected output:

```text
trajectory_id: P0003_c701bd11
num_frames: ...
headset_pose_validity: ...
object_visibility: ...
hand_visibility: ...
hand_object_evidence: ...
qa_pass_rate: ...
trace_score_v0: ...
```

## What To Do First

The next concrete action is:

1. Create the `hot3d` conda environment.
2. Get the two download JSON files from the HOT3D website.
3. Download `assets` and `P0003_c701bd11`.
4. Run the viewer.
5. Then implement the TRACE smoke-test script.

## Progress Log

### 2026-05-28

Completed:

- Created the `hot3d` conda environment.
- Fixed a broken `requests` / `certifi` dependency in the environment.
- Downloaded HOT3D assets to `/home/yifu/TRACE/data/hot3d/assets`.
- Downloaded the Aria training sequence `P0003_c701bd11`.
- Verified that the sequence contains VRS, gaze, SLAM, hand data, object data,
  and mask CSV files.
- Added `scripts/hot3d_quality_smoke_test.py`.
- Generated the first TRACE V0 report:
  `/home/yifu/TRACE/outputs/hot3d/P0003_c701bd11_quality.json`.

Initial result:

```text
trajectory_id: P0003_c701bd11
trace_score_v0: 0.9776
headset_pose_validity: 1.0000
object_pose_validity: 0.8794
hand_pose_validity: 1.0000
object_visibility: 1.0000
hand_visibility: 0.9844
good_exposure: 1.0000
qa_pass_rate: 0.9806
```

Interpretation:

- This sequence is very high-quality, which makes sense for an official example
  training sequence.
- The lowest metric is object pose validity, so the smoke test already exposes
  at least one nontrivial quality signal.

Next:

- Download 2-3 additional Aria sequences, ideally including lower-quality or
  more varied examples.
- Compare TRACE V0 scores across sequences.
- Add stream-level reporting and simple plots.
- Convert the report into the formal TRACE trajectory schema.
