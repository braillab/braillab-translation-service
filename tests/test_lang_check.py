import json, pytest
from pathlib import Path

@pytest.fixture
def data(data_name):
    data_file = Path(f"languages/{data_name}.json")
    with open(data_file, "r") as f:
        return json.load(f)

def test_indicators(data):
    assert "indicators" in data

def test_number_indicator(data):
    assert isinstance(data["indicators"].get("number"), list)

def test_mayus_indicator(data):
    assert isinstance(data["indicators"].get("mayus"), list)

def test_alphabet(data):
    assert len(data.get("letters", [])) > 0

def test_numbers(data):
    assert len(data.get("numbers", [])) > 0

def test_punctuation_signs(data):
    assert len(data.get("punctuation", [])) > 0

def test_lang_info(data):
    lang = data.get("language", {})
    assert lang.get("code") is not None
    assert lang.get("native_name") is not None

def test_grade(data):
    # grade 3 is omitted, but will be considered during the final implementation.
    expected = 2 if len(data.get("contractions", [])) > 0 else 1
    assert data["language"]["grade_supported"] == expected