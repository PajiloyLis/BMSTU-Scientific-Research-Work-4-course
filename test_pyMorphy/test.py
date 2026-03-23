import pymorphy3 

analyzer = pymorphy3.MorphAnalyzer()
print(*analyzer.parse("нейросеть"), sep='\n')

