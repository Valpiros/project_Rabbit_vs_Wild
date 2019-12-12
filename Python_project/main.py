import gym
import gym_foo


def main():
    print("Hello world")
    # reproduction(10, 10, Type(1).name)
    """ 
    rabbit1 = Rabbit(10, 10)
    rabbit1.faim, rabbit1.soif = eat(rabbit1.faim, rabbit1.soif, 0)
    print("lapin manger salade")
    print("faim :", rabbit1.faim, "/ 100")
    print("soif :", rabbit1.soif, "/ 100")
    """

    # RabbitVSWild(map1)

    env = gym.make('FrozenLake8x8-v0')
    print("done")
    env = gym.make("RabbitVSWild-v0")
    env.reset()
    print("done")
    state2, reward, done, info = env.step(1)
    print(state2, " ", reward, " ", done, " ", info)


if __name__ == '__main__':
    main()
