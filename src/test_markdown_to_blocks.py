import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\n"
                "This is the same paragraph on a new line",
                "- This is a list\n"
                "- with items",
            ],
        )

    def test_single_block(self):
        md = "This is a single paragraph."

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is a single paragraph.",
            ],
        )

    def test_multiple_blocks(self):
        md = """First paragraph.

Second paragraph.

Third paragraph."""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "First paragraph.",
                "Second paragraph.",
                "Third paragraph.",
            ],
        )

    def test_extra_newlines(self):
        md = """


First paragraph.


Second paragraph.



Third paragraph.


"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "First paragraph.",
                "Second paragraph.",
                "Third paragraph.",
            ],
        )

    def test_leading_and_trailing_whitespace(self):
        md = """

   First paragraph with spaces   

   Second paragraph with spaces   

"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "First paragraph with spaces",
                "Second paragraph with spaces",
            ],
        )

    def test_multiline_block(self):
        md = """This is a paragraph
that continues on another line
and another line.

This is a second block."""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is a paragraph\n"
                "that continues on another line\n"
                "and another line.",
                "This is a second block.",
            ],
        )

    def test_empty_markdown(self):
        blocks = markdown_to_blocks("")

        self.assertEqual(blocks, [])

    def test_only_whitespace(self):
        blocks = markdown_to_blocks("   \n\n   \n\n   ")

        self.assertEqual(blocks, [])


if __name__ == "__main__":
    unittest.main()