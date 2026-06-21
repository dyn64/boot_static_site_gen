import unittest
from textnode import TextNode, TextType

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



if __name__ == "__main__":
    unittest.main()