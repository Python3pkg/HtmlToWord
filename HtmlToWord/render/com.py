from . import Renderer, renders
from ..operations import HyperLink, Text


class COMRenderer(Renderer):
    def __init__(self, word, selection):
        super().__init__()

    @renders(HyperLink)
    def hyperlink(self, op):
        print(op.href)
        start = self.range.Start
        yield
        end = self.range.End
        # Make a range and turn it into a hyperlink or something
        print("end of hyperlink")

    @renders(Text)
    def text(self, op):
        print(op.text)