import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
 
    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child 1")
        child_node2 = LeafNode("span", "child 2")
        child_node3 = LeafNode("span", "child 3")
        parent_node = ParentNode("div", [child_node1,child_node2,child_node3])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child 1</span><span>child 2</span><span>child 3</span></div>")
 
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )

    def test_to_html_with_nested_grandchildren(self):
        grandchild_node1 = LeafNode("b", "grandchild_node1")
        grandchild_node2 = LeafNode("i", "grandchild_node2")
        child_node1 = ParentNode("span", [grandchild_node1])
        child_node2 = ParentNode("span", [grandchild_node2])
        parent_node = ParentNode("div", [child_node1,child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild_node1</b></span><span><i>grandchild_node2</i></span></div>",
    )

if __name__ == '__main__':
    unittest.main()