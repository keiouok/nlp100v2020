import sys
import pandas as pd

if len(sys.argv) == 1:
    print("Set arg n, like 'python ans14.py 5'")
else:
    n = int(sys.argv[1])
    df = pd.read_csv("./popular-names.txt", sep="\t", header=None)
    print(df.tail(n))