# Public edition: what this repository contains

Prepared 15.11.2026.

## `zenodo/` — the Zenodo deposit, unchanged

12 of the 13 files of the deposit of 05.09.2026 (DOI 10.5281/zenodo.22306911), copied byte for byte from the
folder the deposit was uploaded from; nothing was edited. The 13th file, `supplement.pdf`, is not mirrored because
it carries the author's contact e-mail; download it from the Zenodo record. It is not part of `MANIFEST.sha256`
and no check depends on it. After unpacking the three archives, `python _manifest.py verify` reports 960 files
matching `MANIFEST.sha256`, 0 changed, 0 missing; the 5 files that exist only at deposit level
(`certificates.zip`, `code.zip`, `data.zip`, `LICENSE`, `LICENSE-DATA`) are reported as extra by design.

## `paper/` — the English article

The LaTeX source of the arXiv submission of 05.09.2026, with one change: the author's contact e-mail line was
removed from `frontmatter.tex`. All other source files are byte-identical to the submitted source.
`main.pdf` was rebuilt from this source with `pdflatex` (three passes, using the shipped `main.bbl`): 137 pages,
no undefined references. The mathematics, numbers and references are those of the submitted version.

## Checks run on this edition (15.11.2026)

On the unpacked deposit (Windows, Python 3.13.13, python-flint 0.9.0), from `04-CODE/` with the environment of
`02-REPRODUCE.md`:

| Check | Result |
|---|---|
| `_manifest.py verify` | 960 files match, 0 changed, 0 missing |
| `tube_accept.py` | `ПРИЁМКА: ПРОЙДЕНА` (acceptance passed), 706 boxes, worst value 0.991843707457 |
| `tests/_tau_test.py` | pre-fix version 15 failures, current version 0 (the test is able to fail) |
| `tests/_numbers_check.py` | 0 failures out of 790 checks of article numbers against the certificates |

The full recomputation of the certificates (about 9 core-hours) was not repeated for this edition.
