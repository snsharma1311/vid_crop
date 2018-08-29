# Select ROIs in Images and Videos using Python and OpenCV

The project contains sample codes to select ROIs in images and videos

## Getting Started

## Prerequisites

Python 2.7
Pip
Virtualenv
OpenCV
Numpy

## Installing

### Ubuntu 16.04
Python 2.7 is available by default \
For other prerequisites follow the instructions: 
1. Install Pip \
sudo apt-get update \
sudo apt-get install python-pip 
2. Install virtualenv \
sudo pip install virtualenv  \
3. Setup virtual enviornment 
Download source files in to a folder (use git clone or download ZIP) \
cd path/to/downloaded/folder \
virtualenv venv 
4. Activate venv \
source venv/bin/activate 
5. Add packages \
pip install -r requirements.txt 

## Running the tests

### For Images
python image_crop.py 
* It will take an image from images folder and save the cropped image as cropped.jpg in to same folder

### For Videos
python video_crop.py 
* It will take an sample video from video folder and save the cropped video as cropped.avi in to same folder

### Authors

* **Shashank Sharma** 




