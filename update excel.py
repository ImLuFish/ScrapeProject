import main
import pandas as pd
import numpy as np
import time

Sc = main.Scrape()

df = pd.read_excel("peptide sequence.xlsx")
df["averge"] = np.NaN
df["min"] = np.NaN
df["max"] = np.NaN

for i in range(5):
    seq = df.loc[i, "sequence"]
    print("Now: ", i, ", sequence is ", seq)
    result = Sc.get_result(seq, method="Parker")
    df.loc[i, "average"] = eval(result[0])
    df.loc[i, "min"] = eval(result[1])
    df.loc[i, "max"] = eval(result[2])
    time.sleep(3)

df.to_csv("result.csv", index=False)