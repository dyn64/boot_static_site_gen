# herro wrod

from textnode import *
from copy_files import update_public_dir
from generate_page import generate_page
import logging
logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(filename='debug.log', level=logging.INFO)
    logger.info('-- start --')
    # src = "static"
    # if os.path.exists(src):
    #     content = os.listdir(src)
    #     print(content)
    #     for c in content:
    #         full_p = os.path.join(src, c)
    #         #print(full_p)
    #         if os.path.isdir(full_p):
    #             d = os.listdir(full_p)
    #             for e in d:
    #                 print(os.path.join(full_p, e))
    logger.info('running update_public_dir()')
    update_public_dir()
    logger.info('-- end --')
    generate_page('content/index.md', 'template.html', 'public/index.html')


if __name__ == "__main__":
    main()
