Matplotlib Util Scripts for parsing COSBench Output
===========

@Author: Ryan.Wallner@emc.com

HOW TO
======

sudo apt-get build-dep matplotlib
pip install matplotlib

To use with COSBench CSV Exports
=======

- Export timeline.csv to location where these scripts are located.
- Make sure there is a “figures” directory

How to run
==========

Hand the script the CSV file, and the interval you want the data point plotted

python <script> <csv-file> (every-#)
