#######################################################
# PANDAS
#######################################################

# Pandas Series
# Veri Okuma (Reading Data)
# Veriye Hızlı Bakış (Quick Look Data)
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# Apply ve Lambda
# Birleştirme (Join) İşlemleri

################################
# Pandas Series
################################
import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
type(s)
s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)
s.head(3)
s.tail(3)

################################
# Veri Okuma (Reading Data)
################################
import pandas as pd

df = pd.read_csv("5-DataAnalysisWithPython/datasets/advertising.csv")
df.head()
# pandas cheatsheet

################################
# Veriye Hızlı Bakış (Quick Look at Data)
################################
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()
df["sex"].head()
df["sex"].value_counts()

################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
################################
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]
df.drop(0, axis=0).head()

delete_index = [1, 3, 5, 7]
df.drop(delete_index, axis=0).head(10)

# df = df.drop(delete_index,axis=0)
# df = df.drop(delete_index,axis=0, inplace=True)

##########################
# Değişkeni Index'e Çevirmek
##########################

df["age"].head()
df.age.head()

df.index = df["age"]

df.drop("age", axis=1).head()

df.drop("age", axis=1, inplace=True)
df.head()

##########################
# Indexi Değişkene Çevirmek
##########################

df.index

df["age"] = df.index

df.head()
df.drop("age", axis=1, inplace=True)

df = df.reset_index().head()

################################
# Değişkenler Üzerinde İşlemler
################################
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

"age" in df

df["age"].head()
df.age.head()

df["age"].head()
type(df["age"].head())

df[["age"]].head()
type(df[["age"]].head())

df[["age", "alive"]]

col_names = ["age", "adult_male", "alive"]
df[col_names]

df["age2"] = df["age"] ** 2
df["age3"] = df["age"] / df["age2"]

df.drop("age3", axis=1).head()

df.drop(col_names, axis=1).head()

df.loc[:, ~df.columns.str.contains("age")].head()

################################
# iloc & loc
################################
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# iloc: integer based selection
df.iloc[0:3]
df.iloc[0, 0]

# loc: label based selection
df.loc[0:3]

df.iloc[0:3, 0:3]
df.loc[0:3, "age"]

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]

################################
# Koşullu Seçim (Conditional Selection)
################################
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count()

df.loc[df["age"] > 50, ["age", "class"]].head()

df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()

df["embark_town"].value_counts()

df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male") & (
        (df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()

################################
# Toplulaştırma & Gruplama (Aggregation & Grouping)
################################

# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
# - pivot table

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean()

df.groupby("sex")["age"].mean()

df.groupby("sex").agg({"age": "mean"})
df.groupby("sex").agg({"age": ["mean", "sum"]})

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})

df.groupby(["sex", "embark_town"]).agg({"age": "mean",
                                        "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": "mean",
                                                 "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({
    "age": "mean",
    "survived": "mean",

    "sex": "count"})

################################
# Pivot Table
################################
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived", "sex", "embarked")

df.pivot_table("survived", "sex", "embarked", aggfunc="std")

df.pivot_table("survived", "sex", ["embarked", "class"], aggfunc="std")

df.head()

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
df.head()

df.pivot_table("survived", "sex", ["new_age"])
df.pivot_table("survived", "sex", ["new_age", "class"])

# pd.set_option('display.width',500)
pd.set_option('display.width', 500)

################################
# Pivot Table
################################
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5

(df["age"] / 10).head()
(df["age2"] / 10).head()
(df["age3"] / 10).head()

for col in df.columns:
    if "age" in col:
        df[col] = df[col] / 10

df.head()

df[["age", "age2", "age3"]].apply(lambda x: x / 10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()


def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()


df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

df.loc[:, ["age", "age2", "age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)
df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.head()

################################
# Birleştirme (Join) İşlemleri
################################
import numpy as np
import pandas as pd

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2])

pd.concat([df1, df2], ignore_index=True)

#####################
# Merge ile Birleştirme İşlemleri
#####################

df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ["accounting", "engineering", "engineering", "hr"]})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
pd.merge(df1, df2, on="employees")

# Amaç her çalışanın müdürünün bilgisine erişmek istiyoruz.
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ["Caner", "Mustafa", "Berkcan"]})

pd.merge(df3,df4)