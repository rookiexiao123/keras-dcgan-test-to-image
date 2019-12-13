import os 
from imutils import paths
import random

current_dir = os.path.dirname(__file__)

# 创建一个txt文件，文件名为mytxtfile,并向文件写入msg
def text_create(name):
    full_path = current_dir + 'txt/' + name + '.txt'  
    file = open(full_path, 'w')
    file.write(name)   #写入txt
    # file.close()

def load_data(path):
    imagePaths = sorted(list(paths.list_images(path)))
    random.seed(42)
    random.shuffle(imagePaths)

    for imagePath in imagePaths:
        label = imagePath.split(os.path.sep)[5].split('.')[0]
        print(label)
        text_create(label)	

path = 'D:\ImageRecognition\large logo dataset\LLD-logo_files\LLD-logo-files'

load_data(path)
