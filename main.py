def pangram(entry):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  for i in alphabet:
    if i in entry.lower():
      Pangram = True
    else:
      Pangram = False
  print(f'Pangram = {Pangram}')

sent = input('Enter a sentence, the program will determine whether it is an pangram or not. \nEntry: ')
pangram(sent)
