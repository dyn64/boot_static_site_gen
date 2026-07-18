from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from blocktype import block_to_blocktype, BlockType, rBlockType
from markdown_to_blocks import markdown_to_blocks

import re

def markdown_to_html_node(text: str) -> ParentNode:
    markdown_blocks = markdown_to_blocks(text)
    html_nodes = []

    for block in markdown_blocks:
        block_type = block_to_blocktype(block)
        html_nodes.append(text_to_basenode(block, block_type))

    main_node = ParentNode("div", html_nodes)
    return main_node

def text_to_basenode(text: str, type: BlockType) -> HTMLNode:
    match type:
        case BlockType.PARAGRAPH:
            text = text.replace("\n", " ")
            return HTMLNode("p", text)
        case BlockType.HEADING:
            # splits the text into #+ and heading text
            head = re.match(re.compile(rBlockType[BlockType.HEADING]), text)
            splat = text.split(head.group(0), 1)
            # counts the number of # to determine the heading size
            size = len(head.group(0)) - 1
            return HTMLNode(f"h{size}",splat[-1])
        case BlockType.CODE:
            #raw_codeblock = re.sub(r'```\n', '', text)
            #raw_codeblock = re.sub(r'\n```', '', raw_codeblock)
            raw_codeblock = text.replace('```\n', '')
            raw_codeblock = raw_codeblock.replace('\n```', '')
            children = [LeafNode("code",raw_codeblock)]
            codeblock = HTMLNode("pre", children=children)
            return codeblock
        case BlockType.QUOTE:
            # gets rid of the first >
            tekst = text.split(">", 1)
            # removes the rest of the > while keeping newlines
            tekst = tekst[1].replace("\n>", "\n")
            return HTMLNode("blockquote", tekst)
        case BlockType.UNORDERED_LIST:
            pattern = re.compile(r'^- ', re.MULTILINE)
            block = pattern.sub("", text)
            lines = block.split("\n")
            child_nodes = []
            ListNode = HTMLNode("ul", children=child_nodes)
            for line in lines:
                child_nodes.append(HTMLNode("li", line))
            return ListNode
        case BlockType.ORDERED_LIST:
            pattern = re.compile(r'^\d. ', re.MULTILINE)
            block = pattern.sub("", text)
            lines = block.split("\n")
            child_nodes = []
            ListNode = HTMLNode("ol", children=child_nodes)
            for line in lines:
                child_nodes.append(HTMLNode("li", line))
            return ListNode
        case _:
            raise ValueError("Error - text_to_basenode(): wrong blocktype")
        
    pass