while True:
    mw, mi, tw, ti = input().split(' ')
    mw = int(mw)
    mi = int(mi)
    tw = int(tw) + 273
    ti = int(ti) + 273

    if mw == mi == tw == ti == 0:
        break

    cw = 4.19 * mw * tw
    ci = 2.09 * mi * ti

    em = 355

    if cw > ci:
        t = (ci + mw*tw)/(-mw - mi*em*ti)
        print(t)
    else:
        temp = 0
        print(t)


