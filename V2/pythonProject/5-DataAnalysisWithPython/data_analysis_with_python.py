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

###############################
# Yeniden Şekillendirme(Reshaping)
###############################
import numpy as np

np.random.randint(1, 10, size=9)
np.random.randint(1, 10, size=9).reshape(3, 3)

ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)

np.random.randint(1, 10, size=10).reshape(3, 3)

###############################
#  Index Seçimi (Index Selection)
###############################
import numpy as np

a = np.random.randint(10, size=10)
a[0]
a[0:5]
a[0] = 999

m = np.random.randint(10, size=(3, 5))
m[0, 0]
m[1, 1]
m[2, 3]

m[2, 3] = 999

m[2, 3] = 2.9

m[:, 0]
m[1, :]
m[0:2, 0:3]

###############################
# Fancy Index
###############################
import numpy as np

v = np.arange(0, 30, 3)
v[1]
v[4]

catch = [1, 2, 3]

v[catch]

###############################
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
###############################
import numpy as np

v = np.array([1, 2, 3, 4, 5])

###############################
# Klasik Döngü İle
###############################

ab = []
for i in v:
    print(i)

for i in v:
    if i < 3:
        ab.append(i)

###############################
# Numpy İle
###############################
v < 3

v[v < 3]
v[v > 3]
v[v != 3]
v[v == 3]
v[v >= 3]
