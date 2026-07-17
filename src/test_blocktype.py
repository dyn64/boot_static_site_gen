import unittest

from blocktype import block_to_blocktype, BlockType

class Test(unittest.TestCase):
    def test_heading(self):
        text = "### heading"
        self.assertEqual(block_to_blocktype(text),
                         BlockType.HEADING)
    def test_heading_fail(self):
        text = "###heading"
        self.assertEqual(block_to_blocktype(text),
                         BlockType.PARAGRAPH)

    def test_heading_fail2big(self):
        text = "####### heading"
        self.assertEqual(block_to_blocktype(text),
                         BlockType.PARAGRAPH)

    def test_code(self):
        text = "```\nCode\n```"
        self.assertEqual(block_to_blocktype(text),
                         BlockType.CODE)

    def test_code_fail(self):
        text = "```\nCode```"
        self.assertEqual(block_to_blocktype(text),
                         BlockType.PARAGRAPH)

    def test_quote(self):
        text = "> "
        self.assertEqual(block_to_blocktype(text),
                         BlockType.QUOTE)

    def test_quote_fail(self):
        text = "> \nddddd"
        self.assertEqual(block_to_blocktype(text),
                         BlockType.PARAGRAPH)

    def test_uList(self):
        text = "- list\n- list2"
        self.assertEqual(block_to_blocktype(text),
                         BlockType.UNORDERED_LIST)

    def test_uList_fail(self):
        text = "- list\n- list2\nrrrr"
        self.assertEqual(block_to_blocktype(text),
                         BlockType.PARAGRAPH)

    def test_oList(self):
        text = "1. list\n2. lizt"
        self.assertEqual(block_to_blocktype(text),
                         BlockType.ORDERED_LIST)
    def test_oList_fail(self):
        text = "1. list\n2. lizt\nderp"
        self.assertEqual(block_to_blocktype(text),
                         BlockType.PARAGRAPH)

    def test_paragraph(self):
        text = "just text"
        self.assertEqual(block_to_blocktype(text),
                         BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()