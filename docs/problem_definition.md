# Problem Definition

## Current Working Problem

TRACE aims to assess the quality of egocentric trajectories for embodied data
collection and provide actionable feedback to the operator.

## First Paper Scope

The first paper should not try to solve all trajectory-quality problems across
robotics, AR, and VR. It should focus on one representative setting:

> Egocentric demonstration collection for tabletop manipulation-like tasks using
> Project Aria-style multimodal trajectories.

Before lab access is available, public Aria-style datasets will be used to build
and validate the TRACE prototype.

## Minimum Pre-August Claim

> We can compute interpretable quality signals from egocentric trajectory data
> and use them to identify failure modes such as poor observability, unstable
> motion, missing interaction evidence, and low task-progress coverage.

This claim does not require real-time feedback or lab data yet.

## August-Onward Claim

> TRACE feedback helps operators collect better trajectories, and the resulting
> quality score correlates with human ratings and/or downstream task utility.

This claim requires controlled lab data collection.

## What Is One Trajectory?

Working definition:

> A trajectory is one temporally continuous egocentric recording of a person
> attempting a task, including synchronized sensor streams, device motion, visual
> observations, optional gaze, optional hand/object annotations, and task
> metadata.

## What Is Trajectory Quality?

Working definition:

> Trajectory quality is the degree to which a collected trajectory is valid,
> observable, task-relevant, efficient, and useful for downstream embodied
> learning or evaluation.

## First Operator Feedback Types

- Visibility feedback: key object or hand is occluded or out of view.
- Stability feedback: head/device motion is too shaky.
- Progress feedback: important subgoals are missing or incomplete.
- Efficiency feedback: excessive idle time, repeated motion, or recovery.
- Sensor feedback: tracking loss, timestamp gaps, or missing streams.

## First Success Criteria

Before August:

- Public-data loader works on one Aria-style dataset.
- TRACE V0 generates a per-trajectory quality report.
- The score separates obvious good and bad examples.
- The method section can be drafted around the trajectory schema and metrics.

After August:

- Lab data can be processed by the same schema.
- Operators understand TRACE feedback.
- Feedback improves repeated collection attempts.
- TRACE score correlates with human quality labels or downstream utility.
