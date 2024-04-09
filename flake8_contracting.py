import importlib.metadata
import ast
from contractingLinter.linter import Linter 
from typing import Any, Generator, Type, Tuple

class Plugin:
    name = __name__
    version = importlib.metadata.version(__name__)

    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        contracting_linter = Linter()
        result = contracting_linter.check(self._tree)
        if result is not None: 
            for lineno, col, message in result:
                yield lineno, col, message, type(self)
