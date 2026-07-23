from textnode import *
from copy_files import update_public_dir
from generate_page import generate_pages_recursive
import sys
import logging
logger = logging.getLogger(__name__)

source_dir = 'content'
dest_dir = 'docs'

def main():

    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path="/"

    logging.basicConfig(filename='debug.log', level=logging.INFO)
    logger.info('running update_public_dir()')
    update_public_dir(source_dir, dest_dir)

    logger.info('Generating pages')
#    generate_pages_recursive('content', 'template.html', 'public')
    generate_pages_recursive(f'{base_path}{source_dir}', f'{base_path}template.html', f'{base_path}{dest_dir}')
    logger.info('Done')

if __name__ == "__main__":
    main()
