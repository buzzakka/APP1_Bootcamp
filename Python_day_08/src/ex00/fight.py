import asyncio

from enum import Enum, auto
from random import choice, random, sample


class Action(Enum):
    HIGHKICK = auto()
    LOWKICK = auto()
    HIGHBLOCK = auto()
    LOWBLOCK = auto()


class Agent:

    def __aiter__(self, health=5):
        self.health = health
        self.actions = list(Action)
        return self

    async def __anext__(self):
        return choice(self.actions)


async def choose_move(agents_move):
    if agents_move in (Action.HIGHKICK, Action.LOWKICK):
        return Action(agents_move.value + 2)
    else:
        return Action(5 - agents_move.value)


def print_messge(agents_move, neos_move, health, agents_number=""):
    print(f"Agent{' ' if agents_number else ''}{agents_number}: {agents_move}, Neo: {neos_move}, Agent Health: {health}")


def print_win_message():
    print('Neo wins!')


async def fight_with_one(agent, number=""):
    async for agent_move in agent:
        if agent.health == 0:
            return
        neo_move = await choose_move(agent_move)
        if neo_move in (Action.HIGHKICK, Action.LOWKICK):
            agent.health -= 1
        print_messge(agent_move, neo_move, agent.health, number)
        await asyncio.sleep(0.3 + random())


async def fight():
    agent = Agent()
    await fight_with_one(agent)
    print_win_message()


async def fightmany(n):
    agents = [Agent() for _ in range(n)]
    numbers = sample(range(1, n + 1), n)
    tasks = []
    for number, agent in zip(numbers, agents):
        tasks.append(fight_with_one(agent, number))
    await asyncio.gather(*tasks)
    print_win_message()


if __name__ == "__main__":
    print("------- SOLO FIGHT -------")
    print("------- START -------")
    asyncio.run(fight())
    print("------- END -------\n")
    print("------- FIGHT WITH MANY -------")
    print("------- START -------")
    asyncio.run(fightmany(5))
    print("------- END -------")
