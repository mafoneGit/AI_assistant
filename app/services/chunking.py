def split_text(text: str) -> list[str]:
    chunks = []
    current_section = []

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        if line.startswith("[") and line.endswith("]"):
            if current_section:
                chunks.append("\n".join(current_section))

            current_section = [line]
        else:
            current_section.append(line)

    if current_section:
        chunks.append("\n".join(current_section))

    return chunks