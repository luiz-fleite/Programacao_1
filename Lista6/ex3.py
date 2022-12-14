import pandas as pd
import glob

# recebendo o arquivo apenas cbo 2010-2020
file_list = glob.glob("CBO20[1-2][0-9].csv")
df_cbo = pd.DataFrame(pd.read_csv(file_list[0]))
for i in range(1, len(file_list)):
    data = pd.read_csv(file_list[i])
    df = pd.DataFrame(data)
    df_cbo = pd.concat([df_cbo, df], axis=1)
print(df_cbo)
df_cbo.to_csv("only_cbo.csv", sep=";")
