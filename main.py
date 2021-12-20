def puzzleInput():
  with open("puzzle.txt", "r") as file:
    lines = file.readlines()
    fixed_lines = [line.replace("\n","") for line in lines]
    return fixed_lines


lista = puzzleInput()
# print(lista)

def getHorizontalPos(lista):
  horizontal = 0
  depth = 0
  for line in lista:
    if "forward" in line:
      horizontal = horizontal + int(line[-1])
    elif "down" in line:
      depth += int(line[-1])
    elif "up" in line:
      depth -= int(line[-1])

  return horizontal * depth
      
  
res = getHorizontalPos(lista)
print(res)
