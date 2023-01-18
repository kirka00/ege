slovar = {"кот": "cat",
          "мышь": "mouse",
          "собака": "dog",
          "животные": "animals",
          "солнце": "солнце",
          "машина": "car",
          "и": "and",
          "или": "or",
          "пока": "while"}
print(', '.join([key for key in slovar.keys() if len(key) <= 3]))
print(', '.join([slovar[i]
      for i in [key for key in slovar.keys() if len(key) >= 2]]))
