from collections import Counter
import math
import pandas as pd
# Calculamos la entropía de Shannon

filename = 'E:/UNAP/UNAP-IV/LENGUAJES DE PROGRAMACION II/PROGRAMAS/cuento.txt'
with open(filename, 'r') as file:
    content = file.read()
    words = content.split()

count_words = pd.Series(Counter(words))
total_words = len(words)
entropy = 0

def shannon_entropy(p):
    return -p * math.log2(p)

for word, count in count_words.items():
    p = count / total_words
    entropy += shannon_entropy(p)

print(f"Palabras: {count_words}")
print(f"Entropía: {entropy}")