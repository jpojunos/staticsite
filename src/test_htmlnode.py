import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_constructor_defaults(self):
        # Test instantiating HTMLNode with default values
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_constructor_with_values(self):
        # Test instantiating HTMLNode with specific values
        children = [HTMLNode(tag="p"), HTMLNode(tag="a")]
        props = {"class": "main"}
        node = HTMLNode(tag="div", value="Test content", children=children, props=props)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Test content")
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, props)

    def test_props_to_html(self):
        # Test the props_to_html method
        props = {"href": "https://www.example.com", "target": "_blank"}
        node = HTMLNode(tag="a", props=props)
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com" target="_blank"')

    def test_repr(self):
        # Test the __repr__ method
        children = [HTMLNode(tag="p"), HTMLNode(tag="a")]
        props = {"class": "main"}
        node = HTMLNode(tag="div", value="Test content", children=children, props=props)
        expected_repr = ("Tag: div\n"
                         "Value: Test content\n"
                         "Children: 2\n"
                         "Props: {'class': 'main'}")
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()