# SEO Metadata Generator Script

This script (`generate-ser.py`) is designed to automate the extraction and generation of SEO metadata from an Excel checklist. It is intended for use in the `backend/seo-function` folder of the SeekingSpringfield.com project.

## Purpose
- **Automate SEO metadata extraction** from a project checklist Excel file.
- **Generate JSON and CSV files** containing the extracted metadata for further use in web development or SEO analysis.
- **Support command-line arguments** for flexible input/output and logging control.

## Features
- Reads the latest `SeekingSpringfield_Project_Checklist_*.xlsx` file in the specified folder.
- Extracts the following columns for each row:
  - `Subcategory/Item` → Title
  - `Notes` → Description
  - `SEO Keywords` → Keywords
- Outputs results to both JSON and CSV files (filenames are customizable).
- Logs all actions and errors to both the console and a log file (`seo_script.log`).
- Supports a `--verbose` flag for debug-level logging.

## Usage

```bash
python generate-ser.py [--folder FOLDER] [--json_output JSON_FILE] [--csv_output CSV_FILE] [--verbose]
```

- `--folder` (optional): Path to the folder containing the checklist Excel file. Defaults to the script's directory.
- `--json_output` (optional): Filename for the JSON output. Defaults to `seo_metadata.json`.
- `--csv_output` (optional): Filename for the CSV output. Defaults to `seo_metadata.csv`.
- `--verbose` (optional): Enable debug-level logging.

## Example

```bash
python generate-ser.py --folder "." --json_output my_seo.json --csv_output my_seo.csv --verbose
```

## Code Block Explanations

- **Imports**: Loads required Python modules for file handling, data processing, logging, and argument parsing.
- **Logging Setup**: Configures logging to both a file and the console.
- **Argument Parsing**: Uses `argparse` to allow flexible command-line usage.
- **File Discovery**: Finds the latest checklist Excel file in the specified folder.
- **Data Extraction**: Reads the Excel file with pandas and extracts relevant columns.
- **Output Generation**: Writes the extracted metadata to both JSON and CSV files.
- **Error Handling**: Logs errors and warnings for missing files or data issues.

## Best Practices for Markdown Files
- **Purpose**: Clearly state what the script or project does.
- **Usage**: Show how to run the script, including all options.
- **Examples**: Provide example commands.
- **Code Explanations**: Briefly explain each major code block or function.
- **Dependencies**: List any required Python packages (e.g., `pandas`, `openpyxl`).
- **Contact/Support**: Optionally, add a section for who to contact for help.

## Dependencies
- Python 3.7+
- pandas
- openpyxl

Install dependencies with:
```bash
pip install pandas openpyxl
```

---

Feel free to expand this README with more details as your script evolves!
