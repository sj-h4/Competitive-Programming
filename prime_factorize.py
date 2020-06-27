def eratosthenes(n):
    prime = [2]
    limit = int(n**0.5)
    prime_list = [i + 1 for i in range(2, n, 2)]
    while True:
        p = prime_list[0]
        if limit <= p:
            return prime + prime_list
        prime.append(p)
        prime_list = [e for e in prime_list if e % p != 0]

def prime_factorize(n):
    prime_list = eratosthenes(n)
    arr = []

    for p in prime_list:
        if n % p == 0:
            cnt = 0
            while n % p == 0:
                n //= p
                cnt += 1
            arr.append([p, cnt])
    
    return arr
