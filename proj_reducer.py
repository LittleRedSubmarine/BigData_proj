#! /usr/bin/env python3

import sys

p_name_iter = 'Unknown'
p_goal_sum = 0
p_assist_sum = 0
seasons_play = 0

for line in sys.stdin:
    p_name, p_goal, p_assist = line.strip().split('\t')
    if p_name_iter == 'Unknown': p_name_iter = p_name
    if p_name_iter == p_name:
        p_goal_sum = p_goal_sum + int(p_goal)
        p_assist_sum = p_assist_sum + int(p_assist)
        seasons_play += 1
    else:
        print(f" Player - {p_name_iter},"
              f" Carier goals: {p_goal_sum},"
              f" Caries assists: {p_assist_sum},"
              f" Seasons in league: {seasons_play}")
        p_name_iter = p_name
        p_goal_sum = int(p_goal)
        p_assist_sum = int(p_assist)
        seasons_play = 1
print(f" Player - {p_name_iter}, Carier goals: {p_goal_sum},"
      f" Caries assists: {p_assist_sum}, Seasons in league: {seasons_play}")