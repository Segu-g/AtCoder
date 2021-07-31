s = input()
odd = s[::2]
even = s[1::2]
if odd == odd.lower() and even == even.upper():
    print("Yes")
else:
    print("No")
