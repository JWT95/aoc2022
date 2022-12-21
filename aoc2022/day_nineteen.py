from dataclasses import dataclass
from copy import deepcopy
from enum import Enum, auto
import math

# Rough strategy
# Build clay robots until we have the right ratio of ore to clay robots
# Build obsidian robots until we have the right ratio of obsidian to ore robots

# New strategy
# Always race to build a clay robot
# Once we have a clay robot, race to build obsidian robot
# Work out best way to do that
# Once we have an obsidian robot, race to build geode robot

@dataclass
class Blueprint:
    _id: int
    ore: int
    clay: int
    obsidian: (int, int)
    geode: (int, int)

class Strategy(Enum):
    Ore = auto()
    Clay = auto()
    Obsidian = auto()
    Geode = auto()


@dataclass
class Factory:
    blueprint: Blueprint
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0
    ore_robot: int = 1
    clay_robot: int = 0
    geode_robot: int = 0
    obsidian_robot: int = 0
    rounds_left: int = 24
    clay_factor: int = 0
    obsidian_factor: int = 0
    moves = []

    def work_out_factor(self):
        self.clay_factor = math.ceil(self.blueprint.obsidian[1] / self.blueprint.obsidian[0])
        self.obsidian_factor = math.ceil(self.blueprint.geode[1] / self.blueprint.geode[0])


    def max_score(self):
        if self.rounds_left == 0:
            print("Here")
            return self.geode

        strategies = []
        # Else work out what strategy to go for and go for that
        # We either need lots of ore obsidian or clay
        # If not much ore, set ore low
        # Else set clay low
        # Else set obsidian low


        if self.ore <= 2 * max(self.blueprint.ore, self.blueprint.clay, self.blueprint.obsidian[0], self.blueprint.geode[0]) and self.ore_robot <= max(self.blueprint.ore, self.blueprint.clay, self.blueprint.obsidian[0], self.blueprint.geode[0]):
            strategies.append(Strategy.Ore)

        if self.clay <= 2* self.blueprint.obsidian[1] and self.clay_robot <= self.blueprint.obsidian[1] and self.clay_robot <= self.clay_factor * self.ore_robot:
            strategies.append(Strategy.Clay)

        if self.clay_robot > 0 and self.obsidian <= 2* self.blueprint.geode[1] and  self.obsidian_robot <= self.blueprint.geode[1] and self.obsidian_robot <= self.obsidian_factor * self.ore_robot:
            strategies.append(Strategy.Obsidian)

        if self.obsidian_robot > 0:
            strategies.append(Strategy.Geode)

        # Work out how many turns it would take to execute the strategy
        max_strat = self.rounds_left * self.geode_robot + self.geode
        for strategy in strategies:
            new_factory = Factory(self.blueprint, ore=self.ore, clay=self.clay, obsidian=self.obsidian, geode=self.geode, ore_robot=self.ore_robot, clay_robot=self.clay_robot, obsidian_robot=self.obsidian_robot, geode_robot=self.geode_robot, rounds_left=self.rounds_left, clay_factor=self.clay_factor, obsidian_factor=self.obsidian_factor)
            new_factory.moves = [a for a in self.moves]

            if strategy == Strategy.Ore:
                if (self.blueprint.ore <= self.ore):
                    turns = 1
                else:
                    if (self.blueprint.ore - self.ore) % self.ore_robot == 0:
                        turns = ((self.blueprint.ore - self.ore) // self.ore_robot) + 1
                    else:
                        turns = ((self.blueprint.ore - self.ore) // self.ore_robot) + 2

                if turns >= self.rounds_left:
                    continue

                # Take that many turns
                new_factory.ore += turns * self.ore_robot - self.blueprint.ore
                new_factory.ore_robot += 1
                new_factory.clay += turns * self.clay_robot
                new_factory.obsidian += turns * self.obsidian_robot
                new_factory.geode += turns * self.geode_robot

                new_factory.rounds_left -= turns
                new_factory_max = new_factory.max_score()
                if new_factory_max > max_strat:
                    self.moves = [f"ore: {new_factory.rounds_left}", *new_factory.moves]
                    max_strat = new_factory_max

            if strategy == Strategy.Clay:
                if self.blueprint.clay <= self.ore:
                    turns = 1
                else:
                    if (self.blueprint.clay - self.ore) % self.ore_robot == 0:
                        turns = ((self.blueprint.clay - self.ore) // self.ore_robot) + 1
                    else:
                        turns = ((self.blueprint.clay - self.ore) // self.ore_robot) + 2
                if turns >= self.rounds_left:
                    continue



                # Take that many turns
                new_factory.ore += turns * self.ore_robot - self.blueprint.clay
                new_factory.clay_robot += 1
                new_factory.clay += turns * self.clay_robot
                new_factory.obsidian += turns * self.obsidian_robot
                new_factory.geode += turns * self.geode_robot

                new_factory.rounds_left -= turns

                new_factory_max = new_factory.max_score()
                if new_factory_max > max_strat:
                    self.moves = [f"clay: {new_factory.rounds_left}", *new_factory.moves]
                    max_strat = new_factory_max

            if strategy == Strategy.Obsidian:
                if self.blueprint.obsidian[0] <= self.ore:
                    ore_turns = 1
                else:
                    if (self.blueprint.obsidian[0] - self.ore) % self.ore_robot == 0:
                        ore_turns = ((self.blueprint.obsidian[0] - self.ore) // self.ore_robot) + 1
                    else:
                        ore_turns = ((self.blueprint.obsidian[0] - self.ore) // self.ore_robot) + 2

                if self.blueprint.obsidian[1] <= self.clay:
                    clay_turns = 1
                else:
                    if (self.blueprint.obsidian[1] - self.clay) % self.clay_robot == 0:
                        clay_turns = ((self.blueprint.obsidian[1] - self.clay) // self.clay_robot) + 1
                    else:
                        clay_turns = ((self.blueprint.obsidian[1] - self.clay) // self.clay_robot) + 2

                turns = max(ore_turns, clay_turns)

                if turns >= self.rounds_left:
                    continue

                # Take that many turns
                new_factory.ore += turns * self.ore_robot - self.blueprint.obsidian[0]
                new_factory.clay += turns * self.clay_robot - self.blueprint.obsidian[1]
                new_factory.obsidian_robot += 1

                new_factory.obsidian += turns * self.obsidian_robot
                new_factory.geode += turns * self.geode_robot

                new_factory.rounds_left -= turns

                new_factory_max = new_factory.max_score()
                if new_factory_max > max_strat:
                    self.moves = [f"obsidian {new_factory.rounds_left}", *new_factory.moves]
                    max_strat = new_factory_max

            if strategy == Strategy.Geode:
                if self.blueprint.geode[0] <= self.ore:
                    ore_turns = 1
                else:
                    if (self.blueprint.geode[0] - self.ore) % self.ore_robot == 0:
                        ore_turns = ((self.blueprint.geode[0] - self.ore) // self.ore_robot) + 1
                    else:
                        ore_turns = ((self.blueprint.geode[0] - self.ore) // self.ore_robot) + 2

                if self.blueprint.geode[1] <= self.obsidian:
                    obsidian_turns = 1
                else:
                    if (self.blueprint.geode[1] - self.obsidian) % self.obsidian_robot == 0:
                        obsidian_turns = ((self.blueprint.geode[1] - self.obsidian) // self.obsidian_robot) + 1
                    else:
                        obsidian_turns = ((self.blueprint.geode[1] - self.obsidian) // self.obsidian_robot) + 2

                turns = max(ore_turns, obsidian_turns)
                if turns >= self.rounds_left:
                    continue

                # Take that many turns
                new_factory.ore += turns * self.ore_robot - self.blueprint.geode[0]
                new_factory.obsidian += turns * self.obsidian_robot - self.blueprint.geode[1]
                new_factory.geode_robot += 1

                new_factory.clay += turns * self.clay_robot
                new_factory.geode += turns * self.geode_robot

                new_factory.rounds_left -= turns

                new_factory_max = new_factory.max_score()
                if new_factory_max > max_strat:
                    self.moves = [f"geode_rob {new_factory.rounds_left}", *new_factory.moves]
                    max_strat = new_factory_max


        if max_strat == self.rounds_left * self.geode_robot + self.geode:
            self.moves = [f"geode {self.rounds_left}"]
        return max_strat


if __name__ == "__main__":
    with open("./inputs/day_nineteen.txt") as f:
        lines = f.read().splitlines()

    blueprints = list()

    for line in lines:
        stripped_line = line.split()
        stripped_line = [word.rstrip(":") for word in stripped_line]

        blueprints.append(Blueprint(int(stripped_line[1]), int(stripped_line[6]), int(stripped_line[12]), (int(stripped_line[18]), int(stripped_line[21])), (int(stripped_line[27]), int(stripped_line[30]))))

    my_sum = 1
    for i in range(3):
        print(i)
        factory = Factory(blueprints[i], rounds_left=32)
        factory.work_out_factor()
        score = factory.max_score()
        print(score)
        my_sum *= score

    print(my_sum)
