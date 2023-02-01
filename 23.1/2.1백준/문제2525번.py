hour, minute = map(int, input().split())
plus = int(input())

c_hour = (hour + ((minute + plus) // 60)) % 24
c_minute = (minute + plus) % 60

print(c_hour, c_minute)