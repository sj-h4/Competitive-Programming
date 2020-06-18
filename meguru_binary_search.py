def is_ok(arg):
    # 条件
    pass

def meguru_binary_search(ng, ok):
    while abs(ng - ok) > 1:
        mid = (ng + ok) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
