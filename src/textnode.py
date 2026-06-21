from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, txt: str, txt_type: TextType, url: str) -> None:
        self.text = txt
        self.text_type = txt_type
        self.url = url

    def __eq__(self, other: "TextNode") -> bool:
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )
        #compares self to another TextNode instance (other) and returns True if all of their properties are equal. 
        pass

    def __repr__(self):
        #returns a string representation of the TextNode object.
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
        
