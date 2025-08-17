import json
from pathlib import Path


def json_from_file():
    # BASE_DIR = Path(__file__).resolve(strict=True)
    # file_path = Path(__file__).parent.parent / "country-by-languages.json"
    # file_path = Path(__file__).parents[1] / "country-by-languages.json"
    file_path = Path(__file__).parents[1].resolve(strict=True) / "country-by-languages.json"

    with file_path.open('r') as file:
        countries_items = json.load(file)

    return countries_items