
#  noktasal data görünüm
import pandas as pd
import numpy as np
df = pd.DataFrame(linear_regcsv,columns=["yil","maas"])
import matplotlib.pyplot as mt
mt.scatter(df.yil,df.maas)

#plot data
import pandas as dd
import matplotlib.pyplot as mt
df = dd.read_csv("linear_reg.csv",sep=";")
mt.scatter(df.yil,df.maas)
mt.xlabel="Deneyim"
mt.ylabel="Maas"
mt.show()

