from .transPYler import handler
from .transPYler import blocks


@handler("expr")
def expr(value):
    return value+';'

@handler("assign")
def assign(var, value):
    return f"{var} := {value};"

@handler("new_var")
def new_var(var, value):
    return f"{var} := {value};"

@handler("if")
def _if(compare, body, els):
    if els:
        return f"if {compare} then {body}\n{els}"
    else:
        return f"if {compare} then {body};"

@handler("else")
def _else(body):
    return f"else{body};"

@handler("else_if")
def else_if(_if):
    return "else "+_if

@handler("c_like_for")
def c_like_for(var, body, param):
    start, finish, step = param
    blocks.add_var(var, 'int')
    return f"for {var} := {start} to {finish}-1 do {body};"

@handler("while")
def _while(compare, body, els):
    return f"while {compare} do {body};"

@handler("statement_block")
def statement_block(body):
    tab = '\n'+'    '*blocks.nesting_level
    end = ('\n'+'    '*(blocks.nesting_level-1))+'end'
    return "\nbegin"+tab + tab.join(body)+end
