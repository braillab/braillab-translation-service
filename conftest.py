import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--data_name", 
        action="store", 
        default="en", 
        help="language data abbreviation to test (es, en)"
    )

@pytest.fixture
def data_name(request):
    return request.config.getoption("--data_name")