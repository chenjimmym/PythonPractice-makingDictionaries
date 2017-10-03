def make_dict(arr1, arr2):
  new_dict = {}
  temp = zip(arr1, arr2)
  #print temp
  new_dict = dict(temp)
  print new_dict
  return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

make_dict(name, favorite_animal)