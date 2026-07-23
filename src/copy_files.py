import os
import shutil
import logging
logger = logging.getLogger(__name__)

def update_public_dir(source_dir: str, dest_dir: str) -> None:
    if not os.path.exists(source_dir):
        raise NotADirectoryError(f"{source_dir} not found")
    
    if os.path.exists(dest_dir):
        logger.info(f' "{dest_dir}" found, removing..')
        shutil.rmtree(dest_dir)
    logger.info(f'mkdir "{dest_dir}"')
    os.mkdir(dest_dir)

    copy_tree(source_dir, dest_dir)

def copy_tree(src: str, dest: str) -> None:
    if not os.path.isdir(src) or not os.path.isdir(dest):
        logger.error(f'{src} and {dest} are not both directories')

    for item in os.listdir(src):
        if os.path.isdir(os.path.join(src, item)):
            new_target_dir = os.path.join(dest, item)
            try:
                os.mkdir(new_target_dir)
            except:
                logger.error(f'"{new_target_dir}" already exists')
            new_src = os.path.join(src, item)
            copy_tree(new_src, new_target_dir)
        else:
            source_file = os.path.join(src, item)
            target_file = os.path.join(dest, item)
            shutil.copy(source_file, target_file)