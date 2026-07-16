from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    out_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            out_nodes.append(node)
            continue

    # checks for closing delimiter in input string.
    # (bitwise 'count & 1' is true if count is odd)
        if node.text.count(delimiter) & 1:
            raise ValueError("Uneven amount of delimiters in string")
        parts = node.text.split(delimiter)
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                out_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                out_nodes.append(TextNode(parts[i], text_type))

    return out_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    out_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            out_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if len(images) == 0:
            out_nodes.append(node)
            continue

        rawtext = node.text
        for img in images:
            text_bit = rawtext.split(f"![{img[0]}]({img[1]})", 1)
            if len(text_bit) != 2:
                raise ValueError("Error in markdown, image section not closed")
            if text_bit[0] != "":
                out_nodes.append(TextNode(text_bit[0], TextType.TEXT))

            out_nodes.append(
                TextNode(
                    img[0],
                    TextType.IMAGE,
                    img[1]))
            rawtext = text_bit[1]
        if rawtext != "":
            out_nodes.append(TextNode(rawtext, TextType.TEXT))
    return out_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    out_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            out_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if len(links) == 0:
            out_nodes.append(node)
            continue

        rawtext = node.text
        for link in links:
            text_bit = rawtext.split(f"[{link[0]}]({link[1]})", 1)
            if len(text_bit) != 2:
                raise ValueError("Error in markdown, link section not closed")
            if text_bit[0] != "":
                out_nodes.append(TextNode(text_bit[0], TextType.TEXT))

            out_nodes.append(
                TextNode(
                    link[0],
                    TextType.LINK,
                    link[1]))
            rawtext = text_bit[1]
        if rawtext != "":
            out_nodes.append(TextNode(rawtext, TextType.TEXT))
    return out_nodes

