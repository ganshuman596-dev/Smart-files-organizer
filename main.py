from pathlib import Path
import shutil
import os
import file_categories as f

def path_existence(path):
    '''Check thats path exists and also tells whether it is file or folder'''
    if path.exists():
        if path.is_file():
            return "file"
        else:
            return "folder"
    else:
        return "notExist"

#Welcoming user
print("="*50)
print("Welcome to SMART FILE MANAGER".center(50))
print("="*50)

#Taking path from user
while True:
    user_path=Path(input("Enter the path of folder you want to organize: "))
    if path_existence(user_path)!="folder":
        print("The path entered is not exist or not folder!")
        input("Click enter")
    else:
        break
#Making lists of files and folders in the path
for root,folders,files in os.walk(user_path):
    files_in_path=files
    folders_in_path=folders

#Sorting and moving the files to the folders
for file in files_in_path:
    file=Path(file)

    tempoValue=0        
    for key,value in f.files_categories.items():
        if file.suffix in value:
            create_folder=user_path / key
            create_folder.mkdir(exist_ok=True)     
            old_destination=user_path / file
            new_destination=create_folder / file
            shutil.move(old_destination,new_destination)        
            tempoValue=1

    if tempoValue==0:                       
        create_folder=user_path / "Others"
        create_folder.mkdir(exist_ok=True)
        old_destination=user_path / file
        new_destination=create_folder / file
        shutil.move(old_destination,new_destination)




