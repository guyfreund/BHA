# Final Project - Digital Humanities - Israeli Air Force Magazine

This repository is the implementation of a final project in Digital Humanities course taken by Guy Freund & Amit Haim from The department of Computer Science, Ben-Gurion University, Israel. The project's goal is to create a digital collection of all the issues of IAF magazine. Before this project, all data sources of the IAF magazine weren't machine readable, and our main goal was to produce machine readable data.

## Python Files
1. `tagger.py` - A interactive program to help the tagging process of IAF library issues.
2. `create_database.py` - Gathers all data from the project's data files and to create the `database` directory.
3. `CSVcreator.py` - Creates a CSV file that is written by the `Omeka`'s item type we've created.
4. `get_metadata.py` - Gets all possible metadata from the IAF & IAF library sites (without parsing the issues).
5. `iaf_images.py` - Gets all issue's front page images from the IAF site.
6. `iaf_index.py` - Gets all issue's indexes from the IAF site.
7. `iaf_library_images.py` - Gets all issue's front page images from the IAF library site.

## Generic Files
1. `issue_types.txt` - Differentiates all issues into their format type.
2. `scheme.json` - The scheme of an issue in the created database.

## Data Files
1. `iaf_data.json` - The metadata & index of every issue in the IAF site, starting from issue 219.
2. `iaf_library_data.json` - The metadata of every issue in the IAF library site, 1-218.
3. `schemes` directory - The manual tagging of all IAF library site issues, 1-218.
4. `database` directory - A directory contains of json files, each file represents an issue and is in the format of the `scheme.json` file.
5. `AllDataAsCSV.csv` - All the data gathers into one csv file, created from the `database` directory.

## Resources
1. IAF site - https://www.iaf.org.il/52-he/IAF.aspx
2. IAF Library site - http://iaflibrary.org.il/

## Our project in Omeka
https://betaonlibrary.omeka.net/collections/show/7
