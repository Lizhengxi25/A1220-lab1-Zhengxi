# gpt.py
"""A one-line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Attributes:
    CATEGORIES (list[str]): Possible results of category field in receipts image

Typical usage example:

    import gpt
    data = gpt.extract_receipt_info(image_b64)
"""
import json
from openai import OpenAI

client = OpenAI()

CATEGORIES = ["Meals", "Transport", "Lodging", "Office Supplies", 
"Entertainment", "Other"]
"""
list[str]: categories that "category" field can contain in receipt images
"""

def ai_output_processor(raw_output: dict) -> dict:
    """Re-process the dictionary extracted from ChatGPT

    Remove the “$” symbol if present in amount and convert the parsed value to float

    Args:
        raw_output: original output dict without being processed

    Returns:
        A dict that removes the “$” symbol and converts the parsed value to float.
    """
    raw_output["amount"] = raw_output["amount"].replace("$", "")
    raw_output["amount"] = float(raw_output["amount"])
    return raw_output

def extract_receipt_info(image_b64: str) -> dict:
    """Fetches texts from a image.

    Retrieves texts from images by calling ChatGPT API

    Args:
        image_b64: a string containing base64 characters, embedding images

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a string. For
        example:

        {"date": "30/09/2025 20:15",
         "amount": "$51.30",
         "vendor": "DINEFINE RESTAURANT",
         "category": "Meals"}
        
        Returned keys are always date, amount, vendor, and category
    """
    prompt = f"""
You are an information extraction system.
Extract ONLY the following fields from the receipt image:

date: the receipt date as a string
amount: the total amount paid as it appears on the receipt
vendor: the merchant or vendor name
category: one of [{", ".join(CATEGORIES)}]

Return EXACTLY one JSON object with these four keys and NOTHING ELSE.
Do not include explanations, comments, or formatting.
Do not wrap the JSON in markdown.
If a field cannot be determined, use null.

The output must be valid JSON.
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        seed=43,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_b64}"
                        }
                    }
                ]
            }
        ]
    )
    return ai_output_processor(json.loads(response.choices[0].message.content))
