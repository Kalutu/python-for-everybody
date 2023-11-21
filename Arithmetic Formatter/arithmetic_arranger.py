import operator
test = ["32 + 8","1 - 3801", "9999 + 9999", "523 - 49"]
def error(strin):
    try:
        l_strin = strin.split()
        assert len(l_strin[0])<7, "Numbers cannot be more than six digits"
        assert len(l_strin[2])<7, "Numbers cannot be more than six digits"
    except AssertionError:
        return "Numbers cannot be more than six digits"
    try:
        x, y = l_strin[0], l_strin[2]
        assert l_strin[0].isdigit(), "Numbers must only contain digits"
        assert l_strin[2].isdigit(), "Numbers must only contain digits"
    except AssertionError:
        return "Numbers must only contain digits"
        
    try:
        ops = { "+": operator.add, "-": operator.sub }
        assert l_strin[1] in ops.keys(), "Operator must be"
    except Exception:
        return "Operator must be '+' or '-' "
    return ""
def arithmetic_arranger(list_of_strings, display=False):
    try:
        assert len(list_of_strings)<=7, "Too many Problems"
    except AssertionError:
        return "Too many problems"
    line1 = line2 = line3 = line4 = ""
    side_space = "    "
    first = True
    for i in list_of_strings:
        start = error(i)
        if start != "":
            return start
        l_strin = i.split()
        x, y = l_strin[0], l_strin[2]
        l_strin[0] = int(l_strin[0])
        l_strin[2] = int(l_strin[2])
        space = max(len(x), len(y))
        ops = { "+": operator.add, "-": operator.sub }
        if l_strin[1] in ops.keys():
            result = (ops[l_strin[1]](l_strin[0], l_strin[2]))
        if(first == True):
            line1 += x.rjust(2 + space)
            line2 += l_strin[1].ljust(2) + y.rjust(space)
            line3 += "-" * (space + 2)
            if display == True:
                line4 += str(result).rjust(space + 2)
            first = False
        else:
            line1 += x.rjust(space + 6)
            line2 += l_strin[1].rjust(5) + y.rjust(space + 1)
            line3 += side_space + "-" * (space + 2)
            if display == True:
                line4 += side_space + str(result).rjust(space + 2)
                
    if display == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line3
    return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line3
    
    

print(arithmetic_arranger(test, True))