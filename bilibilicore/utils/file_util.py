import os
from pathlib import Path


def check_and_mkdir(path):
    path = Path(path)
    if not path.is_dir():
        path.mkdir(
            parents=True,
            exist_ok=True,
        )
    return True


def get_app_data_dir(app_name: str, makedir=False) -> Path:
    # Determine the OS-specific app data directory
    app_data_path = None
    if os.name == "nt":  # Windows
        app_data_path = Path(os.getenv("APPDATA"))
    else:  # macOS/Linux
        app_data_path = Path.home() / ".local" / "share"

    # Create the application-specific directory
    app_dir = app_data_path / app_name

    # Ensure the directory exists
    if makedir:
        app_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    return app_dir


def clean_tmp(*files):
    for file in files:
        if file.exists():
            file.unlink()
