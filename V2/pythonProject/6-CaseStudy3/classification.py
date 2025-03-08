import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

#region Görev 1
# Soru1 : miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
df = pd.read_excel("6-CaseStudy3/gezinomi_tanitim/miuul_gezinomi.xlsx")
df.head()
# Soru2: Kaç unique şehir vardır? Frekanslarınedir?
df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()

# Soru3:Kaç unique Concept vardır?
df["ConceptName"].nunique()

# Soru4: Hangi Concept’den kaçar tane satış gerçekleşmiş?
df.groupby("ConceptName").agg({"ConceptName": "count"})

# Soru5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("SaleCityName").agg({"Price": "sum"})

# Soru6: Concept türlerine göre göre ne kadar kazanılmış?
df.groupby("ConceptName").agg({"Price": "sum"})

# Soru7: Şehirlere göre PRICE ortalamaları nedir?
df.groupby("SaleCityName").agg({"Price": "mean"})

# Soru8: Conceptlere göre PRICE ortalamaları nedir?
df.groupby("ConceptName").agg({"Price": "mean"})

# Soru9: Şehir-Concept kırılımındaPRICE ortalamalarınedir?
df.groupby(["SaleCityName", "ConceptName"]).agg({"Price": "mean"})
#endregion