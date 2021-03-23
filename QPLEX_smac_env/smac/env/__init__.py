from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from smac.env.multiagentenv import MultiAgentEnv
from smac.env.starcraft2.starcraft2 import StarCraft2Env
from smac.env.matrix_game_1 import Matrix_game1Env
from smac.env.matrix_game_2 import Matrix_game2Env
from smac.env.matrix_game_3 import Matrix_game3Env
from smac.env.mmdp_game_1 import mmdp_game1Env

from smac.env.checkers.checkers import WrappedCheckers
from smac.env.combat.combat     import WrappedCombat
from smac.env.lumberjacks.lumberjacks import WrappedLumberjacks
from smac.env.pong_duel.pong_duel import WrappedPongDuel
from smac.env.predator_prey.predator_prey import WrappedPredatorPrey
from smac.env.switch.switch_one_corridor import WrappedSwitch
from smac.env.traffic_junction.traffic_junction import WrappedTrafficJunction

__all__ = ["MultiAgentEnv", "StarCraft2Env", "Matrix_game1Env", "Matrix_game2Env", "Matrix_game3Env", "mmdp_game1Env"]
__all__ += ["WrappedCheckers", "WrappedCombat", "WrappedLumberjacks", "WrappedPongDuel", "WrappedPredatorPrey", "WrappedSwitch", "WrappedTrafficJunction"]
