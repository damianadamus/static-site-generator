from textnode import TextNode, TextType
from markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)

        if not images:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text

        for image_alt, image_url in images:
            image_markdown = f"![{image_alt}]({image_url})"

            sections = remaining_text.split(image_markdown, 1)

            before = sections[0]
            after = sections[1]

            if before:
                new_nodes.append(
                    TextNode(before, TextType.TEXT)
                )

            new_nodes.append(
                TextNode(
                    image_alt,
                    TextType.IMAGE,
                    image_url,
                )
            )

            remaining_text = after

        if remaining_text:
            new_nodes.append(
                TextNode(
                    remaining_text,
                    TextType.TEXT,
                )
            )

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)

        if not links:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text

        for link_text, link_url in links:
            link_markdown = f"[{link_text}]({link_url})"

            sections = remaining_text.split(link_markdown, 1)

            before = sections[0]
            after = sections[1]

            if before:
                new_nodes.append(
                    TextNode(before, TextType.TEXT)
                )

            new_nodes.append(
                TextNode(
                    link_text,
                    TextType.LINK,
                    link_url,
                )
            )

            remaining_text = after

        if remaining_text:
            new_nodes.append(
                TextNode(
                    remaining_text,
                    TextType.TEXT,
                )
            )

    return new_nodes