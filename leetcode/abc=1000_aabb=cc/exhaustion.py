# 如果 a+b+c=1000, 且a^2+b^2=c^2  求出所有a,b,c可能的组合

import time
star_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a+b+c == 1000 and a**2+b**2 == c**2:
                print(a, b, c)
end_time = time.time()
print("time:%d" % (end_time - star_time))
