# remove deletes the file
import os
os.remove("demofile.txt")

# delete the file
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# rmdir deletes an empty folder
import os
os.rmdir("myfolder")