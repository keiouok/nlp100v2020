import sys
import pandas as pd

if len(sys.argv) == 1:
    print("Set arg n, like 'python ans14.py 5'")
else:
    n = int(sys.argv[1])
    df = pd.read_csv("./popular-names.txt", sep="\t", header=None)
    nrow = -(-len(df) // n)
    for i in range(n):
        df.loc[nrow*i:nrow*(i+1)].to_csv(f"ans16_{i}", sep="\t", index=False, header=None)
