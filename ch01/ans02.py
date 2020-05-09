S = "パタトクカシーー"
for i in range(len(S)):
    if i % 2 != 0:
        print(S[i], end="")
print()

# upura ans
text = S
print(text[1::2])