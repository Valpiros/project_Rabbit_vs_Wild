from gym.envs.registration import register

register(
    id='FrozenLaketry-v0',
    # entry_point='gym.envs.toy_text:FrozenLakeEnv',
    entry_point='gym_foo.envs.frozen_lake:FrozenLakeEnv',
)

register(
    id='RabbitVSWild-v0',
    entry_point='gym_foo.envs.RabbitVSWild:RabbitVSWildEnv',
)