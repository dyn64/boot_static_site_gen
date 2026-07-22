from markdown_to_html_node import parse_nodes
from extract_markdown import extract_title
import re, os

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    
    with open(from_path) as file:
        markdown_file = file.read()
        file.close()

    with open(template_path) as file:
        template_file = file.read()
        file.close()

    title = extract_title(markdown_file)

    markdown_notitle = extract_title(markdown_file, strip_title=True)

    main_html_node = parse_nodes(markdown_file).to_html()

    new_file = template_file.replace('{{ Title }}', title)
    new_file = new_file.replace('{{ Content }}', main_html_node)

    dirs = re.sub(re.compile(r'/\w+\..{3}$'),"", dest_path)
    #os.makedirs(dirs)

    with open(dest_path, "w") as file:
        file.write(new_file)
        file.close()

