# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "markdown",
#     "pyperclip",
# ]
# ///
import markdown
import pyperclip

def strip_frontmatter(markdown_text):
  """
  Strips the frontmatter (lines starting with "---") from the Markdown text.

  Args:
    markdown_text: The Markdown text.

  Returns:
    The Markdown text without the frontmatter.
  """
  lines = markdown_text.splitlines()
  in_frontmatter = False
  result = []
  for line in lines:
    if line.startswith("---"):
      in_frontmatter = not in_frontmatter
      continue
    if not in_frontmatter:
      result.append(line)
  return "\n".join(result)

def convert_to_html(markdown_file):
  """
  Converts a Markdown file to HTML, converts "---" to em-dashes, and copies it to the clipboard.

  Args:
    markdown_file: Path to the Markdown file.
  """
  try:
    with open(markdown_file, 'r') as f:
      markdown_text = f.read()

    markdown_text = strip_frontmatter(markdown_text)
    markdown_text = markdown_text.replace("---", "—") 

    html_text = markdown.markdown(markdown_text)

    pyperclip.copy(html_text)

    print(f"Markdown file '{markdown_file}' converted to HTML and copied to clipboard.")

  except FileNotFoundError:
    print(f"Error: Markdown file '{markdown_file}' not found.")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  convert_to_html("index.md")
