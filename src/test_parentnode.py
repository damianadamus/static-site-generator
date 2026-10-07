import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("b", "Bold text")
        child2 = LeafNode(None, "Normal text")
        child3 = LeafNode("i", "Italic text")

        parent = ParentNode(
            "p",
            [child1, child2, child3]
        )

        self.assertEqual(
            parent.to_html(),
            "<p><b>Bold text</b>Normal text<i>Italic text</i></p>"
        )

    def test_to_html_with_props(self):
        child = LeafNode("span", "Hello")

        parent = ParentNode(
            "div",
            [child],
            {"class": "container", "id": "main"}
        )

        self.assertEqual(
            parent.to_html(),
            '<div class="container" id="main"><span>Hello</span></div>'
        )

    def test_to_html_with_no_children(self):
        parent = ParentNode("div", [])

        self.assertEqual(
            parent.to_html(),
            "<div></div>"
        )

    def test_to_html_without_tag(self):
        parent = ParentNode(None, [])

        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_without_children(self):
        parent = ParentNode("div", None)

        with self.assertRaises(ValueError):
            parent.to_html()


if __name__ == "__main__":
    unittest.main()