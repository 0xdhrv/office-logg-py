import main as l

l.amOut = True

helpMessage = """
description: a simple logger written in python, as a console 
    application, that is completely off the grid

usage: logg.py
    options:
      i, to trigger in event, and enter in time
      o, to trigger out event, and enter out time
      t, to see time elapsed
      l, to see time left
      s, to send message, to log message
      q, to quit application
      h, to display this help message
"""

print('+ lOgg v0.0')

def menu():
  print('|')
  choice = input('| ')
  print('|')

print('|')
choice = input('| ')
print('|')

while(True):
  if(choice.lower() == 'i'):
    message = input('| In : ')
    l.inn(message)
  elif(choice.lower() == 'o'):
    message = input('| Ot : ')
    l.out(message)
  elif(choice.lower() == 's'):
    message = input('| Ms : ')
    l.snd(message)
  elif(choice.lower() == 't'):
    l.tot()
  elif(choice.lower() == 'l'):
    l.lef()
  elif(choice.lower() == 'h'):
    print(helpMessage)
  elif(choice.lower() == 'q'):
    print('+ Quit')
    break  
  else:
    print('| Error')
  print('|')
  choice = input('| ')
  print('|')
  