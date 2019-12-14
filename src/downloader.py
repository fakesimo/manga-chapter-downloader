import os
import shutil
import time

import click
import requests
from selenium import webdriver


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
    '--archive_type', '-a',
    default=None,
    type=str,
    help='Will archive the downloaded chapter. Only supports \'zip\' and \'cbz\''
)
@click.option(
    '--verbose', '-v',
    default=False,
    is_flag=True,
    help='Will print verbose messages'
)
def downloadChapter(url, folder, verbose, archive_type):

    SLEEP_SECONDS = 5
    print('Starting download process ...')

    # Open browser and obtain all the pages
    driver = webdriver.Firefox()
    driver.get(url)

    # Going to sleep to be sure that the page loads completely
    if verbose:
        print('Going to sleep ...')
    time.sleep(SLEEP_SECONDS)
    pages = driver.execute_script('return window.pages')

    if verbose:
        print(f'Woke up and found {len(pages)} pages')

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

    # Make the archive in case it is wanted
    if(archive_type and archive_type in ('zip', 'cbz')):
        makeArchive(folder, archive_type)

    print('Done!')


def makeArchive(dir_name, archive_type):
    print('Zipping it ...')
    shutil.make_archive(dir_name, 'zip', os.getcwd(), dir_name)

    if archive_type == 'cbz':
        os.rename(f'{dir_name}.zip', f'{dir_name}.cbz')


if __name__ == '__main__':
    downloadChapter()
