import unittest

from htmlnode import HTMLNode

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
        