from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from blocktype import block_to_blocktype, BlockType, rBlockType
from markdown_to_blocks import markdown_to_blocks
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from text_to_textnode import text_to_textnode
import re

def parse_nodes(text: str) -> ParentNode:
    out_htmlnodes = []
    markdown_blocks = markdown_to_blocks(text)

    for block in markdown_blocks:
        block_type = block_to_blocktype(block)
        match block_type:
            case BlockType.CODE:
                #block = block.replace('```\n', '')
                #block = block.replace('\n```', '')
                bloks = block.split("```\n", 1)
                blok = bloks[1].split("```", 1)
                out_htmlnodes.append(
                    ParentNode("pre",
                               [text_node_to_html_node(
                                   TextNode(blok[0],TextType.CODE)
                                   )]
                                )
                )
            case BlockType.HEADING:
                head = re.match(re.compile(rBlockType[BlockType.HEADING]), block)
                heads = block.split(head.group(0), 1)
                heading_size = len(head.group(0)) -1
                out_htmlnodes.append(
                    LeafNode(f"h{heading_size}", heads[-1])
                )
            case BlockType.QUOTE:
                # make htmlnode with tag blockquote
                # check for children
                quote = block.split(">", 1)
                quote = quote[1].replace("\n>", "\n")
                children = parse_children(quote)
                out_htmlnodes.append(ParentNode("blockquote", children))
            case BlockType.UNORDERED_LIST:
                # make parent node with tag ul
                # nodes with tag li
                # check for children
                pattern = re.compile(r'^- ', re.MULTILINE)
                block = pattern.sub("", block)
                lines = block.split("\n")
                ulist_nodes = []
                for line in lines:
                    ulist_nodes.append(ParentNode("li",parse_children(line)))
                out_htmlnodes.append(ParentNode("ul",ulist_nodes))
            case BlockType.ORDERED_LIST:
                # parent node with tag ol
                # nodes with tag li
                # check for children
                pattern = re.compile(r'^\d. ', re.MULTILINE)
                block = pattern.sub("", block)
                lines = block.split("\n")
                list_nodes = []
                for line in lines:
                    list_nodes.append(ParentNode("li",parse_children(line)))
                out_htmlnodes.append(ParentNode("ol",list_nodes))
            case BlockType.PARAGRAPH:
                # node with tag p
                # check for children
                block = block.replace("\n", " ")
                out_htmlnodes.append(ParentNode("p", parse_children(block)))
    return ParentNode("div", out_htmlnodes)


def parse_children(text: str) -> HTMLNode:
    # go through all the split_nodes
    # bold, italic, code?, link, image, (text)
    # 
    out_nodes = []
    nods = text_to_textnode(text)

#    for node in nodes:
#        nods.append(text_to_textnode(node.text))
    
    for nod in nods:
        out_nodes.append(text_node_to_html_node(nod))
        
    return out_nodes
