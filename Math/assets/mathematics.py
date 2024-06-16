from __future__ import division

import sympy
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application,
                                        convert_xor)
from sympy import *
from string import ascii_lowercase
import re

transformations = (standard_transformations + (implicit_multiplication_application,) + (convert_xor,))
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = symbols(
    "a b c d e f g h i j k l m n o p q r s t u v w x y z"
)


# function to convert to superscript

def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)


def refactoring(text):
    if text.__contains__("^"):
        string = str(expand(parse_expr(text, transformations=transformations)))
        iterator = re.finditer(r"\*\*", string)
        req_list = [int(list(i.span())[1]) for i in iterator]
        string_as_list = list(string)
        for index in req_list:
            string_as_list[index] = get_super(string_as_list[index])
            new_string = "".join(string_as_list)
        new_string.replace("*", "")
        return new_string.replace("*", "")
    else:
        string = str((parse_expr(text, transformations=transformations))).replace("*", "")
        return string.replace("*", "")


def simplification(text):
    return refactoring(text)


def solve_ation(text):
    left_hand_side = parse_expr(text.split("=")[0], transformations=transformations)
    right_hand_side = parse_expr(text.split("=")[1], transformations=transformations)
    itr = list(solveset(Eq(left_hand_side, right_hand_side), x))
    return list(map(lambda x: Float(x, 3), itr))


def differentiation(text):
    string: str = str(expand(diff(parse_expr(text, transformations=transformations))))
    if string.__contains__("**"):
        iterator = re.finditer(r"\*\*", string)
        req_list = [int(list(i.span())[1]) for i in iterator]
        string_as_list = list(string)
        for index in req_list:
            string_as_list[index] = get_super(string_as_list[index])
            new_string = "".join(string_as_list)
        final_result = new_string.replace("*", "")
        return final_result
    else:
        return string.replace("*", "")


def integration(text):
    string: str = str(expand(integrate(
        parse_expr(text, transformations=transformations))))
    if string.__contains__("**"):
        iterator = re.finditer(r"\*\*", string)
        req_list = [int(list(i.span())[1]) for i in iterator]
        string_as_list = list(string)
        for index in req_list:
            string_as_list[index] = get_super(string_as_list[index])
            new_string = "".join(string_as_list)
        final_result = new_string.replace("*", "")
        return final_result + " + C"
    else:
        return string.replace("*", "") + " + C"


def factorisation(text):
    string: str = str(factor(
        parse_expr(text, transformations=transformations)))
    if string.__contains__("**"):
        iterator = re.finditer(r"\*\*", string)
        req_list = [int(list(i.span())[1]) for i in iterator]
        string_as_list = list(string)
        for index in req_list:
            string_as_list[index] = get_super(string_as_list[index])
            new_string = "".join(string_as_list)
        final_result = new_string.replace("*", "")
        return final_result
    else:
        return string.replace("*", "")

print(sympy.__version__)

