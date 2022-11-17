import PyPDF2
import os


merge=PyPDF2.PdfFileMerger()
file_number=1

for file in os.listdir(os.curdir): 
        
        if file.endswith(".pdf"):
            
            print(f"file{file_number} = {file}")            
            merge.append(file)
            file_number+=1

merge.write("combine.pdf")


