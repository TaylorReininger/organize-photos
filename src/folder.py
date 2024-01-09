# Imports
import os
from pathlib import Path


class Folder():
    """
    The main class concept here is a "Folder". A folder consists of image files (from a set list of extensions).
    The files shall include information for the modified-by date. 
    The files shall posess a valid image extension (like .png)
    The user can specify a time offset for each folder (for example a phone may be using European time but a DSLR might be using eastern time)
    """
    
    def __init__(self, path_dir: str, shift_in_hours: float = 0) -> None:

        # ==== Initialize some class members for use in the class methods ===

        # The directory to pull images from
        self.path_dir = path_dir
        # The number of hours to shift the time by (negative to shift back in time, positive to shift forward)
        self.shift_in_hours = shift_in_hours
        # The file extensions that will be considered valid images
        self.valid_extensions = ['.jpg', '.jpeg', '.gif', '.png', '.tiff', '.psd', '.pdf', '.eps', '.raw']


    def get_files(self) -> list:

        paths = [(child, os.path.getmtime(child)+self.shift_in_hours*3600) for child in Path(self.path_dir).iterdir() if Path(child).suffix.lower() in self.valid_extensions]
        return paths

