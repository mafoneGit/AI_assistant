from app.services.chunking import split_text


def test_split_text_keeps_small_text_as_one_chunk():
    text = "First paragraph.\n\nSecond paragraph."

    chunks = split_text(text, chunk_size=100)

    assert chunks == ["First paragraph.\n\nSecond paragraph."]


def test_split_text_creates_multiple_chunks():
    text = (
        "First paragraph.\n\n"
        "Second paragraph.\n\n"
        "Third paragraph."
    )

    chunks = split_text(text, chunk_size=30)

    assert len(chunks) > 1


def test_split_text_ignores_empty_paragraphs():
    text = "First paragraph.\n\n\n\nSecond paragraph."

    chunks = split_text(text, chunk_size=100)

    assert chunks == ["First paragraph.\n\nSecond paragraph."]