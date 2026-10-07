import unittest

from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):

    def test_full_markdown(self):
        text = (
            "This is **text** with an _italic_ word "
            "and a `code block` and an "
            "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image",
                    TextType.IMAGE,
                    "https://i.imgur.com/fJRm4Vk.jpeg",
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode(
                    "link",
                    TextType.LINK,
                    "https://boot.dev",
                ),
            ],
        )

    def test_plain_text(self):
        text = "This is just normal text."

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            nodes,
            [
                TextNode(
                    "This is just normal text.",
                    TextType.TEXT,
                ),
            ],
        )

    def test_bold(self):
        text = "This is **bold** text."

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text.", TextType.TEXT),
            ],
        )

    def test_italic(self):
        text = "This is _italic_ text."

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text.", TextType.TEXT),
            ],
        )

    def test_code(self):
        text = "Run `python main.py` now."

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            nodes,
            [
                TextNode("Run ", TextType.TEXT),
                TextNode(
                    "python main.py",
                    TextType.CODE,
                ),
                TextNode(" now.", TextType.TEXT),
            ],
        )

    def test_link(self):
        text = "Visit [Boot.dev](https://boot.dev) today."

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            nodes,
            [
                TextNode("Visit ", TextType.TEXT),
                TextNode(
                    "Boot.dev",
                    TextType.LINK,
                    "https://boot.dev",
                ),
                TextNode(" today.", TextType.TEXT),
            ],
        )

    def test_image(self):
        text = (
            "Here is "
            "![a cat](https://example.com/cat.png)"
        )

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            nodes,
            [
                TextNode("Here is ", TextType.TEXT),
                TextNode(
                    "a cat",
                    TextType.IMAGE,
                    "https://example.com/cat.png",
                ),
            ],
        )

    def test_multiple_types(self):
        text = (
            "**bold** and _italic_ and `code` "
            "and [link](https://example.com) "
            "and ![image](https://example.com/image.png)"
        )

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            nodes,
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "link",
                    TextType.LINK,
                    "https://example.com",
                ),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://example.com/image.png",
                ),
            ],
        )

    def test_empty_text(self):
        nodes = text_to_textnodes("")

        self.assertListEqual(nodes, [])


if __name__ == "__main__":
    unittest.main()