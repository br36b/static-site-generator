import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_strong(self):
        node = LeafNode("strong", "IMPORTANT")
        self.assertEqual(node.to_html(), "<strong>IMPORTANT</strong>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Title")
        self.assertEqual(node.to_html(), "<h1>Title</h1>")


if __name__ == "__main__":
    unittest.main()
