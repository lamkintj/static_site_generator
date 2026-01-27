from enum import Enum

from htmlnode import HTMLNode, LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def text_node_to_html_node(self):
        if self.text_type not in TextType:
            raise ValueError("Provided text type is not included in the TextType Enum")
        elif self.text_type.value == "text":
            return LeafNode(None, self.text)
        elif self.text_type.value == "bold":
            return LeafNode("b", self.text)
        elif self.text_type.value == "italic":
            return LeafNode("i", self.text)
        elif self.text_type.value == "code":
            return LeafNode("code", self.text)
        elif self.text_type.value == "link":
            return LeafNode("a", self.text, {"href": self.url})
        elif self.text_type.value == "image":
            return LeafNode("img", "", {"src": self.url, "alt": self.text})
    
    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

