from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():

    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)
    htmlnode = HTMLNode("p", "This is paragraph text", None, {"href": "https://www.google.com", "target": "_blank"})
    print(htmlnode)
    print(htmlnode.props_to_html())
    leafnode1 = LeafNode("p", "This is a paragraph of text.")
    leafnode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(leafnode1.to_html())
    print(leafnode2.to_html())

    parentnode = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    print(parentnode.to_html())

main()