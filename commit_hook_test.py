import os

import pandas as pd

from new_directory.transfomers import double_number

M = 166_000
r = 3.2
n = 0
m = 1000

while M > 0:
    M = (M - 12 * m) * (1 + r / 100)
    print(M)
    n += 1

print(n)
