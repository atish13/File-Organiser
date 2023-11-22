import os
import shutil

path=input("enter path:")
files=os.listdir(path)

for file in files:
    filename,extension=os.path.splitext(file)
    extension=extension[1:] 

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
        













##import os
##import shutil
##import datetime
##
##def organize_files(directory):
##    # Get a list of all files in the directory
##    files = os.listdir(directory)
##
##    # Create a folder for each file extension
##    for file in files:
##        if os.path.isfile(os.path.join(directory, file)):
##            file_extension = os.path.splitext(file)[1].lower()
##            folder_path = os.path.join(directory, file_extension[1:])
##
##            # Create the folder if it doesn't exist
##            if not os.path.exists(folder_path):
##                os.makedirs(folder_path)
##
##            # Move the file to the respective folder
##            source_file_path = os.path.join(directory, file)
##            destination_file_path = os.path.join(folder_path, file)
##            shutil.move(source_file_path, destination_file_path)
##
##def organize_by_creation_date(directory):
##    # Get a list of all files in the directory
##    files = os.listdir(directory)
##
##    # Create a folder for each month and year combination
##    for file in files:
##        if os.path.isfile(os.path.join(directory, file)):
##            file_path = os.path.join(directory, file)
##            creation_date = os.path.getctime(file_path)
##            creation_date = datetime.datetime.fromtimestamp(creation_date)
##            folder_name = creation_date.strftime('%Y-%B')
##
##            folder_path = os.path.join(directory, folder_name)
##
##            # Create the folder if it doesn't exist
##            if not os.path.exists(folder_path):
##                os.makedirs(folder_path)
##
##            # Move the file to the respective folder
##            destination_file_path = os.path.join(folder_path, file)
##            shutil.move(file_path, destination_file_path)
##
### Specify the directory path to organize
##path=input("enter the path that you want to organise:")#directory_path = '/path/to/your/directory'
##
### Organize files by extension
##organize_files(path)

# Organize files by creation date
#organize_by_creation_date(path)
