from pathlib import Path

import pytest

from app.services.document_loader import load_text_file


def test_load_text_file(tmp_path: Path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello RAG", encoding="utf-8")

    result = load_text_file(str(file_path))

    assert result == "Hello RAG"


def test_load_text_file_raises_error_for_missing_file():
    with pytest.raises(FileNotFoundError):
        load_text_file("missing_file.txt")