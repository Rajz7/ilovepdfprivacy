import subprocess
from pathlib import Path

#excel, ppt 

def file_to_pdf(input_file):
    input_path = Path(input_file)

    if not input_path.exists():
        raise FileNotFoundError(f"{input_file} not found")

    subprocess.run([
        "soffice",
        "--headless",
        "--convert-to", "pdf",
        str(input_path),
        "--outdir",
        str(input_path.parent)
    ], check=True)

    output_file = input_path.with_suffix(".pdf")

    return output_file

pdf_path = file_to_pdf("/home/lamborghini/Downloads/ppt.pptx")
print(f"Created: {pdf_path}")