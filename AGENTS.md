# Entry: one image summing up 23 November 2026 world news

make.fun contest. The deliverable is ONE image, judged by an AI picture editor. It must name the day and show that day's real reported stories, broadly, legibly, unhyped. The judge has no feed: it judges what the image itself shows and can read.

## The day's real headlines (fetched today from BBC World, Al Jazeera, NPR World, NYT World)
- COP31 climate talks fail with no major deal, deep divisions over fossil fuels.
- Russian strike on Ukraine: a 7-year-old boy pulled alive from rubble hours later; war spilling into NATO territory; Russia-bound ship attacked in the Gulf of Finland.
- Mexican army captures a top cartel kingpin in a firefight that left 11 dead.
- Fire at an Indonesian factory: three killed, dozens missing; 24 body bags removed.
- Deadly protests in Bangladesh over the exiled former leader.
- Belgium's airports to shut in an anti-austerity strike.
- AI boom worries: San Francisco enjoys it, a crash is feared; South Korea's education minister resigns over anti-AI cheating rules.

## Design (1024x1024)
A stark newspaper front page on warm off-white paper, black ink, one red accent, generous margins.
- Masthead across the top: "THE WORLD" and directly under it the date "MONDAY · 23 NOVEMBER 2026".
- Six story blocks in a modular grid with thick rules, each with a simple bold SVG icon, a region tag (CLIMATE, EUROPE, LATIN AMERICA, ASIA, SOUTH ASIA, TECH), a short headline and one factual line.
- Lead block larger: COP31 collapse, with a globe/wilted-leaf icon.
- Bottom strip: "A day in one page · 23 Nov 2026" and a row of world-region ticks.
- Everything must stay readable at 300 px across: large type, high contrast, no long paragraphs, no garbled text.
- No photos (none available offline), pure vector/CSS art. Crisp, flat, editorial.

## Files and rules
- `poster.html` (the source), `entry.jpg` (rendered output), `main.py`.
- `main.py`: standard library only, copies `entry.jpg` beside it to `/output/entry.png` (mkdir; `MAKEFUN_OUTPUT_DIR` if set else `/output`).
- Final image: JPEG bytes in a file named entry.png, at most 1 MiB, exactly 1024x1024.
- Render with `~/.cache/ms-playwright/chromium-1248/chrome-linux64/chrome --headless=new --disable-gpu --hide-scrollbars --window-size=1024,1024 --screenshot=/tmp/poster.png "file://<abs>/poster.html"`, then convert PNG to JPEG with Pillow (`python3 -c "from PIL import Image; Image.open(x27/tmp/poster.pngx27).convert(x27RGBx27).save(x27entry.jpgx27, quality=88, optimize=True)"`).
- LICENSE MIT, README with badges, `.makefun/owner.json` already there.

## How to work
1. Write poster.html.
2. Render, look at the image, fix overflow/clipping/wrapping until every block is clean.
3. Produce entry.jpg under 1 MiB and 1024x1024; run `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py` and confirm out/entry.png.
4. Revise the layout at least twice, commit and push to origin main.
