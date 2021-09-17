#!/usr/bin/env python

import gym
import time

env = gym.make('MsPacman-v0')
state = env.reset()
print("state: "+str(state))
print("state.shape: "+str(state.shape))
print("action_space size: "+str(env.action_space.n))
print("action_space meanings: "+str(env.env.get_action_meanings()))

env.render()
time.sleep(1)

