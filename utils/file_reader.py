import json
import pytest
from pathlib import Path

def load_test_data(filename):
    # Mencari path file secara dinamis
    BASE_DIR = Path(__file__).resolve().parent.parent

    file_path = BASE_DIR / "data" / filename

    with open(file_path) as f:
        data = json.load(f)
        # Mengembalikan list of tuples atau values
        return [(d['email'], d['password'], d['expected_status'], d['test_id']) for d in data]