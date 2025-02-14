import pystyle

default_print = print
default_input = input
def print(text : str):
  default_print(pystyle.Center.XCenter(pystyle.Colorate.Horizontal(pystyle.Colors.cyan_to_green, text)))
def input(text : str = "") -> str:
  default_input(pystyle.Center.XCenter(pystyle.Colorate.Horizontal(pystyle.Colors.cyan_to_green, text)))

def main():
  print("""███    ██ ███████ ██     ██         ███████  ██████ ██████  ██ ██████  ████████  ██████
████   ██ ██      ██     ██         ██      ██      ██   ██ ██ ██   ██    ██    ██  ████
██ ██  ██ █████   ██  █  ██         ███████ ██      ██████  ██ ██████     ██    ██ ██ ██
██  ██ ██ ██      ██ ███ ██              ██ ██      ██   ██ ██ ██         ██    ████  ██
██   ████ ███████  ███ ███  ███████ ███████  ██████ ██   ██ ██ ██         ██     ██████""")
  input()

main()
