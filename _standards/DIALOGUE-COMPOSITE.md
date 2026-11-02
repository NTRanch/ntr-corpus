# Dialogue Composite — PROTOTYPE (pending owner eye gate)

Tool: dialogue.py (PIL). Still renders clean; dialogue is a deterministic
derivative (sidecar JSON + composite PNG, derived_from the source still).
Originals immutable. Bubble grammar: speech (rounded rect + tail to the
mouth point), thought (scalloped union-mask cloud + boundary-started
trail circles to the head point), narration (plain rect), whisper
(dashed + tail), shout (spiky + tail). Text auto-wraps and auto-shrinks
to fit; same inputs produce byte-identical output (verified: two runs,
same SHA-256).

Trial 2026-10-23 on img-h-e10-r3-keeper: speech trial passed first run
(tail lands on the mouth, text exact). Thought trial needed two fixes:
v1 drew outlined circles whose arcs crossed the text; v2's union mask
fixed the cloud but the center-started trail ringed the word "serve.";
v3 starts the trail at the cloud boundary and passes. Font placeholder:
DejaVu Sans Bold — a publish-clear OFL comic font must replace it
before any dialogue derivative ships.

## v2 — manga styling (Owner reference pages, 2026-10-23 23:41 PDT)

Style grammar mined from the owner's 8 reference pages (bubble SHAPES
and placement only — no characters, scenes, or lines from those pages
enter the corpus, per the study/build firewall):
- Bubbles live in panel negative space (corners, edges, gutters) and
  overlap hair/background/body freely — but NEVER the features box
  (eyes-to-mouth). The tool enforces this: sidecar "face" is the
  features box, and clear_of_face() relocates a bubble above/below/
  left/right of it or to a corner, else errors for hand placement.
- Manga default is the OVAL bubble with a thin tapered tail, not the
  rounded rect; tails end exactly at the mouth point.
- Alternate-voice coding: black bubble, white text (speech_black).
- SFX: jagged black starburst, white text (sfx), placed in empty areas.
- Oval text layout insets 10% so no line crowds the curve.
Self-caught during v2: a regex patch sliced main() off the file
(silent exit 0, no output); restored and re-verified. Speech v2 trial
passes: oval in the top-right white space, thin tail to the mouth,
features clear, text inset clean.

## Page prototype (Owner: "try again with these", 2026-10-23 23:49 PDT)

manga_page.py assembles our own keeper stills into a 3-panel page
(top wide + two below, white gutters, black borders) with oval speech,
thought cloud, black voice bubble, and SFX starburst — style grammar
only from the reference pages.
v1 FAILED the face rule in all three panels (guessed placements: A
tail ended at the nose line crossing the eye; B cloud covered her
whole face; C bubble sat on her forehead with a spike down her face).
v2 re-placed from face positions measured off the v1 render: A tail
corrected to the true mouth point; B cloud moved to the barn
background; C bubble moved to the shelves background. v2 PASSES: no
bubble body covers any face; tails touch mouths only. Lesson carried
forward: panel bubble placement needs measured face boxes per still,
never guessed coordinates.

## v3 — research rebuild (manga-bubble best practices, 2026-10-24)

Source: ~/workspace/research_notes/manga-bubble-best-practices-20261024-0657/report.md
(Klein / Comicraft / Waterman / Ostlie). dialogue.py rewritten; sandbox and
primo copies verified byte-identical (md5 6fdccae447589776ef81ce4c5e4e4997).
Fonts bundled in fonts/: ComicNeue-{Regular,Bold,Italic,BoldItalic}.ttf +
OFL-ComicNeue.txt, Bangers-Regular.ttf + OFL-Bangers.txt (primo copies in
~/fonts/, since primo dialogue.py lives at ~/dialogue.py).
Changes, per finding:
- TEXT FIRST. Sidecar "rect" is now a placement hint / max box, not the
  balloon. Text is diamond-broken (DP partition, widest line in the
  middle, widow/parking penalties) and the balloon is sized FROM the
  text with ~1 letter-width of air (the "O" width) all round. A tight
  hint re-breaks the lines first; the font shrinks only if no break
  fits at all. No text crowds the edge.
- BLACK-VOICE RESTRICTION. v2 "speech_black" (generic commanding voice)
  is REMOVED — the report supports black fill ONLY for otherworldly /
  demonic / godlike / undead voices. New type "otherworldly"; old
  sidecars fail loudly with a migration message. Shape stays a normal
  oval so the inversion alone carries the meaning. Use sparingly.
- FONTS. Anime Ace is NOT OFL (Blambot freeware, indie/non-profit
  only) and is never used. Default is now Comic Neue Bold (SIL OFL
  1.1, Craig Rozynski, author's repo github.com/crozynski/comicneue;
  licence header verified in the bundled OFL.txt). SFX uses Bangers
  (SIL OFL 1.1, Google Fonts release) — never the dialogue face at
  dialogue size. DejaVu survives ONLY as a warned fallback if no
  Comic Neue file is found; it is never the default.
- FILL / SHADOW. Opaque white stays the default on colour art; there
  is no semi-transparent option, and any sidecar opacity/alpha < 1 is
  now rejected loudly. No drop shadows on balloons. The ONLY shadow
  is deliberate: narration with "first_person": true gets a flat,
  hard, single-direction offset rectangle (never a soft blur) marking
  first-person narration captions.
- TAILS. S-curve (subtle asymmetric bow, capped) instead of straight
  polygons; base at the balloon's centre mass (centre-to-mouth ray
  vs. balloon boundary), constant base width across normal balloons,
  tapering to the mouth point. Self-caught defect: a symmetric
  opposite bow (0.15 x distance) made a fat blade across the face in
  the first v3 renders; capped asymmetric bow fixed it (re-rendered).
- OUTLINE. Default 4 px, overridable via sidecar top-level "outline";
  rule is <= panel border and matched to the art's line weight
  (calibrate per still size; 4 px is the value at this 832-px still
  width). Outlines are slightly irregular: a squashed-oval
  (superellipse) template with a deterministic low-frequency
  perturbation seeded by the bubble text — no two balloons are
  pixel-identical, yet same inputs stay byte-identical.
- TYPE TUNING. Whisper: dashed outline + 0.85x type + 1.5x air.
  Shout: full-perimeter jagged burst (v2 spiked top/bottom only) +
  1.15x type + 0.8x air. Narration: slightly rounded rect, no tail.
- KEPT. Face/features-box guard (bodies never cover eyes-to-mouth;
  tails exempt) and the thought-cloud union mask with
  boundary-started trail — both unchanged in intent.
Trials 2026-10-24, source img-h-e10-r3-keeper.png, sidecars
sidecar-speech-v2.json / sidecar-thought-v2.json (reused, unmodified)
plus new sidecar-otherworldly-v3.json:
- dialogue-trial-speech-v3-20261024.png
  sha256 dd0cd4f58b90d87ead77775f2f9a4df9b95a97d8547b8705e46259d942f2474b
- dialogue-trial-thought-v3-20261024.png
  sha256 c4cb76e296197912d60906af0d66f902f8fe16f24654678a9a2fb0494a7f5750
- dialogue-trial-otherworldly-v3-20261024.png ("We have waited long
  for you.", black oval, white Comic Neue, thin black taper tail)
  sha256 e672c7b8831652e5a7d2009d41be48dd376a9054664fbca2bd21c024ea03204f
Honest verdict: BETTER than v2, thought most of all (Comic Neue +
diamond break + cloud reads as lettering, not a label). Speech meshes
better — hand-drawn letterforms, squashed oval, curved thin tail —
but still slightly pasted: the 4 px uniform outline cannot match the
art's varied brush weight, and the tail must cross hair/cheek to
reach the mouth from the top-right corner (inherent to this still's
composition; a closer/lower balloon would help more than any tail
tweak). No drop shadow, no transparency, no DejaVu anywhere in v3.
Left for the owner's eye check: (1) Comic Neue vs. DejaVu preference
at reading size; (2) whether the tail path across the cheek is
acceptable or the balloon should sit lower/closer; (3) outline weight
4 px vs. the art's line weight. NOTE for a follow-up lane (not
touched here): manga_page.py still references the removed
"speech_black" type and will fail under v3 until renamed to
"otherworldly" or "speech".
