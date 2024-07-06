import html

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        rv = ""
        for key, value in self.props.items():
            rv += f" {key}=\"{value}\""
        return rv
    
    def __repr__(self) -> str:
        return (f"Tag: {self.tag}\n"
                f"Value: {self.value[:60] + '...' if self.value and len(self.value) > 60 else self.value}\n"
                f"Children: {len(self.children) if self.children else 'N/a'}\n"
                f"Props: {self.props}")

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        if props is None:
            props = {}
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value
        attributes = " ".join(f'{key}="{html.escape(value)}"' for key, value in self.props.items())
        if attributes:
            tag_open = f"<{self.tag} {attributes}>"
        else:
            tag_open = f"<{self.tag}>"
        
        tag_close = f"</{self.tag}>"
        return f"{tag_open}{self.value}{tag_close}"

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if children == None:
            raise ValueError("No children provided")
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("No Tag provided")
        open_tag = f"<{self.tag}>"
        close_tag = f"</{self.tag}>"
        collector = ""
        for child in self.children:
            collector += child.to_html()
        return f"{open_tag}{self.props_to_html()}{collector}{close_tag}"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"