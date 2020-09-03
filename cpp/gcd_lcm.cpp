ll gcd(ll x, ll y) {
    if (x > y) swap(x, y);
    if (x == 0) return y;
    return gcd(x, x%y);
};

ll lcm(ll x, ll y) {
    return x*y/gcd(x, y);
};