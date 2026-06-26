from pathlib import Path
import shutil
source = Path("main_folder/example.txt")
destination_folder = Path("backup")
destination_folder.mkdir(exist_ok=True)
# copy file to destination folder
shutil.copy(source, destination_folder)
print("File copied successfully")


# move file to destination folder
from pathlib import Path
import shutil
source = Path("main_folder/example.txt")
destination_folder = Path("moved_files")
destination_folder.mkdir(exist_ok=True)

shutil.move(source, destination_folder)

print("File moved successfully")