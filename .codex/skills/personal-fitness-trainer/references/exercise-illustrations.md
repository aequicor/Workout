# Exercise Illustration Sourcing

Use this reference whenever a workout, program, substitution list, or exercise menu includes exercise names that should be shown with technique visuals.

## Requirement

- Include a visual reference for every prescribed exercise unless the user explicitly asks for text only.
- Use specialized exercise, coaching, certification, or sport-science sources. Do not create illustrations manually, generate them with AI, draw SVGs, use stock photos, or rely on generic image-search thumbnails.
- Prefer a stable exercise page with photos, GIFs, or video plus instructions. Link the page when image reuse or hotlinking permission is unclear.
- Embed a direct image/GIF/video only when it is clearly public and permitted by the source. Otherwise provide a Markdown link labeled `visual/source`.
- Never invent URLs. Search or open the source and verify that the exercise variation, equipment, and movement match the plan.
- Cite sources in the output when using external visuals.

## Preferred Sources

Use these first because they are exercise-specific and include demonstrations or photos:

- ACE Exercise Library: https://www.acefitness.org/resources/everyone/exercise-library/
- MuscleWiki: https://musclewiki.com/
- MuscleWiki API documentation: https://api.musclewiki.com/documentation
- StrengthLog Exercise Directory: https://www.strengthlog.com/exercise-directory/
- Muscle & Strength Exercise Database: https://www.muscleandstrength.com/exercises
- ExRx exercise directory: https://exrx.net/Lists/Directory

Additional acceptable sources:

- National or university exercise libraries with named technique pages.
- Equipment manufacturer technique libraries for equipment-specific movements.
- Sport federation or certified coaching organization demonstrations.

Avoid:

- Pinterest, Instagram, TikTok, Reddit, random blogs, repost sites, and unsourced YouTube compilations.
- AI-generated images, self-made diagrams, placeholder silhouettes, and generic stock photos.
- Medical rehabilitation sources unless the plan is explicitly low-intensity mobility/prehab and still stays outside diagnosis or treatment.

## Output Pattern

For program tables, include a visual/source column:

| Day | Exercise | Visual/source | Sets x reps/time | Intensity | Rest | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Goblet squat | [ACE visual/source](https://www.acefitness.org/resources/everyone/exercise-library/) | 3 x 8-10 | RPE 6-7 | 90 sec | Keep ribs down and knees tracking over toes. |

When exact exercise pages are verified, link directly to the exercise page instead of the directory homepage.

If a plan has many repeated exercises, link the visual the first time the exercise appears and use `same as above` for repeats only when the same source and variation still apply.

## Matching Rules

- Match equipment: dumbbell, barbell, kettlebell, cable, machine, band, bodyweight, or cardio machine.
- Match variation: incline vs flat, Romanian deadlift vs conventional deadlift, bent-knee vs full push-up, assisted vs unassisted pull-up.
- Match user constraints: beginner, home equipment, mobility limits, painful ranges, or no-floor exercises.
- Prefer simpler demonstrated variations over complex movements when the user's training age is unclear.
- If no reliable visual exists for a niche movement, substitute a comparable movement pattern with a reliable visual and explain the substitution briefly.

## Language

Answer in the user's language. Source names and exercise page titles can remain in the source language. Use labels such as `иллюстрация/техника`, `демонстрация`, or `visual/source` depending on the user's language.
