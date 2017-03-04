# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import time
max_c = 997

def is_triplet(a,b,c):
    if a ** 2 + b ** 2 == c**2:
        print(a, b, c)
        return True

def check():
    for a in range(1, max_c + 1):
        print('current a: ', a)
        for b in range(a + 1, 1000 - a):
            #calculating c instead of iterating drops the time from
            # # Time: 9.92964 seconds to  Time: 0.08036 seconds
            c = 1000 - a - b
            if c < b:
                break
            if is_triplet(a,b,c):
                return

start = time.time()
check()
end = time.time() - start
print("Time: {:.5f} seconds".format(end))
