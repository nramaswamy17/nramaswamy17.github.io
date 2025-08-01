#!/usr/bin/env python3
"""
LaTeX to PNG Converter Script

Converts ALL .tex files in a directory to high-quality PNG images.

Requirements:
- pdflatex (from a LaTeX distribution like TeX Live or MiKTeX)
- pdf2image: pip install pdf2image
- Pillow: pip install Pillow
- poppler-utils (for pdf2image backend)

Usage:
    python tex_to_png.py [directory]
    
    If no directory is specified, defaults to images/latex/tex/
    Output PNG files go to images/latex/png/
"""

import os
import sys
import subprocess
import tempfile
from pathlib import Path
import argparse

try:
    from pdf2image import convert_from_path
    from PIL import Image
except ImportError as e:
    print(f"Missing required package: {e}")
    print("Install with: pip install pdf2image Pillow")
    sys.exit(1)

# Fixed high-quality settings
DPI = 600
IMAGE_FORMAT = 'PNG'

# Default directories
DEFAULT_TEX_DIR = Path('images/latex/tex')
DEFAULT_PNG_DIR = Path('images/latex/png')


def check_pdflatex():
    """Check if pdflatex is available in the system."""
    try:
        subprocess.run(['pdflatex', '--version'], 
                      capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def compile_tex_to_pdf(tex_file, output_dir):
    """Compile .tex file to PDF using pdflatex."""
    tex_path = Path(tex_file)
    
    # Run pdflatex in the output directory
    cmd = [
        'pdflatex',
        '-interaction=nonstopmode',
        '-output-directory', str(output_dir),
        str(tex_path.absolute())
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        pdf_name = tex_path.stem + '.pdf'
        pdf_path = output_dir / pdf_name
        
        if pdf_path.exists():
            return pdf_path
        else:
            raise RuntimeError("PDF was not generated successfully")
            
    except subprocess.CalledProcessError as e:
        print(f"LaTeX compilation failed for {tex_file}:")
        print(f"Stderr: {e.stderr}")
        raise


def pdf_to_png(pdf_path, output_path):
    """Convert PDF to PNG using pdf2image with maximum quality."""
    try:
        # Convert PDF to images with high DPI
        images = convert_from_path(pdf_path, dpi=DPI)
        
        if len(images) == 1:
            # Single page - save directly
            images[0].save(output_path, IMAGE_FORMAT, optimize=False)
        else:
            # Multiple pages - save with page numbers
            output_path = Path(output_path)
            base_name = output_path.stem
            
            for i, image in enumerate(images, 1):
                page_path = output_path.parent / f"{base_name}_page_{i}.png"
                image.save(page_path, IMAGE_FORMAT, optimize=False)
                
    except Exception as e:
        raise RuntimeError(f"PDF to PNG conversion failed: {e}")


def convert_tex_to_png(tex_file, output_dir):
    """Convert single .tex file to PNG."""
    tex_path = Path(tex_file)
    output_file = output_dir / f"{tex_path.stem}.png"
    
    # Create temporary directory for compilation
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        try:
            print(f"Converting {tex_path.name}...")
            pdf_path = compile_tex_to_pdf(tex_file, temp_path)
            pdf_to_png(pdf_path, output_file)
            print(f"✓ Created {output_file}")
            
        except Exception as e:
            print(f"✗ Failed to convert {tex_path.name}: {e}")


def convert_directory(directory_path, output_dir=None):
    """Convert all .tex files in directory to PNG."""
    
    # Check if pdflatex is available
    if not check_pdflatex():
        print("ERROR: pdflatex not found. Please install a LaTeX distribution.")
        sys.exit(1)
    
    dir_path = Path(directory_path)
    
    if not dir_path.exists():
        print(f"ERROR: Directory does not exist: {directory_path}")
        sys.exit(1)
    
    if not dir_path.is_dir():
        print(f"ERROR: Path is not a directory: {directory_path}")
        sys.exit(1)
    
    # Use specified output directory or default
    if output_dir is None:
        output_dir = DEFAULT_PNG_DIR
    else:
        output_dir = Path(output_dir)
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all .tex files
    tex_files = list(dir_path.glob("*.tex"))
    
    if not tex_files:
        print(f"No .tex files found in {directory_path}")
        return
    
    print(f"Found {len(tex_files)} .tex files in {directory_path}")
    print(f"Converting to PNG at {DPI} DPI...")
    print(f"Output directory: {output_dir}")
    print("-" * 50)
    
    # Convert each file
    for tex_file in tex_files:
        convert_tex_to_png(tex_file, output_dir)
    
    print("-" * 50)
    print("Conversion completed!")


def main():
    parser = argparse.ArgumentParser(
        description='Convert all LaTeX (.tex) files in a directory to high-quality PNG images',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
This script converts ALL .tex files in the specified directory to PNG images.

Settings (fixed for maximum quality):
- Format: PNG
- DPI: {DPI}
- Optimization: Disabled

Default directories:
- Input: {DEFAULT_TEX_DIR}
- Output: {DEFAULT_PNG_DIR}

Examples:
  python tex_to_png.py                    # Use default directories
  python tex_to_png.py /path/to/tex/files/  # Custom input directory
        """
    )
    
    parser.add_argument('directory', nargs='?', default=str(DEFAULT_TEX_DIR),
                       help=f'Directory containing .tex files (default: {DEFAULT_TEX_DIR})')
    parser.add_argument('-o', '--output', 
                       help=f'Output directory for PNG files (default: {DEFAULT_PNG_DIR})')
    
    args = parser.parse_args()
    
    convert_directory(args.directory, args.output)


if __name__ == '__main__':
    main()