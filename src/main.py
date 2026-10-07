import os
import shutil
import sys

from markdown_to_html_node import markdown_to_html_node


def copy_directory(source: str, destination: str):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)

    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            print(f"Copying: {source_path} -> {destination_path}")
            shutil.copy(source_path, destination_path)
        else:
            copy_directory(source_path, destination_path)


def extract_title(markdown: str) -> str:
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()

    raise ValueError("No h1 heading found")


def generate_page(
    from_path: str,
    template_path: str,
    dest_path: str,
    basepath: str,
):
    print(
        f"Generating page from {from_path} "
        f"to {dest_path} "
        f"using {template_path}"
    )

    with open(from_path, "r") as markdown_file:
        markdown = markdown_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    html = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    template = template.replace(
        "{{ Title }}",
        title,
    )

    template = template.replace(
        "{{ Content }}",
        html,
    )

    template = template.replace(
        'href="/',
        f'href="{basepath}',
    )

    template = template.replace(
        'src="/',
        f'src="{basepath}',
    )

    os.makedirs(
        os.path.dirname(dest_path),
        exist_ok=True,
    )

    with open(dest_path, "w") as output_file:
        output_file.write(template)


def generate_pages_recursive(
    dir_path_content: str,
    template_path: str,
    dest_dir_path: str,
    basepath: str,
):
    for item in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isfile(source_path):
            if source_path.endswith(".md"):
                dest_path = dest_path.replace(".md", ".html")

                generate_page(
                    source_path,
                    template_path,
                    dest_path,
                    basepath,
                )

        else:
            os.makedirs(dest_path, exist_ok=True)

            generate_pages_recursive(
                source_path,
                template_path,
                dest_path,
                basepath,
            )


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    copy_directory("static", "docs")

    generate_pages_recursive(
        "content",
        "template.html",
        "docs",
        basepath,
    )


if __name__ == "__main__":
    main()