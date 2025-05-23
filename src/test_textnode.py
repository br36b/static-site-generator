import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node that does not match", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_empty_url(self):
        node = TextNode("This is a text node", TextType.NORMAL)

        self.assertIsNone(node.url)


if __name__ == "__main__":
    unittest.main()
