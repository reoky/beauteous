#!/usr/bin/python
import struct
import sys

# It's time to make your terminal beauteous

special = {
  "reset":   b"\x1b\x5b\x00\x6d",
  "terminator": b"\x6d",
  "concat": b"\x3b",
  "newline": b"\x0a"
}

ansicodes = {

  # Foreground Colors
  "black":   b"\x1b\x5b\x33\x30",
  "red":     b"\x1b\x5b\x33\x31",
  "green":   b"\x1b\x5b\x33\x32",
  "yellow":  b"\x1b\x5b\x33\x33",
  "blue":    b"\x1b\x5b\x33\x34",
  "magenta": b"\x1b\x5b\x33\x35",
  "cyan":    b"\x1b\x5b\x33\x36",
  "white":   b"\x1b\x5b\x39\x37",
  "light_grey":    b"\x1b\x5b\x33\x37",
  "dark_grey":     b"\x1b\x5b\x39\x30",
  "light_red":     b"\x1b\x5b\x39\x31",
  "light_green":   b"\x1b\x5b\x39\x32",
  "light_yellow":  b"\x1b\x5b\x39\x33",
  "light_blue":    b"\x1b\x5b\x39\x34",
  "light_magenta": b"\x1b\x5b\x39\x35",
  "light_cyan":    b"\x1b\x5b\x39\x36",

  # Background Colors
  "bg_black":   b"\x1b\x5b\x34\x30",
  "bg_red":     b"\x1b\x5b\x34\x31",
  "bg_green":   b"\x1b\x5b\x34\x32",
  "bg_yellow":  b"\x1b\x5b\x34\x33",
  "bg_blue":    b"\x1b\x5b\x34\x34",
  "bg_magenta": b"\x1b\x5b\x34\x35",
  "bg_cyan":    b"\x1b\x5b\x34\x36",
  "bg_white":   b"\x1b\x5b\x31\x30\x37",
  "bg_light_grey":    b"\x1b\x5b\x34\x37",
  "bg_dark_grey":     b"\x1b\x5b\x31\x30\x30",
  "bg_light_red":     b"\x1b\x5b\x31\x30\x31",
  "bg_light_green":   b"\x1b\x5b\x31\x30\x32",
  "bg_light_yellow":  b"\x1b\x5b\x31\x30\x33",
  "bg_light_blue":    b"\x1b\x5b\x31\x30\x36",
  "bg_light_magenta": b"\x1b\x5b\x31\x30\x35",
  "bg_light_cyan":    b"\x1b\x5b\x31\x30\x34"
}

# Sets the color escape code with an optional bgcolor
def write_code(fg=None, bg=None):
  validate_color(fg, bg)
  if (fg in ansicodes):
    sys.stdout.write(get_code(fg))
  if (bg in ansicodes):
    sys.stdout.write(get_code("concat"))
    sys.stdout.write(get_code(bg))
  sys.stdout.write(get_code("terminator"))

# Returns a specific color code
def get_code(fg=None, bg=None):
  result = b""

  # Return reset if this isn't a real color combo
  if (not validate_color(fg, bg)):
    return get_reset()

  # Add a fg color
  if (fg in ansicodes):
    result += ansicodes[fg]

  # Add in a bg color or just start with one if
  # there was no fg color
  if (bg in ansicodes):
    if (result):
      result += special["concat"]
    result += ansicodes[bg]

  # Finally apply a terminator and return
  result += special["terminator"]
  return result

# Changes back to the default color
def write_reset():
  sys.stdout.write(get_reset())

# Changes back to the default color
def get_reset():
  return(special["reset"])

# Color terminal text
def write_msg(text, fg=None, bg=None):
  sys.stdout.write(build_msg(text, fg, bg))
  sys.stdout.write(special["newline"])

# Returns the raw bytes for use on a remote terminal
def build_msg(text, fg=None, bg=None):
  result = b""
  if (validate_color(fg, bg)):
    if (text != None):
      return get_code(fg, bg) + text + get_reset()

# Tests to see when the fg or bg are valid ansi colors
# and returns either true or false
def validate_color(fg, bg):
  if (fg in ansicodes):
    return True
  if (bg in ansicodes):
    return True
  return False

# Writes a template to the terminal
def write_template(template, data):
  sys.stdout.write(build_template(template, data))

# Accepts a multiline string with python template 
def build_template(template, data):
  if (type(template) is str() and type(data) is dict()):

    # Insert color values or replace exiting values
    # for colors, allowing the user to decorate the
    # template with custom data
    try:
      result = template
      for code in ansicodes:
        data[keys] = code
      return result.format(data)
    except Exception as e:
      write_msg("Could not decorate template with colors: %s" % str(e))

  return special["reset"]

# cycles through all the colors as a test
def test_beauteous():

  # Test basic hello world
  print("This is a %stest%s. Now cycling through the colors." % (
    get_code("red"), get_reset()
  ))

  # Test each foreground and background color on its own
  for key in ansicodes:
    write_msg("Testing %s" % key, key)

  # Test decorated templates
  write_template("""
    This is a {value_one} of the multiple colors and
    multiple lines. {value_two} {blue} daba dee daba di.
    The text might {value_three} come out {red}.
  """, {
    "value_one": "test",
    "value_two": "I'm",
    "value_three": "also"
  })

  # Let the user know that terminals vary.
  print("Note that some colors may be %sdifferent%s on your terminal." % (
    get_code("blue"), get_reset()
  ))

# Point of entry
if (__name__ == "__main__"):
  args = sys.argv
  if (len(args) > 1):
    if (sys.argv[1] == "test"):
      test_beauteous()
    elif (sys.argv[1] == "template"):
      template = input("Please enter a {{template}}.")
      if (template != None):
        data = input
        binascii.hexlify(build_template(template, data))
    else:
      print('Entering Interactive Mode...')
