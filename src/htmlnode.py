#from __future__ import annotations

class HTMLNode():
    def __init__(
            self,
            tag: str | None = None,
            value: str | None = None,
            children: list["HTMLNode"] | None = None,
            props: dict[str,str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise ValueError('Not implemented')        
    
    def props_to_html(self) -> str:
        ret_string = ""
        if self.props != None:
            for keys in self.props:
                ret_string += f' {keys}="{self.props[keys]}"'
        return ret_string

    def __repr__(self) -> str:
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props_to_html()}"
        

class LeafNode(HTMLNode):
    def __init__(
            self,
            tag: str | None,
            value: str,
            props: dict[str,str] | None = None
            ) -> None:
        super().__init__(tag, value, None, props)
    
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All nodes must have a value")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, props: {self.props_to_html()}"
    

class ParentNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            children: list["HTMLNode"],
            props: dict[str,str] | None = None
            ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have child nodes")
        
        html_string = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            html_string += child.to_html()
        html_string += f'</{self.tag}>'
        return html_string

    def __repr__(self):
        return f"tag: {self.tag}, children: {self.children}, props: {self.props_to_html()}"