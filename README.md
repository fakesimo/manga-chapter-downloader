# manga-chapter-downloader
A simple python script to download manga chapters from online reader sites which uses the FoOlSlide software

## Installation
Clone the repo:
```bash
$ git clone https://github.com/fakesimo/manga-chapter-downloader.git
```
Install the project dependencies
```bash
$ cd manga-chapter-downloader
$ pip install -r requirements.txt
```
Add the selenium drivers for Firefox as explained [here](https://selenium-python.readthedocs.io/installation.html#drivers)

## Usage
Run with
```bash
$ python src/downloader.py [OPTIONS]
```
The requirement arguments are:
* `--url / -u` the URL from which download the chapter
* `--folder / -f` the folder into which put the files

The full list of available arguments can be seen with
```bash
python src/downloader.py --help
```
