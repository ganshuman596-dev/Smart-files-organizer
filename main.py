from pathlib import Path
import shutil
import os
import file_categories as f
import time
import hashlib
import logging
import uuid
logging.basicConfig(filename = "trial.log",
                     level = logging.INFO,
                     format = "%(asctime)s - %(levelname)s - %(message)s")

def generate_uid():
    unique_id = str(uuid.uuid4())
    return unique_id

def path_existence(path):
    '''Check thats path exists and also tells whether it is folder'''
    if path.exists():
        if path.is_dir():
            return "folder"
        else:
            return "not folder"
    else:
        return "notExist"

def present_time_info():
    t=time.localtime()
    hours=t.tm_hour
    day_of_year=t.tm_yday
    day=t.tm_mday
    month=t.tm_mon
    year=t.tm_year
    present_time_info_list=[hours,day_of_year,month,year,day]
    return present_time_info_list

def file_time_info(file):
    file=Path(file)
    info=file.stat()
    t=time.localtime(info.st_mtime)
    hours=t.tm_hour
    day=t.tm_mday
    day_of_year=t.tm_yday
    month=t.tm_mon
    year=t.tm_year
    file_time_info_list=[hours,day_of_year,month,year,day]
    return file_time_info_list

def take_path_from_user():
    while True:
        user_path = Path(input("Enter the path of folder: "))
        if path_existence(user_path) == "not folder":
            print("The path entered is not a folder!")
            input("Click enter")
        elif path_existence(user_path) == "notExist":
            print("The path entered is not found!")
            input("Click enter")
        else:
            return user_path
        
def list_of_files_folders(user_path):
    '''Making lists of files and folders in the path'''
    files_in_path=[]
    folders_in_path=[]
    user_path=Path(user_path)
    for files in user_path.iterdir():
        files=Path(files)
        if files.is_file():
            files_in_path.append(files)
        elif files.is_dir():
            folders_in_path.append(files)
    return files_in_path, folders_in_path

def create_folder_move_file(file_location,create_folder,unique_id):
    create_folder.mkdir(exist_ok=True)
    new_destination = create_folder / file_location.name
    while True:
        if new_destination.exists():
            print(f"{file_location.name} already exists in the folder")
            newname = input("enter the name without suffix: ")
            newname_ext = Path(newname + file_location.suffix)
            new_destination = create_folder / newname_ext
        else:
            break
    shutil.move(file_location, new_destination)
    logging.info(f'{unique_id} - File Moved - {file_location}')
    logging.info(f'{unique_id} - Moved to - {new_destination}')

def sort_files_by_filetype(user_path):
    '''Sorting files by file type'''
    user_path=Path(user_path)
    files_in_path,folders_in_path=list_of_files_folders(user_path)
    if len(files_in_path) == 0:
        print("No files in given folder")
        input("Click enter")
    else:
        unique_id = generate_uid()
        logging.info(f'{unique_id} - Moving Process Started')
        for file in files_in_path:
            file = Path(file)
            found_category = False       
            for key,value in f.files_categories.items():
                if file.suffix in value:
                    create_folder = user_path / key
                    create_folder_move_file(file,create_folder,unique_id)       
                    found_category = True
                    break
            if not found_category:                       
                create_folder = user_path / "Others"
                create_folder_move_file(file,create_folder,unique_id)
        logging.info(f'{unique_id} - Moving Process Ended')

def sort_files_by_time(user_path):
    '''Sorting files by time'''
    user_path=Path(user_path)
    files_in_path,folders_in_path = list_of_files_folders(user_path)
    if len(files_in_path) == 0:
        print("No files in given folder")
        input("Click enter")
    else:
        unique_id = generate_uid()
        logging.info(f'{unique_id} - Moving Process Started')
        present_time_info_list=present_time_info()
        for file in files_in_path:
            file_time_info_list = file_time_info(file)
            if file_time_info_list[3] == present_time_info_list[3] and file_time_info_list[1] == present_time_info_list[1]:
                create_folder = user_path / "Today"
                create_folder_move_file(file,create_folder,unique_id)
            elif file_time_info_list[3] == present_time_info_list[3] and file_time_info_list[1] + 1 == present_time_info_list[1]:
                create_folder = user_path / "Yesterday"
                create_folder_move_file(file,create_folder,unique_id)
            elif file_time_info_list[3] == present_time_info_list[3] - 1 and present_time_info_list[1] == 1:
                create_folder = user_path / "Yesterday"
                create_folder_move_file(file,create_folder,unique_id)
            else:
                create_folder = user_path / "Others"
                create_folder_move_file(file,create_folder,unique_id)
        logging.info(f'{unique_id} - Moving Process Ended')

def sort_files_by_date(user_path):
    user_path=Path(user_path)
    files_in_path,folders_in_path = list_of_files_folders(user_path)
    if len(files_in_path) == 0:
        print("No files in given path")
        input("Click enter")
    else:
        unique_id = generate_uid()
        logging.info(f'{unique_id} - Moving Process Started')
        for file in files_in_path:
            t=file_time_info(file)
            folder_name = f'{t[4]}-{t[2]}-{t[3]}'
            create_folder = user_path / folder_name
            create_folder_move_file(file,create_folder,unique_id)
        logging.info(f'{unique_id} - Moving Process Ended')

def sort_files_by_month(user_path):
    user_path=Path(user_path)
    files_in_path,folders_in_path = list_of_files_folders(user_path)
    if len(files_in_path) == 0:
        print("No files in given path")
        input("Click enter")
    else:
        unique_id = generate_uid()
        logging.info(f'{unique_id} - Moving Process Started')
        for file in files_in_path:
            t=file_time_info(file)
            folder_name = f'{t[2]}-{t[3]}'
            create_folder = user_path / folder_name
            create_folder_move_file(file,create_folder,unique_id)
        logging.info(f'{unique_id} - Moving Process Ended')

def sort_files_by_year(user_path):
    user_path=Path(user_path)
    files_in_path,folders_in_path = list_of_files_folders(user_path)
    if len(files_in_path) == 0:
        print("No files in given path")
        input("Click enter")
    else:
        unique_id = generate_uid()
        logging.info(f'{unique_id} - Moving Process Started')
        for file in files_in_path:
            t=file_time_info(file)
            folder_name = f'{t[3]}'
            create_folder = user_path / folder_name
            create_folder_move_file(file,create_folder,unique_id)
        logging.info(f'{unique_id} - Moving Process Ended')

def get_file_hash(file_path):
    hash_object = hashlib.sha256()
    with open(file_path, "rb") as hash_file :
        while True:
            chunk = hash_file.read(4096)
            if not chunk :
                break
            hash_object.update(chunk)
    file_hash = hash_object.hexdigest()
    return file_hash

def get_duplicates(user_path):
    user_path = Path(user_path)
    files_in_path, folders_in_path = list_of_files_folders(user_path)
    groups_by_size = {}
    groups_by_hash = {}
    duplicates = {}
    for file in files_in_path:
        file_path = Path(file)
        info = file_path.stat()
        file_size = info.st_size
        if file_size not in groups_by_size:
            groups_by_size.update({file_size : []})
        groups_by_size[file_size].append(file_path)
    for key, value in groups_by_size.items():
        if len(value) == 1:
            continue
        for file_path in value:
            file_hash = get_file_hash(file_path)
            if file_hash not in groups_by_hash:
                groups_by_hash.update({file_hash : []})
            groups_by_hash[file_hash].append(file_path)
    for key, value in groups_by_hash.items():
        if len(value) == 1:
            continue
        duplicates.update({key : value})
    return duplicates
            
def merge_duplicate_files(files_path_list):
    while True:
        common_name = input("Enter the new name of file(without extension): ")
        file_path = Path(files_path_list[0])
        file_extension = file_path.suffix
        new_file_name = f'{common_name}{file_extension}' 
        new_file_path = file_path.parent / new_file_name
        if new_file_path.exists():
            print("The name already exists!")
            input("Click enter")
        else:
            confirmation = input("Enter 'y' if you finaly want to merge this files and permanently delete the duplicates OR click enter to terminate: ")
            if confirmation == "y": 
                file_path.rename(new_file_path)
                for i, duplicate_file_path in enumerate(files_path_list):
                    if i == 0:
                        continue
                    duplicate_file_path = Path(duplicate_file_path)
                    duplicate_file_path.unlink()
                break
            else:
                break

def undo_last_action():
    with open("trial.log", "rt") as log_file:
        last_process = ""
        log_file.seek(0,2)
        total = log_file.tell()
        log_file.seek(0)
        while True:
            line = log_file.readline()
            if "Moving Process Started" in line or "Undo Process Started" in line:
                last_process = line.strip()
                line_post = log_file.tell()
            elif log_file.tell() >= total:
                break
        if "Moving Process Started" in last_process:
            unique_id = generate_uid()
            logging.info(f"{unique_id} - Undo Process Started")
            log_file.seek(line_post)
            while True:
                old_dest_line = log_file.readline()
                if "File Moved" not in old_dest_line:
                    print("There is somthing problematic in log file.")
                    break
                old_dest = old_dest_line.split(" - ", 4)[4].strip()
                new_dest_line = log_file.readline()
                if "Moved to" not in new_dest_line:
                    print("There is somthing problematic in log file.")
                    break
                new_dest = new_dest_line.split(" - ", 4)[4].strip()
                try:
                    shutil.move(new_dest, old_dest)
                    logging.info(f'{unique_id} - File Moved - {new_dest}')
                    logging.info(f'{unique_id} - Moved to - {old_dest}')
                    folder = Path(new_dest).parent
                    if len(list(folder.iterdir())) == 0:
                        os.rmdir(folder)
                except:
                    print(f"{new_dest} - This file has a problem")
                location = log_file.tell()
                if "Moving Process Ended" in log_file.readline():
                    break
                else:
                    log_file.seek(location)
            logging.info(f"{unique_id} - Undo Process Ended")
        elif "Undo Process Started" in last_process:
            print("Last Process was undo")  
        else:
            print("No process found!")    

def view_last_action_log():
    with open("trial.log", "rt") as log_file:
        last_process = ""
        log_file.seek(0,2)
        total = log_file.tell()
        log_file.seek(0)
        checker = False
        while True:
            line = log_file.readline()
            if "Moving Process Started" in line or "Undo Process Started" in line:
                last_process = line.strip()
                line_post = log_file.tell()
                checker = True
            elif log_file.tell() >= total:
                break
        if not checker:
            print("No activity log")
        else:
            log_file.seek(line_post)
            print(last_process)
            while True:
                if log_file.tell() >= total:
                    break
                print(log_file.readline())
                


#Welcoming user
print("="*50)
print("Welcome to SMART FILE MANAGER".center(50))
print("="*50)
print("1. Organize files")
print("2. Find duplicates")
print("3. Undo last operation")
print("4. View last action activity log")
print("5. Exit")

while True:
    try:
        user_choosen_srno=int(input("Enter the serial number number of window you want to enter: "))
        if 1<=user_choosen_srno<=5:
            break
        else:
            print("Invalid Input!")
            input("Click enter")
    except:
        print("Invalid Input!")
        input("Click enter")

if user_choosen_srno==1:
    print("1. Sort by file type")
    print("2. Sort by Today/Yesterday/Others")  
    print("3. Sort by date") 
    print("4. Sort by month") 
    print("5. Sort by year")

    while True:
        try:
            sorting_method = int(input("Enter the serial of method you want to choose for sorting files: "))
            if 1 <= sorting_method <= 5:
                break
            else:
                print("Invalid Input!")
                input("Click enter")
        except:
            print("Invalid Input!")
            input("Click enter")

    if sorting_method == 1: 
        #Sort by file type    
        user_path = take_path_from_user()
        sort_files_by_filetype(user_path)
        print("DONE!")
        input("Click enter")

    elif sorting_method == 2:
        #Sort by Today/Yesterday/Others
        user_path = take_path_from_user()
        sort_files_by_time(user_path)
        print("DONE!")
        input("Click enter")

    elif sorting_method == 3:
        #sort by date
        user_path = take_path_from_user()
        sort_files_by_date(user_path)
        print("DONE!")
        input("Click enter")

    elif sorting_method == 4:
        #sort by month
        user_path = take_path_from_user()
        sort_files_by_month(user_path)
        print("DONE!")
        input("Click enter")

    elif sorting_method == 5:
        #sort by year
        user_path = take_path_from_user()
        sort_files_by_year(user_path)
        print("DONE!")
        input("Click enter")


elif user_choosen_srno == 2:
    #find duplicates
    user_path = Path(take_path_from_user()) 
    duplicates = get_duplicates(user_path)
    if len(duplicates) == 0:
        print("No duplicates found!")
        input("Click enter")
    else:
        i = 1
        print("Following are the groups of duplicates: ")
        for hash, files_path_list in duplicates.items():
            print(f'Group {i}:')
            for file_path in files_path_list:
                file_path = Path(file_path)
                print(file_path.name)
            i += 1
            print('\n')
            while True:
                try:
                    replace_or_skip = int(input("Enter 1 to skip these group and 2 to merge these group: "))
                    if replace_or_skip not in [1,2]:
                        print("Invalid Input!")
                        input("Click enter")
                    else:
                        break
                except:
                    print("Invalid Input!")
                    input("Click enter")
            if replace_or_skip == 1:
                continue
            elif replace_or_skip == 2:
                merge_duplicate_files(files_path_list)
                print("Done!")
                input("Click enter")

elif user_choosen_srno == 3:
    # Undo last operation
    input("Confirm undo operation by clicking enter")
    undo_last_action()
    print("Done")

elif user_choosen_srno == 4:
    # View activity log
    view_last_action_log()
    print("Done")

elif user_choosen_srno == 5:
    #exit
    input("Click Enter")

else:
    print("Invalid Input!")