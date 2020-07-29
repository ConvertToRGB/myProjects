#!python2
def allSum(src):
    s = 0
    for i in src:
        if i.isdigit():
            s += int(i)
    return s

ok = True

while ok:
    src  = str(raw_input("enter number: (type 's' to stop) "))
    if src == "s":
        ok = False
    result = allSum(src)
    print result

    