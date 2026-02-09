from pathlib import Path #Path is used to find the path of the required flies or folders
import os #os is used to perform operations on operating system level
import shutil #shutil is used to perform high level file and directory operations which os cannot do 

def readparentfolder():
    path = Path('')
    print("all the parent folders of this directory are shown below : ")
    if path.is_dir():#used to check if anything is a folder or not
        items = list(path.glob('*/'))#glob collects only the selected parent objects of the directory 
    else:
        items = []
    for i , item in enumerate(items):
        print(f"{i+1} : {item}")
    return items 

def readallfolders():
    path = Path('')
    print("all the folders of this directory are shown below : ")
    if path.is_dir():
        items = list(path.rglob('*/'))#rglob collects all the selected objects of the directory 
    else:
        items = []
    for i , item in enumerate(items):
        print(f"{i+1} : {item}")
    return items 


def readmaintxtfiles():
    path = Path('')
    print("all the text files inside the parent directory are shown below :\n ")
    if path.is_dir():
        items = list(path.glob('*.txt'))
    else:
        items = []
    for i , item in enumerate(items):
        print(f"{i+1} : {item}")
    return items

def readalltxtfiles():
    path = Path('')
    print("all the text files inside this directory are shown below :\n ")
    if path.is_dir():
        items = list(path.rglob('*.txt'))
    else:
        items = []
    for i , item in enumerate(items):
        print(f"{i+1} : {item}")
    return items  

def createfolder():
    try:
       print("press 1 if you want to create a parent folder")
       print("press 2 if you want to create a child folder")
       print("press 3 if you want to create a grandchid folder")
       userinput = int(input("enter your choice : "))
       if userinput == 3 :
          items = readparentfolder()
          index = int(input("please tell the serial number of the folder inside which you want to create a new folder : "))
          path = items[index-1]
          if path.exists() and path.is_dir():
              print(f"{path} is a valid directory \nshowing all the child folders inside it :\n")
              if path.is_dir():
                  items2 = list(path.rglob('*/'))
              else:
                  items2 = []    
              for i , item in enumerate(items2):
                  print(f"{i+1} : {item}")
              index2 = int(input("select the serial number of the folder inside which you want to create a new grandchild folder : "))  
              path2 = items2[index2-1] 
              if path2.exists():
                  name = input("enter the name of the folder you want to add : ")
                  path3 = path2/name
                  if path3.exists() and path3.is_dir():
                      print(f"there is already a folder existing with the name {name}\n")
                  else :
                      path3.mkdir()
                      print(f"{name} folder created successfully \n")
              else:
                  print("please select a valid child folder\n")          
          else:
              print("please select a valid serial number \n") 
       elif userinput==1 :
           items = readparentfolder()
           mainpath = Path('')
           name = input("enter the name of the new folder : ")
           path = mainpath/name
           if path.exists() and path.is_dir():
               print(f"there is another folder already present with the name {name}\n")
           else:
               path.mkdir()
               print(f"{name} folder created succesfully\n") 
       elif userinput==2 :
           items = readparentfolder()
           index = int(input("enter the serial number of the folder inside which you want to create a child folder : ")) 
           path = items[index-1]
           if path.exists() and path.is_dir():
               print(f"{path} is a valid directory")
               print("showing all the child folders inside the selected folder : \n")
               if path.is_dir():
                  items2 = list(path.glob('*/'))
               else:
                   items2 =[]    
               for i,item in enumerate(items2):
                   print(f"{i+1} : {item}")
               name = input("enter the name of the folder you want to create : ")
               path2 = path/name
               if path2.exists():
                   print(f"a folder with the name {name} already exists inside the folder\n")
               else:
                   path2.mkdir()
                   print(f"{name} folder created succesfully\n")  
           else:
               print("please enter a valid serial number\n")   
       else:
           print("please select a valid option\n")             

    except Exception as x :
        print(f"oops! we got an exception as {x}\n")                 

def updatefolder():
    try:
       print("press 1 if you want to add a text file")
       print("press 2 if you want to delelete a text file")
       print("press 3 if you want to read a text file")
       print("press 4 if you want to write in a text file")
       print("press 5 if you want to rename a text file or a folder")
       userinput = int(input("enter your choice : "))
       if userinput==1:
           print("press 1 if you want to add the text file in the main directory")
           print("press 2 if you want to add a text file inside any folder")
           choice = int(input("enter your choice : "))
           if choice ==1:
               readmaintxtfiles()
               mainpath =Path('')
               name = input("enter the name of your text file : ")
               if not name.endswith(".txt"):
                   name+=".txt"
               path = mainpath/name   
               if path.exists() and path.is_file():
                   print(f"a text file with the name {name} already exists \n")
               else:
                   path.touch() #used to create an empty file
                   print(f"{name} file created succesfully \n")
           elif choice==2:
               items = readallfolders()
               index = int(input("enter the serial number of the folder inside which you want to create a new text file : "))
               path = items[index-1]
               if path.exists() and path.is_dir():
                   print("all the text files of this folder are shown below : \n")
                   if path.is_dir():
                       items2 = list(path.rglob('*.txt'))
                   else:
                       items2 = []
                   for i , item in enumerate(items2):
                       print(f"{i} : {item}") 
                   name = input("enter the name of your text file : ")
                   if not name.endswith(".txt"):
                       name+=".txt"
                   path2 = path/name
                   if path2.exists() and path2.is_file():
                       print(f"there is already a file existing with the name {name} in this folder \n")
                   else:
                       path2.touch()
                       print(f"{name} file succesfully created\n")   
           else:
               print("please enter a valid choice \n") 
       elif userinput==2 :
           items = readalltxtfiles()
           index = int(input("enter the serial number of the text file you want to delete : "))
           name = items[index-1]  
           if name.exists() and name.is_file():
               os.remove(name)
               print(f"{name} text file has been succesfully delteted\n")  
           else:
               print(f"please select a valid text file\n") 
       elif userinput==3 :
           items = readalltxtfiles()
           index = int(input("enter the serial number of the text file you want to read : "))
           name = items[index-1]
           if name.exists() and name.is_file():
               with open (name , "r") as x:
                   data = x.read()
                   print(data)
           else :
               print("please select a valid text file")
       elif userinput==4:
           print("press 1 for overwriting your file")
           print("press 2 for appending your file")
           choice = int(input("type your choice : "))
           if choice ==1:
              items = readalltxtfiles()
              index = int(input("enter the serial number of the text file you want to overwrite : "))
              name = items[index-1]
              if name.exists() and name.is_file():
                  with open (name , "w") as x:
                      data = input("enter the data you want to write : \n")
                      x.write(data)
                      print("the file has been successfully overwritten\n")    
              else:
                  print("please select a valid text file\n")       
           elif choice ==2:
              items = readalltxtfiles()
              index = int(input("enter the serial number of the text file you want to append : "))
              name = items[index-1]
              if name.exists() and name.is_file():
                  print("showing the existing data of the file :\n")
                  with open (name , "r") as x:
                      data = x.read()
                      print(data)
                      print("\n")
                  with open (name , "a") as x:
                      data = input("enter the data you want to write : \n")
                      x.write(" "+data)
                      print("the file has been successfully appended\n")
              else:
                  print("please select a valid text file\n")              
           else:
               print("please choose a valid option\n")                     
       elif userinput==5:
           print("press 1 for renaming a folder ")
           print("press 2 for renaming a text file")
           choice = int(input("enter your choice : "))
           if choice==1:
               items=readallfolders()
               index=int(input("enter the serial number of the folder you want to rename : ")) 
               path=items[index-1]
               newname = input("enter the new name of your folder : ")
               path2 = path.parent/newname
               if path2.exists() and path2.is_dir():
                   print(f"a folder already exists with the name {newname}\n ")
               else:
                   path.rename(path2)
                   print(f"the folder has been successfully renamed to {newname}\n")
           elif choice==2:
               items=readalltxtfiles()
               index = int(input("enter the serial number of the file you want to rename : "))
               name=items[index-1]
               newname=input("enter the new name of your text file : ")
               if not newname.endswith(".txt"):
                   newname+=".txt"
               newfilename = name.parent/newname
               if newfilename.exists() and newfilename.is_file():
                   print(f"a file already exists with the name {newname}\n")
               else:
                   name.rename(newfilename)
                   print(f"the file has been successfully renamed to {newname}\n ")
           else:
               print("please choose a valid option\n") 
       else:
           print("please choose a valid option\n")
    except Exception as err :
        print(f"oops! we got an exception as {err}\n")      

def deletefolder():
    try:
       print("showing all the folders of the directory : ")
       items=readallfolders()
       index=int(input("enter the serial number of the folder you want to delete : "))
       path = items[index-1]
       if path.exists() and path.is_dir():
           print("showing all the contents of the selected folder : ")
           content = list(path.rglob('*'))
           for i , item in enumerate(content):
               print(f"{i} : {item}")
           print("NOTE : all the contents of your folder will get deleted")
           print("if you still want to delete the folder type yes")
           print("if you don't want to delete the folder press no")
           choice = input("enter your input : ")
           if choice=="yes":
               shutil.rmtree(path)
               print(f"{path} directory has been successfully deleted with all of it's content\n")
           elif choice=="no":
               print("folder deletion process has been terminated\n")
           else:
               print("received an invalid input\n")
       else:
           print("please choose a valid directory")  
    except Exception as err :
        print(f"opps! we got an exception as {err}") 

print("press 1 if you want to create new folder inside the directory")
print("press 2 if you want to update any folder inside the directory")
print("press 3 if you want to delete any folder from the directory")
try:
    choice=int(input("enter your choice : "))
    if choice == 1:
        createfolder()
    elif choice == 2:
        updatefolder()
    elif choice == 3:
        deletefolder()
    else:
        print("please select a valid option\n")
except Exception as err:
    print(f"oops! we got an exception as {err}\n")            