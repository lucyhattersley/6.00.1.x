s = '1.23,2.4,3.123' 

nums = s.split(',')

ans = 0
for num in nums:
    ans += float(num)
print ans