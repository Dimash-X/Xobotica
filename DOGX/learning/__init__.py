"""Reinforcement-learning package for the Dogx quadruped.

Contains a Gymnasium environment (`DogxEnv`) that wraps the existing
``simulation/dogx.urdf`` in PyBullet, plus training and evaluation scripts.
"""

from .dogx_env import DogxEnv, DogxEnvConfig

__all__ = ["DogxEnv", "DogxEnvConfig"]
