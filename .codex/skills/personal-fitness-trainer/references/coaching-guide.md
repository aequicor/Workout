# Coaching Guide

## Safety Boundaries

- Stay within fitness coaching. Do not diagnose injuries, prescribe rehabilitation, adjust medication, or promise medical outcomes.
- Recommend clinician clearance before intense training when the user reports cardiovascular disease, uncontrolled hypertension, unexplained chest pain, fainting, severe dizziness, significant breathing limitation, recent surgery, pregnancy/postpartum complications, or pain that changes gait or worsens during a session.
- Stop or modify exercise for sharp pain, joint instability, numbness/tingling, unusual shortness of breath, dizziness, or form breakdown.
- For minors, older adults, pregnancy/postpartum, chronic conditions, or disability, keep intensity conservative and suggest qualified supervision when risk is unclear.

## Public Guideline Anchors

Use these as broad health targets, not as rigid prescriptions:

- ODPHP/HHS Physical Activity Guidelines for Americans, current guidelines page: https://odphp.health.gov/our-work/nutrition-physical-activity/physical-activity-guidelines/current-guidelines
- WHO physical activity fact sheet/guidelines: https://www.who.int/news-room/fact-sheets/detail/physical-activity
- For adults, common public-health targets are 150-300 minutes/week moderate aerobic activity or 75-150 minutes/week vigorous aerobic activity, plus muscle-strengthening work involving major muscle groups on 2 or more days/week.
- More activity is not automatically better for every user. Balance goals against recovery, injury history, adherence, and stress.

## Intake Template

Ask only what is needed for the task.

Before composing a workout plan, ask for biometric intake and storage consent:

- Required-to-ask biometrics: age, height, body weight.
- Optional relevant biometrics: resting heart rate, blood pressure, waist/hip measurement, recent body-composition estimate, tested maxes or recent performance metrics.
- Ask for sex/gender only when relevant to safety screening, pregnancy/postpartum considerations, body-composition estimates, or a user-requested goal; make it explicitly optional.
- Tell the user any biometric field can be skipped and estimates are acceptable.
- Ask whether the user permits saving the biometric intake locally in `res/` for future plan updates.
- Save biometric intake only after clear consent, using a dated local file such as `res/YYYY-MM-DD-biometric-intake.md` or `.json`.
- If the user declines, does not answer, or gives ambiguous consent, do not save the data; use it only for the current response.

Core:

- Goal: strength, muscle, fat loss, endurance, mobility, general health, sport, return to routine.
- Timeline: event date or desired review interval.
- Training history: beginner, returning, intermediate, advanced; current weekly training.
- Availability: days/week, minutes/session, preferred days.
- Equipment: bodyweight, bands, dumbbells, barbell, machines, cardio equipment, home/gym.
- Constraints: injuries, painful movements, medical restrictions, sleep, work schedule, travel.
- Preferences: exercises enjoyed/disliked, solo/group, cardio tolerance, language/units.
- Tracking: bodyweight, step count, estimated 1RM, recent lifts, resting heart rate, soreness, energy.

If the user refuses intake, provide a conservative general plan and label assumptions.

## Program Design

### Beginner General Fitness

- Start with 2-3 full-body strength sessions/week.
- Use 5-8 core movements per session.
- Keep most work at RPE 6-7 for the first 2-4 weeks.
- Favor stable, easy-to-learn movements: squat pattern, hinge pattern, push, pull, carry/core, low-impact cardio.
- Progress by adding reps first, then small load increases.

### Hypertrophy

- Train each major muscle group 2 or more times/week when schedule allows.
- Use mostly 6-15 reps, with some 12-20 rep accessory work.
- Keep 1-3 reps in reserve for most sets; avoid routine failure for beginners.
- Add weekly sets gradually only if recovery and performance are stable.

### Strength

- Prioritize technique, consistent setup, and adequate rest.
- Use lower-rep work for main lifts and moderate-rep accessories.
- Avoid max testing unless the user is experienced and specifically asks.
- Progress load only when bar speed/form and recovery are acceptable.

### Fat Loss Support

- Strength training protects performance and lean mass; cardio and steps support energy expenditure.
- Keep nutrition advice non-medical: protein-forward meals, fiber-rich foods, hydration, regular meal structure, and sustainable calorie awareness.
- Do not prescribe extreme diets, detoxes, or aggressive weight-loss targets.

### Mobility And Return-To-Training

- Use pain-free ranges and controlled tempo.
- Prefer low-load isometrics, range-of-motion work, and technique practice before high fatigue.
- If pain persists, radiates, causes swelling/instability, or changes movement mechanics, suggest evaluation by a qualified professional.

## Session Structure

1. Warmup: 5-10 minutes easy cardio or movement prep plus specific ramp-up sets.
2. Main work: most technical and goal-relevant exercises first.
3. Accessories: balance movement patterns and address weak links.
4. Conditioning: optional and sized to recovery budget.
5. Cooldown: breathing, easy walking, or light mobility when useful.

## Exercise Visuals

When a workout or program names exercises, include visual technique references from specialized sources. Follow `exercise-illustrations.md` for source selection, verification, output format, and copyright-safe linking. Do not create, draw, generate, or invent exercise illustrations.

## Program Artifacts

When creating file deliverables for a complete workout program, follow `artifact-workflow.md`: save the program `.docx` and companion progress-tracking `.xlsx` in `programms/`, and use `res/` for intermediate data, images, charts, and render previews.

## Movement Pattern Checklist

Use this to keep plans balanced:

- Squat/lunge: squat, split squat, step-up, leg press.
- Hinge: Romanian deadlift, hip thrust, deadlift variation, kettlebell swing.
- Horizontal push: push-up, bench press, dumbbell press.
- Vertical push: overhead press, landmine press.
- Horizontal pull: row variations.
- Vertical pull: pulldown, pull-up assistance, pull-up.
- Core: anti-extension, anti-rotation, carry, controlled flexion when appropriate.
- Conditioning: walking, cycling, rowing, intervals, sport-specific work.

## Progression Rules

Use simple rules the user can execute:

- Double progression: keep load fixed until all sets reach the top of the rep range at target RPE, then increase load slightly.
- Time progression: add 2-5 minutes to easy cardio until target duration is reached.
- Density progression: do the same work with slightly shorter rest only when form stays clean.
- Deload: reduce volume by about 30-50% for a week when performance drops, soreness persists, sleep/stress is poor, or motivation collapses.
- Hold steady when the user reports pain, poor form, missed sessions, or high fatigue.

## Substitution Rules

When substituting, preserve the intent:

- Same movement pattern first.
- Similar range of motion and stability demand.
- Similar equipment difficulty if possible.
- Lower complexity when fatigue, pain, or skill is a constraint.

Examples:

- Barbell back squat -> goblet squat, leg press, split squat.
- Conventional deadlift -> Romanian deadlift, trap-bar deadlift, hip thrust.
- Bench press -> dumbbell press, push-up, machine chest press.
- Pull-up -> assisted pull-up, lat pulldown, band pulldown.

## Workout Log Review

Check:

- Completion: missed sessions, skipped exercises, time bottlenecks.
- Performance: reps, loads, RPE/RIR, form notes.
- Recovery: sleep, soreness, energy, stress, appetite.
- Pain: location, movement trigger, severity, trend.
- Adherence: what felt easy to repeat and what created friction.

Decision:

- Progress when completion is high, RPE is within target, and no concerning pain appears.
- Repeat when performance is mixed or schedule disrupted.
- Regress or modify when pain, excessive soreness, or form breakdown appears.

## Nutrition Guardrails

Keep nutrition coaching general unless the user provides qualified medical direction:

- Encourage protein with each meal, fruits/vegetables, whole-food carbohydrates, healthy fats, and hydration.
- Avoid diagnosing deficiencies, prescribing supplements as required, or managing eating disorders.
- For diabetes, kidney disease, pregnancy, eating disorder history, or medically prescribed diets, suggest working with a registered dietitian or clinician.

## Default Plan Template

Use this shape for a 4-week beginner-friendly plan:

| Week | Focus | Progression |
| --- | --- | --- |
| 1 | Learn technique, low soreness | RPE 6, stop with 3-4 reps in reserve |
| 2 | Build consistency | Add 1-2 reps per set if form is clean |
| 3 | Add small challenge | Add light load or one accessory set |
| 4 | Consolidate | Keep load steady or deload if fatigue is high |

Per-workout table:

| Block | Exercise | Sets x reps/time | Intensity | Rest | Notes |
| --- | --- | --- | --- | --- | --- |
| Warmup |  |  |  |  |  |
| Main |  |  |  |  |  |
| Accessory |  |  |  |  |  |
| Conditioning |  |  |  |  |  |
| Cooldown |  |  |  |  |  |

Illustrated workout tables should add a `Visual/source` column next to `Exercise` and link verified exercise demonstrations from specialized sources.
