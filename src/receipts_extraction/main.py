# main.py
"""Information extraction system extracts fields from the receipt image

It extracts **ONLY** the following fields from the receipt image:
1. date: the receipt date as a string
2. amount: the total amount paid as it appears on the receipt
3. vendor: the merchant or vendor name
4. category: one of [{", ".join(CATEGORIES)}]
and it returns **EXACTLY** one JSON object with these four keys and **NOTHING ELSE**.

Example:
    Run with make:

        $ make run

    Run in terminal:

        $ python -m src.receipts_extraction.main
"""

import json
import argparse
from . import file_io as io_mod
from . import gpt

def process_directory(dirpath: str) -> dict:
    """Iterate images under dirpath and run process function

    Args:
        dirpath: The path of directory that contains images.

    Returns:
        A dictionary. Keys are the name of files in dirpath. Values are JSON object in str format

    """
    results = {}
    for name, path in io_mod.list_files(dirpath):
        image_b64 = io_mod.encode_file(path)
        data = gpt.extract_receipt_info(image_b64)
        results[name] = data
    return results

def main():
    """Engine that calls every models"""
    parser = argparse.ArgumentParser()
    parser.add_argument("dirpath")
    parser.add_argument("--print", action="store_true")
    args = parser.parse_args()

    data = process_directory(args.dirpath)
    if args.print:
        print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()

