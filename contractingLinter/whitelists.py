import ast, builtins

ALLOWED_BUILTINS = {'Exception', 'False', 'None', 'True', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray',
                    'bytes', 'chr', 'dict', 'divmod', 'filter', 'format', 'frozenset', 'hex', 'int', 'isinstance',
                    'issubclass', 'import', 'len', 'list', 'map', 'max', 'min', 'oct', 'ord', 'pow', 'range', 'reversed',
                    'round', 'set', 'sorted', 'str', 'sum', 'tuple', 'zip'}

ILLEGAL_BUILTINS = set(dir(builtins)) - ALLOWED_BUILTINS

ALLOWED_AST_TYPES = {ast.Module, ast.Eq, ast.Call, ast.Dict, ast.Attribute, ast.Pow, ast.Index, ast.Not, ast.alias,
                     ast.If, ast.FunctionDef, ast.Global, ast.GtE, ast.LtE, ast.Load, ast.arg, ast.Add, ast.Import,
                     ast.ImportFrom, ast.Name, ast.Num, ast.BinOp, ast.Store, ast.Assert, ast.Assign, ast.AugAssign,
                     ast.Subscript, ast.Compare, ast.Return, ast.NameConstant, ast.Expr, ast.keyword, ast.Sub,
                     ast.arguments, ast.List, ast.Set, ast.Str, ast.UnaryOp, ast.Pass, ast.Tuple, ast.Div, ast.In,
                     ast.NotIn, ast.Gt, ast.Lt, ast.Starred, ast.Mod, ast.NotEq, ast.For, ast.While, ast.ListComp,
                     ast.comprehension, ast.Slice, ast.USub, ast.BoolOp, ast.And, ast.Or, ast.Mult, ast.IsNot, ast.Is}

ILLEGAL_AST_TYPES = {
    ast.AsyncFor,
    ast.AsyncFunctionDef,
    ast.AsyncWith,
    ast.Await,
    ast.ClassDef,
    ast.Ellipsis,
    ast.GeneratorExp,
    ast.Global,
    ast.ImportFrom,
    ast.Interactive,
    ast.Lambda,
    ast.MatMult,
    ast.Nonlocal,
    ast.Suite,
    ast.Try,
    ast.With,
    ast.Yield,
    ast.YieldFrom,
}

ALLOWED_ANNOTATION_TYPES = {'dict', 'list', 'str', 'int', 'float', 'bool', 'datetime.timedelta', 'datetime.datetime', 'Any'}

VIOLATION_TRIGGERS = [
    "CXN1 Illegal contracting syntax type used",
    "CXN2 Illicit use of '_' before variable",
    "CXN3 Illicit use of Nested imports",
    "CXN4 ImportFrom compilation nodes not yet supported",
    "CXN5 Contract not found in lib",
    "CXN6 Illicit use of classes",
    "CXN7 Illicit use of Async functions",
    "CXN8 Invalid decorator used",
    "CXN9 Multiple use of constructors detected",
    "CXN10 Illicit use of multiple decorators",
    "CXN11 Illicit keyword overloading for ORM assignments",
    "CXN12 Multiple targets to ORM definition detected",
    "CXN13 No valid contracting decorator found",
    "CXN14 Illegal use of a builtin",
    "CXN15 Reuse of ORM name definition in a function definition argument name",
    "CXN16 Illegal argument annotation used",
    "CXN17 No valid argument annotation found",
    "CXN18 Illegal use of return annotation",
    "CXN19 Illegal use of a nested function definition."
]
