"""
Main module: is the application starting point.

Now it is a test version with constant file name.
"""

# Std Import
import csv
import os
import sys

# Site-package Import
from PyPDF2 import PdfReader

# Project Import


CSV_FILE_NAME = "exported.csv"


try:
    os.remove(CSV_FILE_NAME)
    
except:
    pass


# Create the files iterator
dirs = os.listdir(sys.path[0])


# for each file found
for i, file in enumerate(dirs):
    
    # Check if is not a PDF
    if(not file[-4:].lower() == ".pdf"):
        # skip it
        continue
    
    # otherwise collect data
    with open(file, 'rb') as f:
        pdf = PdfReader(f)
     
        # Get field data from the module
        fields = pdf.get_fields()
    
    if(i == 0):
        file_mode = "w"
        
    else:
        file_mode = "a"
    
    # Create the CSV, add header and write rows
    with open(CSV_FILE_NAME, file_mode, newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields.keys())
        
        if(i == 0):
            writer.writeheader()
    
        # Write fields to the CSV (the field name seems to be in the '/V' element)
        writer.writerow({k: v['/V'] for k, v in fields.items()})