import time
import gym
import random

env = gym.make("CartPole-v1")

def Random_games():
    # Each of this episode is its own game.
    for episode in range(10):
        print("Episode = ", episode)
        env.reset()
        # this is each frame, up to 500...but we wont make it that far with random.
        for t in range(500):
            # This will display the environment
            # Only display if you really want to see it.
            env.render()
            
            # This will just create a sample action in any environment.
            action = env.action_space.sample()
            # print(action)

            # give an action to the environment
            next_state, reward, done, info = env.step(action)
            
            # lets print everything in one line:
            # t = time/step
            # state
            # | Num | Observation           | Min                  | Max                |
            # |-----|-----------------------|----------------------|--------------------|
            # | 0   | Cart Position         | -4.8                 | 4.8                |
            # | 1   | Cart Velocity         | -Inf                 | Inf                |
            # | 2   | Pole Angle            | ~ -0.418 rad (-24°)  | ~ 0.418 rad (24°)  |
            # | 3   | Pole Angular Velocity | -Inf                 | Inf                |
            # reward = score of the game
            # done = True is over, False stil survives
            # info = info
            # action
            # | Num | Action                 |
            # |-----|------------------------|
            # | 0   | Push cart to the left  |
            # | 1   | Push cart to the right |
            print(t, next_state[2], reward, done, action)
            if done:
                break
    env.close()
                
Random_games()