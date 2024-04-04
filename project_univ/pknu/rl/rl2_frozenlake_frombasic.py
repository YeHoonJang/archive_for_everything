# Virtual display
from pyvirtualdisplay import Display

virtual_display = Display(visible=0, size=(1400, 900))
virtual_display.start()
import numpy as np
import gymnasium as gym
import random
import imageio
import os
from tqdm import tqdm

import pdb

import pickle5 as pickle

env = gym.make(
    id="FrozenLake-v1",         # environment name
    map_name="4x4",             # map grid size
    is_slippery=False,          # False:deterministic / True:stochastic
    render_mode="rgb_array"     # visualization
)

desc = ["SFFF", "FHFH", "FFFH", "HFFG"]
gym.make(id='FrozenLake-v1', desc=desc, is_slippery=True)

print("_____Observation Space_____ \n")
print("Observation Space:", env.observation_space)
print("Observation Sample:", env.observation_space.sample())

print("_____Action Space_____ \n")
print("Action Space Size:", env.action_space.n)
print("Action Space Sample:", env.action_space.sample())

state_space = env.observation_space.n
print("There are ", state_space, " possible states")

action_space = env.action_space.n
print("There are ", action_space, " possible actions")


# Let's create our Qtable of size (state_space, action_space) and initialized each values at 0 using np.zeros. np.zeros needs a tuple (a,b)
def initialize_q_table(state_space, action_space):
    Qtable = np.zeros((state_space, action_space))
    return Qtable


Qtable_frozenlake = initialize_q_table(state_space, action_space)
print("Qtable\n",Qtable_frozenlake)


def greedy_policy(Qtable, state):
    action = np.argmax(Qtable[state][:])
    return action


def epsilon_greedy_policy(Qtable, state, epsilon):
    # Randomly generate a number between 0 and 1
    random_num = random.uniform(0,1)
    # if random_num > greater than epsilon --> exploitation
    if random_num > epsilon:
        # Take the action with the highest value given a state
        # np.argmax can be useful here
        action = greedy_policy(Qtable, state)
    # else --> exploration
    else:
        action = env.action_space.sample()  # Take a random action

    return action


# train parameter
n_training_episodes = 10000
learning_rate = 0.7

# evaluate parameter
n_eval_episodes = 100

# env parameter
env_id = "FrozenLake-v1"
max_steps = 99               # max step per episode
gamma = 0.95
eval_seed = []

# exploration parameter
max_epsilon = 1.0
min_epsilon = 0.05
decay_rate = 0.0005


def train(n_training_episodes, min_epsilon, max_epsilon, decay_rate, env, max_steps, Qtable):
  for episode in tqdm(range(n_training_episodes)):
    # epsilon decay
    epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode)

    # reset environment
    state, info = env.reset()
    step = 0
    terminated = False
    truncated = False

    for step in range(max_steps):
      # 엡실론 탐욕 정책을 사용하여 행동 At를 선택합니다
      action = epsilon_greedy_policy(Qtable, state, epsilon)

      # 행동 At를 취하고 Rt+1과 St+1을 관찰합니다
      # 행동(a)를 취하고 결과 상태(s')와 보상(r)을 관찰합니다
      new_state, reward, terminated, truncated, info = env.step(action)

      # Q(s,a)를 업데이트합니다: Q(s,a) := Q(s,a) + 학습률 [R(s,a) + 감마 * max Q(s',a') - Q(s,a)]
      Qtable[state][action] = Qtable[state][action] + learning_rate*(reward + gamma*np.max(Qtable[new_state])-Qtable[state][action])

      # 만약 종료되었거나 중단되었다면 에피소드를 마칩니다
      if terminated or truncated:
        break

      # 다음 상태는 새로운 상태입니다
      state = new_state
  return Qtable


Qtable_frozenlake = train(n_training_episodes, min_epsilon, max_epsilon, decay_rate, env, max_steps, Qtable_frozenlake)

print(Qtable_frozenlake)


def evaluate_agent(env, max_steps, n_eval_episodes, Q, seed):
  """
  에이전트를 ``n_eval_episodes`` 에피소드 동안 평가하고 평균 보상과 보상의 표준 편차를 반환합니다.
  :param env: 평가 환경
  :param max_steps: 에피소드당 최대 스텝 수
  :param n_eval_episodes: 에이전트를 평가할 에피소드 수
  :param Q: Q-테이블
  :param seed: 평가 시드 배열 (taxi-v3용)
  """
  episode_rewards = []  # 각 에피소드의 총 보상을 저장할 리스트
  for episode in tqdm(range(n_eval_episodes)):  # 평가할 에피소드 수만큼 반복
    if seed:
      state, info = env.reset(seed=seed[episode])  # 시드가 있다면 시드를 사용하여 환경 리셋
    else:
      state, info = env.reset()  # 시드가 없다면 일반적으로 환경 리셋
    step = 0
    truncated = False
    terminated = False
    total_rewards_ep = 0  # 현재 에피소드의 총 보상

    for step in range(max_steps):  # 최대 스텝 수만큼 반복
      # 현재 상태에서 미래 보상이 예상되는 최대값을 가지는 행동을 선택
      action = greedy_policy(Q, state)
      new_state, reward, terminated, truncated, info = env.step(action)
      total_rewards_ep += reward  # 보상을 총 보상에 추가

      if terminated or truncated:  # 에피소드가 종료되거나 중단되면 반복 중단
        break
      state = new_state  # 새로운 상태를 현재 상태로 업데이트
    episode_rewards.append(total_rewards_ep)  # 현재 에피소드의 총 보상을 리스트에 추가
  mean_reward = np.mean(episode_rewards)  # 평균 보상 계산
  std_reward = np.std(episode_rewards)  # 보상의 표준 편차 계산

  return mean_reward, std_reward  # 평균 보상과 표준 편차 반환


mean_reward, std_reward = evaluate_agent(env, max_steps, n_eval_episodes, Qtable_frozenlake, eval_seed)
print(f"Mean_reward={mean_reward:.2f} +/- {std_reward:.2f}")

