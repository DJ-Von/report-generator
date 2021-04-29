from . import transPYler
from . import expr, blocks, macros
import re


def exe(file):
    out = ''
    code = open(file, 'r').read()
    out += 'Program main;\nUses CRT;\n\n'
    body = transPYler.core.compiler(code).split('\n')
    var = transPYler.core.variables.get('main')
    if var:
        variables = ""
        for i in var:
            _type = macros.type_to_type.get(var.get(i))
            if not(_type):
                _type = var.get(i)
            variables += f'    {i}: {_type};\n'
        out += 'Var\n'+variables+'\n'
    transPYler.core.variables |= {"main": {}}
    transPYler.blocks.nesting_level += 1
    tab = '\n'+'    '*transPYler.blocks.nesting_level
    end = ('\n'+'    '*(transPYler.blocks.nesting_level-1))+'End.'
    out += 'Begin'+tab+tab.join(body)+end
    transPYler.blocks.nesting_level -= 1
    return out
