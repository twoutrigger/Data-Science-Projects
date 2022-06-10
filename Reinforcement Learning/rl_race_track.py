import gym
import numpy as np

env = gym.make("CarRacing-v1")

print(env.action_space)
print(env.spec.max_episode_steps)
# print(type(env.action_space.sample()))

EPISODES = 10 #25000

# for episode in range(EPISODES):
env.reset()
done = False

while not done:

    # action = np.random.randint(0, 3)
    # new_state, reward, done, _ = env.step([4 for i in range(200)])
    action = env.action_space.sample()
    action = np.array([0, 1, 0])
    print(action)
    new_state, reward, done, _ = env.step(action)
    # print(new_state.shape)
    # print(reward)

    env.render()

env.close()
