import attr
import magnum as mn
import numpy as np
import quaternion  # noqa: F401

import habitat_sim
from habitat_sim.utils.common import quat_from_angle_axis, quat_rotate_vector

try:
    import pprint

    _pprint = pprint.pprint
except ImportError:
    _pprint = print

def create_actions():
    agent_config = habitat_sim.AgentConfiguration()
    _pprint(agent_config.action_space)

    agent_config.action_space["look_left_90"] = habitat_sim.ActionSpec("look_left", habitat_sim.agent.ActuationSpec(90)
            )

    agent_config.action_space["look_right_180"] = habitat_sim.ActionSpec("look_right", habitat_sim.agent.ActuationSpec(180)
            )
    agent_config.action_space["look_up_30"] = habitat_sim.ActionSpec("look_up", habitat_sim.agent.ActuationSpec(30)
            )
    agent_config.action_space["look_down_60"] = habitat_sim.ActionSpec("look_down", habitat_sim.agent.ActuationSpec(60)
            )

    #_pprint(agent_config.action_space)
