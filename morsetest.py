import morse

test = "this is a test, 123."
print(test)
f = morse.encodeMorse(test)
print(f)
print(morse.decodeMorse(f +" / .- -. -..  / .-. . ...- . .-. ... ."))
