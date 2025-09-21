import pandas as pd
import os
import json
import csv
import sys



import logging
import argparse

def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,  # You can change this to DEBUG, WARNING, etc.
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("seo_script.log"),  # Logs to a file
            logging.StreamHandler()  # Also prints to console
        ]
    )

    # Set up command-line arguments
    parser = argparse.ArgumentParser(description='Generate SEO metadata from checklist.')
    parser.add_argument('--folder', type=str, default=os.path.dirname(__file__),
                        help='Path to the folder containing the checklist file.')
    parser.add_argument('--json_output', type=str, default='seo_metadata.json',
                        help='Filename for the JSON output.')
    parser.add_argument('--csv_output', type=str, default='seo_metadata.csv',
                        help='Filename for the CSV output.')
    parser.add_argument('--verbose', action='store_true', help='Enable debug logging.')
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    folder = args.folder

    # Dynamically find the latest version of the checklist file
    files = [f for f in os.listdir(folder) if f.startswith('SeekingSpringfield_Project_Checklist') and f.endswith('.xlsx')]
    files.sort(reverse=True)  # Assuming newest version has highest suffix
    file_path = os.path.join(folder, files[0]) if files else None

    if not file_path:
        logging.error("❌ No checklist file found.")
        sys.exit(1)

    try:
        df = pd.read_excel(file_path)
        seo_metadata = []
        for _, row in df.iterrows():
            title = row.get('Subcategory/Item', 'Untitled')
            description = row.get('Notes', 'No description available')
            keywords = row.get('SEO Keywords', '')

            metadata = {
                'title': title,
                'description': description,
                'keywords': keywords
            }
            seo_metadata.append(metadata)

        if not seo_metadata:
            logging.warning("No SEO metadata was extracted from the Excel file.")

        for meta in seo_metadata:
            logging.info(f"Title: {meta['title']}")
            logging.info(f"Description: {meta['description']}")
            logging.info(f"Keywords: {meta['keywords']}")
            logging.info("-" * 40)

        # Write to JSON
        json_path = os.path.join(folder, args.json_output)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(seo_metadata, f, ensure_ascii=False, indent=4)
        logging.info(f"JSON file written to {json_path}")

        # Write to CSV
        csv_path = os.path.join(folder, args.csv_output)
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['title', 'description', 'keywords'])
            writer.writeheader()
            writer.writerows(seo_metadata)
        logging.info(f"CSV file written to {csv_path}")

    except Exception as e:
        logging.error(f"❌ Error processing file: {e}")




    if not seo_metadata:
        logging.warning("No SEO metadata was extracted from the Excel file.")

    for meta in seo_metadata:
        json_path = os.path.join(folder, args.json_output)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(seo_metadata, f, ensure_ascii=False, indent=4)
        logging.info(f"JSON file written to {json_path}")

        # Write to CSV
        csv_path = os.path.join(folder, args.csv_output)
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['title', 'description', 'keywords'])
            writer.writeheader()
            writer.writerows(seo_metadata)
        logging.info(f"CSV file written to {csv_path}")
    csv_path = os.path.join(folder, args.csv_output)
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'description', 'keywords'])


if __name__ == '__main__':
    main()
        writer.writeheader()
        writer.writerows(seo_metadata)
    logging.info(f"CSV file written to {csv_path}")

except Exception as e:
    logging.error(f"❌ Error processing file: {e}")

