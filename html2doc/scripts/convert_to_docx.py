#!/usr/bin/env python3
"""
Convert HTML with MathML to DOCX with native Word equations

Usage: python convert_to_docx.py [--input input.html] [--output output.docx]
"""

import argparse
import os
import sys
import zipfile

# Try to import pypandoc, install if missing
try:
    import pypandoc
except ImportError:
    print("Installing pypandoc...")
    os.system("pip install pypandoc")
    import pypandoc

from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT


def convert_html_to_docx(input_file, output_file):
    """Convert HTML with MathML to DOCX with native Word equations."""
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
    
    print(f"Converting: {input_file} -> {output_file}")
    
    # Convert HTML to DOCX using MathML (this creates native OMML equations)
    try:
        output = pypandoc.convert_file(
            input_file,
            'docx',
            outputfile=output_file,
            extra_args=['--mathml']
        )
        print("Conversion complete")
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)
    
    # Verify conversion
    with zipfile.ZipFile(output_file, 'r') as z:
        doc_xml = z.read('word/document.xml').decode('utf-8')
        has_omml = '<m:oMath' in doc_xml
        eq_count = doc_xml.count('<m:oMath')
        dollar_count = doc_xml.count('\\$')
        
        print(f"\n=== Conversion Results ===")
        print(f"Native Word equations: {eq_count}")
        print(f"Unconverted $ signs: {dollar_count}")
        
        if has_omml:
            print("Status: SUCCESS - Equations are native Word OMML")
        else:
            print("Warning: No native equations found")
    
    return output_file


def main():
    parser = argparse.ArgumentParser(
        description='Convert HTML with MathML to DOCX with native Word equations'
    )
    parser.add_argument(
        '--input', '-i',
        default='paper_with_mathml.html',
        help='Input HTML file (default: paper_with_mathml.html)'
    )
    parser.add_argument(
        '--output', '-o',
        default='paper_converted.docx',
        help='Output DOCX file (default: paper_converted.docx)'
    )
    
    args = parser.parse_args()
    
    convert_html_to_docx(args.input, args.output)
    
    print("\nNext step: python scripts/apply_academic_style.py")


if __name__ == '__main__':
    main()
