# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python utility tool for removing passwords from PDF files using PyMuPDF. The tool supports both interactive and command-line modes, uses environment variables for secure password storage, and automatically organizes output files.

## Development Commands

- **Setup virtual environment**: `python -m venv venv`
- **Activate virtual environment (macOS/Linux)**: `source venv/bin/activate`
- **Install dependencies**: `pip install -r requirements.txt`
- **Run interactive mode**: `python index.py`
- **Run command-line mode**: `python index.py "path/to/file.pdf"`

## Architecture

### Tech Stack
- **Python 3**: Core language
- **PyMuPDF (fitz)**: PDF manipulation library for password removal
- **python-dotenv**: Environment variable management for secure password storage

### Key Components

**Main Script** (`index.py`):
- **PDF Processing**: Core function `remove_pdf_password()` handles encrypted PDF files
- **Environment Variables**: Uses `.env` file for secure password storage via `PDF_PASSWORD`
- **Dual Mode Operation**: Supports both interactive input and command-line arguments
- **Smart Output Management**: Automatically generates output filenames with `-unlock` suffix
- **Error Handling**: Comprehensive error checking for file existence, password validation, and processing errors

### File Structure
- `index.py` - Main Python script with PDF password removal functionality
- `requirements.txt` - Python dependencies (PyMuPDF, python-dotenv)
- `readme` - Comprehensive documentation in Traditional Chinese
- `.env` - Environment variables file (not tracked by Git)
- `output/` - Directory for processed PDF files (auto-created, not tracked by Git)
- `.gitignore` - Excludes sensitive files and build artifacts

### Environment Variables
- `PDF_PASSWORD` - The password to use for unlocking PDF files (required)

### Key Features
- **Security-First Design**: Password stored in environment variables, never hardcoded
- **Automatic File Organization**: All output files go to `output/` directory with `-unlock` suffix
- **Intelligent Processing**: Detects if PDF needs password and handles unencrypted files
- **Path Handling**: Supports files with spaces and special characters in paths
- **Bilingual Support**: Chinese interface with emoji indicators for user feedback

### Usage Patterns
- **Interactive Mode**: Run `python index.py` and follow prompts for file path input
- **Command-Line Mode**: Run `python index.py "file_path"` for direct processing
- **Output Naming**: Input `document.pdf` becomes `output/document-unlock.pdf`
- **Directory Creation**: Output directory is automatically created if it doesn't exist

### Security Considerations
- Password is stored in `.env` file which is excluded from version control
- No sensitive information is hardcoded in the source code
- Safe for sharing and collaboration through Git

### Error Handling
- File existence validation before processing
- Password authentication verification
- Directory creation for output path
- Graceful handling of processing exceptions with user-friendly Chinese messages