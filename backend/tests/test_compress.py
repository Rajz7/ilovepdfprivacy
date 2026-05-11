import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.pdf.compress_service import compress_pdf

def test_compress_pdf():
    input_path = "/home/lamborghini/Downloads/test.pdf"
    output_path = compress_pdf(input_path)


