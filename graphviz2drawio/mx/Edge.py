from graphviz2drawio.models import DotAttr

from .Curve import Curve
from .GraphObj import GraphObj


class Edge(GraphObj):
    """An edge connecting two nodes in the graph."""

    def __init__(
        self,
        sid: str,
        fr: str,
        to: str,
        curve: Curve | None,
        label: str,
    ) -> None:
        super().__init__(sid=sid, gid=f"{fr}->{to}")
        self.fr = fr
        self.to = to
        self.curve = curve
        self.line_style = None
        self.dir = None
        self.arrowtail = None
        self.label = label

    def curve_start_end(self):
        if self.dir == DotAttr.BACK:
            return self.curve.end, self.curve.start
        return self.curve.start, self.curve.end

    @property
    def key_for_label(self) -> str:
        return f"{self.gid}-{self.curve}"

    def __repr__(self) -> str:
        return (
            f"{self.fr}->{self.to}: "
            f"{self.label}, {self.line_style}, {self.dir}, {self.arrowtail}"
        )
