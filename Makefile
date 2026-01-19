# Set shell to bash for better compatibility
SHELL := /bin/bash

# read OpenAI API key from a file
.PHONY: run
run:
	python -m src.receipts_extraction.main receipts --print

# Clean up cache files
.PHONY: clean
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Install dependencies
.PHONY: install
install:
	pip install -r requirements.txt
