import os

import shutil

base_dir = r'C:\Users\akash.tripathi\Desktop\python1.0\os_module_Folder'

os.chdir(base_dir)  #go to os module folder 

# print(os.listdir())  #print list of folders

# print(os.walk(base_dir))

# for path, folders, files in os.walk(base_dir):
#     print(path)
#     print(folders)
#     print(files)


# os.rmdir('Akash')    #to delete empty folder

# os.makedirs('Akash/Anay/Vibha')

# shutil.rmtree('Akash') #to delete non empty folder

# shutil.copytree('study','documents/new_study') # copy folder to anther folder

# shutil.copy('file.txt','documents/new_study') # copy file to folder 

# shutil.move('file.txt','study/new_file.txt') # move and rename file 

# shutil.move('study','documents/study_new') # move and rename file 