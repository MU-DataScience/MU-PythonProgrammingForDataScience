import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
pd.set_option("display.float_format", lambda x: '%.2f' % x)

# region Görev 1
# Soru1 : miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
df = pd.read_excel("6-CaseStudy3/gezinomi_tanitim/miuul_gezinomi.xlsx")
df.head()
df.shape
df.info()
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
df.groupby(by=["SaleCityName", "ConceptName"]).agg({"Price": "mean"})
# endregion
# region Görev 2 SaleCheckInDayDiff değişkenini kategorik bir değişkene çeviriniz.
# SaleCheckInDayDiff değişkeni müşterinin CheckIn tarihinden ne kadar önce satin alımını tamamladığını gösterir.
# Aralıkları ikna edici şekilde oluşturunuz.
# Örneğin: ‘0_7’, ‘7_30', ‘30_90', ‘90_max’ aralıklarını kullanabilirsiniz.
# Bu aralıklar için "Last Minuters", "Potential Planners", "Planners", "Early Bookers“ isimlerini kullanabilirsiniz

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max() + 1],
                        labels=["Last Minuters", "Potential Planners", "Planners", "Early Bookers"])
# endregion
# region Görev 3: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
# Şehir-Concept-EB Score, Şehir-Concept- Sezon, Şehir-Concept-CInDay kırılımında ortalama ödenen ücret ve yapılan işlem sayısı cinsinden inceleyiniz.


df.groupby(["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price": ["mean", "count"]}).head()
df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean", "count"]}).head()
df.groupby(["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean", "count"]}).head()
# endregion
#region Görev 4: City-Concept-Season kırılımının çıktısını PRICE'a göre sıralayınız.
# Elde ettiğiniz çıktıyı agg_df olarak kaydediniz.
agg_df = df.groupby(["SaleCityName","ConceptName","Seasons"]).agg({"Price":"mean"}).sort_values("Price",ascending=0)
#endregion