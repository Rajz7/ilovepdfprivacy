import subprocess
from pathlib import Path

# works for .doc and .docx
def convert_word_to_pdf(input_path):
    input_path = Path(input_path).resolve()

    output_dir = input_path.parent

    pdf_name = f"{input_path.stem}.pdf"
    output_path = output_dir / pdf_name

    i = 1
    while output_path.exists():
        output_path = output_dir / f"{input_path.stem}_{i}.pdf"
        i += 1

    command = [
        "soffice",
        "--headless",
        "--convert-to",
        "pdf",
        str(input_path),
        "--outdir",
        str(output_dir)
    ]

    subprocess.run(command, check=True)
    generated_pdf = output_dir / f"{input_path.stem}.pdf"

    if generated_pdf != output_path:
        generated_pdf.rename(output_path)

    return output_path


pdf = convert_word_to_pdf("/home/lamborghini/Downloads/odtfile.docx")

print("Created:", pdf)