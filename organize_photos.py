
# Imports
from src.folder import Folder
from src.sorter import Sorter


if __name__ == "__main__":

    # Grab files from a folder
    f1 = Folder('../your/folder/here', -3)
    friend1 = f1.get_files()

    f2 = Folder('../other/folder/here', 0)
    friend2 = f2.get_files()

    # Combine, sort, and copy/rename the image files
    s = Sorter()
    s.combine(friend1, friend2)
    s.copy_and_rename('./PhotosOrganized', 'Vacation2024')



































