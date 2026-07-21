import os
import shutil
import logging
logger = logging.getLogger(__name__)

def update_public_dir() -> None:
    source_dir = "static"
    destination_dir = "public"
    if not os.path.exists(source_dir):
        raise NotADirectoryError(f"{source_dir} not found")
    
#    dest_content = os.listdir(destination_dir)
    if os.path.exists(destination_dir):
        logger.info(f' "{destination_dir}" found, removing..')
        shutil.rmtree(destination_dir)
    logger.info(f'mkdir "{destination_dir}"')
    os.mkdir(destination_dir)

    copy_tree(source_dir, destination_dir)

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