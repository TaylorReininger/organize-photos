# Imports
import numpy as np
import os
from pathlib import Path
import shutil

"""

====== Sorter =====
Combine lists of images and their associated modified-by date (already shifted if necessary)
The lists shall be combined
The combined list shall be sorted by modified-by date
The contents shall be copied and renamed with a new naming structure (provided by the user)

"""


class Sorter():

    def __init__(self):
        self.out_dir = None
        self.paths_sorted = list()

    def combine(self, *args: list) -> None:

        # Group the lists of files into one list
        paths = list()
        dates = list()

        for batch in args:
            paths += [item[0] for item in batch]
            dates += [item[1] for item in batch]

        # Sort the list based on the 2nd value of each
        indices_sorted = np.argsort(np.array(dates))

        self.paths_sorted = [paths[int(this_index)] for this_index in indices_sorted]
        

    def copy_and_rename(self, out_dir: str, base_name: str = 'ImageNameHere') -> None:

        # Store output directory name and ensure that it exists
        self.out_dir = out_dir
        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

        
        # Naming convention
        num_files = len(self.paths_sorted)
        # Get the number of digits required to represent all the images
        if num_files <= 0:
            raise Exception("No images found with valid extensions")
        

        num_digits_required = int(np.log10(num_files))+1
        # Get the format for the image names as a function of the number of digits required to number all the images sequentially
        image_format = '%s_%0' + str(num_digits_required) + 'd%s'

        index_image = 0
        for original_path in self.paths_sorted:
            
            # Create the filename for this particular image
            this_image_extension = Path(original_path).suffix
            this_image_name = image_format % (base_name, index_image, this_image_extension)
            
            new_path = os.path.join(self.out_dir, this_image_name)
            shutil.copy(original_path, new_path)

            index_image += 1



































