.PHONY: docx clean help

# Default target
help:
	@echo "Makefile for LaTeX to DOCX conversion"
	@echo ""
	@echo "Available targets:"
	@echo "  make docx    - Convert LaTeX paper to DOCX format"
	@echo "  make clean   - Remove generated files"
	@echo "  make help    - Show this help message"

# Convert to DOCX
docx:
	@echo "Converting LaTeX to DOCX..."
	./convert_to_docx.sh

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	@rm -f Attention_reinvestment_cycle.docx
	@rm -f Attention_reinvestment_cycle_preprocessed.tex
	@rm -f reference_aptos.docx reference_calibri.docx
	@echo "Done."

