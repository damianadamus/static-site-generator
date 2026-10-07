import unittest

from markdown import (
    extract_markdown_images,
    extract_markdown_links,
)


class TestMarkdown(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )

        self.assertListEqual(
            [
                (
                    "image",
                    "https://i.imgur.com/zjjcJKZ.png",
                )
            ],
            matches,
        )

    def test_extract_multiple_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with a "
            "![rick roll](https://i.imgur.com/aKaOqIh.gif) "
            "and "
            "![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )

        self.assertListEqual(
            [
                (
                    "rick roll",
                    "https://i.imgur.com/aKaOqIh.gif",
                ),
                (
                    "obi wan",
                    "https://i.imgur.com/fJRm4Vk.jpeg",
                ),
            ],
            matches,
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a "
            "[to boot dev](https://www.boot.dev)"
        )

        self.assertListEqual(
            [
                (
                    "to boot dev",
                    "https://www.boot.dev",
                )
            ],
            matches,
        )

    def test_extract_multiple_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link "
            "[to boot dev](https://www.boot.dev) "
            "and "
            "[to youtube](https://www.youtube.com/@bootdotdev)"
        )

        self.assertListEqual(
            [
                (
                    "to boot dev",
                    "https://www.boot.dev",
                ),
                (
                    "to youtube",
                    "https://www.youtube.com/@bootdotdev",
                ),
            ],
            matches,
        )

    def test_images_do_not_match_links(self):
        matches = extract_markdown_links(
            "Here is an ![image](https://example.com/image.png)"
        )

        self.assertListEqual([], matches)

    def test_links_do_not_match_images(self):
        matches = extract_markdown_images(
            "Here is a [link](https://example.com)"
        )

        self.assertListEqual([], matches)

    def test_no_images(self):
        matches = extract_markdown_images(
            "There are no images here."
        )

        self.assertListEqual([], matches)

    def test_no_links(self):
        matches = extract_markdown_links(
            "There are no links here."
        )

        self.assertListEqual([], matches)

    def test_empty_alt_text(self):
        matches = extract_markdown_images(
            "![](https://example.com/image.png)"
        )

        self.assertListEqual(
            [
                (
                    "",
                    "https://example.com/image.png",
                )
            ],
            matches,
        )

    def test_empty_link_text(self):
        matches = extract_markdown_links(
            "[](https://example.com)"
        )

        self.assertListEqual(
            [
                (
                    "",
                    "https://example.com",
                )
            ],
            matches,
        )


if __name__ == "__main__":
    unittest.main()