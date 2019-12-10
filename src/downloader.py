import os
import time

import click
from selenium import webdriver
import requests


@click.command()
@click.option(
    '--url', '-u',
    required=True,
    type=str,
    help='URL of the first page of the chapter'
)
@click.option(
    '--folder', '-f',
    required=True,
    type=str,
    help='Name of the folder into which put the pages'
)
@click.option(
    '--verbose', '-v',
    default=False,
    is_flag=True,
    help='Verbose'
)
def downloadChapter(url, folder, verbose):

    SLEEP_SECONDS = 5

    # Open browser and obtain all the pages
    driver = webdriver.Firefox()
    driver.get(url)

    # Going to sleep to be sure that the page loads completely
    if verbose:
        print('Going to sleep ...')
        time.sleep(5)
        print('Awake!')

    pages = driver.execute_script('return window.pages')

    # Download all the pages
    for i, p in enumerate(list(filter(lambda p: 'thumb_url' in p, pages))):

        # Get the directory. If it doesn't exists, create it
        directory = f'{os.getcwd()}/{folder}'
        if not os.path.isdir(directory):
            os.makedirs(directory)

        if verbose:
            print(f'Downloading page {i+1}')
        img_url = p['thumb_url']
        response = requests.get(img_url, allow_redirects=False)

        # Save the image
        with open(f'{directory}/'+p['filename'], 'wb') as file:
            file.write(response.content)

    # Close the browser
    driver.close()


if __name__ == '__main__':
    downloadChapter()
