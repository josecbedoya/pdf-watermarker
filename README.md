# PDF Watermark Script

This simple Python script adds a watermark PDF (`wtr.pdf`) to every page of another PDF (`dummy.pdf`) and saves the result as `watermarked_output.pdf`. This can be used for watermarking large amounts of a document.

## Requirements

- Python 3.8+
- PyPDF2

## Project files

- `pdf.py` → watermark script
- `dummy.pdf` → input PDF to be watermarked
- `wtr.pdf` → watermark PDF (single page or multiple pages)
- `watermarked_output.pdf` → generated output file

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python pdf.py
```

If `wtr.pdf` has fewer pages than `dummy.pdf`, watermark pages are reused in a loop.

## How it works

1. Opens `dummy.pdf` and `wtr.pdf`
2. Iterates through all pages in `dummy.pdf`
3. Merges the corresponding watermark page
4. Writes the final PDF to `watermarked_output.pdf`

