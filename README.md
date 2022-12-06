# Pdf-merger

If you want to change the directory fromn which the program mergers multiple pdfs intro a single one, you need to run the cd command in the terminal (cd = change directory), followed by your desired path, for example: cd C:\Users\Public\PDFfiles , the script will merge all the pdfs from PDFfiles.

Also instead of: for file in os.listdir(os.curdir): we can also replace os.curdir with the desired path, for example: for file in os.listdir("D:\User\PDFfolders"),
the cd command must still be used.

The 2 pdfs used as an example and the programs result:

![combined pdfs](https://user-images.githubusercontent.com/118382269/206042137-a41c4714-d957-4eeb-bf5a-ec681ef9b951.JPG)

![example](https://user-images.githubusercontent.com/118382269/206042399-76175cd9-494a-4e83-be2e-5283cc0dbe06.JPG)
