improt sys
improt random

def clean():
  istring = "";

def iao(times):
  word = "";
  text = "";
  index = -1;
  while index < times:
    word = raw_input("\nPlease enter a sentence:\n");
    text = text + "\n" + word;
    index += 1;
  return text;

def sortm(ofs):
  if ofs.lower() == "stop" or ofs.lower() == "end" or ofs.lower() == "quit" or ofs.lower() == "exit":
    print "OK, now you stop this program.";
    sys.exit();
  else:
    ofs = int(ofs)-1;
    if type(ofs) == int:
      text = iao(ofs);
      print "\n--------------------------------", text, "\n--------------------------------";
    else:
      print "\nError: You can't enter string, boolean, or other things\n";

def main():
  clean();
  while True:
    istring = raw_input("Please enter run times: ");
    sortm(istring);

main();
