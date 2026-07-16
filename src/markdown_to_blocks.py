import re
from textnode import TextNode

def markdown_to_blocks(text: str) -> list[str]:
    if len(text) == 0:
        return [""]
    
    blocks = text.split('\n\n')
    output = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        block = re.sub(r'\n\s+', '\n', block)
        output.append(block)

    return output