import os
import PyPDF2

# Função para ordenar os arquivos por nome
def sort_files_by_name(directory):
    files = os.listdir(directory)
    sorted_files = sorted(files)
    return sorted_files

# Função para concatenar as páginas dos arquivos PDF
def concatenate_pdf_pages(files, output_path):
    merger = PyPDF2.PdfMerger()
    for file in files:
        if file.endswith('.pdf'):
            file_path = os.path.join(directory, file)
            merger.append(file_path)
    merger.write(output_path)
    merger.close()

# Pasta contendo os arquivos PDF a serem processados
directory = 'E:/aulas_python/pdf_project/amostras'

# Caminho de saída para o arquivo final
output_path = 'E:/aulas_python/pdf_project/amostras/pdf_final/arquivo_final1.pdf'

# Ordenar os arquivos por nome
sorted_files = sort_files_by_name(directory)

# Concatenar as páginas dos arquivos PDF em um único arquivo final
concatenate_pdf_pages(sorted_files, output_path)