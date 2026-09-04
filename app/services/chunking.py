def split_text(text: str) -> list[dict]:
    chunks = []
    current_section = None
    current_lines = []

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        if line.startswith("[") and line.endswith("]"):
            if current_section and current_lines:
                chunks.append(
                    {
                        "section": current_section,
                        "text": "\n".join(current_lines),
                    }
                )

            current_section = line[1:-1]
            current_lines = []
        else:
            current_lines.append(line)

    if current_section and current_lines:
        chunks.append(
            {
                "section": current_section,
                "text": "\n".join(current_lines),
            }
        )

    return chunks