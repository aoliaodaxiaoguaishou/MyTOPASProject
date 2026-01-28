# MyTOPASProject
The pipeline couples track-structure Monte Carlo simulation in realistic ellipsoidal cell/nucleus geometries with mechanistic DNA repair/misrepair modeling, enabling dose–response analysis before and after repair under low-dose-rate internal irradiation.
> [!NOTE]
> This repository is a **research code bundle** for reproducible Monte Carlo radiobiology studies built on **OpenTOPAS + TOPAS-nBio + TOPAS-CellModels**.  
> Key custom additions include **regular multi-cell arrangement at the bottom of a medium**, **ellipsoidal cell/nucleus geometry**, **ellipsoidal cell membrane/cytoplasm**, and an **ellipsoidal phase-space scoring surface** on the target nucleus.

# MyTOPASProject

This project couples **track-structure Monte Carlo simulation** in realistic **ellipsoidal cell/nucleus geometries** with downstream **DNA damage / repair / misrepair analysis**, enabling **dose–response characterization** for low-dose-rate internal irradiation scenarios.

---

## Repository layout

- `OpenTOPAS/`  
  OpenTOPAS source code (included for reproducibility).

- `TOPAS-nBio/`  
  TOPAS-nBio extension (sub-cellular radiobiology framework).

- `TOPAS-CellModels/`  
  Cell modeling extension (cell/nucleus/membrane-related geometries).

- `geant4/`  
  Geant4 source (included for reproducibility / local builds depending on your workflow).

- Python helper scripts (project-specific):
  - `process_phsp.py`  
    **Data collection & summarization**.  
    Used to collect:
    1) particle information reaching the **target ellipsoidal phase-space surface** (on/around the nucleus), and  
    2) information related to **DNA damage** induced in the nucleus after irradiation,  
    then exports **tables** for convenient statistics (e.g., CSV/Excel-style summaries).

  - `beta_medium_topasfile.py`  
    Generates TOPAS input for the scenario: **β electrons emitted by radionuclides in the culture medium** → scored on the **target nucleus surface phase space**.

  - `IC_medium_topasfile.py`  
    Generates TOPAS input for the scenario: **IC (internal conversion) electrons emitted by radionuclides in the culture medium** → scored on the **target nucleus surface phase space**.

  - `beta_cell_topasfile.py`  
    Generates TOPAS input for the scenario: **β electrons emitted by radionuclides in the target cell and surrounding cells** (typically **cytoplasm**, and can also represent **membrane** depending on the configuration) → scored on the **target nucleus surface phase space**.

  - `IC_cell_topasfile.py`  
    Generates TOPAS input for the scenario: **IC electrons emitted by radionuclides in the target cell and surrounding cells** (typically **cytoplasm**, and can also represent **membrane** depending on the configuration) → scored on the **target nucleus surface phase space**.

---

## What is custom in this project

Compared with stock extensions, this project includes custom implementations for:

- **Regular multi-cell arrangement** on the **bottom of the culture medium** (ordered cell layout)
- **Ellipsoidal phase-space scoring surface** (for collecting particles incident on the nucleus boundary)
- **Ellipsoidal cell membrane/cytoplasm**
- **Ellipsoidal nucleus**

These components are intended to better match realistic cell morphology and to support consistent phase-space based downstream analysis.

---

## Build & installation (recommended workflow)

> [!TIP]
> If you are on Debian/Ubuntu, use the provided quick start file:
> **`OpenTOPAS_quickStart_Debian.md`** (install deps → build Geant4/OpenTOPAS → run a first demo).

### Build OpenTOPAS with extensions in this repo

When configuring OpenTOPAS, include extensions via `TOPAS_EXTENSIONS_DIR`.

Example (from repository root):

```bash
mkdir -p OpenTOPAS-build
cd OpenTOPAS-build

# NOTE: Use '\;' between multiple extension paths (GitHub README callout style)
cmake ../OpenTOPAS \
  -DCMAKE_INSTALL_PREFIX=../OpenTOPAS-install \
  -DTOPAS_EXTENSIONS_DIR=../TOPAS-nBio\;../TOPAS-CellModels

make -j8 install
