from textnode import *
from copy_files import update_public_dir
from generate_page import generate_page
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
    generate_page('content/index.md', 'template.html', 'public/index.html')
    generate_page('content/blog/glorfindel/index.md', 'template.html', 'public/blog/glorfindel/index.html')
    generate_page('content/blog/tom/index.md', 'template.html', 'public/blog/tom/index.html')
    generate_page('content/blog/majesty/index.md', 'template.html', 'public/blog/majesty/index.html')
    generate_page('content/contact/index.md', 'template.html', 'public/contact/index.html')


if __name__ == "__main__":
    main()
