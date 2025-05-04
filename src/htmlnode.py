class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Function is not implemented")

    def props_to_html(self):
        output = []

        if not self.props:
            return ""

        for k, v in self.props.items():
            output.append(f"{k}={v}")

        return " ".join(output)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
