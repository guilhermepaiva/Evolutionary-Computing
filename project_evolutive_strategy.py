import random
import math
import numpy as np
import matplotlib.pyplot as plt
import os

clear = lambda: os.system('cls')

# TODO random.uniform sem timestamp

PROBABILITY_CROSSOVER = 0.3
sum_fitness = []
mean_fitness = []
list_mean_fitness_100_generations = []

def makechromosome():
	length_chromosome = 31
	chromosome = [random.uniform(-15.0,15.0) for gene in range(length_chromosome-1)]
	chromosome.append(np.random.normal(0,0.5))
	return chromosome

def makepopulation(population_size):
	return [makechromosome() for individual in range(population_size)]

def calculate_ackley(chromosome):
	a, b, c = 20.0, 0.2, (math.pi)*2.0
	first_sum = 0.0
	for i in range(len(chromosome)-1):
		first_sum += chromosome[i]**2.0
	first_sum = math.sqrt(first_sum * (1.0/(len(chromosome)-1)))
	first_sum *= -b
	second_sum = 0.0
	for j in range(len(chromosome)-1):
		second_sum += math.cos(c*chromosome[j])
	second_sum *= (1.0/(len(chromosome)-1))
	result = (-a * math.exp(first_sum)) - math.exp(second_sum) + a + math.exp(1)
	return result

def calculate_fitness(chromosome):
	return 1.0/(calculate_ackley(chromosome) + 1.0)

def check_fitness(population):
	ideal_fitness = 0.9
	sum_fitness_current_population = 0.0
	for individual in population:
		fit = calculate_fitness(individual)
		sum_fitness_current_population += fit
		if fit >= ideal_fitness:
			return True
	sum_fitness.append(sum_fitness_current_population)
	return False

def check_overfitting(current_generation):
	mean_of_mean_fitness = 0.0
	if current_generation % 100 == 0:
		for i in range(current_generation-1, current_generation-100, -1):
			mean_of_mean_fitness += mean_fitness[i]
		mean_of_mean_fitness = mean_of_mean_fitness / 100
		list_mean_fitness_100_generations.append(mean_of_mean_fitness)
	if len(list_mean_fitness_100_generations) >= 2:
		difference = math.fabs(list_mean_fitness_100_generations[-1] - list_mean_fitness_100_generations[-2])
		if difference <= 0.004:
			return True
		else:
			return False
	else:
		return False



def get_mean_fitness(population):
	sum_fitness_current_population = 0.0
	for individual in population:
		fit = calculate_fitness(individual)
		sum_fitness_current_population += fit
	mean_fitness_current_population = sum_fitness_current_population/len(population)
	mean_fitness.append(mean_fitness_current_population)
	return mean_fitness_current_population

def mutate(chromosome):
	threshold = 0.1
	learning_tax = 1.0/math.sqrt(len(chromosome)-1)
	normal_random = np.random.normal(0,1)
	next_sigma = chromosome[-1]*math.exp(learning_tax*normal_random)
	if next_sigma < threshold:
		next_sigma = threshold
	new_individual = [chromosome[i] + next_sigma*np.random.normal(0,1) for i in range(len(chromosome)-1)]
	new_individual.append(next_sigma)
	return new_individual


def pick_pivots():
	left = random.randrange(1, 29)
	right = random.randrange(left, 30)
	return left, right

def check_bounds(chromosome):
	flag_return = True
	chromosome_without_sigma = chromosome[:-1]
	for nucleotide in chromosome_without_sigma:
		if -15 <= nucleotide <= 15:
			pass
		else:
			return False
	return flag_return

def crossover_intermadiate(mate1, mate2):
	chromosome = [((mate1[i] + mate2[i]) / 2.0) for i in range(len(mate1))]
	if check_bounds(chromosome) == True:
		return chromosome
	else:
		return makechromosome()

def crossover_random_point(mate1, mate2):
	left, right = pick_pivots()
	child1 = mate1[:left] + mate2[left:]
	child2 = mate2[:left] + mate1[left:]
	if calculate_fitness(child1) > calculate_fitness(child2):
		return child1
	else:
		return child2

def crossover_scrotum(mate1, mate2):
	length_chromosome = len(mate1)
	return [random.uniform(-15.0,15.0) for gene in range(length_chromosome-1)]


def crossover(mate1, mate2):
	probability = 0.5
	if np.random.uniform(0.0, 1.0) < probability:
		return crossover_intermadiate(mate1, mate2)
	else:
		return crossover_random_point(mate1, mate2)
		#return crossover_scrotum(mate1, mate2)
	#return crossover_scrotum(mate1, mate2)


def next_generation(population):
	var_mu = len(population)-1
	lambda_factor = 7
	mates = []
	for i in range(var_mu):
		index = random.randint(0, len(population)-1)
		individual = population[index]
		mates.append(individual)
		population.remove(individual)
	offspring = []
	for i in range(var_mu):
		individual = mates[i]
		for j in range(lambda_factor):
			individual = mutate(individual)
			offspring.append(individual)
		if random.uniform(0.0, 1.0) <= PROBABILITY_CROSSOVER:
			individual = crossover(individual,population[random.randint(0,len(population)-1)])
			offspring.append(individual)

	offspring = sorted(offspring, key=lambda x:calculate_fitness(x))
	population = population + offspring[-var_mu:]
	return population

def get_best_individual(population):
	population = sorted(population, key=lambda x:calculate_fitness(x))
	return population[-1]




if __name__ == "__main__":
	my_population = makepopulation(30)
	max_generations = 10000
	current_generation = 0	
	while (not check_fitness(my_population) and current_generation < max_generations):
		current_generation += 1
		my_population = next_generation(my_population)
		fitness_medio = get_mean_fitness(my_population)
		if check_overfitting(current_generation):
			print "Tem que explorar - Geracao", str(current_generation)
	print "Curent Generation: ", str(current_generation)
	best_individual = get_best_individual(my_population)
	
	print "Best Fitness: ", str(calculate_fitness(best_individual))
	print str(len(range(1, max_generations+2)))

	#plt.plot(range(1, max_generations+2), sum_fitness)
	#plt.show()

	plt.plot(range(1, max_generations+1), mean_fitness)
	plt.show()
		



		