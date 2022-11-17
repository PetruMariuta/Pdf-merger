# Pdf-merger

If you want to change the directory fromn which the program mergers multiple pdfs intro a single one, you need to run the cd command in the terminal (cd = change directory), followed by your desired path, for example: cd C:\Users\Public\PDFfiles , the script will merge all the pdfs from PDFfiles.

Also instead of: for file in os.listdir(os.curdir): we can also replace os.curdir with the desired path, for example: for file in os.listdir("D:\User\PDFfolders"),
the cd command must still be used.
