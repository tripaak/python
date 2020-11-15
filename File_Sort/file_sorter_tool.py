import os
import shutil


# Sort the files based on extension 
# create folder for each extension 
# move those files to respective folder 


extensions = {
    'video_extensions' : ('.flv','.mp4'),
    'document_extensions' : ('.txt', '.pdf', '.docx'),
    'image_extensions' : ('.jpg','.JPG'),
    'songs_extensions' : ('.mp3'),

}

base_folder = r"C:\Users\akash.tripathi\Desktop\python1.0\File_Sort"

def file_finder(folder_path, file_extensions):
    files = []
    for items in os.listdir(folder_path):
        for extension in file_extensions:
            if items.endswith(extension):
                files.append(items)
    return files


for extension_type, extension_tuple in extensions.items():
    new_folder_name = extension_type.split('_')[0]+'_Files'
    new_folder_path = os.path.join(base_folder,new_folder_name)  # This will crete new folders based on extension type
    if os.path.exists(new_folder_path):
        print(f"Folder {new_folder_name}, already exist!!")
    else:
        os.mkdir(new_folder_path)
    temp = file_finder(base_folder,extension_tuple)
    for item in temp:
        print(item)
        current_folder_file = os.path.join(base_folder,item)
        shutil.move(current_folder_file,new_folder_path)
         


   
      


    
