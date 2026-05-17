import subprocess
from pathlib import Path
import uuid

def convert_ppt_to_pdf(input_file: str, output_dir: str) -> Path:
    """
    Converts a PowerPoint file to a PDF.

    Args:
        input_file (str): The path to the input PowerPoint file.
        output_dir (str): The directory to save the output PDF file.

    Returns:
        Path: The path to the generated PDF file.
    """
    input_path = Path(input_file).resolve()

    if not input_path.exists():
        raise FileNotFoundError(f"{input_file} not found")

    output_path = Path(output_dir).resolve()
    output_path.mkdir(parents=True, exist_ok=True)

    pdf_name = f"{uuid.uuid4().hex}.pdf"
    final_output_path = output_path / pdf_name

    command = [
        "soffice",
        "--headless",
        "--convert-to",
        "pdf:writer_pdf_Export",
        "--outdir",
        str(output_path),
        str(input_path),
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())

    generated_pdf = output_path / f"{input_path.stem}.pdf"

    if not generated_pdf.exists():
        raise RuntimeError("PDF was not created")

    generated_pdf.rename(final_output_path)

    return final_output_path
