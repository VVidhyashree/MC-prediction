import gym
import pandas as pd
from collections import defaultdict
#create blackjack environment
env=gym.make('Blackjack-v0')
# define policy
def policy(state):
   return 0 if state[0]>19 else 1
state =env.reset()
state=state[0]
print(state)
print(policy(state))

#generate the episode
num_timesteps=100
def generate_episode(policy):
    episode=[]
    state=env.reset()
#for each timestep
    for t in range(num_timesteps):
          action=policy(state)
          next_state,reward,done,info=env.step(action)
          episode.append((state,action,reward))
          if done:
             break
          state=next_state
   return episode
print(generate_episode(policy))
#compute the value function
total_return=defaultdict(float)
N=defaultdict(int)
num_iterations=10
for i in range(num_iterations):
    episode=generate_episode(policy)
    states,action,rewards=zip(*episode)
    for t in enumerate(states):
        R=(sum(rewards[t:]))
        total_return[state]=total_return[state]+R
        N[state]=N[state]+1
print(total_return[state])
print([N[state])
