"""
Load .env from project root so API keys work when running from any directory.
"""

import os
from pathlib import Path

from dotenv import load_dotenv


def find_project_env() -> Path | None:
    """Find .env by walking up from cwd (so CLI/scripts work from any subdir)."""
    cwd = Path(os.getcwd()).resolve()
    for parent in [cwd, *cwd.parents]:
        env_file = parent / ".env"
        if env_file.is_file():
            return env_file
    return None


def load_env() -> None:
    """Load .env from project root; fall back to cwd. Does not override existing env."""
    env_path = find_project_env()
    if env_path:
        load_dotenv(env_path, override=False)
    else:
        load_dotenv()


def require_openai_key() -> bool:
    """Return True if a supported LLM provider key is set."""
    return bool(
        os.getenv("OPENAI_API_KEY") or os.getenv("GROQ_API_KEY")
    )
