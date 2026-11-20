# -*- coding: utf-8 -*-
"""IT 405L  --  LABORATORY ACTIVITY 3
A Rule Engine -- Facts, Rules, Queries and Backward Chaining

    Sumacot, Christian G.
    2310121-1        slip B05-4        Section B        Group B05

THE VALUES BELOW ARE YOURS ALONE. A classmate may help you understand the work; a classmate
cannot answer it for you, because their answer belongs to their parameters, not to yours.

HOW TO USE THIS FILE
    1. Keep it in the same folder as the code you write. Your activity sheet names that file.
    2. Write your code there, following the steps on your sheet. The markers below are for your
       own notes.
    3. Run THIS file last:   python IT405_A03_2310121-1.py
       It imports your code, computes your stamp and prints one line. Put that line in stamp.txt.

Until you have written the function named at the bottom of this file, running it reports
ModuleNotFoundError or NameError. That is expected -- there is nothing to import yet.

It needs nothing but Python: no internet, no administrator rights and no installation, so it
behaves the same on a laboratory computer, on a borrowed laptop and on your own machine.
"""
import hashlib


# ==================================================================== YOUR PARAMETERS
STUDENT_NO = '2310121-1'

# Your eight family facts.
FACTS = [
    ('gina', 'hugo'),
    ('hugo', 'olen'),
    ('olen', 'nico'),
    ('hugo', 'pia'),
    ('pia', 'rey'),
    ('olen', 'ben'),
    ('olen', 'ivy'),
    ('hugo', 'dina'),
]

# The fact step 8 adds.
STEP8 = ('olen', 'olen')


# ==================================================================== YOUR WORK

# ---- Step 1: Represent a fact as a tuple, for example ("parent", "ana", "ben"). Use the eight ... ----
# Done in rules.py: FACTS loaded via importlib as ("parent", older, younger).

# ---- Step 2: Write matches(pattern, fact) that returns a dictionary of variable bindings, or None. ... ----
# Done in rules.py (matches / unify). Empty {} means success; test with "is not None".

# ---- Step 3: Test matches with ("parent", "X", "ben") against your facts. It should bind X to ... ----
# [('X': 'olen')] -- olen is the only parent of ben in my facts.

# ---- Step 4: Represent a rule as a head and a list of conditions, for example head ("grandparent", ... ----
# Done in rules.py RULES: grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

# ---- Step 5: Write query(goal) that returns every set of bindings satisfying the goal, trying ... ----
# Done in rules.py (query / _solve): facts first, then rules; fresh names each rule use.

# ---- Step 6: Ask for all grandparents. Check the answers by hand against your fact list. ----
# 7 pairs: (gina,dina), (gina,olen), (gina,pia), (hugo,ben), (hugo,ivy), (hugo,nico), (hugo,rey).

# ---- Step 7: Add a rule for ancestor that refers to itself: an ancestor is a parent, or a parent ... ----
# ancestor(X, Z) :- parent(X, Z).  /  ancestor(X, Z) :- parent(X, Y), ancestor(Y, Z).  -> 19 pairs.

# ---- Step 8: Now add STEP8 from your own file and run the ancestor query again. Record exactly ... ----
# RuntimeError (depth 60); without bound -> RecursionError. See note.txt.




# ==================================================================== THE STAMP -- DO NOT EDIT
# Computed from YOUR parameters and the answer YOUR OWN code produced. Run this last, and put the
# printed line in stamp.txt.
def stamp(student_no, activity, *values):
    payload = '|'.join([str(student_no).strip(), str(activity)] + [repr(v) for v in values])
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()[:10].upper()


if __name__ == '__main__':
    # grandparents -> every grandparent your engine finds, as a tuple of
    #                 (older, younger) tuples, sorted alphabetically.
    grandparents = (('gina', 'dina'), ('gina', 'olen'), ('gina', 'pia'), ('hugo', 'ben'),
                    ('hugo', 'ivy'), ('hugo', 'nico'), ('hugo', 'rey'))  # what my query() returned, sorted
    print(stamp(STUDENT_NO, 3, tuple(tuple(f) for f in FACTS), grandparents))
