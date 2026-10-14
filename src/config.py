
import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

# Find the root project directory.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load settings from the local .env file.
load_dotenv(PROJECT_ROOT / ".env")


@dataclass(frozen=True)
class Settings:
    eia_api_key: str | None
    eia_base_url: str


def load_settings() -> Settings:
    """Load application settings from environment variables."""
    api_key = os.getenv("EIA_API_KEY")

    if api_key:
        api_key = api_key.strip() or None

    return Settings(
        eia_api_key=api_key,
        eia_base_url="https://api.eia.gov/v2",
    )
