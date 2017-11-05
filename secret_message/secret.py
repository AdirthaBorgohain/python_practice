


import os

#funtion to rename files
def rename_files():

    #get the files names from a folder
    file_list=os.listdir('./prank/')
    #print(file_list)

    os.chdir('./prank')
    # for renameing the files we need to go to prank folder
    
    
    #for each file rename file
    for file_name in file_list:
        new_name=file_name.translate(None,'0123456789')
        #printing the old and the new name
        print("old name : "+file_name)
        print("new name : "+new_name)
        #translate(table,"list of chars to remove)
        os.rename(file_name,new_name)

#rename file funtion completed

rename_files()
