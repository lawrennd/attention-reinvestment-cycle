# Attention Reinvestment Cycle

This repository contains the paper **"Mind the gap: Connecting AI innovation to widespread public value"** by Neil D. Lawrence and Jessica K. Montgomery.

## About the Paper

The paper examines the gap between public aspirations for AI and areas of greatest technical progress. It proposes an "attention reinvestment cycle" as an alternative innovation model that prioritizes human attention over economic returns, aiming to align AI development with societal needs.

**Key themes:**
- Analysis of public dialogues on AI from 2016-2024
- The "social productivity paradox" in AI innovation
- Attention economy and its impact on innovation direction
- Framework for directing AI development toward societal priorities
- Case studies from healthcare, education, and public services

## Repository Contents

### Paper Files

- **`Attention reinvestment cycle.tex`** - Main LaTeX source file
- **`bibliography.bib`** - BibTeX bibliography
- **`innovation-reinvestment-cycle.pdf`** - Figure illustrating the innovation cycle
- **`CUP-JNL-DTM.cls`** - Cambridge University Press journal template class
- **`User-Manual.pdf`** - Template documentation

### LaTeX to DOCX Conversion Pipeline

This repository includes a complete automated pipeline for converting the LaTeX paper to Microsoft Word format (DOCX), suitable for journal submission.

#### Conversion Scripts

- **`convert_to_docx.sh`** - Main conversion script that orchestrates the entire pipeline
- **`preprocess_for_docx.py`** - Preprocesses CUP-specific LaTeX commands to standard format
- **`create_reference_docx.py`** - Creates a reference document with proper styling (Calibri font, justified paragraphs)
- **`Makefile`** - Convenient build automation (`make docx`, `make clean`)
- **`README_DOCX_CONVERSION.md`** - Detailed documentation for the conversion pipeline

#### Pipeline Features

✅ **Font & Formatting**
- Calibri font throughout document
- 11pt body text, appropriate heading sizes
- Justified paragraph alignment

✅ **Academic Elements**
- Extracts and formats title, authors, affiliations
- Processes abstract and keywords
- Handles footnote superscripts properly
- Preserves hyperlink formatting (blue, underlined)

✅ **Bibliography**
- Automatically processes citations using `citeproc`
- Generates formatted reference list from `bibliography.bib`

✅ **Figures**
- Includes images (PDF converted inline)
- Maintains figure captions

## Quick Start

### Viewing the Paper

The paper is written in LaTeX. To compile:

```bash
# Using your LaTeX editor/build system
# Or via command line:
pdflatex "Attention reinvestment cycle.tex"
bibtex "Attention reinvestment cycle"
pdflatex "Attention reinvestment cycle.tex"
pdflatex "Attention reinvestment cycle.tex"
```

### Converting to DOCX

To generate a Microsoft Word version:

```bash
# Simple option
make docx

# Or run the script directly
./convert_to_docx.sh
```

This will create `Attention_reinvestment_cycle.docx` ready for journal submission.

**Requirements:**
- Python 3
- pandoc
- python-docx (installed automatically on first run)

For more details on the conversion pipeline, see [`README_DOCX_CONVERSION.md`](README_DOCX_CONVERSION.md).

## Project Structure

```
.
├── README.md                           # This file
├── README_DOCX_CONVERSION.md          # Conversion pipeline documentation
├── Attention reinvestment cycle.tex    # Main paper (LaTeX)
├── bibliography.bib                    # References
├── innovation-reinvestment-cycle.pdf   # Figure
├── CUP-JNL-DTM.cls                    # CUP journal class
├── Makefile                            # Build automation
├── convert_to_docx.sh                  # Conversion orchestration script
├── preprocess_for_docx.py             # LaTeX preprocessor
└── create_reference_docx.py           # Reference document generator
```

## Authors

- **Neil D. Lawrence** - Department of Computer Science and Technology, University of Cambridge
- **Jessica K. Montgomery** - Department of Computer Science and Technology, University of Cambridge

## Citation

```bibtex
@article{lawrence2024attention,
  title={Mind the gap: Connecting AI innovation to widespread public value},
  author={Lawrence, Neil D. and Montgomery, Jessica K.},
  journal={Data and Policy},
  year={2024},
  note={In submission}
}
```

## License

See individual files for licensing information.

## Related Links

- [ai@cam](https://ai.cam.ac.uk/) - University of Cambridge AI initiative
- [Data Science Africa](https://www.datascienceafrica.org/) - Community-centered AI capacity building
- [The Atomic Human](https://www.penguin.co.uk/books/455130/the-atomic-human-by-lawrence-neil-d/9780241625248) - Related book by Neil D. Lawrence

