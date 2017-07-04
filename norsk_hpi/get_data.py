#!/usr/bin/python
from __future__ import print_function
from six.moves.urllib import request
import zipfile
import os
import sys

last_percent_reported = None

def download_progress_hook(count, blockSize, totalSize):
    """A hook to report the progress of a download. This is mostly intended for users with
    slow internet connections. Reports every 5% change in download progress.

    Entirely taken from:
    https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/1_notmnist.ipynb
    """
    global last_percent_reported
    percent = int(count * blockSize * 100 / totalSize)

    if last_percent_reported != percent:
        if percent % 5 == 0:
            sys.stdout.write("%s%%" % percent)
            sys.stdout.flush()
        else:
            sys.stdout.write(".")
            sys.stdout.flush()

        last_percent_reported = percent


def download_file(skip_this=False):
    """Download the dataset from a website
    then unzip it.
    """

    if not skip_this:

        if not os.path.isdir("baseballdatabank-2017.1"):

            print("Starting download")
            # Get baseball data in csv form from website
            url = "http://data.ssb.no/api/v0/dataset/1060.json?lang=en"
            request.urlretrieve(url, filename="house_price_index.json", reporthook=download_progress_hook)

            print("Data downloaded and unzipped")
            print("Data licensed under Norwegian Licence for Open Government Data (NLOD).")

        else:
            print("Data not downloaded")
