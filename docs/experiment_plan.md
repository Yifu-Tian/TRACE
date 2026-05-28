# Experiment Plan

## Initial Scenario

Start with one representative egocentric demonstration collection scenario using
Project Aria, likely a tabletop manipulation task.

## Candidate Tasks

- Pick and place
- Tool use
- Drawer or container opening
- Assembly or sorting

## Candidate Quality Signals

- Sensor validity: missing frames, tracking confidence, timestamp consistency
- Visual observability: object visibility, hand visibility, occlusion
- Egocentric behavior: gaze coverage, head motion stability, viewpoint quality
- Motion quality: smoothness, jerk, idle time, repeated motion, path efficiency
- Task quality: subgoal completion, task success, unnecessary recovery behavior
- Dataset utility: novelty, coverage, diversity, downstream learning gain

## Evaluation Ideas

- Correlation with human expert quality ratings
- Correlation with downstream imitation learning performance
- Improvement from operator feedback versus no feedback
- Ablation of quality signal groups
- Failure case analysis: bad view, tracking loss, jitter, unnecessary motions

## Baselines

- Success/failure label only
- Simple motion smoothness metrics
- Offline-only data filtering
- Human expert rating
