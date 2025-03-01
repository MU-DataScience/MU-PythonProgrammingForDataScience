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
