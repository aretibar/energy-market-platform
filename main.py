from src.config import load_settings

settings = load_settings()
print("Key loaded:", settings.eia_api_key is not None)

import requests

from src.config import load_settings


def describe_route(path: str) -> None:
    """Ask EIA what exists at a given route and print a short summary."""
    settings = load_settings()

    if settings.eia_api_key is None:
        raise SystemExit("EIA_API_KEY is missing. Check your .env file.")

    url = f"{settings.eia_base_url}/{path}"
    response = requests.get(
        url,
        params={"api_key": settings.eia_api_key},
        timeout=30,
    )
    response.raise_for_status()

    body = response.json()["response"]
    print(f"Route: {path} -> {body.get('name')}")

    for child in body.get("routes", []):
        print(f"  child route: {child['id']} - {child['name']}")

    for frequency in body.get("frequency", []):
        print(f"  frequency: {frequency['id']}")

    for facet in body.get("facets", []):
        print(f"  facet (filter): {facet['id']}")

    for column in body.get("data", {}):
        print(f"  data column: {column}")


if __name__ == "__main__":
    describe_route("petroleum/pri")