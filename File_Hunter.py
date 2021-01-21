#=======================FURRO404 && s0n1c268=======================#
#File_Hunter.py
#Line 39 is commented as a 'safety' to this gun, remove the "#" to make it actually delete.
import os
import time
import random
#----------------#
ext = str(input("Extension to hunt for ~ "))
location = str(input("\nPath to Target?~ "))

print("\n\n\nLooking for", ext, "files in", location)

while True:  
    # File name 
    file = random.choice(os.listdir(location)) # Change dir name to whatever
    
    if not file.endswith(ext): # Check if file ends with ".txt"
        print("\nThis is not a", ext, "file (", file,")\nSearching for", ext)
        loop = True
        
        while loop == True:
            time.sleep(0.8)
            file = random.choice(os.listdir(location))
            # Keep picking randomly until it finds a ".txt" file
            
            if file.endswith(ext):
                loop = False
                print("\nFound a", ext, "file!")
                
            else:
                print("\nContinuing to search for", ext, "(Selected File ~", file,")")
            
#--------------------------------------------#  

    # Path 
    path = os.path.join(location, file) 
  
    # Remove the file 
    #os.remove(path) 
    print("%s has been removed successfully" %file)
    print("")
    time.sleep(0.3)
#=======================FURRO404 && s0n1c268=======================#
