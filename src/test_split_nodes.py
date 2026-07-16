import unittest
from split_nodes import split_nodes_delimiter,split_nodes_link,split_nodes_image, text_to_textnode, markdown_to_blocks
from textnode import TextNode, TextType

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_text(self):
        test_node = [
                  TextNode("this is just text",TextType.TEXT),
                  TextNode("Also just text", TextType.TEXT)
                  ]
        split_node = split_nodes_delimiter(test_node, "**", TextType.BOLD)
        self.assertListEqual(test_node, split_node)

    def test_bold(self):
        test_node = [
                  TextNode("this is **bold** text",TextType.TEXT),
                  TextNode("just text", TextType.TEXT)
                  ]
        split_node = split_nodes_delimiter(test_node, "**", TextType.BOLD)
        correct_node = [
                  TextNode("this is ",TextType.TEXT),
                  TextNode("bold",TextType.BOLD),
                  TextNode(" text",TextType.TEXT),
                  TextNode("just text", TextType.TEXT)
                  ]
        self.assertListEqual(split_node, correct_node)

    def test_bold_twice(self):
        test_node = [
                  TextNode("**this** is **bold** text",TextType.TEXT)
                  ]
        split_node = split_nodes_delimiter(test_node, "**", TextType.BOLD)
        correct_node = [
                  TextNode("this",TextType.BOLD),
                  TextNode(" is ",TextType.TEXT),
                  TextNode("bold",TextType.BOLD),
                  TextNode(" text",TextType.TEXT)
                  ]
        self.assertListEqual(split_node, correct_node)

    def test_bold_multi(self):
        test_node = [
                  TextNode("this is **bold text**",TextType.TEXT)
                  ]
        split_node = split_nodes_delimiter(test_node, "**", TextType.BOLD)
        correct_node = [
                  TextNode("this is ",TextType.TEXT),
                  TextNode("bold text",TextType.BOLD)
                  ]
        self.assertListEqual(split_node, correct_node)

    def test_italic(self):
        test_node = [
                  TextNode("this is _italic_ text",TextType.TEXT),
                  TextNode("just text", TextType.TEXT)
                  ]
        split_node = split_nodes_delimiter(test_node, "_", TextType.ITALIC)
        correct_node = [
                  TextNode("this is ",TextType.TEXT),
                  TextNode("italic",TextType.ITALIC),
                  TextNode(" text",TextType.TEXT),
                  TextNode("just text", TextType.TEXT)
                  ]
        self.assertListEqual(split_node, correct_node)

    def test_bold_italic(self):
        test_node = [
                  TextNode("**bold** and _italic_ text",TextType.TEXT)
                  ]
        split_node = split_nodes_delimiter(test_node, "_", TextType.ITALIC)
        split_node = split_nodes_delimiter(split_node, "**", TextType.BOLD)
        correct_node = [
                  TextNode("bold",TextType.BOLD),
                  TextNode(" and ", TextType.TEXT),
                  TextNode("italic",TextType.ITALIC),
                  TextNode(" text",TextType.TEXT)
                  ]
        self.assertListEqual(split_node, correct_node)

    def test_code(self):
        test_node = [
                  TextNode("this is `code` text",TextType.TEXT),
                  TextNode("just text", TextType.TEXT)
                  ]
        split_node = split_nodes_delimiter(test_node, "`", TextType.CODE)
        correct_node = [
                  TextNode("this is ",TextType.TEXT),
                  TextNode("code",TextType.CODE),
                  TextNode(" text",TextType.TEXT),
                  TextNode("just text", TextType.TEXT)
                  ]
        self.assertListEqual(split_node, correct_node)

class TestSplitNodeImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

class TestSplitNodeLink(unittest.TestCase):
    def test_split_link(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

class TestTexttoTextnodes(unittest.TestCase):
    def test_all(self):
        in_string = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        correct_output = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(correct_output, text_to_textnode(in_string))

class TestMarkdownToBlocks(unittest.TestCase):
    def test_base(self):
        text = """
This is **bold**    

This is _italic_ and `code`.


    - list item 1
    - list item 2
"""
        correct_response = [
            "This is **bold**",
            "This is _italic_ and `code`.",
            "- list item 1\n- list item 2",
        ]
        self.assertEqual(correct_response, markdown_to_blocks(text))

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line





- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

if __name__ == "__main__":
    unittest.main()