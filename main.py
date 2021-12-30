import random

data = [0]
num = 0
name = ''

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

while num != -1 or name != '-1':
  name = input('Name: ')
  if name == '':
    print(f"{bcolors.WARNING}Plz Enter a Name!{bcolors.ENDC}\n")
    continue

  if name == 'p':
    break

  num = input("Number: ")
  try:
    num = int(num)
  except ValueError:
    print(f"{bcolors.FAIL}Guarbage Number!{bcolors.WARNING} Try Again!{bcolors.ENDC}\n")
    continue
  if name and num:
    if data[0] == 0:
      data.pop() 
    data.append([name, num])
    print(f"{bcolors.OKCYAN}Have a good luck!{bcolors.ENDC}")
  print('\n')

data.pop()

print("The Winners are:")
for idx, elem in enumerate([random.choice(data) for _ in range(3)]):
  print(f"{idx + 1} - {elem[0]} with number {elem[1]}")

print(f"\n{bcolors.OKGREEN + bcolors.BOLD}Congrats!{bcolors.ENDC}\n\n")

print(f"\t\t{bcolors.BOLD + bcolors.WARNING}Copyrights are reserved to the author, Eng. Mohammad Basyouni{bcolors.ENDC}\n")
