#!/usr/bin/python

import os
from norsk_hpi import get_data

def main():
    """Process the dataset for analysis
    """

    # Reset path
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    os.chdir("..") # Store downloaded data outside of repo
    get_data.download_file()

    # Specify data folder location
    directory = os.path.dirname(os.path.abspath(os.path.join(__file__, "..")))
    file_loc = os.path.join(directory, "house_price_index.csv")

    return file_loc


if __name__ == '__main__':
    main()
