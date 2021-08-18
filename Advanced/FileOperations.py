import shutil
import os


def move_files(src, destination):
    files = os.listdir(src)
    for f in files:
        file_path = os.path.join(src, f)
        print(("copying file" + str(f)).center(70, "#"))
        if os.path.isfile(file_path) and os.path.isdir(destination):
            print(("Moving file" + str(f)).center(70, "#"))
            print(file_path)
            shutil.move(file_path, destination)
