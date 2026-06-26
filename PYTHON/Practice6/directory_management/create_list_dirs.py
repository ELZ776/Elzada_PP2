# pathlib is used to work with files and folders
from pathlib import Path
# create nested directories: main_folder/sub_folder/files
path = Path("main_folder/sub_folder/files")
path.mkdir(parents=True, exist_ok=True)
print("Nested directories created successfully")

from pathlib import Path

# choose current directory
path = Path(".")
# iterate through all items in the directory
for item in path.iterdir():
    if item.is_file():
        print("File:", item.name)
    elif item.is_dir():
        print("Folder:", item.name)

from pathlib import Path

# choose current directory
path = Path(".")
# find all .txt files
for file in path.rglob("*.txt"):
    print(file)