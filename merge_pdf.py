import PyPDF2 as pdf
#TODO: embed .getpage into a single function which returns a reader object
#TODO: reiterate function for a defined list of file locations
#TODO: Write to target file

# ----------  FIRST SOURCE FILE ------------ #
first_file = pdf.PdfFileReader("./Input/employmentletter.pdf")
page_one = first_file.getPage(0)

# ----------  SECOND SOURCE FILE ------------ #
second_file = pdf.PdfFileReader("./Input/Employment_Letter_1.pdf")
page_two = second_file.getPage(1)

# ----------  CREATING TARGET FILE ------------ #
merged_file = pdf.PdfFileWriter()
with open("./Output/merged_file.pdf", "wb") as file:
    merged_file.insertPage(page_one, 0)
    merged_file.insertPage(page_two, 1)
    merged_file.write(file)

