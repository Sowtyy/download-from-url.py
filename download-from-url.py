import requests


def inputVar(printText = ""):
  var = input(printText)
  print(var)

  return var

def replaceStringChars(string, chars, replaceTo = "_"):
  for char in chars:
    string = string.replace(char, replaceTo)
  
  print(string)

  return string

def subtractString(string, i1):
  string = string[i1:]
  print(string)

  return string

def getUrl(url):
  req = requests.get(url)
  print(req.status_code)

  return req

def fWrite(path, content):
  with open(path, "wb") as file:
    file.write(content)

  return


def main():
  specialChars = "#%&}{\\><*?/ $!'\":@+`|="
  filenameLengthLimit = 250

  d = inputVar("Save directory: ")
  url = ""

  while True:
    filename = ""
    inp = inputVar("URL or /d: ")

    if inp == "/d":
      d = inputVar("Save directory: ")
      continue
    elif inp == "/q":
      break


    url = inp
    filename = url

    req = getUrl(url)

    filename = replaceStringChars(filename, specialChars)

    if len(filename) > filenameLengthLimit:
      filename = subtractString(len(filename) - filenameLengthLimit)


    fWrite(d + "/" + filename, req.content)

    
    print("Done.\n")

  return


if __name__ == "__main__":
  try:
    main()
  except Exception as e:
    print("-- error in main:", repr(e))
    input()
