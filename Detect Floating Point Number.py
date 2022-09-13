# Detect Floating Point Number
import re
n = int(input())
for _ in range(n):
    inp = str(input())
    ans = re.compile(r'^[-+]?[0-9]*\.[0-9]+$')
    print(bool(re.fullmatch(ans,inp)))