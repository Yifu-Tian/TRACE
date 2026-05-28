# TRACE ICRA Roadmap

This roadmap assumes the target is ICRA 2027. The official ICRA 2027 submission
deadline has not been announced yet. Based on recent ICRA cycles, use
mid-September 2026 as the working deadline until the official date is released.

## North Star

**TRACE** studies trajectory quality assessment for egocentric embodied data
collection. The first submission should prove that quality feedback can help
operators collect better trajectories and that the proposed quality score is
meaningful for downstream embodied learning.

Candidate title:

**TRACE: Trajectory Assessment for Collection Enhancement in Egocentric Robot
Demonstrations**

## Target Contributions

- A task-aware quality formulation for egocentric trajectory collection.
- A multimodal quality scoring pipeline using Project Aria signals.
- An operator feedback loop that converts quality failures into actionable
  guidance.
- Experiments showing correlation with human ratings and/or downstream learning
  utility.
- A focused dataset and benchmark protocol for one representative task family.

## Stage 0: Project Definition

Target window: now to 1 week

Goal: reduce the idea from "trajectory quality" to one publishable ICRA problem.

Tasks:

- Fix the primary task scenario.
- Decide whether the first paper is about human demonstration quality,
  teleoperation quality, or AR/VR collection quality.
- Define what counts as one trajectory.
- Define what feedback the operator receives and when.
- Decide the first downstream use case: human rating, imitation learning, task
  success prediction, or dataset curation.

Recommended first scenario:

- Human wears Project Aria.
- Human performs tabletop manipulation demonstrations.
- TRACE scores each trajectory and gives feedback about visibility, stability,
  task progress, and unnecessary motion.
- Evaluation checks whether high TRACE score predicts expert rating and/or
  downstream imitation learning utility.

Deliverables:

- `docs/problem_definition.md`
- One-page paper pitch
- A diagram of the data collection and feedback loop
- List of required hardware, software, and human subjects

Go / no-go criterion:

- The problem can be explained in 3 sentences.
- The experiment can be run with available lab hardware.
- The score can be evaluated against at least one external target.

## Stage 1: Literature And Positioning

Target window: weeks 1-2

Goal: know exactly what TRACE is not, and where it is new.

Tasks:

- Build a Zotero or BibTeX library.
- Read 20-30 papers across demonstration quality, data curation, teleoperation
  feedback, egocentric perception, and Project Aria datasets.
- Make a comparison table: input modality, quality definition, online/offline,
  feedback/no feedback, downstream validation.
- Identify 3-5 closest baselines.

Must-cover literature buckets:

- Demonstration quality for imitation learning
- Robot data curation and trajectory filtering
- Online teleoperation feedback
- Egocentric human demonstration datasets
- Project Aria tooling and calibration

Deliverables:

- `docs/literature_matrix.md`
- `literature/references.bib`
- Related-work outline
- Baseline list

Go / no-go criterion:

- You can state the novelty in one sentence without saying "nobody has done
  this."

## Stage 2: Data Pipeline Smoke Test

Target window: weeks 2-4

Goal: prove that Project Aria data can be read, synchronized, and converted into
trajectory features.

Tasks:

- Record 5-10 short pilot sessions with Project Aria.
- Export or parse VRS data.
- Extract timestamps, camera frames, SLAM/device pose, IMU, and gaze if
  available.
- Define a common trajectory schema.
- Create visualization scripts for trajectories and failure cases.

Trajectory schema should include:

- Session metadata
- Time-aligned observations
- Device pose or head trajectory
- Gaze signal if available
- RGB frames or frame references
- Task labels or event annotations
- Quality labels or computed metrics

Deliverables:

- `src/trace/` package skeleton
- `scripts/inspect_aria_recording.py`
- `scripts/extract_trajectory_features.py`
- First pilot data report
- Example visualization figure

Go / no-go criterion:

- One recording can be converted into features and visualized end-to-end.

## Stage 3: Task And Dataset Protocol

Target window: weeks 4-5

Goal: make the data collection repeatable enough for a paper.

Tasks:

- Choose 2-3 tabletop tasks with increasing difficulty.
- Write task instructions for operators.
- Define success/failure labels.
- Define subgoal annotations.
- Define bad-quality variants deliberately: poor viewpoint, occlusion, shaky
  motion, repeated motion, incomplete demonstration, tracking loss.
- Decide number of operators and trajectories.

Recommended minimum dataset:

- 5-8 operators
- 2-3 tasks
- 20-30 trajectories per task per condition if feasible
- Balanced high-quality and low-quality examples

Deliverables:

- `docs/data_collection_protocol.md`
- Annotation guide
- Consent / IRB notes if needed by the lab
- Pilot dataset v0.1

Go / no-go criterion:

- A new lab member can follow the protocol and collect comparable data.

## Stage 4: Quality Metric V0

Target window: weeks 5-7

Goal: build a transparent metric baseline before any learning-heavy method.

Quality groups:

- Sensor validity: missing frames, tracking confidence, timestamp gaps
- Visual observability: target object visible, hand visible, occlusion
- Egocentric stability: head motion smoothness, viewpoint stability
- Motion efficiency: idle time, jerk, path length, repeated motion
- Task progress: subgoal completion, ordering, success/failure
- Dataset novelty: similarity to existing trajectories

Tasks:

- Implement per-metric computation.
- Normalize metrics to comparable ranges.
- Create per-trajectory quality report.
- Create simple weighted TRACE score.
- Build failure explanations from the lowest-scoring components.

Deliverables:

- `src/trace/metrics/`
- `src/trace/scoring/`
- Quality report examples
- Pilot correlation with human labels

Go / no-go criterion:

- TRACE V0 can rank obviously good trajectories above obviously bad ones.
- Each score has an interpretable failure reason.

## Stage 5: Human Rating Study

Target window: weeks 7-9

Goal: establish an external ground truth for quality.

Tasks:

- Sample trajectories across tasks and quality levels.
- Ask expert raters to score trajectory quality.
- Use multiple axes: observability, task correctness, efficiency, usefulness for
  learning.
- Compute inter-rater agreement.
- Compare TRACE V0 to human ratings.

Deliverables:

- Rating form
- Human-rating dataset
- Correlation analysis
- Failure analysis

Go / no-go criterion:

- TRACE score has a meaningful correlation with at least one human quality axis.
- Disagreements reveal useful design changes, not random behavior.

## Stage 6: Operator Feedback Prototype

Target window: weeks 9-11

Goal: turn assessment into collection improvement.

Feedback modes:

- Post-trajectory feedback: shown immediately after each attempt.
- Near-online feedback: warnings during collection if tracking, view, or motion
  quality degrades.

Recommended first implementation:

- Start with post-trajectory feedback because it is easier and safer.
- Add near-online warnings only for simple signals such as tracking loss,
  excessive occlusion, or too much idle time.

Tasks:

- Build a lightweight feedback dashboard.
- Display total score, component scores, and actionable suggestions.
- Avoid vague feedback; every message should say what to change next time.
- Run a small user pilot with feedback versus no feedback.

Deliverables:

- Feedback UI or notebook report
- Feedback message taxonomy
- Pilot user-study results

Go / no-go criterion:

- Operators understand the feedback and improve on repeated attempts.

## Stage 7: Learning-Aware Validation

Target window: weeks 11-14

Goal: show the score is useful beyond aesthetics or human preference.

Possible validation paths:

- Train a policy or behavior cloning model on high-score versus low-score
  demonstrations.
- Predict task success or subgoal completion from trajectory features.
- Use TRACE for dataset filtering and compare downstream performance.
- Estimate trajectory utility by leave-one-out or subset training.

Recommended first path:

- If robot policy training is feasible, use high-score versus random versus
  low-score filtering for imitation learning.
- If real robot training is too heavy, use a proxy task: action segmentation,
  subgoal recognition, or task success prediction.

Deliverables:

- Downstream evaluation script
- Main quantitative table
- Ablation table
- Learning-utility analysis

Go / no-go criterion:

- TRACE-selected data outperforms random or naive baselines, or TRACE score
  predicts downstream utility.

## Stage 8: Main Data Collection

Target window: weeks 14-17

Goal: collect the final dataset for the ICRA submission.

Tasks:

- Freeze the protocol.
- Freeze the metric implementation.
- Collect final data.
- Track every failed recording and reason.
- Back up raw and processed data.
- Keep a collection log with operator, task, condition, and notes.

Deliverables:

- Dataset v1.0
- Processing scripts
- Data statistics
- Failure-case gallery

Go / no-go criterion:

- Dataset is large enough to support all main claims.
- Results do not depend on a few cherry-picked examples.

## Stage 9: Experiments And Ablations

Target window: weeks 17-20

Goal: produce the final evidence package.

Main experiments:

- Human-rating correlation
- Feedback improves operator collection quality
- TRACE-based filtering improves downstream utility
- Ablation over quality signal groups
- Generalization across tasks or operators

Baselines:

- Success/failure only
- Smoothness-only score
- Random selection
- Human expert rating upper bound if available
- Offline filtering without feedback

Deliverables:

- Final result tables
- Final plots
- Statistical tests
- Qualitative examples

Go / no-go criterion:

- At least two independent claims are strongly supported.
- The weakest claim can be removed without collapsing the paper.

## Stage 10: Paper Writing V1

Target window: weeks 18-21, overlapping experiments

Goal: write early enough that writing reveals missing experiments.

Paper structure:

- Introduction: data quality bottleneck in embodied collection
- Related work: demonstration quality, data curation, egocentric data,
  teleoperation feedback
- Method: trajectory representation, quality score, feedback generation
- System: Project Aria collection pipeline
- Experiments: rating, feedback, downstream utility, ablations
- Discussion: limitations and generalization

Figures to prepare early:

- System overview
- Quality taxonomy
- Feedback interface
- Dataset examples
- Main quantitative plot
- Failure cases

Deliverables:

- Full paper draft v1
- Figure list
- Table list
- Internal review checklist

Go / no-go criterion:

- A reader can understand the contribution from the abstract, intro, and Figure
  1 alone.

## Stage 11: Internal Review And Rework

Target window: weeks 21-23

Goal: make the paper robust to ICRA reviewer attacks.

Likely reviewer concerns:

- "Quality" is subjective.
- Metrics are hand-designed and task-specific.
- Feedback improvement may come from practice, not TRACE.
- Dataset is too small.
- Aria is unnecessary; a normal camera would work.
- Downstream robot relevance is weak.

Preemptive fixes:

- Include human-rating agreement.
- Include no-feedback repeated-attempt control.
- Include ablations showing Aria-specific signals help.
- Include task/operator split.
- Connect quality score to downstream utility.
- Be honest about task-specific components while framing a general interface.

Deliverables:

- Review response memo
- Revised paper draft
- Extra experiment list
- Limitations section

Go / no-go criterion:

- You can answer the top 5 reviewer objections with data or a clear limitation.

## Stage 12: Final Submission Sprint

Target window: final 2-3 weeks before deadline

Goal: submit a clean, coherent, reproducible paper.

Tasks:

- Freeze experiments.
- Re-run main tables from clean scripts.
- Check all plots and captions.
- Check all citations.
- Check LaTeX formatting and page limit.
- Ask 2-3 people for final reviews.
- Prepare supplementary material if allowed.
- Prepare code/data release plan.

Deliverables:

- Camera-ready-quality submission PDF
- Supplementary video
- Supplementary appendix if allowed
- Anonymous project page if allowed
- Reproducibility package snapshot

Final checklist:

- The title matches the actual contribution.
- The abstract states the problem, method, and evidence.
- The intro clearly says why online feedback matters.
- Every main claim has a corresponding experiment.
- Every metric is defined.
- Every baseline is fair.
- All figures are readable in grayscale.
- The conclusion does not overclaim generality.

## Fallback Plans

If downstream robot learning is too hard:

- Use task success prediction, subgoal recognition, or human rating as the main
  validation.
- Keep downstream learning as a smaller supporting experiment.

If real-time feedback is too hard:

- Submit with immediate post-trajectory feedback.
- Present near-online signals as an extension.

If Aria gaze is unreliable:

- Use head pose, egocentric view, and visual observability as the main signals.
- Treat gaze as optional ablation.

If dataset size is limited:

- Emphasize controlled collection, repeated measures, and within-operator
  improvement.
- Avoid claiming large-scale generalization.

## Weekly Operating Rhythm

- Monday: define weekly goal and blocking risks.
- Wednesday: run one concrete experiment or collection session.
- Friday: update plots, notes, and paper outline.
- Every week: write at least one paragraph of the paper or related work.
- Every two weeks: produce one artifact that can appear in the final submission.

## Minimal Publishable Version

If time becomes tight, the minimum viable ICRA paper should include:

- One clear egocentric manipulation data collection task.
- A transparent TRACE quality score.
- Human expert rating correlation.
- Operator feedback study showing quality improvement.
- Ablation showing which quality signals matter.

Downstream imitation learning is highly valuable, but it should not be the only
pillar of the paper unless the lab can run it reliably.
