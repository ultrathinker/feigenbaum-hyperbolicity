# Existence and hyperbolicity of the period-doubling renormalization fixed point for non-integer critical exponents

**Yevhen Borzenkov** · ORCID [0009-0002-7946-589X](https://orcid.org/0009-0002-7946-589X)
Deposited at Zenodo, DOI [10.5281/zenodo.22306911](https://doi.org/10.5281/zenodo.22306911) (05.09.2026). Not peer-reviewed.
Русская версия — [README.ru.md](README.ru.md).

A computer-assisted proof, in validated interval arithmetic, that for **every** critical exponent ℓ ∈ [2, 4] —
not only at even integers — the period-doubling renormalization operator has a fixed point, and that this fixed
point is hyperbolic with a one-dimensional unstable direction.

## Theorems

For every ℓ ∈ [2, 4], in a space of analytic functions on an explicit disk:

- **A (existence).** The Feigenbaum–Cvitanović equation has a solution G*(ℓ), G*(0) = 1, in a ball of radius
  8.49·10⁻¹³ around an explicit centre; it is unique within 1.75·10⁻⁷ on the normalization slice.
  46 boxes, Newton–Kantorovich.
- **B (hyperbolicity).** The derivative of renormalization at G*(ℓ) has exactly one eigenvalue outside the unit
  circle, δ(ℓ), real and simple; the rest of the spectrum lies strictly inside. 706 boxes, operator Rouché theorem,
  worst acceptance value 0.9919 < 1.
- **C (analyticity).** G*(ℓ) and δ(ℓ) depend real-analytically on ℓ; δ(ℓ) ∈ [4.6747, 7.2854].
- **D (independence of the layer).** The non-zero spectrum and its multiplicities do not depend on the choice of
  the function-space layer within an explicitly certified family.

Control: δ(4) agrees with the high-precision quartic value of Burbanks–Osbaldestin–Thurlby to 6.68·10⁻¹⁵.
Earlier results (Gorbovickis–Yampolsky; Cruz–Smania) cover neighbourhoods of even integers of unspecified width;
here the covering is explicit and uniform and contains ℓ = 5/2 and ℓ = 3.

## Repository layout

| Path | Contents |
|---|---|
| [`paper/main.pdf`](paper/main.pdf) | The article in English (137 pages), built from the LaTeX source in [`paper/`](paper/) |
| [`zenodo/`](zenodo/) | The Zenodo deposit, file for file: article and reproduction guide (in Russian), `code.zip`, `certificates.zip`, `data.zip`, `MANIFEST.sha256`, `_manifest.py`; the supplement PDF is in the [Zenodo record](https://doi.org/10.5281/zenodo.22306911) |
| [`PUBLICATION-NOTES.md`](PUBLICATION-NOTES.md) | How this repository relates to the Zenodo deposit and to the arXiv source |

## Reproducing

Python 3.13, `python-flint` 0.9.0 (FLINT 3.6.0), `numpy`, `scipy`, `mpmath` 1.3.0. Unpack the three archives of
`zenodo/` next to the markdown files and check the package:

```
cd zenodo
python -c "import zipfile, glob; [zipfile.ZipFile(z).extractall('.') for z in glob.glob('*.zip')]"
python _manifest.py verify     # 960 files match; the 5 deposit-level files (zips, licenses) are reported as extra
```

Then follow `zenodo/02-REPRODUCE.md` (environment variables, commands, expected output). Quick checks from
`04-CODE/`: `tube_accept.py` (acceptance of the hyperbolicity tube), `tests/_tau_test.py`, `tests/_numbers_check.py`
(every number of the article against the certificates). All three pass on this edition (15.11.2026).

## Use of AI tools

The computations, code and text were prepared with the help of AI tools; every claim marked rigorous rests
on an interval-arithmetic certificate that is reproduced by the code in this repository.

## Related work by the author

- Zeros of the universal scaling function of the period-doubling cascade —
  [feigenbaum-h-zeros](https://github.com/ultrathinker/feigenbaum-h-zeros).
- The "parameter ↔ unstable manifold" correspondence for universality classes d = 2, 4, 6 —
  [feigenbaum-universality-classes](https://github.com/ultrathinker/feigenbaum-universality-classes).

## Citation and license

Please cite the Zenodo record, DOI [10.5281/zenodo.22306911](https://doi.org/10.5281/zenodo.22306911); metadata —
[`CITATION.cff`](CITATION.cff). License — MIT ([`LICENSE`](LICENSE)), for code, data and text.
