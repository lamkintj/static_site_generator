
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Children should override this method themselves")

    def props_to_html(self):
        if self.props == None:
            return ""
        props_html = ""
        for item in self.props:
            props_html += f' {item}="{self.props[item]}"'
        return props_html
    
    def __eq__(self, other):
        return (
            self.tag == other.tag and
            self.value == other.value and 
            self.children == other.children and
            self.props == other.props
        )

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __eq__(self, other):
        return (
            self.tag == other.tag and
            self.value == other.value and 
            self.props == other.props
        )

    def __repr__(self):
        return f"LeafNode(tag: {self.tag}, value: {self.value}, props: {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("A parent node's tag can not be None")
        if self.children == None:
            raise ValueError("A parent node must have children")
        # Start string with parent opening tag and any props info
        html_string = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html_string += child.to_html()
        # Close string with parent closing tag
        html_string += f"</{self.tag}>" 
        return html_string

    def __repr__(self):
        return f"ParentNode(tag: {self.tag}, children: {self.children}, props: {self.props})"

