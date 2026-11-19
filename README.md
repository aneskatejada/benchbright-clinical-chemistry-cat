# BenchBright Learning — Clinical Chemistry Computer-Adaptive Practice Exam

**Standalone responsive CAT website • 100 questions per attempt • 976 indexed questions (608 presently usable)**

This repository is self-contained and designed for GitHub Pages. The exam loads from a single generated `index.html`; no separate CSS or JavaScript paths are necessary. It works when opened locally and on GitHub Pages.

## Exam mechanics

- **100 questions per attempt** selected from the current pool of `status=ready` items.
- **Dynamic item selection:** the system selects the next question *after* receiving each response, rather than fixing a 100-question test in advance.
- **Bayesian ability estimate:** an estimated ability theta (θ) is updated using all prior correct and incorrect responses, with a standard-normal-like prior and a provisional Rasch/1PL item response model.
- **Difficulty bands 1–5:** used to target questions close to the current ability estimate. These are **uncalibrated heuristic labels** until sufficient student response data becomes available.
- **Randomized questions and answer positions** on every attempt; no repeats within a session.
- **Topic coverage:** a randomized subject-slot plan allocates the test in proportion to the available bank, while each actual question is adaptively selected in its category.
- **No backtracking or instant answer reveal**, so users cannot change earlier responses after seeing harder/easier items. Full review is available at the end.
- **Results:** raw percentage correct, estimated theta, approximate SE, scores by topic, 100 question rationales, and downloadable results CSV.
- **Local resume:** in-progress attempt stored in each student's browser via `localStorage` (not synchronized between devices). Data changes reset in-progress attempts.

> This is an adaptive *practice* exam, **not** a validated psychometric ASCP CAT. No official pass/fail score or prediction is calculated.

## How to publish on GitHub Pages

1. Create a **new repository**, suggested name: `benchbright-clinical-chemistry-cat`.
2. **Before making the repository public:** review copyright and permission considerations below. Your CSV contains near-verbatim content derived from named review books.
3. Extract the ZIP, and upload **all files and folders to the repository root**, including the hidden `.github` folder. You can also add them using the GitHub web upload interface.
4. Commit to branch `main`.
5. Open **Settings → Pages → Build and deployment → Source: GitHub Actions**.
6. Open **Actions** and wait for the `Build and publish Chemistry CAT` workflow to pass.
7. The public address (if you are authorized to publish) will be `https://YOUR-USERNAME.github.io/benchbright-clinical-chemistry-cat/`.
8. After deployment, open the link and start an exam to confirm the browser can run JavaScript. The page should have dark navy / teal styling. If it looks like plain text, re-upload this *single-file build* rather than a previous multi-file version.

The supplied `index.html` can be opened locally for offline testing before publishing.

## Update questions from Excel

All **976** source questions are retained in `data/questions.csv`. `status=review` entries are excluded from live exams. The initial bank has 608 `status=ready` questions and 368 review items.

1. Open `data/questions.csv` in Excel or Google Sheets.
2. Edit `question`, `A`, `B`, `C`, `D`, `answer`, `rationale`, `section`, and `difficulty` (1 through 5) as needed.
3. For reviewed/corrected entries, change `status` from `review` to `ready` after checking that the stem, all four answer options, and answer key are accurate and that you have permission to publish the content.
4. Save back to **CSV UTF-8**. Preserve header names and unique IDs.
5. Commit the CSV update to `main` on GitHub. The Actions workflow validates, rebuilds, and redeploys the page automatically.
6. For an updated standalone offline HTML: run `python scripts/build.py` locally and replace `index.html` in the repository if desired.

**Do not mark all unreviewed questions as `ready` without checking the content.** Many BOC OCR rows have answer options merged with neighboring questions.

## Repository files

```text
index.html                  Single-file, prebuilt functioning website
site/index.template.html    Source HTML/CSS/JavaScript without embedded question data
data/questions.csv          Full editable bank + review status + difficulty
scripts/build.py            Pure Python standard-library website builder
tests/test_bank.py          Data validation tests
.github/workflows/pages.yml  Automatic GitHub Pages builder and deployer
QUALITY_REVIEW.md           Data-quality and qualification report
README.md                   Setup and maintenance instructions
```

## Current-bank limitations

- There are 976 spreadsheet rows: 356 BOC and 620 Harr. The bank currently exposes **608 structurally valid Harr items**; it retains all 356 BOC entries plus 12 Harr review entries for correction.
- The spreadsheet's BOC selections include OCR artifacts and missing options. All BOC questions are initially flagged for source review.
- Harr source taxonomy footers such as `Chemistry/Apply ...` have been removed *from displayed option D* during import. Their original text is retained in the supplied original workbook.
- Three later duplicate stems, one duplicated-choice item and eight structurally incomplete Harr items are held out pending review.
- Heuristic difficulty levels were assigned from stems/complexity within a topic, **not** statistically calibrated. The ability estimate is a learning metric only.
- Rationale text is copied from the uploaded Excel and should be verified by a chemistry subject-matter expert before teaching/publication.
- The website embeds questions in HTML. Anyone with the URL can view page source and extract the answer key; **GitHub Pages is not a secure paid testing platform**. Hosting a public repository exposes the full source question bank and answer key.

## Copyright and access control

**Important:** This Excel bank identifies BOC Study Guide (5th ed.) and Harr Medical Laboratory Science Review (4th ed.) as its sources. The uploaded text may be copyrighted. Owning a textbook or having compiled an Excel sheet does **not** automatically grant redistribution or commercial publishing rights. Do not upload these textbook-derived questions to a public repository or sell the exam without appropriate licenses or permission. For a Payhip product, a bank of fully original, licensed questions is safer. Even if the GitHub repo is private, free GitHub Pages may require public publication depending on the account plan; the single static-file approach does not secure answers. This project is a technical prototype and does not establish publication rights.

## Troubleshooting

- **White, unstyled page / broken button:** This version uses *one self-contained HTML file*. Make sure Pages deploys `dist/index.html` from the workflow (or upload `index.html` at the root for branch-based publishing).
- **Workflow fails:** Open Actions logs. A newly marked-ready question may be missing a correct answer, options, rationale or difficulty.
- **Changes not showing:** Wait until Actions reports success, then hard-refresh the browser.
- **Exam restarts on a new phone:** Saved progress is local to the browser/device.
- **Changing the CSV doesn't update the standalone downloaded HTML:** Commit the CSV to GitHub (workflow rebuilds) or run `python scripts/build.py` yourself to regenerate it locally.
