from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    # Heading
    first_line = lines[0]

    for i in range(1, 7):
        if first_line.startswith("#" * i + " "):
            return BlockType.HEADING

    # Code block
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    # Quote block
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list
    expected_number = 1

    for line in lines:
        prefix = f"{expected_number}. "

        if not line.startswith(prefix):
            return BlockType.PARAGRAPH

        expected_number += 1

    return BlockType.ORDERED_LIST