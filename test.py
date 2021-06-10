from PIL import Image
import pytesseract
import sys
import os


dict_ = {}

filelimit = 1



for i in range(1, filelimit + 1):

    filename = "a.jpg"
          
    text = str(((pytesseract.image_to_string(Image.open(filename)))))
    text = text.replace('-\n', '')


def test(name,counter):
    tmp = []
    try:
        if name in text.split()[counter].lower():
            tmp = []
            beta_counter = counter+1
            while ":" not in text.split()[beta_counter].lower():
                tmp.append(text.split()[beta_counter])
                beta_counter += 1
            dict_[name] = tmp
    except IndexError:
        pass


outfile = ''

counter = 0

while counter <= len(text.split()):
    test('names',counter)
    test('surname',counter)
    test('sex',counter)
    test("number",counter)
    test("birth",counter)
    counter += 1

print(dict_)  

outfile = f"{os.environ['HOME']}/Desktop/Docs/{'_'.join(dict_['names']).lower()}"
with open(outfile+".txt", "w+") as f:

    f.write(text)
