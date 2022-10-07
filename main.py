def pangram(entry):
  Pangram = False
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  for zq in alphabet:
    if zq in entry.lower():
      Pangram = True
      print(f'The entry was: {entry}')
      print(f'Pangram = {Pangram}')
      quit()
    else:
      Pangram = False
      print(f'The entry was: {entry}')
      print(f'Pangram = {Pangram}')
      quit()

sent = input('Enter a sentence, the program will determine whether it is an angram or not. \nEntry: ')
pangram(sent)
