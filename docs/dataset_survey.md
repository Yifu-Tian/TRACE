# Dataset Survey

This file tracks public datasets that can support TRACE before lab data
collection starts.

## Recommendation

Start with **HOT3D** if the first TRACE prototype should be manipulation-centric.
Start with **Aria Digital Twin** if the first prototype should be Project
Aria-tooling-centric.

Important distinction:

- These are public research datasets, not "open-source" in the same sense as
  MIT/BSD code.
- Access usually requires accepting dataset-specific license terms.
- Some parts may have different licenses, so check the specific data type before
  redistribution or commercial use.

For TRACE, the best practical order is:

1. HOT3D: hand-object interaction quality.
2. Aria Digital Twin: Aria tooling, gaze, object visibility, scene grounding.
3. Ego-Exo4D: larger-scale skilled activity, proficiency, and task progress.

## HOT3D

Use case:

- Prototype hand-object and manipulation-related quality metrics.

Access / license status:

- Publicly available research dataset.
- Downloaded through Project Aria / HOT3D tooling.
- Released under the HOT3D dataset license agreement.
- Different data types have different terms; for example, hand annotations are
  more restricted than some sequence data.

Relevant modalities:

- Project Aria and Quest egocentric recordings
- 3D hand pose
- 3D object pose
- 2D bounding boxes
- object models
- Aria eye gaze
- Aria semi-dense point cloud

TRACE metrics it can support:

- hand visibility
- object visibility
- hand-object tracking continuity
- gaze-object alignment
- interaction evidence
- manipulation smoothness proxies

Risks:

- The task setting may be more perception/hand-object tracking than full robot
  demonstration collection.
- Need to avoid overfitting TRACE to its annotation format.

## Aria Digital Twin

Use case:

- Prototype Aria-compatible data loading and object-centric observability
  metrics.

Access / license status:

- Publicly available research dataset.
- Downloaded through the Project Aria dataset downloader.
- Downloading requires accepting the Aria Digital Twin Dataset License
  Agreement.

Relevant modalities:

- Project Aria recordings
- device trajectory
- eye gaze
- object-level ground truth
- human-level ground truth
- synthetic/digital-twin style annotations

TRACE metrics it can support:

- sensor validity
- object visibility
- gaze-object alignment
- head motion smoothness
- viewpoint quality
- trajectory visualization

Risks:

- It may not match the final manipulation task perfectly.
- Dataset access and tooling setup may take time.

## Ego-Exo4D

Use case:

- Study skilled activity, procedural task progress, and proficiency-style
  quality.

Relevant modalities:

- Aria egocentric video
- synchronized exocentric video
- IMU
- eye gaze
- SLAM trajectory
- point clouds
- narrations
- task annotations
- proficiency-style annotations

TRACE metrics it can support:

- task progress coverage
- skill/proficiency proxy
- long-horizon segmentation
- head-motion quality
- gaze behavior
- cross-view validation

Risks:

- Large and complex dataset.
- Less directly aligned with tabletop robot manipulation than HOT3D.
- Download and preprocessing overhead can be high.

## Selection Rule

Pick the first dataset by asking:

- Do we need manipulation? Choose HOT3D.
- Do we need Aria pipeline compatibility? Choose Aria Digital Twin.
- Do we need skill/proficiency and long-horizon procedure? Choose Ego-Exo4D.

Current choice:

> Start with HOT3D for manipulation-centric TRACE V0, then test Aria Digital
> Twin for Aria-specific trajectory and gaze tooling.
