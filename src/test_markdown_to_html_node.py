import unittest
from markdown_to_html_node import parse_nodes
from htmlnode import HTMLNode, ParentNode, LeafNode

class Test_Markdown_to_html_node(unittest.TestCase):
    def test_heading1(self):
        text = "### Heading 3"
        node = parse_nodes(text)
        html = "<div><h3>Heading 3</h3></div>"
        self.assertEqual(html, node.to_html())

    def test_quote(self)        :
        text = """
> kvote 1
> q 2"""
        node = parse_nodes(text)
        html = "<div><blockquote>kvote 1\nq 2</blockquote></div>"
        self.assertEqual(html, node.to_html())

    def test_ulist(self):
        text = """
- list 1
- list 2
"""
        html = "<div><ul><li>list 1</li><li>list 2</li></ul></div>"
        node = parse_nodes(text)
        self.assertEqual(html, node.to_html())

    def test_olist(self):
        text = """
1. list 1
2. list 2
"""
        html = "<div><ol><li>list 1</li><li>list 2</li></ol></div>"
        node = parse_nodes(text)
        self.assertEqual(html, node.to_html())

    def test_paragraph(self):
        text = "blabla, bare en paragraf\nmed flere linjer?"
        node = parse_nodes(text)
        html = "<div><p>blabla, bare en paragraf med flere linjer?</p></div>"
        self.assertEqual(html, node.to_html())

    def test_codeblock(self):
        md = """
```
    This is text that _should_ remain
    the **same** even with inline stuff
```
"""

        node = parse_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = parse_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
if __name__ == "__main__":
    unittest.main()