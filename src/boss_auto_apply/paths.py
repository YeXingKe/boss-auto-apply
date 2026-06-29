"""Repository paths — config and runtime data live at project root."""
from __future__ import annotations

import os
import sys
from pathlib import Path

_PKG_DIR = Path(__file__).resolve().parent
_SRC_DIR = _PKG_DIR.parent


def _detect_project_root() -> Path:
    override = os.environ.get("BOSS_PROJECT_ROOT", "").strip()
    if override:
        return Path(override).resolve()

    for candidate in (_SRC_DIR.parent, _SRC_DIR, _PKG_DIR):
        if (candidate / "pyproject.toml").exists():
            return candidate
        if (candidate / "config.yaml.example").exists():
            return candidate
    return _SRC_DIR.parent


PROJECT_ROOT = _detect_project_root()
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "docs"
CONFIG_PATH = PROJECT_ROOT / "config.yaml"
ENV_LOCAL_PATH = PROJECT_ROOT / ".env.local.ps1"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"


def venv_python() -> Path:
    candidate = PROJECT_ROOT / ".venv" / "Scripts" / "python.exe"
    if candidate.exists():
        return candidate
    return Path(sys.executable)


def runtime_dir() -> Path:
    raw = ""
    if os.name == "nt":
        raw = os.getenv("HERMES_BOSS_RUNTIME_DIR_WIN", "").strip()
    if not raw:
        raw = os.getenv("HERMES_BOSS_RUNTIME_DIR", "").strip()
    path = Path(raw) if raw else DATA_DIR
    path.mkdir(parents=True, exist_ok=True)
    return path


def ensure_data_dir() -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return DATA_DIR
