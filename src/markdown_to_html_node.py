from blocktype import BlockType, block_to_block_type
from htmlnode import HTMLNode
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import (
    TextNode,
    TextType,
    text_node_to_html_node,
)


def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)

    children = []

    for text_node in text_nodes:
        children.append(
            text_node_to_html_node(text_node)
        )

    return children


def paragraph_to_html_node(block: str) -> HTMLNode:
    text = " ".join(block.split("\n"))

    return ParentNode(
        "p",
        text_to_children(text),
    )


def heading_to_html_node(block: str) -> HTMLNode:
    first_space = block.find(" ")

    level = first_space
    text = block[first_space + 1:]

    return ParentNode(
        f"h{level}",
        text_to_children(text),
    )


def code_to_html_node(block: str) -> HTMLNode:
    code = block[4:-3]

    text_node = text_node_to_html_node(
        TextNode(code, TextType.TEXT)
    )

    code_node = ParentNode(
        "code",
        [text_node],
    )

    return ParentNode(
        "pre",
        [code_node],
    )


def quote_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")

    quote_lines = []

    for line in lines:
        line = line[1:]

        if line.startswith(" "):
            line = line[1:]

        quote_lines.append(line)

    text = " ".join(quote_lines)

    return ParentNode(
        "blockquote",
        text_to_children(text),
    )


def unordered_list_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")

    children = []

    for line in lines:
        text = line[2:]

        children.append(
            ParentNode(
                "li",
                text_to_children(text),
            )
        )

    return ParentNode(
        "ul",
        children,
    )


def ordered_list_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")

    children = []

    for line in lines:
        dot_index = line.find(".")
        text = line[dot_index + 2:]

        children.append(
            ParentNode(
                "li",
                text_to_children(text),
            )
        )

    return ParentNode(
        "ol",
        children,
    )


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)

    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            block_nodes.append(
                paragraph_to_html_node(block)
            )

        elif block_type == BlockType.HEADING:
            block_nodes.append(
                heading_to_html_node(block)
            )

        elif block_type == BlockType.CODE:
            block_nodes.append(
                code_to_html_node(block)
            )

        elif block_type == BlockType.QUOTE:
            block_nodes.append(
                quote_to_html_node(block)
            )

        elif block_type == BlockType.UNORDERED_LIST:
            block_nodes.append(
                unordered_list_to_html_node(block)
            )

        elif block_type == BlockType.ORDERED_LIST:
            block_nodes.append(
                ordered_list_to_html_node(block)
            )

    return ParentNode(
        "div",
        block_nodes,
    )