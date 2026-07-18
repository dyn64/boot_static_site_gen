#from textnode import TextType, TextNode
import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

class PatternBlockType(Enum):
    PARAGRAPH = ''
    HEADING = r'#+'
    CODE = r'```\n'
    QUOTE = r'> '
    UNORDERED_LIST = r'- '
    ORDERED_LIST = r'\d\. '

rBlockType = {
        BlockType.HEADING : re.compile(r'#{1,6} '),
        BlockType.CODE: re.compile(r'```\n'),
        BlockType.QUOTE: re.compile(r'>'),
        BlockType.UNORDERED_LIST: re.compile(r'- '),
        BlockType.ORDERED_LIST: re.compile(r'\d\. ')
    }


def block_to_blocktype(text: str) -> BlockType:

    if re.match(rBlockType[BlockType.HEADING], text) != None:
        return BlockType.HEADING
    if re.search(r'\n```$', text) != None:
        return BlockType.CODE
    if re.match(rBlockType[BlockType.QUOTE], text) != None and re.search(r'\n(?!>)', text) == None:
        return BlockType.QUOTE
    if re.match(rBlockType[BlockType.ORDERED_LIST], text) != None and re.search(r'\n(?!\d\. )', text) == None:
        return BlockType.ORDERED_LIST
    if re.match(rBlockType[BlockType.UNORDERED_LIST], text) != None and re.search(r'\n(?!- )', text) == None:
        return BlockType.UNORDERED_LIST
    return BlockType.PARAGRAPH
    