# manga-chapter-downloader
A simple python script to download manga chapters from online reader sites

## Installation
* Clone the repo: `git clone https://github.com/fakesimo/manga-chapter-downloader.git`
* `cd manga-chapter-downloader`
* Install the dependencies: `pip install -r requirements.txt`
* Add the selenium drivers for Firefox as explained [here](https://selenium-python.readthedocs.io/installation.html#drivers)
* Run it! `python src/downloader.py [OPTIONS]`

## Usage
The requirement arguments are:
* `--url / -u` the URL from which download the chapter
* `--folder / -f` the folder into which put the files

The full list of available arguments can be seen running `python src/downloader.py --help`
