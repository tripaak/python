import os


os.chdir(r"C:\Users\akash.tripathi\Desktop\python1.0\Sample_Folder")

# print(os.getcwd()) # get working directory

# os.mkdir('Sample_Folder')

# print(os.path.exists('Sample_Folder'))   # to check Folder is there ?

# if os.path.exists('Sample_Folder'):
#     print("Folder Already Exist")
# else:
#     os.mkdir('Sample_Folder')  
#     print("Folder Created ")  


# for files in os.listdir():   #get list of files in dire 
#     if files == 'try1.py':
#         print("exist")
# print("doesnt exist")  

# print(os.listdir())

open('test.txt','a').close() # to create new file 

# os.chdir(r"C:\ATLAS_PY_TRANSFER\CSV FILE TO IMPORT")   # to cange dir
# print(os.getcwd())

for item in os.listdir():
    path = os.path.join(os.getcwd(),item)
    print(path)



