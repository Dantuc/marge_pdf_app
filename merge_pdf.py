import os
import PyPDF2

# Function to sort files by name
def sort_files_by_name(directory):
    files = os.listdir(directory)
    sorted_files = sorted(files)
    return sorted_files

# Function to concat pdf files
def concatenate_pdf_pages(files, output_path, directory):
    merger = PyPDF2.PdfMerger()
    for file in files:
        if file.endswith('.pdf'):
            file_path = os.path.join(directory, file)
            merger.append(file_path)
    merger.write(output_path)
    merger.close()

# merge pdfs in directory
def merge_pdf(directory, output_path):

    sorted_files = sort_files_by_name(directory)
    concatenate_pdf_pages(sorted_files, output_path, directory)

