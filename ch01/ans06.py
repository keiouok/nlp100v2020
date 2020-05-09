def n_gram(target, n):
    return [target[idx:idx+n] for idx in range(len(target) - (n - 1))]

WordA = "paraparaparadise"
WordB = "paragraph"
X = n_gram(WordA, 2)
Y = n_gram(WordB, 2)
t = "se"
print(f"和集合:{set(X) | set(Y)}")
print(f"積集合:{set(X) & set(Y)}")
print(f"差集合:{set(X) - set(Y)}")
print("se" in (set(X) & set(Y)))
