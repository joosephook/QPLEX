import abc
import warnings

import numpy as np
from typing import List, Any, Union


class MultiAgentBase(abc.ABC):
    @abc.abstractmethod
    def step(self, actions) -> (float, float, dict):
        """Returns reward, terminated, info."""
        pass

    @abc.abstractmethod
    def get_obs(self) -> List[np.ndarray]:
        """Returns all agent observations in a list."""
        pass

    @abc.abstractmethod
    def get_obs_agent(self, agent_id):
        """Returns observation for agent_id."""
        pass

    @abc.abstractmethod
    def get_obs_size(self) -> int:
        """Returns the size of the observation."""
        pass

    @abc.abstractmethod
    def get_state(self):
        """Returns the global state."""
        pass

    @abc.abstractmethod
    def get_state_size(self) -> int:
        """Returns the size of the global state."""
        pass

    @abc.abstractmethod
    def get_avail_actions(self):
        """Returns the available actions of all agents in a list."""
        pass

    @abc.abstractmethod
    def get_avail_agent_actions(self, agent_id):
        """Returns the available actions for agent_id."""
        pass

    @abc.abstractmethod
    def get_total_actions(self) -> int:
        """Returns the total number of actions an agent could ever take."""
        pass

    @abc.abstractmethod
    def reset(self):
        """Returns initial observations and states."""
        pass

    @abc.abstractmethod
    def render(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass

    @abc.abstractmethod
    def seed(self):
        pass

    @abc.abstractmethod
    def save_replay(self):
        """Save a replay."""
        pass

    def get_env_info(self):
        env_info = {"state_shape": self.get_state_size(),
                    "obs_shape": self.get_obs_size(),
                    "n_actions": self.get_total_actions(),
                    "n_agents": self.n_agents,
                    "episode_limit": self.episode_limit}
        return env_info

    @property
    def unwrapped(self):
        """Completely unwrap this env.

        Returns:
            gym.Env: The base non-wrapped gym.Env instance
        """
        return self

from typing import  Callable

class Features:
    def __init__(self, feature_functions: List[Callable[[], Union[List[float], np.ndarray]]]):
        self.feature_functions = feature_functions
        self.features = []
        self.update()

    def update(self):
        self.features = [np.array(f()) for f in self.feature_functions]

    @property
    def vector(self):
        self.update()
        return np.hstack(self.features)

    @property
    def sections(self):
        if not len(self.features):
            self.update()

        feature_lengths = [0]
        for f in self.features:
            feature_lengths.append(len(f))

        return np.cumsum(feature_lengths)




class EpisodeCounterMixin:
    def __init__(self):
        self.__episode_count = 0

    def inc(self):
        self.__episode_count += 1

    @property
    def episode_count(self):
        return self.__episode_count

class TranslatorMixin:
    def __init__(self, o_src, o_dst, s_src, s_dst):
        assert len(o_src) == len(o_dst), f"Source and destination observations have different number of sections, {len(o_src)} vs {len(o_dst)}"
        assert len(s_src) == len(s_dst), f"Source and destination states have different number of sections, {len(s_src)} vs {len(s_dst)}"
        self.obs_src = o_src
        self.obs_dst = o_dst
        self.state_src = s_src
        self.state_dst = s_dst

    def translate_obs(self, obs):
        return self._translate(obs, self.obs_src, self.obs_dst)

    def _translate(self, src, src_structure, target_structure):
        dst = np.zeros(target_structure[-1])

        for i in range(len(target_structure) - 1):
            width = src_structure[i + 1] - src_structure[i]
            dst[target_structure[i]:target_structure[i] + width] = src[src_structure[i]: src_structure[i + 1]]

        return dst

    def translate_state(self, state):
        return self._translate(state, self.state_src, self.state_dst)

import gym

class MultiAgentWrapper(MultiAgentBase):
    def __init__(self, env: gym.Env):
        self.env = env
        self.env.reset()

    def step(self, actions) -> (float, float, dict):
        assert len(actions)
        actions = list(map(int, actions))# may be torch.tensor

        observations, reward, done, info = self.env.step(actions)
        return sum(reward), done, info

    def get_obs(self) -> List[np.ndarray]:
        return self.env.get_agent_obs()

    def get_obs_agent(self, agent_id):
        return self.env.get_agent_obs()[agent_id]

    def get_obs_size(self) -> int:
        return len(self.get_obs()[0])

    def get_state(self):
        return np.array(self.env.get_agent_obs()).flatten().tolist()

    def get_state_size(self) -> int:
        return len(self.get_state())

    def get_avail_actions(self):
        return [self.get_avail_agent_actions(i) for i in range(self.env.n_agents)]

    def get_avail_agent_actions(self, agent_id):
        return np.ones(self.env.action_space._agents_action_space[agent_id].n)

    def get_total_actions(self) -> int:
        return self.env.action_space._agents_action_space[0].n

    def reset(self):
        self.env.reset()
        return self.get_obs()

    def render(self):
        self.env.render()

    def close(self):
        self.env.close()

    def get_env_info(self):
        env_info = {"state_shape": self.get_state_size(),
                    "obs_shape": self.get_obs_size(),
                    "n_actions": self.get_total_actions(),
                    "n_agents": self.env.n_agents,
                    "episode_limit": 100,
                    "unit_dim": self.get_state_size(),
                    }

        warnings.warn("Using hardcoded episode limit of 100, please change me!")

        return env_info

    @property
    def episode_limit(self):
        warnings.warn("Using hardcoded episode limit of 100, please change me!")
        return 100

    # ignore for now
    def seed(self):
        pass

    def save_replay(self):
        pass
