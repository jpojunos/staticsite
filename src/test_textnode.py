import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", None, None)
        node2 = TextNode("This is a text node", None, None)

        node3 = TextNode("This is a text node", "bold",None)
        node4 = TextNode("This is a text node", "bold",None)
         
        node7 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node8 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        
        node9 = TextNode(None, None, url="https://www.boot.dev")
        node10 = TextNode(None, None, url="https://www.boot.dev")
        
        node11 = TextNode(None, text_type="bold", url="https://www.boot.dev")
        node12 = TextNode(None, text_type="bold", url="https://www.boot.dev")

        node5 = TextNode(None, text_type="bold", url=None)
        node6 = TextNode(None, text_type="bold", url=None)
        
        self.assertEqual(node1, node2)
        self.assertEqual(node3, node4)
        self.assertEqual(node5, node6)
        self.assertEqual(node7, node8)
        self.assertEqual(node9, node10)
        self.assertEqual(node11, node12)


if __name__ == "__main__":
    unittest.main()
 