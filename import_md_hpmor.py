#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 Yuliy Lobarev

__author__ = 'Yuliy Lobarev'
__description__ = 'Converting Markdown formatted chapters from Drupal 7 to Hugo Markdown files.'

"""Converting exported from DOCX,
Markdown files
to Hugo site generator Markdown files.

The script works on a folder with Markdown files.
"""

import os
import datetime


def convert_files(filepath, filepathout):
    """Function to conver MD files to Hugo suitable format with a Front Matter.
    
    Syntax: convert_files(input_folder, output_folder)
    """
    title = None
    outfile = None
    fileslist = []

    for file in os.listdir(filepath):
        if file.endswith(".md"):
            fileslist.append(file)
            
    for filename in fileslist:
        
        # finding output file name
        # and opening the file
        if filename.startswith('0'):
            title = filename[1:2]
        elif filename.startswith('1') and filename[3:4] == ' ':
            title = filename[0:3]
        else:
            title = filename[0:2]
        
        with open( os.path.join(filepath, filename), encoding='utf_8_sig') as infile, \
            open( os.path.join(filepathout, (title + ".md") ), 'w', encoding='utf_8_sig') as outfile:
            print("Converting file " + filename)
            
            for line in infile:
                
                # creating a Front Matter
                if line.startswith('##'):
                    chaptername = line[3:-1]
                    line = '---\ntitle: "' + chaptername + '"\ndescription: "' + chaptername \
                        + '"\ncategories: "глава"\nlayout: "chapters"\n'
                        
                    # adding weight to sort later
                    line = line + 'weight: "' + title + '"\n'
                    
                    # inserting fake first publishing date
                    firstdate = datetime.date(2013, 11, 26)
                    chapterdate = firstdate + datetime.timedelta(days = int(title))
                    line = line + 'date: "' + chapterdate.isoformat() + '"\n'
                    
                    # inserting file modification date
                    moddate = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(filepath, filename))).date()
                    line = line + 'lastmod: "' + moddate.isoformat() + '"\n'
                    
                    # finishing the Front Matter
                    line = line + '---\n'
                    
                    print("The chapter name is " + chaptername)
                    
                # saving lines to file
                outfile.write(line)
            
            # finishing with the file
            outfile.close()

    return 0
                
                
def main():
    """The main list of commands.
    """
    # converting the files
    # assuming that the script exists in the folder
    # with input and output folders
    print("Running conversion...")
    convert_files("data/parts", "data/out")
    return 0
    

if __name__ == "__main__":
    main()

