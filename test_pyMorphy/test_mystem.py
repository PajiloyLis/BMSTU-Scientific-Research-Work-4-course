import pymystem3

m = pymystem3.Mystem()

lemmas = m.lemmatize("нейросеть")
print(''.join(lemmas))
print(m.analyze("нейросеть"))
