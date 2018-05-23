from datetime import datetime
from Modules import csv_creation as createCSV
from Modules import xml_module as textXML
import os

# headers = ['date', 'as_level', 'tds_level', 'f_level', 'ecol_bool', 'as_safe', 'f_safe', 'tds_rec', 'ecol_safe', 'safe', 'unknown']


# Get file path
path = createCSV.file_path()

# Create output file if it doesn't exist then open
if not os.path.exists(path):
    createCSV.create_csv()
out_file = open(path, 'a')


# Get new texts
new_texts = textXML.new_texts()


# Process each text
for text in new_texts:
    # We need date, arsenic level, tds level, fluoride level, e coli bool
    arsenic_level = 0
    tds_level = 0
    fluoride_level = 0
    ecoli = False
    unknown = ''
    as_safe, f_safe, tds_rec, ecol_safe, safe = False, False, False, False, False

    text_list = text.text.split(',')

    for result in text_list:
        if result.upper().startswith('A'):
            arsenic_level = int(result[1])
            if arsenic_level < 2:
                as_safe = True

        elif result.upper().startswith('T'):
            tds_level = int(result[1])
            if tds_level < 1:
                tds_rec = True

        elif result.upper().startswith('F'):
            fluoride_level = int(result[1])
            if fluoride_level < 2:
                f_safe = True

        elif result.upper().startswith('E'):
            if result[1].upper() == 'Y':
                ecoli = True
            elif result[1].upper() == 'N':
                ecol_safe = True
            else:
                unknown = unknown + result.strip() + ':'
        else:
            unknown = unknown + result.strip() + ':'

    safe = as_safe and f_safe and ecol_safe
    unknown = unknown[:-2]

    out_csv = '{},{},{},{},{},{},{},{},{},{},{}'.format(text.date, arsenic_level, tds_level, fluoride_level, ecoli, as_safe, tds_rec, f_safe, ecol_safe, safe, unknown)
    out_file.write(out_csv + '\n')

out_file.close()
