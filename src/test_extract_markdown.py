import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links, extract_title

class TestExtractMarkdown(unittest.TestCase):
    def test_image(self):
        markdown_text = 'text text and ![alt text](https://nerd.net/test.png) text'
        correct_links = [("alt text", "https://nerd.net/test.png")]
        self.assertListEqual(extract_markdown_images(markdown_text), correct_links)

    def test_link(self):
        markdown_text = 'text text and [anchor text](https://nerd.net) text'
        correct_links = [("anchor text", "https://nerd.net")]
        self.assertListEqual(extract_markdown_links(markdown_text), correct_links)

    def test_link_multiple(self):
        markdown_text = 'text [anchor 1](https://slashdot.org) text and [anchor text](https://nerd.net) text'
        correct_links = [
            ("anchor 1", "https://slashdot.org"),
            ("anchor text", "https://nerd.net")
            ]
        self.assertListEqual(extract_markdown_links(markdown_text), correct_links)

class TestExtractMarkdown_title(unittest.TestCase):
    def test_h1(self):
        text = "# title 1"
        correct_response = "title 1"
        self.assertEqual(correct_response, extract_title(text))

    def test_h1_more(self):
        text = "# title 1\n\nsome other text\nmore"
        correct_response = "title 1"
        self.assertEqual(correct_response, extract_title(text))

    def test_h1_fail(self):
        text = "## title 1"
        correct_error = "No header found"
        with self.assertRaises(ValueError) as context:
            title = extract_title(text)
        self.assertEqual(str(context.exception), correct_error)

    def test_h2_fail(self):
        text = "## title 2"
        correct_error = "No header found"
        with self.assertRaises(ValueError) as context:
            title = extract_title(text)
        self.assertEqual(str(context.exception), correct_error)
        

if __name__ == "__main__":
    unittest.main()