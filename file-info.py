#Created By: @Kaorrosi
#Date: 12.24.2021
# This program identifies the file type of a file regardless of its extension,
# Calculates the hash of a file
# and searches for strings in a file.

import hashlib, magic
from argparse import ArgumentParser

#Create a function that creates the md5 hash of a file
def make_hash(file, empty):
    file_name = file
    with open(file_name) as f:
        data = f.read().encode('utf-8')
        md5hash = hashlib.md5(data).hexdigest()

    print(md5hash)

#Create a function that determines the file format regardless of extention
def file_type(file,empty):
    # printing the mime type of the file
    print(magic.from_file(file))
    print(magic.from_file(file, mime=True))

#Create a function that finds strings in a file:
def find_string(file,text):
    with open(file) as f:
        if text != None:
            text = text.strip().lower()
            if text in f.read():
                print("Found in file")
            else:
                print("Not found in file")
        else:
            print("No search parameter supplied")


if __name__=='__main__':
    choices = {'hash':make_hash, 'type':file_type, 'search':find_string}
    parser= ArgumentParser()
    parser.add_argument('action', choices= choices)
    parser.add_argument('file')
    parser.add_argument('text', nargs='?')
    args = parser.parse_args()
    function = choices[args.action]
    function(args.file, args.text)