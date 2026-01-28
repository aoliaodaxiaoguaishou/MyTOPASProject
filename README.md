# MyTOPASProject
The pipeline couples track-structure Monte Carlo simulation in realistic ellipsoidal cell/nucleus geometries with mechanistic DNA repair/misrepair modeling, enabling dose–response analysis before and after repair under low-dose-rate internal irradiation.


This repository supports **low-dose-rate internal irradiation** studies by coupling **track-structure Monte Carlo simulation** (OpenTOPAS / TOPAS-nBio / TOPAS-CellModels) with downstream **DNA damage analysis** (and optionally repair/misrepair modeling), enabling **dose–response characterization** in realistic **ellipsoidal cell/nucleus geometries**.

---

## Key custom features (implemented in this project)

Compared with stock components, this project includes custom implementations for:

- **Regular multi-cell arrangement** on the **bottom of the culture medium**
- **Ellipsoidal phase-space scoring surface** on/around the **target nucleus**  
  (used to collect particles reaching the target ellipsoidal surface)
- **Ellipsoidal cell membrane/cytoplasm**
- **Ellipsoidal nucleus**

---

## Repository layout

- `OpenTOPAS/`  
  OpenTOPAS source code (included for reproducibility)

- `TOPAS-nBio/`  
  TOPAS-nBio extension (sub-cellular radiobiology framework)

- `TOPAS-CellModels/`  
  Cell model extension (cell/nucleus/membrane geometries)

- `geant4/`  
  Geant4 source code (included for reproducibility)

- Project Python scripts (workflow entry points)
  - `process_phsp.py`  
    **Data collection & summarization**.  
    This script is used to:
    1) collect particle information reaching the **target ellipsoidal phase-space surface**, and  
    2) collect information related to **nuclear DNA damage** induced by irradiation,  
    then export **structured tables** for convenient statistics and plotting.

  - `beta_medium_topasfile.py`  
    Scenario: **β electrons** emitted by radionuclides in the **culture medium** → scored on the **target nucleus surface phase space**.

  - `IC_medium_topasfile.py`  
    Scenario: **IC (internal conversion) electrons** emitted by radionuclides in the **culture medium** → scored on the **target nucleus surface phase space**.

  - `beta_cell_topasfile.py`  
    Scenario: **β electrons** emitted by radionuclides in the **target cell and surrounding cells** (typically **cytoplasm**, and can also represent **membrane** depending on configuration)  
    → scored on the **target nucleus surface phase space**.

  - `IC_cell_topasfile.py`  
    Scenario: **IC electrons** emitted by radionuclides in the **target cell and surrounding cells** (typically **cytoplasm**, and can also represent **membrane** depending on configuration)  
    → scored on the **target nucleus surface phase space**.

> Note: With appropriate parameter settings, `beta_cell_topasfile.py` and `IC_cell_topasfile.py` can also represent radionuclide distributions in the **cell membrane** (instead of cytoplasm).

---

## Typical pipeline

1. **Generate TOPAS input** using one of:
   - `beta_medium_topasfile.py`
   - `IC_medium_topasfile.py`
   - `beta_cell_topasfile.py`
   - `IC_cell_topasfile.py`

2. **Run OpenTOPAS** with the generated parameter file(s) to produce:
   - phase-space outputs on the **target ellipsoidal surface**
   - DNA damage outputs (depending on your scoring configuration)

3. **Post-process / summarize** using `process_phsp.py` to obtain structured tables for statistics and plotting.

> [!NOTE]
> The exact output paths / naming conventions depend on how you set parameters inside each script and which TOPAS scoring blocks you enable. If you change output directories or file name prefixes, keep the post-processing script consistent.

---

## Quick start

- For Debian/Ubuntu, follow:
  - `OpenTOPAS_quickStart_Debian.md`

> If you already have your own OpenTOPAS build workflow, make sure the build/runtime configuration properly enables the `TOPAS-nBio` and `TOPAS-CellModels` extensions.

---

## Reproducibility tips (recommended)

To make results easier to reproduce, consider recording the following in your notes / issues / supplementary material:

- OS / compiler / CMake versions
- Geant4 / OpenTOPAS / TOPAS-nBio versions (or commit IDs)
- key physics list + cuts/steps + scoring configuration summary
- random seed strategy and number of histories
- output directory structure (phase space vs. damage outputs)

---

## References & acknowledgements

- OpenTOPAS documentation: https://opentopas.readthedocs.io/
- TOPAS-nBio documentation: https://topas-nbio.readthedocs.io/
- Geant4: https://geant4.org/

If you use TOPAS-nBio in publications, please cite the TOPAS-nBio reference listed in the TOPAS-nBio repository documentation.

---

## Bugs / contact

If you encounter issues, please open a GitHub Issue with:

- your OS + compiler + CMake version
- build log snippet (or runtime error log)
- minimal input needed to reproduce the issue (minimal parameter file + relevant scripts/data)

