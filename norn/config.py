from pathlib import Path

cwd = Path(__file__).absolute()

PROJECT_BASEPATH = cwd.parent.parent

DATA_BASEPATH = PROJECT_BASEPATH / "Data"