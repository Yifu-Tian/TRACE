# Pre-August Plan

This plan is for the period before physical Project Aria data collection becomes
available in the lab.

## Core Principle

Do not start by searching for the "perfect" dataset. Start by defining the
minimum claim that can be tested without real lab data.

Recommended minimum claim:

> Egocentric trajectory quality can be estimated from multimodal signals such as
> visual observability, head motion, gaze, task progress, and motion efficiency.

Before August, public datasets should be used to prototype the TRACE pipeline,
not to finalize the full ICRA claim.

## First Step

Create a small benchmark from existing public Aria-style data and implement
TRACE V0 on top of it.

The benchmark should support:

- loading egocentric trajectory data
- extracting quality-related signals
- producing a per-trajectory quality report
- comparing scores across good and bad examples
- visualizing why a trajectory is considered low-quality

## Recommended Public Datasets

### Aria Digital Twin

Best for early engineering and metric prototyping.

Why it helps:

- Project Aria VRS recordings
- ground-truth object poses and bounding boxes
- human tracking
- eye gaze
- SLAM/device trajectory
- indoor object-centric activities

Use it for:

- visual observability metrics
- object visibility and occlusion proxies
- head/device trajectory quality
- gaze-object alignment
- basic quality report generation

### HOT3D

Best for hand-object interaction metrics.

Why it helps:

- Project Aria and Quest egocentric recordings
- 3D hand and object pose annotations
- object models
- eye gaze and semi-dense point cloud for Aria

Use it for:

- hand visibility
- hand-object interaction quality
- object tracking continuity
- manipulation-centric quality signals

### Ego-Exo4D

Best for skilled human activity and proficiency-style evaluation.

Why it helps:

- egocentric Aria videos
- exocentric synchronized videos
- IMU, eye gaze, SLAM trajectory, and point clouds
- procedural tasks and skill/proficiency-style annotations

Use it for:

- task progress and skill/proficiency proxies
- operator-quality style analysis
- long-horizon trajectory segmentation
- multimodal visualization

## What To Build Before August

### 1. Dataset Survey

Deliverable:

- `docs/dataset_survey.md`

Contents:

- available modalities
- access requirements
- annotation types
- task relevance
- expected download size
- which TRACE metrics each dataset can support

### 2. Trajectory Schema

Deliverable:

- `docs/trajectory_schema.md`

The schema should abstract away the dataset source:

- trajectory id
- timestamps
- egocentric frames
- head/device pose
- gaze
- hand/object annotations if available
- task labels or subgoal labels
- metric outputs
- final quality score

### 3. TRACE V0 Metrics

Deliverable:

- `src/trace/metrics/`

Start with metrics that public data can support:

- timestamp continuity
- head motion smoothness
- gaze stability
- object visibility
- hand/object tracking continuity
- idle or low-motion periods
- task phase coverage if annotations exist

### 4. Quality Report Generator

Deliverable:

- `scripts/generate_quality_report.py`

The report should show:

- total score
- component scores
- top failure reasons
- trajectory plot
- example frames for failure points

### 5. Paper Skeleton

Deliverable:

- `paper/outline.md`

Write the paper skeleton early:

- problem
- motivation
- method overview
- expected experiments
- what public-data experiments can show
- what August lab-data experiments must show

## Suggested Timeline

### Week A: Define Data Requirements

- Decide which signals TRACE must use.
- Build the dataset comparison table.
- Pick one public dataset for the first prototype.

Recommended first choice:

- Aria Digital Twin if the goal is fast Project Aria compatibility.
- HOT3D if the goal is manipulation and hand-object interaction.

### Week B: Tooling Smoke Test

- Download a tiny subset.
- Parse one sequence.
- Visualize frames, pose, gaze, and annotations.
- Save features into the TRACE trajectory schema.

### Week C: Metric Prototype

- Implement 3-5 simple metrics.
- Generate quality reports.
- Manually inspect good and bad examples.

### Week D: Mini Evaluation

- Create weak labels from annotations or manual inspection.
- Test whether TRACE V0 ranks obvious good cases above obvious bad cases.
- Write a 2-page internal memo with plots.

## What Not To Do Yet

- Do not overfit to a public dataset's annotation format.
- Do not claim public-data results prove operator feedback works.
- Do not spend weeks downloading every dataset.
- Do not start with deep learning unless simple metrics fail.
- Do not design the final user study before seeing real lab constraints.

## August Transition

When lab access begins:

- Reuse the same trajectory schema.
- Reuse the same quality report generator.
- Replace public-dataset loaders with the lab Aria loader.
- Collect 5 pilot sessions first, not a full dataset.
- Compare public-data failure modes with real lab failure modes.

The goal is to arrive in August with a working TRACE prototype, not just a list
of papers.
