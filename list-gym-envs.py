#!/usr/bin/env python

import gym

try:
    import gym_csv
except ImportError:
    print("Not loading gym_csv environments")

try:
    import pybullet_envs
except ImportError:
    print("Not loading pybullet_envs environments")

print(gym.envs.registry.all())

