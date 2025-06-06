from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, children, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")

        if not self.tag:
            return f"{self.value}"

        return f"<{self.tag}>{self.value}</{self.tag}>"
