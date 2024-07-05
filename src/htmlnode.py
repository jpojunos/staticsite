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