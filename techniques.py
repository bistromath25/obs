import random
import re
import regex
import ast
import time
from util import RandomVariableNameGenerator, RandomDataGenerator


name_generator = RandomVariableNameGenerator()
data_generator = RandomDataGenerator()

def rename_variables(code):
    code = "\n" + code
    variable_names = re.findall(r"(\w+)(?=( |)=( |))", code)
    function_names = re.findall(r"(?<=f )(.*?)(?=\()", code)
    do_not_replace = ["len", "str"]
        
    for i in range(len(variable_names)):
        obfuscated_name = name_generator.get_random(i + 1)
        code = re.sub(
            r"(?<=[^.])(\b{}\b)".format(variable_names[i][0]), obfuscated_name, code
        )
    
    for i in range(len(function_names)):
        if function_names[i] in do_not_replace:
            continue
        
        obfuscated_name = name_generator.get_random(i + 1)
        code = re.sub(
            r"(?<=[^.])(\b{}\b)".format(function_names[i]), obfuscated_name, code
        ) 
                
    return code


def add_random_variables(code):
    variables_to_add = random.randint(1, 4)

    for i in range(1, variables_to_add):
        rand_data = data_generator.get_random()
        if type(rand_data) == str:
            rand_data = '"{}"'.format(rand_data)
        if i % 2 == 0:
            code = "{} = {}\n".format(name_generator.get_random(i), rand_data) + code
        else:
            code = code + "\n{} = {}".format(name_generator.get_random(i), rand_data)
    
    return code
    
def add_random_ifs(code):
    ifs_to_add = random.randint(1, 4)
    
    ifs = [
        "print(str('{}')) if not len('{}') and not True or False else '{}' + '{}'\n",
        "print('{}') if not len('{}') and '{}' != None else True and str('{}')\n",
        "print('{}') if str('{}') == str('{}') else str('{}')\n",
        "{} = '{}' if False else '{}' + '{}'\n",
        "{} = str('{}') if len('{}') == -2 else str('{}')[-1]\n"
    ]
    
    for i in range(1, ifs_to_add):
        code = random.choice(ifs).format(name_generator.get_random(i), data_generator.get_random(), data_generator.get_random(), data_generator.get_random()) + "\n" + code
    
    return code
    
def add_random_functions(code):
    funcs_to_add = random.randint(1, 3)
    
    funcs = [
"""
def {}({}):
    {} = ""
    while False:
        {} += '{}'[0]
    
    if True:
        return False
        
    else:
        return '{}'[::-1]\n
""",
"""
def {}({}):
    if len('{}') == -len('{}'):
        return True

    try:
        return False and True and None
    
    except:
        return len('{}') == {}\n
"""
    ]
    
    for i in range(1, funcs_to_add):
        func_name = name_generator.get_random(i)
        code = random.choice(funcs).format(func_name, func_name, func_name, func_name, data_generator.get_random(), func_name) + "\n" + code
    
    return code
    

def str_to_hex_bytes(code):
    python_string_decoraters = ['"""', "'''", '"', "'"]
    
    for s in python_string_decoraters:
        pattern = r"((?<=(( |	|\n)\w+( |)=( |))({}))[\W\w]*?(?=({})))".format(s, s)
        t = regex.findall(pattern, code)
        for v in t:
            string_contents = v[0]
            if s == '"' and string_contents == '"':
                continue
            if s == "'" and string_contents == "'":
                continue
            hex_bytes = "\\" + "\\".join(
                x.encode("utf-8").hex() for x in string_contents
            )
            code = regex.sub(pattern, str(hex_bytes).replace("\\", "\\\\"), code)
            
    return code


def obfuscate(code, remove_techniques=[]):
    if len(remove_techniques) == 0:
        methods = all_methods
    else:
        for technique in remove_techniques:
            methods.remove(technique)
    
    for technique in methods:
        code = technique(code)

    return code


all_methods = [rename_variables, add_random_variables, add_random_ifs, add_random_functions]
