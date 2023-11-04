import requests
import os


VERSION = "1.2.0"
VERSION_DATE = "15.08.2023"


def inputVar(printText = ""):
  var = input(printText)
  print(f"Inputted: '{var}'.")

  return var

def replaceStringChars(string, chars, replaceTo = "_"):
  for char in chars:
    string = string.replace(char, replaceTo)
  
  print(f"Replaced special characters in string. New string: '{string}'.")

  return string

def subtractString(string, i1):
  string = string[i1:]
  
  print(f"String subtracted. New string: '{string}'.")

  return string

def getUrl(url):
  print(f"Requesting '{url}'...")
  
  req = requests.get(url)
  
  print(f"Request status code: '{req.status_code}'.")

  return req

def fWrite(path, content):
  print(f"Writing file to '{path}'...")
  
  with open(path, "wb") as file:
    file.write(content)

  print(f"Wrote file to '{path}'.")

  return


def main():
  specialChars = "#%&}{\\><*?/ $!'\":@+`|="
  filenameLengthLimit = 250

  d = inputVar("Save directory: ")
  url = ""

  while True:
    inp = inputVar("URL or /d: ")

    if inp == "/d":
      d = inputVar("Save directory: ")
      continue
    elif inp == "/q":
      break


    url = inp
    filename = replaceStringChars(url, specialChars)

    req = getUrl(url)

    if len(filename) > filenameLengthLimit:
      filename = subtractString(len(filename) - filenameLengthLimit)


    fWrite(os.path.join(d, filename), req.content)

    
    print("Done.\n")

  return


if __name__ == "__main__":
  main()
