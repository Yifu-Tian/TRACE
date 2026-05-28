# Weekly Checklist

Use this as the operational checklist for TRACE. The roadmap explains why each
stage matters; this file tracks concrete execution.

## Week 1: Problem Freeze

- [ ] Choose the first task scenario.
- [ ] Define one trajectory.
- [ ] Define the operator feedback timing.
- [ ] Write the 3-sentence project pitch.
- [ ] Sketch Figure 1: collection, scoring, feedback loop.
- [ ] List available Aria devices, calibration status, and recording tools.

## Week 2: Literature Matrix

- [ ] Create `literature/references.bib`.
- [ ] Read 5 demonstration-quality papers.
- [ ] Read 5 robot-data-curation papers.
- [ ] Read 5 teleoperation-feedback or active-data-collection papers.
- [ ] Read 3-5 Project Aria or egocentric-data papers.
- [ ] Build `docs/literature_matrix.md`.
- [ ] Write the novelty sentence.

## Week 3: Aria Smoke Test

- [ ] Record 5 pilot Aria sessions.
- [ ] Parse VRS files.
- [ ] Extract camera timestamps.
- [ ] Extract device/head trajectory.
- [ ] Extract IMU and gaze if available.
- [ ] Visualize one session end-to-end.
- [ ] Write a pilot data report.

## Week 4: Task Protocol

- [ ] Choose 2-3 tabletop tasks.
- [ ] Define success and failure.
- [ ] Define subgoals.
- [ ] Define deliberate low-quality conditions.
- [ ] Write operator instructions.
- [ ] Test whether a new person can follow the protocol.

## Weeks 5-6: TRACE Score V0

- [ ] Implement sensor validity metrics.
- [ ] Implement visual observability metrics.
- [ ] Implement motion quality metrics.
- [ ] Implement task progress metrics.
- [ ] Implement weighted score aggregation.
- [ ] Generate per-trajectory quality reports.
- [ ] Rank pilot trajectories and inspect failures.

## Weeks 7-8: Human Ratings

- [ ] Select trajectories for rating.
- [ ] Create rating form.
- [ ] Recruit expert raters.
- [ ] Compute inter-rater agreement.
- [ ] Compare TRACE score with human ratings.
- [ ] Identify metric failures and revise score.

## Weeks 9-10: Feedback Prototype

- [ ] Define feedback message taxonomy.
- [ ] Build post-trajectory feedback UI or report.
- [ ] Run feedback pilot.
- [ ] Compare first attempt versus later attempts.
- [ ] Compare feedback versus no-feedback if possible.
- [ ] Collect operator comments.

## Weeks 11-14: Downstream Validation

- [ ] Choose validation target.
- [ ] Implement random, success-only, and smoothness-only baselines.
- [ ] Evaluate high-score versus low-score trajectories.
- [ ] Run ablations by signal group.
- [ ] Produce the first main result table.
- [ ] Decide whether downstream learning is main or supporting evidence.

## Weeks 14-17: Final Collection

- [ ] Freeze protocol.
- [ ] Freeze processing code.
- [ ] Collect final dataset.
- [ ] Maintain collection log.
- [ ] Back up raw data.
- [ ] Process all sessions.
- [ ] Generate dataset statistics.

## Weeks 17-20: Final Experiments

- [ ] Re-run human-rating correlation.
- [ ] Re-run feedback study analysis.
- [ ] Re-run downstream validation.
- [ ] Re-run ablations.
- [ ] Create qualitative failure gallery.
- [ ] Prepare final tables and plots.

## Weeks 18-23: Paper Draft

- [ ] Write abstract.
- [ ] Write introduction.
- [ ] Write related work.
- [ ] Write method.
- [ ] Write experiment setup.
- [ ] Write results.
- [ ] Write limitations.
- [ ] Create all figures.
- [ ] Run internal review.

## Final Sprint

- [ ] Freeze experiments.
- [ ] Regenerate all plots from clean scripts.
- [ ] Check citations.
- [ ] Check page limit.
- [ ] Check anonymization.
- [ ] Prepare supplementary video.
- [ ] Prepare code/data release notes.
- [ ] Submit.
