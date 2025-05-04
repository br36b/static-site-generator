import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_node_attributes(self):
        simple_node = HTMLNode(value="normal text here", props={"aria-level": "0"})
        node = HTMLNode("p", "test paragraph", simple_node)

        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "test paragraph")

        self.assertIsNone(simple_node.children)
        self.assertEqual(simple_node.props, {"aria-level": "0"})

    def test_empty_node(self):
        empty_node = HTMLNode()

        self.assertIsNone(empty_node.tag)
        self.assertIsNone(empty_node.value)
        self.assertIsNone(empty_node.children)
        self.assertIsNone(empty_node.props)

    def test_children(self):
        child_node = HTMLNode(value="Test")
        parent_node = HTMLNode("div", "", child_node)

        self.assertEqual(parent_node.children, child_node)


if __name__ == "__main__":
    unittest.main()
