from __future__ import annotations

class HTMLNode():
    def __init__(
            self,
            tag: str | None = None,
            value: str | None = None,
            children: HTMLNode | None = None,
            props: dict | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("not implemented")
    
    def props_to_html(self) -> str:
        ret_string = ""
        if self.props != None:
            for keys in self.props:
                ret_string += f' {keys}="{self.props[keys]}"'
        return ret_string

    def __repr__(self) -> str:
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props_to_html()}"
        

