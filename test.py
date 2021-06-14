from PIL import Image
import pytesseract
import sys
import os


dict_ = {}

filelimit = 1


    

def test():
    tmp = []
    counter = 0
    beta_counter = 0
    while counter < len(text.splitlines()):
        if ":" in text.splitlines()[counter]:
            key = text.splitlines()[counter]
            beta_counter = counter
            try:
                while ":" not in text.splitlines()[beta_counter+1]:
                    tmp.append(text.splitlines()[beta_counter+1])
                    beta_counter+=1
                dict_[key.lower().strip(":")] = tmp
                tmp = []
            except IndexError:
                print(dict_)
            # beta_counter = 0
        counter += 1
    

def final(text):
    test()

   

    outfile = f"{os.environ['HOME']}/Desktop/Docs/{'_'.join(dict_['names']).lower()}"
    # os.system(f"touch {outfile}")
    with open(outfile+".txt", "w+") as f:
        f.write(text)
    

for dir, folder, files in os.walk("pictures"):
    for i in files:
        filename =  "pictures/"+ i
        text = str(((pytesseract.image_to_string(Image.open(filename)))))
        text = text.replace('-\n', '')
        final(text)
        os.system(f"rm -rf {filename}")
