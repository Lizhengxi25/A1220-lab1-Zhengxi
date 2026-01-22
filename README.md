# Receipts Information Extraction System

[Github link](https://github.com/Lizhengxi25/A1220-lab1-Zhengxi)

### Functionality

This information extraction system extracts **ONLY** the following fields from the receipt image:

1. date: the receipt date as a string
2. amount: the total amount paid as it appears on the receipt
3. vendor: the merchant or vendor name
4. category: one of [{", ".join(CATEGORIES)}]

and it returns **EXACTLY** one JSON object with these four keys and **NOTHING ELSE**.

### How to Run

To run the program with the --print option enabled, after setting the key in an environment variable.
```bash
make run
```

To clean cache:
```bash
make clean
```

To install dependencies:
```bash
make install
```