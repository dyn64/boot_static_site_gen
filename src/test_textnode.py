import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("Testnode 1", TextType.BOLD)
        node2 = TextNode("Testnode 2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_noteq_type(self):
        node = TextNode("Testnode", TextType.BOLD)
        node2 = TextNode("Testnode", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_urlequal(self):
        node = TextNode("Testnode 1", TextType.BOLD, "www.ingensteder.net")
        node2 = TextNode("Testnode 1", TextType.BOLD, "www.ingensteder.net")
        self.assertEqual(node, node2)

    def test_nourl(self):
        node = TextNode("Testnode 1", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_repr(self):
        node = TextNode("Testnode 1", TextType.BOLD, "www.ingensteder.net")
        self.assertEqual(
            "TextNode(Testnode 1, bold, www.ingensteder.net)",repr(node)
        )

class TextTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold text")

    def test_italic(self):
        node = TextNode("italian text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "italian text")

    def test_code(self):
        node = TextNode("matrix text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "matrix text")

    def test_link(self):
        node = TextNode("click", TextType.LINK, "www.ulv.no")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "click")
        self.assertEqual(html_node.props, {"href": "www.ulv.no"})

    def test_image(self):
        node = TextNode("icon", TextType.IMAGE, "/img/icon.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "/img/icon.png", "alt": "icon"})

if __name__ == "__main__":
    unittest.main()