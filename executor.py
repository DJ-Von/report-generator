import subprocess
import sys
import ast
import _ast
from ast_decompiler import decompile
import img_gen
from pascal import exe


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
    return '\n'.join(strings)

o=0
c=0
#def execute(file, data):
#    global o
#    print(compiler(open(file, 'r').read(), data), file=open('buffer.py', 'w'))
#    open(f'test{o}.svg', 'w').write(img_gen.result_img(subprocess.getoutput('python buffer.py')))

#def code_gen(file):
#    global c
#    open(f'test_{c}.svg', 'w').write(img_gen.code_img(exe(file)))

def execute(file, data):
    print(compiler(open(file, 'r').read(), data), file=open('buffer.py', 'w'))
    return img_gen.result_img(subprocess.getoutput('python buffer.py'))

def code_gen(file):
    return img_gen.code_img(exe(file))
