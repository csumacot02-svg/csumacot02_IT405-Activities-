# -*- coding: utf-8 -*-
"""IT 405L  --  LABORATORY ACTIVITY 1
Logical Operators and an Expression Evaluator

    Sumacot, Christian G.
    2310121-1        slip B05-4        Section B        Group B05

THE VALUES BELOW ARE YOURS ALONE. A classmate may help you understand the work; a classmate
cannot answer it for you, because their answer belongs to their parameters, not to yours.

HOW TO USE THIS FILE
    1. Keep it in the same folder as the code you write. Your activity sheet names that file.
    2. Write your code there, following the steps on your sheet. The markers below are for your
       own notes.
    3. Run THIS file last:   python IT405_A01_2310121-1.py
       It imports your code, computes your stamp and prints one line. Put that line in stamp.txt.

Until you have written the function named at the bottom of this file, running it reports
ModuleNotFoundError or NameError. That is expected -- there is nothing to import yet.

It needs nothing but Python: no internet, no administrator rights and no installation, so it
behaves the same on a laboratory computer, on a borrowed laptop and on your own machine.
"""
import hashlib


# ==================================================================== YOUR PARAMETERS
STUDENT_NO = '2310121-1'

# The expression you must evaluate, in the nested-tuple form your evaluator takes.
EXPR = ('not', ('or', ('implies', True, False), ('and', False, True)))

# The same expression written out, for your hand working.
EXPR_TEXT = 'not ((True implies False) or (False and True))'


# ==================================================================== YOUR WORK

# ---- Step 1: Open a terminal and confirm your Python version with python --version. Record the ... ----
# Observed: python --version -> Python 3.13.7 (meets 3.10+).


# ---- Step 2: In a new file logic_ops.py, write three functions: my_and(a, b), my_or(a, b) and ... ----
# Done in logic_ops.py: my_and / my_or / my_not built from comparisons only (no and / or / not).


# ---- Step 3: Write a fourth function my_implies(a, b) that returns the truth value of "a implies ... ----
# On paper: T T -> T, T F -> F, F T -> T, F F -> T. Code: my_implies is False only for (True, False).


# ---- Step 4: For every function, print the result for all combinations of True and False. Compare ... ----
# Printed all combinations in logic_ops.py; every line matched the paper table (see results.txt).


# ---- Step 5: Write evaluate(expr) that takes a nested tuple such as ("and", True, ("not", False)) ... ----
# Done in logic_ops.py: evaluate recurses on nested tuples and calls my_and / my_or / my_not / my_implies.


# ---- Step 6: Test evaluate with at least six expressions, one of which must be EXPR from your own ... ----
# Six tests OK; last is EXPR. Hand value True. evaluate(EXPR) = True (see results.txt).


# ---- Step 7: Now write the expression ("or", True, ("and", 1/0, False)). Run it. Record the error ... ----
# Error: ZeroDivisionError: division by zero (raised while building the tuple, before evaluate).
# Python's own or would not raise it: or short-circuits when the left side is True.




# ==================================================================== THE STAMP -- DO NOT EDIT
# Computed from YOUR parameters and the answer YOUR OWN code produced. Run this last, and put the
# printed line in stamp.txt.
def stamp(student_no, activity, *values):
    payload = '|'.join([str(student_no).strip(), str(activity)] + [repr(v) for v in values])
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()[:10].upper()


if __name__ == '__main__':
    from logic_ops import evaluate      # the file you wrote in step 2
    print(stamp(STUDENT_NO, 1, EXPR, evaluate(EXPR)))
