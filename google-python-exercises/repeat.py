def repeat(s, exclaim):
  """
  Hey so this is a multiline
  comment.
  """
  s = s*3
  if exclaim:
    s += "!!!"
  return s

def main():
  name = "sourab"
  if name == "sourabh":
    # Error and typo, but python fails to flag it at compile time and program
    # runs as normal since this code won't get execute.
    printt("dummy")
  else:
    print(repeat("hey", True))
    print(repeat("hey", False))

if __name__ == "__main__":
  main()
