translations = {
  "hello":"hola",
  "thank you":"gracias",
  "sorry":"lo siento",
  "goodbye":"adios",
  "son":"hijo",
  "daughter":"hija",
  "baby":"bebé",
  "grandson":"nieto",
  "granddaughter":"nieta",
}

done = False
while not done:
  print('Type "done" at any time to exit')
  word = (input("Type an English word: ")).lower()
  # Check whether "done" entered
  if (word == "done"):
    done = True
  elif (word.lower() in translations):
    print ('The Spanish word is "' + translations.pop(word) + '"')
  else:
    print ("Word not listed in dictionary")

