import os
from PyPDF2 import PdfReader, PdfWriter
import zipfile

def split_pdf(input_path: str, ranges_str: str, output_dir: str) -> str:
    """
    Splits a PDF file based on specified ranges.

    Args:
        input_path (str): The path to the input PDF file.
        ranges_str (str): A string of comma-separated page ranges (e.g., "1-3,5,7-9").
        output_dir (str): The directory to save the output files.

    Returns:
        str: The path to the generated zip file containing the split PDFs.
    """
    reader = PdfReader(input_path)
    ranges = _parse_ranges(ranges_str, len(reader.pages))
    
    output_paths = []
    for i, page_range in enumerate(ranges):
        writer = PdfWriter()
        for page_num in page_range:
            writer.add_page(reader.pages[page_num - 1])
        
        base_filename = os.path.splitext(os.path.basename(input_path))[0]
        output_filename = f"{base_filename}_range_{i+1}.pdf"
        output_path = os.path.join(output_dir, output_filename)
        
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        output_paths.append(output_path)

    zip_path = os.path.join(output_dir, "split_files.zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file_path in output_paths:
            zipf.write(file_path, os.path.basename(file_path))
            os.remove(file_path)

    return zip_path

def _parse_ranges(ranges_str: str, total_pages: int) -> list[list[int]]:
    """
    Parses a string of page ranges into a list of page lists.
    Example: "1-3,5,7-9" -> [[1, 2, 3], [5], [7, 8, 9]]
    """
    result = []
    for part in ranges_str.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            if start > end or start < 1 or end > total_pages:
                raise ValueError(f"Invalid page range: {part}")
            result.append(list(range(start, end + 1)))
        else:
            page_num = int(part)
            if page_num < 1 or page_num > total_pages:
                raise ValueError(f"Invalid page number: {page_num}")
            result.append([page_num])
    return result

        