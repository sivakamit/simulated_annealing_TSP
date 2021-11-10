import random
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Routes:
    def __init__(self, width, height, nodesNumber):
        self.width = width
        self.height = height
        self.nodesNumber = nodesNumber

    def generate(self):
        a = np.random.randint(self.width, size=self.nodesNumber)
        b = np.random.randint(self.height, size=self.nodesNumber)

        return np.column_stack((a, b))


def DistMatrix(cities):
    return np.sqrt((np.square(cities[:, np.newaxis] - cities).sum(axis=2)))


def nearestNeighbourSolution(dist_matrix):
    node = random.randrange(len(dist_matrix))
    result = [node]

    nodes_to_visit = list(range(len(dist_matrix)))
    nodes_to_visit.remove(node)

    while nodes_to_visit:
        nearest_node = min([(dist_matrix[node][j], j)
                           for j in nodes_to_visit], key=lambda x: x[0])
        node = nearest_node[1]
        nodes_to_visit.remove(node)
        result.append(node)

    return result


class SimulatedAnnealing:
    def __init__(self, cities, initial_temp, desc_factor, end_temp, iteration):
        self.cities = cities
        self.sample = len(cities)
        self.initial_temp = initial_temp
        self.desc_factor = desc_factor
        self.end_temp = end_temp
        self.iteration = iteration
        self.init_iter = 1

        self.dist_matrix = DistMatrix(cities)
        self.curr_solution = nearestNeighbourSolution(self.dist_matrix)
        self.best_solution = self.curr_solution

        self.solution_history = [self.curr_solution]

        self.curr_weight = self.weight(self.curr_solution)
        self.initial_weight = self.curr_weight
        self.min_weight = self.curr_weight

        self.weight_list = [self.curr_weight]

        print('Intial weight: ', self.curr_weight)

    def weight(self, sol):
        return sum([self.dist_matrix[i, j] for i, j in zip(sol, sol[1:] + [sol[0]])])

    def acceptance_probability(self, candidate_weight):

        return math.exp(-abs(candidate_weight - self.curr_weight) / self.initial_temp)

    def accepted(self, candidate):

        candidate_weight = self.weight(candidate)
        if candidate_weight < self.curr_weight:
            self.curr_weight = candidate_weight
            self.curr_solution = candidate
            if candidate_weight < self.min_weight:
                self.min_weight = candidate_weight
                self.best_solution = candidate

        else:
            if random.random() < self.acceptance_probability(candidate_weight):
                self.curr_weight = candidate_weight
                self.curr_solution = candidate

    def anneal(self):

        while self.initial_temp >= self.end_temp and self.init_iter < self.iteration:
            candidate = list(self.curr_solution)
            l = random.randint(2, self.sample - 1)
            i = random.randint(0, self.sample - l)

            candidate[i: (i + l)] = reversed(candidate[i: (i + l)])

            self.accepted(candidate)
            self.initial_temp *= self.desc_factor
            self.init_iter += 1
            self.weight_list.append(self.curr_weight)
            self.solution_history.append(self.curr_solution)

        print('Minimum weight: ', self.min_weight)
        print('Improvement: ',
              round((self.initial_weight - self.min_weight) / (self.initial_weight), 4) * 100, '%')

    def plotLearning(self):
        plt.plot([i for i in range(len(self.weight_list))], self.weight_list)
        plt.ylabel('Weight')
        plt.xlabel('Iteration')
        plt.show()


def main():

    initial_temp = 1200
    end_temp = 0.00000001
    desc_factor = 0.9995
    iteration = 10000000

    width = 200
    height = 200

    city_size = 100

    nodes = Routes(width, height, city_size).generate()

    sa = SimulatedAnnealing(nodes, initial_temp,
                            desc_factor, end_temp, iteration)
    sa.anneal()

    sa.plotLearning()


if __name__ == "__main__":
    main()
