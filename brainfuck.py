# brainfuck interpreter
# i am not adding the comma.

import sys
sys.tracebacklimit = 3 # 3 is a good value. it is not a myth so its automatically the best number ever. if you disagree with me i will contact my lawyer and fine you 500 dollars for every word you speak until you say "level 3 is the best ever cool yes wow".


memory = [0] * 512 # limitations

class Error(Exception):
  def __init__(self, message):
    self.message = message
    super().__init__("customError")

  def __str__(self):
    sys.tracebacklimit = 0
    return self.message


def run(commands: str):
  pos = 0 # first item in memory
  depth = 0 # 0 = main
  repdep = []
  x = 0 # you little trickster!
  cmds = commands + "!"
  popped = 0
  while x <= len(cmds): # what
    match cmds[x]:
      case "!":
        break
      case "+":
        if memory[pos] > 255:
          raise Error("Each memory cell has a maximum value of 255.")
        else:
          memory[pos] = memory[pos] + 1
      case "-":
        if memory[pos] < 1:
          raise Error("Each memory cell has a minimum value of 0.")
        else:
          memory[pos] = memory[pos] - 1
      case ">":
        if pos > 511:
          raise Error("Cannot go outside of memory bounds!")
        else:
          pos += 1
      case "<":
        if pos < 0:
          raise Error("Cannot go outside of memory bounds!")
        else:
          pos -= 1
      case ".":
        print(memory[pos])
      case ",":
        print("I am NOT!! adding the comma function.")
      case "[":
        if len(repdep) < 1:
          repdep.append(x)
        elif repdep[-1] != (pos):
          repdep.append(x)
        depth += 1
      case "]":
        if memory[pos] != 0:
          x = repdep[-1]
        else:
          depth -= 1
          popped = repdep.pop()
        if depth < 0:
          raise Error("Unmatched ] detected.")
      case _:
        pass
        # things that the runner dont know, the runner dont care about!
        # that's how comments work, you know!
    x += 1
  if depth > 0:
    raise Error("Unmatched [ detected.")

exex = "+++++[->+>++>+++<<<].>.>.>.>.>.>.>.>.>.>."
run(exex)
print(memory[0:10])
