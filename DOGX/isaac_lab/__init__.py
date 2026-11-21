"""Isaac Lab locomotion task for the Dogx quadruped.

Importing this package registers the Gym task ids. It must be importable as the
top-level ``isaac_lab`` package, i.e. the repository root should be on
``sys.path`` (the provided train.py / play.py handle this).
"""

import gymnasium as gym

gym.register(
    id="Isaac-Velocity-Flat-Dogx-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.flat_env_cfg:DogxFlatEnvCfg",
        "rsl_rl_cfg_entry_point": f"{__name__}.rsl_rl_ppo_cfg:DogxFlatPPORunnerCfg",
    },
)

gym.register(
    id="Isaac-Velocity-Flat-Dogx-Play-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.flat_env_cfg:DogxFlatEnvCfg_PLAY",
        "rsl_rl_cfg_entry_point": f"{__name__}.rsl_rl_ppo_cfg:DogxFlatPPORunnerCfg",
    },
)

gym.register(
    id="Isaac-Velocity-Rough-Dogx-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.rough_env_cfg:DogxRoughEnvCfg",
        "rsl_rl_cfg_entry_point": f"{__name__}.rsl_rl_ppo_cfg:DogxRoughPPORunnerCfg",
    },
)

gym.register(
    id="Isaac-Velocity-Flat-Dogx-Distill-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.distill_env_cfg:DogxFlatDistillEnvCfg",
        "rsl_rl_cfg_entry_point": f"{__name__}.rsl_rl_distill_cfg:DogxFlatDistillationRunnerCfg",
    },
)

gym.register(
    id="Isaac-Velocity-Rough-Dogx-Play-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.rough_env_cfg:DogxRoughEnvCfg_PLAY",
        "rsl_rl_cfg_entry_point": f"{__name__}.rsl_rl_ppo_cfg:DogxRoughPPORunnerCfg",
    },
)
