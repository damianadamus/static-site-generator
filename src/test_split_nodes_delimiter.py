import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_code(self):
        node = TextNode(
            "This is text with a `code block` word",
            TextType.TEXT,
        )

        new_nodes = split_nodes_delimiter(
            [node],
            "`",
            TextType.CODE,
        )

        self.assertEqual(
            new_nodes,
            [
                TextNode(
                    "This is text with a ",
                    TextType.TEXT,
                ),
                TextNode(
                    "code block",
                    TextType.CODE,
                ),
                TextNode(
                    " word",
                    TextType.TEXT,
                ),
            ],
        )

    def test_bold(self):
        node = TextNode(
            "This is **bold text** here",
            TextType.TEXT,
        )

        new_nodes = split_nodes_delimiter(
            [node],
            "**",
            TextType.BOLD,
        )

        self.assertEqual(
            new_nodes,
            [
                TextNode(
                    "This is ",
                    TextType.TEXT,
                ),
                TextNode(
                    "bold text",
                    TextType.BOLD,
                ),
                TextNode(
                    " here",
                    TextType.TEXT,
                ),
            ],
        )

    def test_italic(self):
        node = TextNode(
            "This is _italic text_ here",
            TextType.TEXT,
        )

        new_nodes = split_nodes_delimiter(
            [node],
            "_",
            TextType.ITALIC,
        )

        self.assertEqual(
            new_nodes,
            [
                TextNode(
                    "This is ",
                    TextType.TEXT,
                ),
                TextNode(
                    "italic text",
                    TextType.ITALIC,
                ),
                TextNode(
                    " here",
                    TextType.TEXT,
                ),
            ],
        )

    def test_multiple_delimiters(self):
        node = TextNode(
            "This is `code` and **bold** text",
            TextType.TEXT,
        )

        code_nodes = split_nodes_delimiter(
            [node],
            "`",
            TextType.CODE,
        )

        result = split_nodes_delimiter(
            code_nodes,
            "**",
            TextType.BOLD,
        )

        self.assertEqual(
            result,
            [
                TextNode(
                    "This is ",
                    TextType.TEXT,
                ),
                TextNode(
                    "code",
                    TextType.CODE,
                ),
                TextNode(
                    " and ",
                    TextType.TEXT,
                ),
                TextNode(
                    "bold",
                    TextType.BOLD,
                ),
                TextNode(
                    " text",
                    TextType.TEXT,
                ),
            ],
        )

    def test_no_delimiter(self):
        node = TextNode(
            "This is normal text",
            TextType.TEXT,
        )

        new_nodes = split_nodes_delimiter(
            [node],
            "`",
            TextType.CODE,
        )

        self.assertEqual(
            new_nodes,
            [
                TextNode(
                    "This is normal text",
                    TextType.TEXT,
                ),
            ],
        )

    def test_unclosed_delimiter(self):
        node = TextNode(
            "This is `unclosed code",
            TextType.TEXT,
        )

        with self.assertRaises(ValueError):
            split_nodes_delimiter(
                [node],
                "`",
                TextType.CODE,
            )

    def test_non_text_node(self):
        node = TextNode(
            "already bold",
            TextType.BOLD,
        )

        new_nodes = split_nodes_delimiter(
            [node],
            "`",
            TextType.CODE,
        )

        self.assertEqual(
            new_nodes,
            [node],
        )

    def test_empty_sections(self):
        node = TextNode(
            "before``after",
            TextType.TEXT,
        )

        new_nodes = split_nodes_delimiter(
            [node],
            "`",
            TextType.CODE,
        )

        self.assertEqual(
            new_nodes,
            [
                TextNode("before", TextType.TEXT),
                TextNode("after", TextType.TEXT),
            ],
        )


if __name__ == "__main__":
    unittest.main()