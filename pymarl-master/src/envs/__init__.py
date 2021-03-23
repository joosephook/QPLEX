from functools import partial
from smac.env import MultiAgentEnv, StarCraft2Env, Matrix_game1Env, Matrix_game2Env, Matrix_game3Env, mmdp_game1Env

from smac.env import (WrappedCheckers, WrappedCombat, WrappedLumberjacks,
                      WrappedPongDuel, WrappedPredatorPrey, WrappedSwitch,
                      WrappedTrafficJunction)

import sys
import os

def env_fn(env, **kwargs) -> MultiAgentEnv:
    return env(**kwargs)

REGISTRY = {
    "sc2": partial(env_fn, env=StarCraft2Env),
    "matrix_game_1": partial(env_fn, env=Matrix_game1Env),
    "matrix_game_2": partial(env_fn, env=Matrix_game2Env),
    "matrix_game_3": partial(env_fn, env=Matrix_game3Env),
    "mmdp_game_1": partial(env_fn, env=mmdp_game1Env),

    "WrappedCheckers": partial(env_fn, env=WrappedCheckers),
    "WrappedCombat": partial(env_fn, env=WrappedCombat),
    "WrappedLumberjacks": partial(env_fn, env=WrappedLumberjacks),
    "WrappedPongDuel": partial(env_fn, env=WrappedPongDuel),
    "WrappedPredatorPrey": partial(env_fn, env=WrappedPredatorPrey),
    "WrappedSwitch": partial(env_fn, env=WrappedSwitch),
    "WrappedTrafficJunction": partial(env_fn, env=WrappedTrafficJunction),
}


if sys.platform == "linux":
    os.environ.setdefault("SC2PATH",
                          os.path.join(os.getcwd(), "3rdparty", "StarCraftII"))
