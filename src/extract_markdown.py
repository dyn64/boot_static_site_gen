import re

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_title(markdown: str, strip_title=False) -> str:
    h1_pattern = re.compile(r'^# ', re.MULTILINE)
    h1 = re.match(h1_pattern, markdown)
    if h1 == None:
        raise ValueError("No header found")
    #title1 = markdown.split(h1.group(0))[1]
    title1 = (markdown.split(h1.group(0))[1]).split("\n",1)
    if strip_title:
        #title = (markdown.split(h1.group(0))[0]).split("\n",1)[1]
        #title = markdown.split("\n",1)[1]
        title = title1[1]
    else:
        title = title1[0]

    #title = (markdown.split(h1.group(0))[1]).split("\n",1)[0]
    #title.strip()
    return title
