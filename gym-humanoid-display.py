#!/usr/bin/env python

import gym
import time
import pybullet_envs

env = gym.make('HumanoidBulletEnv-v0')
env.render()
state = env.reset()
print("state: "+str(state))

time.sleep(10)
