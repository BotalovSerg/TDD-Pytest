import pytest
from pathlib import Path


@pytest.fixture(autouse=True)
def clean_text_file(test_file_path):
    """Очищает файл перед каждым тестом."""
    with open(test_file_path, "w", encoding="utf-8") as f:
        f.truncate()


@pytest.fixture
def test_file_path() -> Path:
    """Возвращает путь к тестовому файлу во временной директории."""
    file_path = (Path(__file__).parent / "testfile.txt").resolve()
    return file_path
