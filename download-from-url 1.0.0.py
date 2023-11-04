import requests


def main():
  specialChars = "#%&}{\\><*?/ $!'\":@+`|="
  filenameLengthLimit = 250

  d = input("Save directory: ")
  print(d)
  url = ""
  filename = ""

  while True:
    filename = ""
    url = input("URL: ")
    print(url)

    req = requests.get(url)
    print(req.status_code)

    filename = url
    for specialChar in specialChars:
      filename = filename.replace(specialChar, "_")
      print(filename)

    if len(filename) > filenameLengthLimit:
      filename = filename[len(filename) - filenameLengthLimit:]
      print(filename)

    with open(d + "/" + filename, "wb") as file:
      file.write(req.content)

    print("Done\n")

  return


try:
  main()
except Exception as e:
  print("-- error in main:", repr(e))

input()
