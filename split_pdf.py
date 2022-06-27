import PyPDF2 as pdf
from math import floor
num_files_reqd = 2
files_created = 0
page_num = 0
count = 0

# ----------  SOURCE FILE ------------ #
source_file = pdf.PdfFileReader("./Input/split_file_1.pdf")
pages = source_file.getNumPages()


def get_page_objects(page_num):
    page_obj = source_file.getPage(page_num)
    split_file.insertPage(page_obj, page_num)


page_list = [*range(pages)]
pages_in_each_file = floor(pages / num_files_reqd)
while files_created < num_files_reqd:
    split_file = pdf.PdfFileWriter()
    while count <= pages_in_each_file:
        try:
            get_page_objects(page_num)
            count += 1
            page_num += 1
        except IndexError:
            break
    count = 0
    files_created += 1
    with open(f"./Output/split_file_{files_created}.pdf", "wb") as file:
        split_file.write(file)
