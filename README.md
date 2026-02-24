# PDF Watermark Script

This simple Python script adds a watermark PDF (`wtr.pdf`) to every page of another PDF (`dummy.pdf`) and saves the result as `watermarked_output.pdf`. This can be used for watermarking large amounts of a document.

## Requirements

- Python 3.8+
- PyPDF2

## Project files

- `pdf.py`  watermark script
- `dummy.pdf` input PDF to be watermarked
- `wtr.pdf` watermark PDF
- `watermarked_output.pdf` generated output file

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python pdf.py
```
