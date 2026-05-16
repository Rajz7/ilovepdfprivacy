import subprocess
from pathlib import Path
import uuid


def convert_word_to_pdf(input_file: str, output_dir: str | None = None) -> Path:
    input_path = Path(input_file).resolve()

    if not input_path.exists():
        raise FileNotFoundError(input_path)

    output_dir = Path(output_dir).resolve() if output_dir else input_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_name = f"{uuid.uuid4().hex}.pdf"
    output_path = output_dir / pdf_name

    command = [
        "soffice",
        "--headless",
        "--convert-to",
        "pdf:writer_pdf_Export",
        "--outdir",
        str(output_dir),
        str(input_path),
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())

    generated_pdf = output_dir / f"{input_path.stem}.pdf"

    if not generated_pdf.exists():
        raise RuntimeError("PDF was not created")

    generated_pdf.rename(output_path)

    return output_path
