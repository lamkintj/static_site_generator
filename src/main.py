from functions import *
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

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

    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))

    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))


main()