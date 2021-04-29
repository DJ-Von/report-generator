import os
import sys
import ast
import _ast
from ast_decompiler import decompile
import subprocess

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

def read(tree, data):
    try:
        if type(tree.value.args[0]) == _ast.Call:
            msg = f"print('{tree.value.args[0].args[0].value}', end='')\n"
        elif type(tree.value.args[0]) == _ast.Constant:
            msg = f"print('{tree.value.args[0].value}', end='')\n"
    except:
        msg = ''
    var = tree.targets[0].id
    return f"{msg}print({data.get(var)})\n{var} = {data.get(var)}"


def compiler(code, data):
    strings = []
    body = ast.parse(code).body
    for i in body:
        if is_read(i):
            strings.append(read(i, data))
        else:
            strings.append(decompile(i))
    print('------------\n', '\n'.join(strings), '\n----------------------\n')
    return '\n'.join(strings)

def execute(file, data):
    print(compiler(open(file, 'r').read(), data), file=open('buffer.py', 'w'))
    return subprocess.getoutput('python3.9 buffer.py')
