import img2pdf
import os
import uuid
from typing import List

def convert_images_to_pdf(image_paths: List[str], output_dir: str) -> str:
    """
    Converts one or more images to a single PDF file.

    Args:
        image_paths (List[str]): A list of paths to the input image files.
        output_dir (str): The directory to save the output PDF file.

    Returns:
        str: The path to the generated PDF file.
    """
    pdf_filename = f"{uuid.uuid4().hex}.pdf"
    pdf_path = os.path.join(output_dir, pdf_filename)

    with open(pdf_path, "wb") as f:
        f.write(img2pdf.convert(image_paths))

    return pdf_path
