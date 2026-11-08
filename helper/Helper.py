from pathlib import Path


def read_prompts(filename):
    data_folder = Path(__file__).parent.parent / "prompts"
    file_path = data_folder / filename

    try:
        # Read and return the entire prompt as a clean string
        return file_path.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        print(f"⚠️ Warning: Prompt file '{filename}' not found at {file_path}")
        return ""  # Return empty string or fallback prompt
