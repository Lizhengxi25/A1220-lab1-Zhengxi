# file_io.py
"""File input/output utilities for encoding and listing files.

This module provides utility functions for common file operations including
base64 encoding of file contents and directory traversal. These functions are
useful for data processing pipelines, file management scripts, and applications
that need to handle binary data as text.

The module contains two main functions:
    - encode_file: Converts file contents to base64-encoded strings
    - list_files: Iterates through files in a directory

Typical usage example:
    
    import file_io
    
    # Encode an image file for embedding in JSON
    encoded_image = file_io.encode_file('logo.png')
    
    # Process all files in a directory
    for filename, filepath in file_io.list_files('./data'):
        print(f"Processing {filename}")
        encoded = file_io.encode_file(filepath)
"""
import os
import base64

def encode_file(path: str) -> str:
    """Encodes a file's contents to a base64 string.
    
    Reads a file in binary mode and converts its contents to a base64-encoded
    string representation. This is useful for transmitting binary data as text,
    such as embedding images in JSON or HTML.
    
    Args:
        path: The file path to encode. Must be a valid path to an existing file.
            For example, '/home/user/image.png' or 'data/document.pdf'.
    
    Returns:
        A base64-encoded string representation of the file contents.
        For example, a small text file containing 'Hello' would return 'SGVsbG8='.
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def list_files(dirpath: str):
    """Generates tuples of filenames and paths from a directory.
    
    Iterates through a directory and yields information about each file found.
    Subdirectories are skipped; only regular files are included. This is useful
    for processing all files in a directory without loading them into memory.
    
    Args:
        dirpath: The directory path to list files from. Must be a valid path to
            an existing directory. For example, '/home/user/documents' or './data'.
    
    Yields:
        tuple: A 2-tuple containing (filename, full_path) for each file.
            - filename (str): The name of the file without directory path.
              For example, 'report.pdf'.
            - full_path (str): The complete path to the file.
              For example, '/home/user/documents/report.pdf'.
    """
    for name in os.listdir(dirpath):
        path = os.path.join(dirpath, name)
        if os.path.isfile(path):
            yield name, path