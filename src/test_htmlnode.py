import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_1(self):
        props = {
            "href": "www.wubbalubba.com",
        }
        ref = ' href="www.wubbalubba.com"'
        node = HTMLNode(None,None,None, props)
        self.assertEqual(node.props_to_html(), ref)

    def test_props_2(self):
        props = {
            "href": "www.wubbalubba.com",
            "target": "_blank",
        }
        ref = ' href="www.wubbalubba.com" target="_blank"'
        node = HTMLNode(None,None,None, props)
        self.assertEqual(node.props_to_html(), ref)

    def test_props_3(self):
        props = {
            "href": "www.wubbalubba.com",
            "target": "_blank",
        }
        ref = ' href="www.wubbalubba.com" target="_blank"'
        node = HTMLNode("tag","val",None, props)
        self.assertEqual(node.props_to_html(), ref)

    def test_child(self):
        child = HTMLNode("child_tag", "child_val", None, None)
        node = HTMLNode("main_tag", "main_val", child, None)
        self.assertEqual(child, node.children)

    def test_repr(self):
        props = {
            "href": "www.wubbalubba.com",
            "target": "_blank",
        }
        node = HTMLNode("tag1", "val1", None, props)
        ref = f'tag: tag1, value: val1, children: None, props: {node.props_to_html()}'
        self.assertEqual(ref, repr(node))

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        props = {
            "href": "www.wubbalubba.com",
            "target": "_blank",
        }
        node = LeafNode("a","Link", props=props)
        self.assertEqual(
            node.to_html(),
             '<a href="www.wubbalubba.com" target="_blank">Link</a>'
             )

    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "No tags")
        self.assertEqual(node.to_html(), "No tags")

    def test_leaf_repr(self):
        props = {
            "href": "www.wubbalubba.com",
            "target": "_blank",
        }
        node = LeafNode("tag1", "val1", props)
        ref = f'tag: tag1, value: val1, props: {node.props_to_html()}'
        self.assertEqual(ref, repr(node))

if __name__ == '__main__':
    unittest.main()