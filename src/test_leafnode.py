import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")

        self.assertEqual(
            node.to_html(),
            "<p>Hello, world!</p>"
        )

    def test_leaf_to_html_a(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"}
        )

        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "My heading")

        self.assertEqual(
            node.to_html(),
            "<h1>My heading</h1>"
        )

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "This is raw text.")

        self.assertEqual(
            node.to_html(),
            "This is raw text."
        )

    def test_leaf_to_html_with_multiple_props(self):
        node = LeafNode(
            "a",
            "Google",
            {
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )

        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com" target="_blank">Google</a>'
        )

    def test_leaf_to_html_without_value(self):
        node = LeafNode("p", None)

        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()