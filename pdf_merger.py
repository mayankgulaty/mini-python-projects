import PyPDF2
import os

def merge_pdfs(paths, output):
    pdf_merger = PyPDF2.PdfFileMerger()
    for path in paths:
        pdf_merger.append(path)
    with open(output, 'wb') as fileobj:
        pdf_merger.write(fileobj)
    print(f"Merged {len(paths)} PDFs into {output}")

def main():
    print("PDF Merger Tool")
    print("Enter the names of the PDF files you want to merge.")
    print("Type 'done' when you have finished entering file names.")

    pdfs = []
    while True:
        pdf_file = input("Enter a PDF file name or 'done': ").strip()
        if pdf_file.lower() == 'done':
            break
        if os.path.exists(pdf_file) and pdf_file.endswith('.pdf'):
            pdfs.append(pdf_file)
        else:
            print("File does not exist or is not a PDF. Please try again.")

    if len(pdfs) > 1:
        output_file = input("Enter the name of the output merged PDF file: ").strip()
        if not output_file.endswith('.pdf'):
            output_file += '.pdf'
        merge_pdfs(pdfs, output_file)
    else:
        print("At least two PDF files are required to merge.")

if __name__ == "__main__":
    main()
