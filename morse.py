morseTree = [" ", ["E", ["I", ["S", ["H", ["5", [""], [""]], ["4", [""], [""]]], ["V", ["", [""], [""]], ["3", [""], [""]]]], ["U", ["F", ["", [""], [""]], ["", [""], [""]]], ["", ["", ["?"], ["-"]], ["2", [""], [""]]]]], ["A", ["R", ["L", ["", [""], [""]], ["", ["\""], [""]]], ["", ["+", [""], ["."]], ["", [""], [""]]]], ["W", ["P", ["", [""], [""]], ["", ["@"], [""]]], ["J", ["", [""], [""]], ["1", ["\'"], [""]]]]]],["T", ["N", ["D", ["B", ["6", [""], ["-"]], ["=", [""], [""]]], ["X", ["/", [""], [""]], ["", [""], [""]]]], ["K", ["C", ["", [""], [""]], ["", [";"], [""]]], ["Y", ["(", [""], [")"]], ["", [""], [""]]]]], ["M", ["G", ["Z", ["7", [""], [""]], ["", [""], [","]]], ["Q", ["", [""], [""]], ["", [""], [""]]]], ["O", ["", ["8", [":"], [""]], ["", [""], [""]]], ["CH", ["9", [""], [""],],["0", [""], [""]]]]]]]

def decodeMorseCharacter(code, tree = morseTree):
    a = ""
    if len(tree) > 1 and len(code) > 0:
        if code[0] == ".":
            a = decodeMorseCharacter(code[1:],tree[1])
        else:
            if code[0] == "-":
                a = decodeMorseCharacter(code[1:],tree[2])
    else:
        a = tree[0]
    return a

def decodeMorse(code, tree = morseTree):
    a = ""
    for j in code.split(" / "):
        for i in j.split():
            a += decodeMorseCharacter(i, tree)
        a += " "
    return a
    
def encodeMorseCharacter(character, tree = morseTree, path = ""):
    r = ""
    if tree[0] == character:
        r = path
    else:
        if len(tree) == 3:
            p1 = encodeMorseCharacter(character, tree[1], path+".")
            if len(p1) > 0:
                r = p1
            else:
                p2 = encodeMorseCharacter(character, tree[2], path+"-")
                if len(p2) > 0:
                    r = p2
    return r

def encodeMorse(text, tree = morseTree):
    text = text.upper()
    a = ""
    for i in text:
        if i == " ":
            a += " / "
        else:
            a += encodeMorseCharacter(i, tree, "")
            a += " "
    return a
