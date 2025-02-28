#######################################################
# PYTHON İLE VERİ ANALİZİ (DATA ANALYSIS WITH PYTHON)
#######################################################
# - NumPy
# - Pandas
# - Veri Görselleştirme: Matplotlib & Seaborn
# - Gelişmiş Fonksiyonel Keşifçi Veri Analizi (Advanced Functional Exploratory Data Analysis)

#######################################################
# NUMPY
#######################################################

# Neden NumPy (Why Numpy?)
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
# Numpy Array Özellikleri (Attributes of Numpy Arrays)
# Yeniden Şekillendirme(Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)

###############################
# Neden NumPy (Why Numpy?)
###############################

import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b

###############################
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
###############################
import numpy as np

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype=int)
np.random.randint(0, 10, size=10)
np.random.normal(10, 4, (3, 4))

###############################
# Numpy Array Özellikleri (Attributes of Numpy Arrays)
###############################
import numpy as np

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)
a.ndim
a.shape
a.size
a.dtype
