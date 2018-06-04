import os

def rename_files():
    # Get file names from a folder
    file_list = os.listdir(r"/Users/daichengbin/Downloads/prank")
    print(file_list)
    
    # Change to working folder
    saved_path = os.getcwd()
    print ("Current working directory is "+saved_path)
    os.chdir(r"/Users/daichengbin/Downloads/prank")
    saved_path = os.getcwd()
    print ("Changed working directory is "+saved_path)
    # For each file, rename filename
    for file_name in file_list:
        map = str.maketrans('', '', '0123456789')
        print ("Old Name - "+file_name+"   "+"New Name - "+file_name.translate(map))
        os.rename(file_name,file_name.translate(map))
    
    print(file_list)
rename_files()