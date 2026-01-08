#!/usr/bin/env python3
"""
Preprocess LaTeX file for better pandoc conversion to DOCX.
Handles custom journal-specific commands and formats them for pandoc.
"""

import re
import sys

def extract_balanced_braces(text, start_pos):
    """Extract content within balanced braces starting at position."""
    level = 0
    result = []
    i = start_pos
    
    while i < len(text):
        if text[i] == '{':
            if level > 0:
                result.append(text[i])
            level += 1
        elif text[i] == '}':
            level -= 1
            if level == 0:
                return ''.join(result), i + 1
            result.append(text[i])
        elif text[i] == '\\' and i + 1 < len(text):
            # Handle escaped characters
            result.append(text[i:i+2])
            i += 1
        else:
            if level > 0:
                result.append(text[i])
        i += 1
    
    return ''.join(result), i

def clean_org_commands(text):
    r"""Remove \orgdiv, \orgname, \orgaddress and related commands."""
    # Remove org commands but keep their content
    text = re.sub(r'\\orgdiv\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\orgname\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\email\{([^}]+)\}', r'Email: \1', text)
    
    # Handle \orgaddress with nested braces more carefully
    while '\\orgaddress{' in text:
        match = re.search(r'\\orgaddress\{', text)
        if match:
            start = match.end() - 1
            content, end = extract_balanced_braces(text, start)
            # Extract nested command contents
            content = re.sub(r'\\city\{([^}]+)\}', r'\1', content)
            content = re.sub(r'\\postcode\{([^}]+)\}', r'\1', content)
            content = re.sub(r'\\state\{([^}]+)\}', r'\1', content)
            content = re.sub(r'\\country\{([^}]+)\}', r'\1', content)
            text = text[:match.start()] + content + text[end:]
        else:
            break
    
    return text

def preprocess_latex(input_file, output_file):
    """Preprocess LaTeX file to make it more pandoc-friendly."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'\\title\[([^\]]+)\]\{([^}]+)\}', content)
    title = title_match.group(2) if title_match else "Untitled"
    
    # Extract authors
    authors = []
    for match in re.finditer(r'\\author\[(\d+)\]\{([^}]+)\}', content):
        authors.append(match.group(2))
    
    # Extract addresses with better handling
    addresses = []
    for match in re.finditer(r'\\address\[(\d+)\]\{', content):
        addr_id = match.group(1)
        start = match.end() - 1
        addr_content, end = extract_balanced_braces(content, start)
        addr_clean = clean_org_commands(addr_content)
        addresses.append(f"{addr_clean}")
    
    # Extract keywords
    keywords_match = re.search(r'\\keywords\{([^}]+)\}', content)
    keywords = keywords_match.group(1) if keywords_match else None
    
    # Extract abstract
    abstract_match = re.search(r'\\abstract\{', content)
    if abstract_match:
        start = abstract_match.end() - 1
        abstract, end = extract_balanced_braces(content, start)
    else:
        abstract = None
    
    # Create a simplified LaTeX document
    output_lines = []
    
    # Preamble
    output_lines.append(r'\documentclass{article}')
    output_lines.append(r'\usepackage[utf8]{inputenc}')
    output_lines.append(r'\usepackage{hyperref}')
    output_lines.append(r'\usepackage{graphicx}')
    output_lines.append(r'')
    output_lines.append(r'\title{' + title + '}')
    
    if authors:
        output_lines.append(r'\author{' + r' \and '.join(authors) + '}')
    
    output_lines.append(r'')
    output_lines.append(r'\begin{document}')
    output_lines.append(r'\maketitle')
    output_lines.append(r'')
    
    # Add abstract
    if abstract:
        output_lines.append(r'\begin{abstract}')
        output_lines.append(abstract)
        output_lines.append(r'\end{abstract}')
        output_lines.append(r'')
    
    # Add keywords
    if keywords:
        output_lines.append(r'\noindent\textbf{Keywords:} ' + keywords)
        output_lines.append(r'')
    
    # Add affiliations
    if addresses:
        output_lines.append(r'\noindent\textbf{Author Affiliations:}')
        output_lines.append(r'\begin{enumerate}')
        for addr in addresses:
            output_lines.append(r'\item ' + addr)
        output_lines.append(r'\end{enumerate}')
        output_lines.append(r'')
    
    # Extract main content (from Impact Statement to Backmatter)
    # Find the Impact Statement
    impact_start = content.find(r'\section*{Impact Statement}')
    if impact_start == -1:
        # Try finding Introduction instead
        impact_start = content.find(r'\section{Introduction}')
    
    # Find where Backmatter starts
    backmatter_start = content.find(r'\begin{Backmatter}')
    
    if impact_start != -1 and backmatter_start != -1:
        main_content = content[impact_start:backmatter_start]
        
        # Clean up the main content
        # Replace \paragraph with \subsubsection
        main_content = re.sub(r'\\paragraph\{([^}]+)\}', r'\\subsubsection*{\1}', main_content)
        
        # Add the main content
        output_lines.append(main_content)
        output_lines.append(r'')
    
    # Extract backmatter content (acknowledgments, funding, etc.)
    if backmatter_start != -1:
        backmatter_end = content.find(r'\end{Backmatter}')
        if backmatter_end != -1:
            backmatter_content = content[backmatter_start+len(r'\begin{Backmatter}'):backmatter_end]
            # Clean up paragraphs in backmatter
            backmatter_content = re.sub(r'\\paragraph\{([^}]+)\}', r'\\subsection*{\1}', backmatter_content)
            output_lines.append(r'\section*{Acknowledgments}')
            output_lines.append(backmatter_content)
    
    # Don't include \printbibliography - pandoc will handle this
    output_lines.append(r'')
    output_lines.append(r'\end{document}')
    
    # Write output
    output_content = '\n'.join(output_lines)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_content)
    
    print(f"Preprocessed {input_file} -> {output_file}")
    print(f"  Title: {title}")
    print(f"  Found {len(authors)} author(s)")
    print(f"  Found {len(addresses)} affiliation(s)")
    print(f"  Abstract: {'Yes' if abstract else 'No'}")
    print(f"  Keywords: {'Yes' if keywords else 'No'}")

if __name__ == '__main__':
    input_file = 'Attention reinvestment cycle.tex'
    output_file = 'Attention_reinvestment_cycle_preprocessed.tex'
    preprocess_latex(input_file, output_file)
