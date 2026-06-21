from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, txt, txt_type, url):
        self.text = txt
        self.text_type = txt_type
        self.url = url

    def __eq__(self, value):
        #compares self to another TextNode instance (other) and returns True if all of their properties are equal. 
        pass

    def __repr__(self):
        #returns a string representation of the TextNode object.
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
        
