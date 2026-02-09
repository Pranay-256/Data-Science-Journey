from pathlib import Path #Path finds the path of the existing file and creates the path of the new file which was not existed earlier but now it does
import os #Loads the OS module, which help us to  interact with the operating system (like files, folders, paths)

def readfileandfolder():
    path = Path('')#empty space is used to get the path of the current file/directory
    items = list(path.rglob('*'))#rglob is used to recursively see/iterate to  the items the current path
    #items will give the list of files and folders in the current directory
    for i, items in enumerate(items):#enumerate fxn is used to save the index and the value of a list seperately
                                     #i will have all the index values and items will have all the actual values
         print(f"{i+1} : {items}")                                 

def createfile():
    try:

         readfileandfolder()
         name = input("please tell your file name : ")
         p = Path(name)
         if not p.exists():  #checks if the file with the same file name exists in the current folder / directory or not 
              with open(p,'w') as fs:   #with closes the python file automatically
                  data = input("What you want to write in this file : ")
                  fs.write(data)
              print("FILE CREATED SUCCESFULLY\n")
         else:
             print("THIS FILE ALREADY EXISTS \n")     
    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:
         readfileandfolder() 
         name = input("which file you want to read : ")       
         p = Path(name)
         if p.exists() and p.is_file(): #checks if the there is something on the given path with the given name and it must be a file
             with open(p , "r") as fs:
                 data = fs.read()
                 print(data)
             print("FILE SUCCESSFULLY READED\n")
         else :
             print("THE FILE DOES NOT EXIST\n")    
    except Exception as err:
        print(f"an error occured as {err}")  

def updatefile():
    try:
         readfileandfolder()
         name = input("tell which file you want to update :")  
         p = Path(name)
         if p.exists() and p.is_file():
             print("press 1 for changing the name of your file : ")
             print("press 2 for overwriting the data of your file : ")
             print("press 3 for appending your file : ")

             res = int(input("tell your response : "))
             if res == 1:
                  name2 = input("tell your new file name : ")
                  p2 = Path(name2)
                  p.rename(p2) #rename fxn is used to rename  file of the respected path
                  print("THE FILE HAS BEEN RENAMED\n")


             if res == 2:
                 with open(p ,"w") as fs:
                     data = input("tell what do you want to write ? This will overwrite the file : ")
                     fs.write(data)
                     print("THE FILE HAS BEEN OVERWRITTEN\n ")

             if res == 3:
                 with open(p,'a') as fs :
                     data = input("tell what do you want to append : ")   
                     fs.write(" "+data)  
                     print("THE FILE HAS BEEN APPENDED\n ")
    except Exception as err:
        print(f"an error occured as {err}") 

def deletefile():
    try:
         readfileandfolder()
         name = input("which file you want to delete : ")
         p = Path(name)

         if p.exists() and p.is_file(): 
             os.remove(name) #Deletes the specified file from the system

             print("FILE REMOVED SUCCESFULLY\n")

         else:
             print("NO SUCH FILE EXISTS\n")   

    except Exception as err :
        print(f"an error occured as {err}")          


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deletion of a file")

check = int(input("please tell your response : "))

if check == 1:
    createfile()

if check  == 2:
    readfile()   

if check == 3:
    updatefile()

if check == 4:
    deletefile()    


               
