import gym
import numpy as np

env = gym.make("CarRacing-v1")

print(env.action_space)
print(env.spec.max_episode_steps)

EPISODES = 10 #25000

# for episode in range(EPISODES):
env.reset()
done = False

while not done:

    # action = np.random.randint(0, 3)
    new_state, reward, done, _ = env.step([0 for i in range(200)])

    # env.step([0 for i in range(200)])
    env.render()

env.close()
