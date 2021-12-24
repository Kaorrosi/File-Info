# File-Info
A simple command line tool that can be used to identify file types, search for specific words in a file, and calculate the hash of a file.

# Requirments
python-magic: 'pip install python-magic'

# Usage
To calculate the md5 hash of a file: `python file-info.py hash full_path_of_file`

To identify the type of a file, regardless of extension: `python file-info.py type full_path_of_file`

To find out if a string is present in a file: `python file-info.py search full_path_of_file "words you want to search for"`
