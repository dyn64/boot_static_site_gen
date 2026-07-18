import unittest
from markdown_to_html import markdown_to_html_node, text_to_basenode
from htmlnode import HTMLNode
from blocktype import BlockType

class Test_TextToBasenode(unittest.TestCase):
    def test_paragraph(self):
        text = "bare en paragraff"
        self.assertEqual("p", (text_to_basenode(text, BlockType.PARAGRAPH)).tag)

    def test_paragraph(self):
        text = "bare en para\ngraff"
        self.assertEqual("bare en para graff", (text_to_basenode(text, BlockType.PARAGRAPH)).value)

    def test_heading1(self):
        text = "# Heading1"
        node = text_to_basenode(text, BlockType.HEADING)
        self.assertEqual("h1", node.tag)
        self.assertEqual("Heading1", node.value)

    def test_heading6(self):
        text = "###### Heading 6"
        node = text_to_basenode(text, BlockType.HEADING)
        self.assertEqual("h6", node.tag)
        self.assertEqual("Heading 6", node.value)

    def test_quote(self):
        text = "> quote line 1\n>quote line 2"
        correct_response = " quote line 1\nquote line 2"
        node = text_to_basenode(text, BlockType.QUOTE)
        self.assertEqual("blockquote", node.tag)
        self.assertEqual(correct_response, node.value)

    def test_unordered_list(self):
        text = "- line 1\n- line 2\n- line 3"
        node = text_to_basenode(text, BlockType.UNORDERED_LIST)
        self.assertEqual("ul", node.tag)

    def test_unordered_list_children(self):
        text = "- line 1\n- line 2\n- line 3"
        node = text_to_basenode(text, BlockType.UNORDERED_LIST)
        self.assertEqual("line 1", node.children[0].value)
        self.assertEqual("li", node.children[2].tag)

    def test_ordered_list(self):
        text = "1. line 1\n2. line 2\n3. line 3"
        node = text_to_basenode(text, BlockType.ORDERED_LIST)
        self.assertEqual("ol", node.tag)

    def test_ordered_list_children(self):
        text = "1. line 1\n2. line 2\n3. line 3"
        node = text_to_basenode(text, BlockType.ORDERED_LIST)
        self.assertEqual("line 1", node.children[0].value)
        self.assertEqual("li", node.children[2].tag)

    def test_code_block(self):
        text = """
```
this be code
this too
```
"""
        node = text_to_basenode(text, BlockType.CODE)
        self.assertEqual("pre", node.tag)

    def test_code_block2(self):
        text = """```
this be code
this too
```"""
        node = text_to_basenode(text, BlockType.CODE)
        self.assertEqual("code", node.children[0].tag)
        self.assertEqual("this be code\nthis too", node.children[0].value)

class Test_MarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )    

if __name__ == "__main__":
    unittest.main()