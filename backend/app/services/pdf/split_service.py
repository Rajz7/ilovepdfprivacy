from PyPDF2 import PdfReader, PdfWriter

#incomplete
def split_pdf_in_each_pages(input_pdf: str):
    reader = PdfReader(input_pdf)

    for page_num in range(len(reader.pages)):
        writer = PdfWriter()

        writer.add_page(reader.pages[page_num])

        output_filename = input_pdf[:input_pdf.rfind('.')]
        output_filename = f"{output_filename}_page_{page_num + 1}.pdf"

        with open(output_filename, "wb") as output_file:
            writer.write(output_file)

        print(f"Created: {output_filename}")

def split_pdf_in_chunks(input_pdf: str, chunk_size: int):

    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)

    for start in range(0, total_pages, chunk_size):
        writer = PdfWriter()

        end = min(start + chunk_size, total_pages)

        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])

        output_filename = input_pdf[:input_pdf.rfind('.')]
        output_filename = f"{output_filename}_page_{page_num + 1}.pdf"

        with open(output_filename, "wb") as output_file:
            writer.write(output_file)

        print(f"Created: {output_filename}")

def split_pdf_in_range(input_pdf: str, ranges: list):
    reader = PdfReader(input_pdf)

    for idx, (start, end) in enumerate(ranges, start=1):
        writer = PdfWriter()

        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])

        output_filename = input_pdf[:input_pdf.rfind('.')]
        output_filename = f"{output_filename}_page_{page_num + 1}.pdf"

        with open(output_filename, "wb") as output_file:
            writer.write(output_file)

        print(f"Created: {output_filename}")
        