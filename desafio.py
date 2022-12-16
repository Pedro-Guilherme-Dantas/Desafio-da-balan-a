def find_ball(balls):
    group_1 = balls[:6]
    group_2 = balls[6:9]

    match = lambda x : x[0] if x[0] > x[2] else (x[2] if x[2] > x[0] else x[1])

    if sum(group_1[:3]) > sum(group_1[3:6]):
      return match(group_1[:3])
    elif sum(group_1[:3]) < sum(group_1[3:6]):
      return match(group_1[3:6])
    else:
      return match(group_2)
