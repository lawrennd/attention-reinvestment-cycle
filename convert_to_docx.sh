#!/bin/bash

# Pandoc LaTeX to DOCX conversion script
# For submission to Springer AI in Society journal

INPUT_FILE="Attention reinvestment cycle.tex"
PREPROCESSED_FILE="Attention_reinvestment_cycle_preprocessed.tex"
OUTPUT_FILE="Attention_reinvestment_cycle.docx"
BIB_FILE="bibliography.bib"
REFERENCE_DOC="reference_calibri.docx"

# Step 1: Create reference document with Calibri font (if it doesn't exist)
if [ ! -f "$REFERENCE_DOC" ]; then
    echo "Step 1a: Creating reference document with Calibri font and justified paragraphs..."
    python3 create_reference_docx.py
    if [ $? -ne 0 ]; then
        echo "✗ Failed to create reference document."
        exit 1
    fi
    echo ""
fi

# Step 2: Preprocess the LaTeX file
echo "Step 1: Preprocessing LaTeX file..."
python3 preprocess_for_docx.py

if [ $? -ne 0 ]; then
    echo "✗ Preprocessing failed."
    exit 1
fi

echo ""
echo "Step 3: Converting $PREPROCESSED_FILE to $OUTPUT_FILE with Calibri font..."

# Run pandoc with comprehensive options, including reference document
pandoc "$PREPROCESSED_FILE" \
    --from=latex \
    --to=docx \
    --output="$OUTPUT_FILE" \
    --bibliography="$BIB_FILE" \
    --citeproc \
    --reference-doc="$REFERENCE_DOC" \
    --number-sections \
    --metadata link-citations=true \
    --standalone \
    --wrap=auto \
    --verbose

# Check if conversion was successful
if [ $? -eq 0 ]; then
    echo "✓ Conversion successful!"
    echo "  Output: $OUTPUT_FILE"
    ls -lh "$OUTPUT_FILE"
else
    echo "✗ Conversion failed. See error messages above."
    exit 1
fi

