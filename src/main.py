from textnode import *
from copy_files import update_public_dir
from generate_page import generate_pages_recursive
import os
import logging
logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(filename='debug.log', level=logging.INFO)
    logger.info('-- start --')
    logger.info('running update_public_dir()')
    update_public_dir()
    logger.info('-- end --')

    logger.info('Generating pages')
    generate_pages_recursive('content', 'template.html', 'public')
    logger.info('Done')
    
if __name__ == "__main__":
    main()
