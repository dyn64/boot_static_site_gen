from markdown_to_html_node import parse_nodes
from extract_markdown import extract_title
import re, os
import logging
logger = logging.getLogger(__name__)

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    
    with open(from_path) as file:
        markdown_file = file.read()
        file.close()

    with open(template_path) as file:
        template_file = file.read()
        file.close()

    title = extract_title(markdown_file)

    main_html_node = parse_nodes(markdown_file).to_html()

    new_file = template_file.replace('{{ Title }}', title)
    new_file = new_file.replace('{{ Content }}', main_html_node)

    dirs = dest_path.split(dest_path.split('/')[-1])[0]
    os.makedirs(dirs,exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(new_file)
        file.close()

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    if os.path.isfile(dir_path_content):
        new_dest = dest_dir_path.replace('.md', '.html')
        logger.info(f'generating file: "{new_dest}" from: "{dir_path_content}"')
        generate_page(dir_path_content, template_path, new_dest)
    else:
        content = os.listdir(dir_path_content)
        logger.info(f'"{dir_path_content}" is a directory. Parsing')
        for c in content:
            new_src  = os.path.join(dir_path_content, c)
            new_dest = os.path.join(dest_dir_path, c)
            logger.info(f'Calling recursive function')
            logger.info(f'Source: "{new_src}" - Dest: "{new_dest}"')
            generate_pages_recursive(new_src, template_path, new_dest)
