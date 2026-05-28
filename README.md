# TRACE

**TRACE**: **TR**ajectory **A**ssessment for **C**ollection **E**nhancement.

TRACE is a research workspace for studying trajectory quality assessment and
operator feedback during embodied data collection, with an initial focus on
egocentric trajectories captured by Project Aria.

## Research Direction

Large-scale robot learning, AR, and VR systems increasingly rely on collected
trajectory datasets. TRACE asks:

> How can we assess the quality and downstream utility of a collected trajectory
> while data collection is still in progress, and provide actionable feedback to
> the operator?

## Initial Scope

- Target venue: ICRA
- Hardware: Project Aria
- Initial task family: egocentric demonstration collection for embodied /
  robotic manipulation tasks
- Core idea: online or near-online trajectory quality scoring with feedback for
  the operator

## Workspace Layout

- `docs/`: idea notes, literature notes, experiment plans
- `literature/`: papers, summaries, and bibliography files
- `experiments/`: experiment configs, logs, and analysis notes
- `data/`: local datasets or dataset links
- `scripts/`: utility scripts
- `src/`: source code
- `assets/`: figures, diagrams, and presentation materials

## Candidate Paper Framing

**TRACE: Trajectory Assessment for Collection Enhancement in Egocentric Robot
Demonstrations**

The first version should likely fix one representative task setting, then show
that the proposed quality assessment generalizes conceptually to broader
embodied trajectory collection scenarios.
