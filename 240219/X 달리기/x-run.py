x = int(input())

#최대 속도로 간 후 유지하다가 내려가는 게 가장 빠를 것!
#k가 최대 속도라면 유지한 것은 k이하의 속도가 가능!

speed = 0
idx = 0
cnt = 0
while idx + 2*(speed+1) <= x: #올라가고 내려감으로 최고 속도 계산
    speed += 1
    idx += 2*speed
    cnt += 2
    # print("중간체크", idx, cnt, speed)

if idx + speed + 1 < x: #최고 속도가 1번시
    idx += speed + 1
    cnt += 1
    speed += 1
    # print("최고 속도 한번", idx, cnt, speed)

# t = 0
# v = 0
# total_d = 0
# is_increase = 0
# while True:
#     if total_d == dist:
#         break
#     if is_increase == 0:
#         v += 1
#     elif is_increase == 1:
#         v -= 1
#     else:
#         v = v

#     t += 1
#     total_d += v
#     print(t, v, total_d)

#     # if v == 0:
#     #     v = 1
print(cnt if idx == x else cnt + 1)