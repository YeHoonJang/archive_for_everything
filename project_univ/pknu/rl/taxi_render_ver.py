import imageio
import numpy as np
import gymnasium as gym
import random
import os
from tqdm import tqdm

import pdb

def epsilon_greedy_policy(Q, state, epsilon):
    if random.uniform(0, 1) < epsilon:
        return random.randint(0, env.action_space.n - 1)
    else:
        return np.argmax(Q[state])

def train_agent(env, max_steps, n_episodes, alpha, gamma, epsilon_start, epsilon_end, epsilon_decay, out_directory, record_every):
    Q = np.zeros((env.observation_space.n, env.action_space.n))
    epsilon = epsilon_start

    for episode in tqdm(range(n_episodes)):
        state = env.reset()
        truncated = False
        terminated = False

        images = []
        step = 0
        # print(Q)
        while not (terminated or truncated) and step < max_steps:
            # pdb.set_trace()
            action = epsilon_greedy_policy(Q, state[0], epsilon)
            new_state, reward, terminated, truncated, info = env.step(action)
            if terminated:
                target = reward
            else:
                target = reward + gamma * np.max(Q[new_state])

            Q[state[0]][action] = Q[state[0]][action] + alpha * (target - Q[state[0]][action])

            if episode % record_every == 0:
                img = env.render()
                images.append(img)

            # pdb.set_trace()
            state = (new_state, {})
            step += 1

        if episode % record_every == 0:
            video_path = os.path.join(out_directory, f'episode_{episode:05d}.mp4')
            imageio.mimsave(video_path, [np.array(img) for img in images], fps=30)

        epsilon = max(epsilon_end, epsilon * epsilon_decay)

    return Q

def create_final_video(out_directory, final_video_path, fps=30):
    video_paths = [os.path.join(out_directory, f) for f in os.listdir(out_directory) if f.endswith('.mp4')]
    video_paths.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))

    with imageio.get_writer(final_video_path, fps=fps) as writer:
        for video_path in video_paths:
            video = imageio.get_reader(video_path)
            for frame in video:
                writer.append_data(frame)

    for video_path in video_paths:
        os.remove(video_path)


env = gym.make(id='Taxi-v3', render_mode='rgb_array')
max_steps = 100
# 수정된 하이퍼파라미터
n_episodes = 10000
alpha = 0.05
gamma = 0.95
epsilon_start = 1.0
epsilon_end = 0.05
epsilon_decay = 0.005
record_every = 100
out_directory = './training_videos/taxi'
os.makedirs(out_directory, exist_ok=True)

Qtable = train_agent(env, max_steps, n_episodes, alpha, gamma, epsilon_start, epsilon_end, epsilon_decay, out_directory, record_every)

final_video_path = './taxi_training_video.mp4'
create_final_video(out_directory, final_video_path, fps=10)