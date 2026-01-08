# LaTeX to DOCX Conversion Pipeline

This directory contains scripts to convert the LaTeX paper to Microsoft Word format (DOCX) for journal submission.

## Files

- **`convert_to_docx.sh`** - Main conversion script that runs the full pipeline
- **`preprocess_for_docx.py`** - Python script that preprocesses the LaTeX file to make it pandoc-friendly
- **`create_reference_docx.py`** - Python script that creates a reference document with Aptos font styling
- **`Attention_reinvestment_cycle.docx`** - Output Word document (generated)
- **`Attention_reinvestment_cycle_preprocessed.tex`** - Intermediate preprocessed LaTeX file (generated)
- **`reference_aptos.docx`** - Reference document for font styling (generated)

## Usage

### Quick Start

Simply run the conversion script:

```bash
./convert_to_docx.sh
```

This will:
1. Create a reference document with Aptos font styling (if it doesn't exist)
2. Preprocess the LaTeX file to extract and format key elements (title, authors, abstract, keywords, affiliations)
3. Convert the preprocessed LaTeX to DOCX using pandoc with bibliography support and Aptos font
4. Generate `Attention_reinvestment_cycle.docx` ready for submission

### What the Pipeline Does

The preprocessing step (`preprocess_for_docx.py`):
- Extracts title, authors, abstract, keywords, and author affiliations
- Converts custom Cambridge University Press (CUP) LaTeX commands to standard LaTeX
- Restructures the document for better pandoc compatibility
- Handles nested LaTeX commands in addresses and affiliations

The conversion step (via `pandoc`):
- Converts LaTeX to DOCX format
- Processes citations using the bibliography.bib file
- Includes the figure (innovation-reinvestment-cycle.pdf)
- Numbers sections appropriately
- Maintains document structure and formatting

## Requirements

- **pandoc** - Document converter (already installed on your system)
- **Python 3** - For preprocessing script (already installed)
- **python-docx** - Python library for creating Word documents (installed automatically)

## Output

The generated DOCX file (`Attention_reinvestment_cycle.docx`) includes:
- Title and author information
- Abstract
- Keywords
- Author affiliations
- Full paper content with proper section numbering
- In-text citations and reference list
- Figure(s)
- Acknowledgments section

## Notes for Springer AI in Society Submission

After generating the DOCX file, you may want to:

1. **Check formatting**: Open the file in Word and verify that:
   - Title, authors, and affiliations appear correctly
   - Abstract and keywords are properly formatted
   - Section headings are at the right levels
   - Citations appear correctly
   - Figure is included and captioned

2. **Apply Springer template** (if required): Some journals prefer you to use their Word template. You can copy content from this file into their template.

3. **Review references**: Ensure the reference list follows the journal's citation style requirements.

4. **Check figure placement**: Verify that the figure appears where expected and is properly captioned.

## Customization

To modify the conversion:

- **Edit preprocessing logic**: Modify `preprocess_for_docx.py`
- **Change pandoc options**: Edit the pandoc command in `convert_to_docx.sh`
- **Use a reference document**: If you have a Springer Word template, add `--reference-doc=your_template.docx` to the pandoc command

## Font Customization

The output document uses **Aptos** as the default font (Microsoft's modern default font). This is configured through the `reference_aptos.docx` reference document that is automatically created on first run.

To change to a different font:
1. Edit `create_reference_docx.py` and change `'Aptos'` to your desired font name
2. Delete `reference_aptos.docx` 
3. Run `./convert_to_docx.sh` again

## Cleanup

To remove generated files:

```bash
make clean
# or manually:
rm Attention_reinvestment_cycle.docx Attention_reinvestment_cycle_preprocessed.tex reference_aptos.docx
```

Then run `./convert_to_docx.sh` again to regenerate them.

