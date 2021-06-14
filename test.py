from PIL import Image
import pytesseract
import sys
import os


dict_ = {}

filelimit = 1

id_book_keys = ["i.d.","surname","forenames","country of birth","date of birth","date issued",]
    

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


    

def final(text,filename):
    if 'I.D.' in text or "HOME" in text:
        # print(text.splitlines())
        counter = 0
        while counter < len(text.splitlines()):
            for i in id_book_keys:
                if i in text.splitlines()[counter].lower():
                    beta_counter = counter
                    try:
                        while text.splitlines()[beta_counter].lower() not in id_book_keys:
                            print(text.splitlines()[beta_counter])
                            beta_counter += 1
                    except IndexError:
                        pass

            counter += 1

        # print("ID BOOK")
    else:
        test()
    # exit()

   
    try:
        outfile = f"{os.environ['HOME']}/Desktop/OCR/{'_'.join(dict_['names']).lower()}"
    except KeyError:
        outfile = ""
        os.system(f"mv {filename} {os.environ['HOME']}/Desktop/OCR/redo")

    # os.system(f"touch {outfile}")
    with open(outfile+".txt", "w+") as f:
        f.write(text)
    

for dir, folder, files in os.walk("pictures"):
    for i in files:
        filename =  "pictures/"+ i

        text = str(((pytesseract.image_to_string(Image.open(filename)))))
        text = text.replace('-\n', '')
        final(text,filename)
        if len(dict_) >= 8:
            os.system(f"rm -rf {filename}")
        else:
            print("not done")
            os.system(f"mv {filename} {os.environ['HOME']}/Desktop/OCR/redo")

