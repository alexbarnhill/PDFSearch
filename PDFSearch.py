import PyPDF3
import argparse
import bcolors
import re
from os.path import isfile, join, isdir, splitext
from os import listdir


def print_usage():
    print("----------------------------------------------------------------------------------------")
    print("PDF Searcher searches recursively through a directory for PDFs containing a given key")
    print("\t usage: PDFSearch.py --directory=<starting directory --term=<term to search for>")
    print("----------------------------------------------------------------------------------------")


def print_searching(string):
    bcolors.print_ok_blue(string)


def print_found(string):
    bcolors.print_ok_green(string)


def search(path, term, flags):

    # Check every item in the directory
    for item in listdir(path):
        # If the item is another directory, enter the directory and keep searching
        if isdir(join(path, item)):
            search(join(path, item), term, flags)

        if isfile(join(path, item)):
            filename, file_extension = splitext(item)

            # We only care about PDFs
            if file_extension == ".pdf":

                print_searching("Searching in: " + filename + " ... ")
                pdf_file_object = open(join(path, item), 'rb')
                pdf_reader = PyPDF3.PdfFileReader(pdf_file_object)

                # Go through each page in the pdf
                for page_number in range(0, pdf_reader.getNumPages()):
                    page = pdf_reader.getPage(page_number)
                    text = page.extractText()
                    # If the term exists in the PDF, print out the file and the page

                    if re.search(term, text, flags=flags):
                        print_found("\tFOUND: " + join(path, item) + " Page: " + str(page_number))

                # Close after searching
                pdf_file_object.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", help="Directory to start search from")
    parser.add_argument("--term", help="Term to search for")
    parser.add_argument("-i", help="Add this flag for case insensitve searches", action='store_true')
    args = parser.parse_args()

    base = args.directory
    term = args.term
    insensitive = args.i

    flags = 0
    if insensitive:
        flags = flags | re.IGNORECASE

    if not base or not term or term == "":
        print_usage()
        exit(1)
    search(base, term, flags)


if __name__ == "__main__":
    main()
