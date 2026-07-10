from textnode import TextNode, TextType

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
