# IMPORTS
from pathlib import Path

# RANDOM SEED
SEED = 42

# ========================================================
# PATHS (relative to notebook files)
# ========================================================
PROJECT_ROOT = Path("..")

# DATA PATHS
RAW_DATA_DIR = PROJECT_ROOT / "01_data" / "01_raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "01_data" / "02_processed"

RAW_ANNDATA_FILE = RAW_DATA_DIR / "Norman_2019_raw.h5ad"

# OUTPUT PATHS
FIGURES_DIR = PROJECT_ROOT / "03_figures"
RESULTS_DIR = PROJECT_ROOT / "04_results"