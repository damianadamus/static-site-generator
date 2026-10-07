import unittest

from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):

    def test_paragraphs(self):
        md = (
            "This is **bolded** paragraph\n"
            "text in a p\n"
            "tag here\n"
            "\n"
            "This is another paragraph with _italic_ text and `code` here"
        )

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div>"
            "<p>This is <b>bolded</b> paragraph text in a p tag here</p>"
            "<p>This is another paragraph with "
            "<i>italic</i> text and <code>code</code> here</p>"
            "</div>",
        )

    def test_codeblock(self):
        md = (
            "```\n"
            "This is text that _should_ remain\n"
            "the **same** even with inline stuff\n"
            "```"
        )

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div>"
            "<pre><code>"
            "This is text that _should_ remain\n"
            "the **same** even with inline stuff\n"
            "</code></pre>"
            "</div>",
        )

    def test_heading(self):
        md = "# This is a heading"

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            "<div><h1>This is a heading</h1></div>",
        )

    def test_headings(self):
        md = (
            "# Heading 1\n"
            "\n"
            "## Heading 2\n"
            "\n"
            "### Heading 3"
        )

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            "<div>"
            "<h1>Heading 1</h1>"
            "<h2>Heading 2</h2>"
            "<h3>Heading 3</h3>"
            "</div>",
        )

    def test_quote(self):
        md = (
            "> This is a quote\n"
            "> with multiple lines"
        )

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            "<div>"
            "<blockquote>This is a quote with multiple lines</blockquote>"
            "</div>",
        )

    def test_unordered_list(self):
        md = (
            "- First item\n"
            "- Second item\n"
            "- Third item"
        )

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            "<div>"
            "<ul>"
            "<li>First item</li>"
            "<li>Second item</li>"
            "<li>Third item</li>"
            "</ul>"
            "</div>",
        )

    def test_ordered_list(self):
        md = (
            "1. First item\n"
            "2. Second item\n"
            "3. Third item"
        )

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            "<div>"
            "<ol>"
            "<li>First item</li>"
            "<li>Second item</li>"
            "<li>Third item</li>"
            "</ol>"
            "</div>",
        )

    def test_mixed_markdown(self):
        md = (
            "# My document\n"
            "\n"
            "This is **bold** and _italic_.\n"
            "\n"
            "- First item\n"
            "- Second item\n"
            "\n"
            "1. One\n"
            "2. Two\n"
            "\n"
            "> This is a quote"
        )

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            "<div>"
            "<h1>My document</h1>"
            "<p>This is <b>bold</b> and <i>italic</i>.</p>"
            "<ul>"
            "<li>First item</li>"
            "<li>Second item</li>"
            "</ul>"
            "<ol>"
            "<li>One</li>"
            "<li>Two</li>"
            "</ol>"
            "<blockquote>This is a quote</blockquote>"
            "</div>",
        )


if __name__ == "__main__":
    unittest.main()