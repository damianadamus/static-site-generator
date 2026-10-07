import unittest

from main import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_extract_title(self):
        markdown = "# Hello"

        self.assertEqual(
            extract_title(markdown),
            "Hello",
        )

    def test_extract_title_with_whitespace(self):
        markdown = "#    Hello World   "

        self.assertEqual(
            extract_title(markdown),
            "Hello World",
        )

    def test_extract_title_from_multiple_lines(self):
        markdown = """Some text

## Heading 2

# My Title

Some more text"""

        self.assertEqual(
            extract_title(markdown),
            "My Title",
        )

    def test_missing_title(self):
        markdown = """## Heading 2

Some paragraph"""

        with self.assertRaises(ValueError):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()