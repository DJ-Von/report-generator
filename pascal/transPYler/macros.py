import _ast
from .utils import transpyler_type
from .ast_decompiler import decompile


def what_macro(name):
    if type(name) == tuple:
        name = (transpyler_type(name[0]), transpyler_type(name[1]), name[2])
        print(name)
        ol_data = [(name[0], name[1], name[2]),
                   (name[0], name[1], 'any'),
                   ('any', name[1], name[2]),
                   (name[0], 'any', name[2]),
                   ('any', 'any', name[2]),
                   ('any', 'any', 'any'),
                   ]
        for i in ol_data:
            if ol := macros.get(i):
                return ol

    elif type(name)==str:
        if name in macros:
            name = macros.get(name)
            return name
    else:
        for i in macros:
            if callable(i):
                if i(name):
                    return macros.get(i)

def macro(name, args, keys):
    def get_val(val):
        if type(val)==_ast.Constant:
            val = val.value
            if type(val) == str:
                val = '"'+val+'"'
            val = str(val)
            return val
        else:
            return decompile(val)
    args = '('+', '.join(list(map(lambda i:'"'+get_val(i)+'"', args)))
    keys = f", {', '.join(list(map(decompile, keys)))})"
    print(args+keys)
    return eval(f"name{args+keys}")


def power(l, r):
    return {'type': 'int', 'val': f'power({l.get("val")}, {r.get("val")})'}
macros = {('any', 'any', '**'): power}
