import unittest

from split_nodes_image_link import (
    split_nodes_image,
    split_nodes_link,
)
from textnode import TextNode, TextType


class TestSplitNodesImageLink(unittest.TestCase):

    # ==========================================
    # IMAGE TESTS
    # ==========================================

    def test_split_images(self):
        node = TextNode(
            "This is text with an "
            "![image](https://i.imgur.com/zjjcJKZ.png)"
            " and another "
            "![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode(
                    "This is text with an ",
                    TextType.TEXT,
                ),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://i.imgur.com/zjjcJKZ.png",
                ),
                TextNode(
                    " and another ",
                    TextType.TEXT,
                ),
                TextNode(
                    "second image",
                    TextType.IMAGE,
                    "https://i.imgur.com/3elNhQu.png",
                ),
            ],
            new_nodes,
        )

    def test_split_single_image(self):
        node = TextNode(
            "Before ![cat](https://example.com/cat.png) after",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("Before ", TextType.TEXT),
                TextNode(
                    "cat",
                    TextType.IMAGE,
                    "https://example.com/cat.png",
                ),
                TextNode(" after", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_image_at_start(self):
        node = TextNode(
            "![cat](https://example.com/cat.png) after",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode(
                    "cat",
                    TextType.IMAGE,
                    "https://example.com/cat.png",
                ),
                TextNode(" after", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_image_at_end(self):
        node = TextNode(
            "Before ![cat](https://example.com/cat.png)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("Before ", TextType.TEXT),
                TextNode(
                    "cat",
                    TextType.IMAGE,
                    "https://example.com/cat.png",
                ),
            ],
            new_nodes,
        )

    def test_only_image(self):
        node = TextNode(
            "![cat](https://example.com/cat.png)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode(
                    "cat",
                    TextType.IMAGE,
                    "https://example.com/cat.png",
                ),
            ],
            new_nodes,
        )

    def test_no_images(self):
        node = TextNode(
            "This is just normal text.",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [node],
            new_nodes,
        )

    def test_non_text_node_with_image(self):
        node = TextNode(
            "already an image",
            TextType.IMAGE,
            "https://example.com/image.png",
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [node],
            new_nodes,
        )

    # ==========================================
    # LINK TESTS
    # ==========================================

    def test_split_links(self):
        node = TextNode(
            "This is text with a link "
            "[to boot dev](https://www.boot.dev)"
            " and "
            "[to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode(
                    "This is text with a link ",
                    TextType.TEXT,
                ),
                TextNode(
                    "to boot dev",
                    TextType.LINK,
                    "https://www.boot.dev",
                ),
                TextNode(
                    " and ",
                    TextType.TEXT,
                ),
                TextNode(
                    "to youtube",
                    TextType.LINK,
                    "https://www.youtube.com/@bootdotdev",
                ),
            ],
            new_nodes,
        )

    def test_split_single_link(self):
        node = TextNode(
            "Before [Google](https://google.com) after",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("Before ", TextType.TEXT),
                TextNode(
                    "Google",
                    TextType.LINK,
                    "https://google.com",
                ),
                TextNode(" after", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_link_at_start(self):
        node = TextNode(
            "[Google](https://google.com) after",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode(
                    "Google",
                    TextType.LINK,
                    "https://google.com",
                ),
                TextNode(" after", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_link_at_end(self):
        node = TextNode(
            "Before [Google](https://google.com)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("Before ", TextType.TEXT),
                TextNode(
                    "Google",
                    TextType.LINK,
                    "https://google.com",
                ),
            ],
            new_nodes,
        )

    def test_only_link(self):
        node = TextNode(
            "[Google](https://google.com)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode(
                    "Google",
                    TextType.LINK,
                    "https://google.com",
                ),
            ],
            new_nodes,
        )

    def test_no_links(self):
        node = TextNode(
            "This is just normal text.",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [node],
            new_nodes,
        )

    def test_non_text_node_with_link(self):
        node = TextNode(
            "already a link",
            TextType.LINK,
            "https://example.com",
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [node],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()