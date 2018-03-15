from PIL import Image

import subprocess

def cleanFile(filePath, newFilePath):

    image = Image.open(filePath)

    #对图片进行过滤，然后保存

    image = image.point(lambda x:0 if x<143 else 255)

    image.save(newFilePath)


    subprocess.call(["tesseract",newFilePath,"output"])

    file = open("output.txt",'r')

    print(file.read())

    file.close()

cleanFile("tess2.jpg", "text2clean.png")
