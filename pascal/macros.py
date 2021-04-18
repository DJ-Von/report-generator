import _ast
from .transPYler import macro, blocks


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
def write(*args):
    arg = list(map(lambda a: a.replace('"', '\''), args))
    arg = ", ' ', ".join(arg)
    return {'val': f'Writeln({arg})'}
