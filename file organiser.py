import os
import shutil

path=r'C:\Users\Dell\OneDrive\file organise'
if not os.path.exists(path):
    print(f"the path '{path}' does not exist.")
    exit()

list_of_file=os.listdir(path)

for file in list_of_file:
    name, extension =os.path.splitext(file)
    print(name,extension)
    extension=extension[1:]

    extension_path=os.path.join(path,extension)
    if os.path.exists(path +'/'+extension):
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)

    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
