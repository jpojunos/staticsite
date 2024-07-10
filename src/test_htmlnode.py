import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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
        self.assertEqual(
            node.props_to_html(), ' href="https://www.example.com" target="_blank"'
        )

    def test_repr(self):
        # Test the __repr__ method
        children = [HTMLNode(tag="p"), HTMLNode(tag="a")]
        props = {"class": "main"}
        node = HTMLNode(tag="div", value="Test content", children=children, props=props)
        expected_repr = (
            "Tag: div\n"
            "Value: Test content\n"
            "Children: 2\n"
            "Props: {'class': 'main'}"
        )
        self.assertEqual(repr(node), expected_repr)


class TestLeafNode(unittest.TestCase):
    def test_initialization_without_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode()  # No value provided

    def test_initialization_with_value(self):
        leaf = LeafNode(tag="p", value="This is a paragraph.")
        self.assertEqual(leaf.value, "This is a paragraph.")
        self.assertEqual(leaf.tag, "p")

    def test_to_html_without_tag(self):
        leaf = LeafNode(value="Just text")
        self.assertEqual(leaf.to_html(), "Just text")

    def test_to_html_with_tag_no_props(self):
        leaf = LeafNode(tag="p", value="This is a paragraph.")
        self.assertEqual(leaf.to_html(), "<p>This is a paragraph.</p>")

    def test_to_html_with_tag_and_props(self):
        leaf = LeafNode(
            tag="a", value="Click me!", props={"href": "https://www.google.com"}
        )
        self.assertEqual(
            leaf.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )


class TestLeafNodeAdditional(unittest.TestCase):
    def test_long_value(self):
        long_value = "a" * 1000  # Very long string
        leaf = LeafNode(tag="p", value=long_value)
        self.assertEqual(leaf.to_html(), f"<p>{long_value}</p>")

    def test_special_characters_in_value(self):
        special_value = "Text with <special> characters & more"
        leaf = LeafNode(tag="p", value=special_value)
        self.assertEqual(leaf.to_html(), f"<p>{special_value}</p>")

    def test_empty_string_value(self):
        leaf = LeafNode(tag="p", value="")
        self.assertEqual(leaf.to_html(), "<p></p>")

    def test_special_characters_in_props(self):
        props = {"title": "Title with \"double\" and 'single' quotes"}
        leaf = LeafNode(tag="div", value="Content", props=props)
        expected_html = '<div title="Title with &quot;double&quot; and &#x27;single&#x27; quotes">Content</div>'
        self.assertEqual(leaf.to_html(), expected_html)

    def test_tag_with_special_character(self):
        leaf = LeafNode(tag="my-tag", value="special tag")
        self.assertEqual(leaf.to_html(), "<my-tag>special tag</my-tag>")


class TestParentNode(unittest.TestCase):
    def setUp(self):
        self.leaf1 = LeafNode("b", "Bold text")
        self.leaf2 = LeafNode(None, "Normal text")
        self.leaf3 = LeafNode("i", "italic text")
        self.leaf4 = LeafNode(None, "Normal text")

    def test_single_level(self):
        node = ParentNode("p", [self.leaf1, self.leaf2, self.leaf3, self.leaf4])
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_nested(self):
        nested_child = ParentNode("div", [self.leaf1, self.leaf2])
        node = ParentNode("section", [nested_child, self.leaf3])
        self.assertEqual(
            node.to_html(),
            "<section><div><b>Bold text</b>Normal text</div><i>italic text</i></section>",
        )

    def test_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [self.leaf1, self.leaf2])
            node.to_html()

    def test_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div")


if __name__ == "__main__":
    unittest.main()
