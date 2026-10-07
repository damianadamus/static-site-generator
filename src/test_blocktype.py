import unittest

from blocktype import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(
            block_to_block_type("# Heading"),
            BlockType.HEADING,
        )

        self.assertEqual(
            block_to_block_type("## Heading"),
            BlockType.HEADING,
        )

        self.assertEqual(
            block_to_block_type("### Heading"),
            BlockType.HEADING,
        )

        self.assertEqual(
            block_to_block_type("###### Heading"),
            BlockType.HEADING,
        )

    def test_invalid_heading(self):
        self.assertEqual(
            block_to_block_type("####### Heading"),
            BlockType.PARAGRAPH,
        )

        self.assertEqual(
            block_to_block_type("##Heading"),
            BlockType.PARAGRAPH,
        )

    def test_code_block(self):
        block = """```
print("hello")
print("world")
```"""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE,
        )

    def test_invalid_code_block(self):
        block = """```
print("hello")
print("world")"""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_quote_block(self):
        block = """> First line
> Second line
> Third line"""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE,
        )

    def test_quote_without_space(self):
        block = """>First line
>Second line
>Third line"""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE,
        )

    def test_invalid_quote_block(self):
        block = """> First line
> Second line
Third line"""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_unordered_list(self):
        block = """- First item
- Second item
- Third item"""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.UNORDERED_LIST,
        )

    def test_invalid_unordered_list(self):
        block = """- First item
- Second item
Third item"""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_ordered_list(self):
        block = """1. First item
2. Second item
3. Third item"""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST,
        )

    def test_ordered_list_must_start_at_one(self):
        block = """2. First item
3. Second item
4. Third item"""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_ordered_list_must_increment(self):
        block = """1. First item
2. Second item
4. Third item"""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_paragraph(self):
        block = "This is a normal paragraph."

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )


if __name__ == "__main__":
    unittest.main()