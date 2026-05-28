# TRACE Idea Notes

## One-line Pitch

TRACE evaluates the quality of egocentric trajectories during embodied data
collection and gives feedback that helps operators collect more useful data.

## Motivation

Robotics, AR, and VR systems increasingly depend on trajectory datasets collected
by human operators. However, trajectories vary widely in quality because of
operator skill, sensor failures, occlusion, poor viewpoints, repeated motions,
tracking loss, and task-irrelevant behavior.

Instead of only filtering trajectories after collection, TRACE aims to close the
loop during collection.

## Working Hypothesis

A trajectory is high-quality if it is:

- valid: synchronized, calibrated, and trackable
- task-relevant: captures key objects, actions, and subgoals
- efficient: avoids unnecessary stalls, jitter, or repeated motions
- informative: adds coverage or diversity to the dataset
- useful: improves downstream model learning or evaluation

## Project Aria Angle

Project Aria enables egocentric multimodal signals such as visual observations,
head motion, gaze, IMU, and device trajectory. This makes it possible to judge
not only whether a task succeeded, but whether the demonstration was observable,
stable, and useful for downstream embodied learning.

## Possible Contributions

- A taxonomy of trajectory quality for egocentric embodied data collection
- A learning-aware trajectory quality score
- An online or near-online feedback interface for operators
- Evidence that feedback improves collected data quality
- Evidence that quality scores correlate with downstream learning utility
