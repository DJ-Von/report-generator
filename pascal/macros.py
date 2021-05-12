import _ast
from .transPYler import macro, blocks


type_to_type = {"int": "Longint",
                "str": "String",
                "float": "Real"
                }


def is_read(tree):
    try:
        name = tree.value.func.id
        types = ['str', 'int']
        if name in types:
            if type(tree.value.args[0]) == _ast.Call:
                if tree.value.args[0].func.id == 'input':
                    return 1
        elif name == 'input':
            return 1
    except:
        return 0

@macro(is_read)
def read(tree):
    if tree.value.func.id == 'input':
        _type = 'str'
    else:
        _type = tree.value.func.id
    blocks.add_var(tree.targets[0].id, _type)
    msg = ""
    if type(tree.value.args[0]) == _ast.Call:
        if tree.value.args[0].args[0].value[-2:] == '\\n':
            msg = f"Writeln('{tree.value.args[0].args[0].value[:-2]}');\n"
        else:
            msg = f"Write('{tree.value.args[0].args[0].value}');\n"
    elif type(tree.value.args[0]) == _ast.Constant:
        if tree.value.args[0].value[-2:] == '\\n':
            msg = f"Writeln('{tree.value.args[0].value[:-2]}');\n"
        else:
            msg = f"Write('{tree.value.args[0].value}');\n"
    return f"{msg}Readln({tree.targets[0].id});"

@macro('print')
def write(*args, x=0, y=0):
    arg = list(map(lambda a: a.replace('"', '\''), args))
    arg = ", ' ', ".join(arg)
    conf = ''
    print(args)
    print(x, y) 
    return {'val': f'{conf}Writeln({arg})'}

def _list(l, r):
    ls = r.get('val').get('list')
    arr = ''
    var = l.get('val')
    blocks.add_var(var, f'array [0..{len(ls)-1}] of {type_to_type.get(r.get("val").get("type"))}')
    for n, i in enumerate(ls):
        arr += f'{var}[{n}] := {i};\n'
    return arr
macro({('any', 'list', '='): _list
})
