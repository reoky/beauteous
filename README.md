# Beauteous
Beauteous is a simple library for coloring terminal output in a templatized fashion. There is support for the following items, and for many people, this may be all you need.

- Build templates as bytes
- Write templates to terminal
- Return specific codes and specials
- Output specific codes to terminal
- Interactive mode for building colored byte arrays

write_msg(text, fg, bg)
build_msg(text, fg, bg)
write_template(template, data)
build_template(template, data)
write_reset()

In general writes output to the terminal, whereas builds return only the bytes for use on a remote terminal.

## Using Beauteous
Below you can find some code examples of templates and bindings. These should be pretty straight forward, and you can use them in your coding:

# Use this test to 
write_template("""
  This is a {value_one} of the multiple colors and
  multiple lines. {value_two} {blue} daba dee daba di.
  The text might {value_three} come out {red}.
  """, {
  "value_one": "test",
  "value_two": "I'm",
  "value_three": "also"
})