def strcounter(s):
    syms_count = {}
    for sym in s:
        syms_count[sym] = syms_count.get(sym, 0) + 1

    for sym, count in syms_count.items():
        print(sym, count)




strcounter('aab')