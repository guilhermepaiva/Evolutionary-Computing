import random
import math
import numpy as np

# TODO random.uniform sem timestamp

def makechromosome():
	length_chromosome = 31
	chromosome = [random.uniform(-15.0,15.0) for gene in range(length_chromosome-1)]
	chromosome.append(1.0)
	return chromosome

def makepopulation(population_size):
	return [makechromosome() for individual in range(population_size)]

def calculate_ackley(chromosome):
	a, b, c = 20, 0.2, (math.pi)*2
	first_sum = 0.0
	for i in range(len(chromosome)-1):
		first_sum += chromosome[i]**2
	first_sum = math.sqrt(first_sum * (1.0/(len(chromosome)-1)))
	first_sum *= -b
	second_sum = 0.0
	for j in range(len(chromosome)-1):
		second_sum += math.cos(c*chromosome[j])
	second_sum *= (1/(len(chromosome)-1))
	result = (-a * math.exp(first_sum)) - math.exp(second_sum) + a + math.exp(1)
	return result

def calculate_fitness(chromosome):
	return 1.0/(calculate_ackley(chromosome) + 1.0)

def check_fitness(population):
	ideal_fitness = 0.9
	for individual in population:
		if calculate_fitness(individual) >= ideal_fitness:
			return True
	return False

def mutate(chromosome):
	threshold = 0.1
	learning_tax = 1.0/math.sqrt(len(chromosome)-1)
	normal_random = np.random.normal(0,1)
	next_sigma = chromosome[-1]*math.exp(learning_tax*normal_random)
	if next_sigma < threshold:
		next_sigma = threshold
	return [chromosome[i] + next_sigma*np.random.normal(0,1) for i in range(len(chromosome)-1)]


def pick_pivots():
	left = random.randrange(1, 29)
	right = random.randrange(left, 30)
	return left, right


def crossover(mate1, mate2):
	probability = 0.5
	if random.uniform(0.0, 1.0) < probability:
		return [((mate1[i] + mate2[i]) / 2.0) for i in range(len(mate1)-1)]
	else:
		left, right = pick_pivots()
		child1 = mate1[:left] + mate2[left:]
		child2 = mate2[:left] + mate1[left:]
		if calculate_fitness(child1) > calculate_fitness(child2):
			return child1
		else:
			return child2


#def next_generation(population):

	





if __name__ == "__main__":
	my_population = makepopulation(10)
	max_generations = 100
	current_generation = 0

	print crossover(my_population[0], my_population[1])
	
	while (not check_fitness(my_population) and current_generation < max_generations):
		current_generation += 1
		



		