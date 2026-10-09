import json, pytest
from pathlib import Path

@pytest.fixture
def data(data_name):
    data_file = Path(f"languages/{data_name}.json")  

    with open(data_file, "r") as f:
        return json.load(f)

def check_indicators(data):
    assert "indicators" in data

def check_number_indicator(data):
    assert isinstance(data.get("indicators").get("number"), list)

def check_mayus_indicator(data):
    assert isinstance(data.get("indicators").get("mayus"), list)

def check_alphabet(data):
    assert "letters" in data and len(data["letters"]) == o

def check_numbers(data):
    assert "numbers" in data and len(data["numbers"]) == 0

def check_punctuation_signs(data):
    assert "punctuation" in data and len(data["punctuation"]) == 0


def check_lang_info(data):
    assert "language" in data and data["language"]["code"] is not None and data["language"]["native_name"] is not None

def check_grade(data):
    # grade 3 is omitted, but will be considered during the final implementation.
    if not "contractions" in data:
        assert data["language"]["grade_supported"] == 1
    elif "contractions" in data:
        assert data["language"]["grade_supported"] == 2