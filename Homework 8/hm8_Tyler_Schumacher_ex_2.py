'''
Homework 8, Exercise 2
Tyler Schumacher
October 27, 2019
Write a program that decrypts a PDF file trying every possible English word
until it finds the right one
'''
import os
import sys
import PyPDF2

password = sys.argv[1]
decryptFailed = []

# Walks the folder path, finds the folder, reads the folder, and writes the folder
for folders, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            path = os.path.join(folders, filename)
            pdfReader = PyPDF2.PdfFileReader(open(path, 'rb'))
            if pdfReader.isEncrypted is True:
                if pdfReader.decrypt(password) != 1:
                    print(filename + 'failed to decrypt.')
                    decryptFailed.append(filename)
                else:
                    pdfWriter = PyPDF2.PdfFileWriter()
                    for pageNum in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))

                    # Encrypt copy of the PDF file and have a sufix of '_decrypted'
                    decryptedPath = path[:-4] + '_decrypted.pdf'
                    decryptedVersion = open(decryptedPath, 'wb')
                    pdfWriter.write(decryptedVersion)
                    decryptedVersion.close()
if decryptFailed != []:
    print("All encrypted PDF's, except those listed above, were "
          "decrypted successfully. All of the original files have been kept.")
else:
    print("All decrypted PDF's in the folder tree were decrypted successfully."
          "The original files have been kept.")