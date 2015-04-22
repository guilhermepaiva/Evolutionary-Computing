#coding:utf-8

import random

def makechromosome(alleles, length_chromosome):
	return [random.choice(alleles) for gene in range(length_chromosome)]

def mutate(gene, alleles, chromosome):
	chromosome[gene] = random.choice(alleles)

def makepopulation(population_size, alleles, length_chromosome):
	return [makechromosome(alleles, length_chromosome) for individual in range(population_size)]

def pick_pivots():
	left = random.randrange(1, length_chromosome-2)
	right = random.randrange(left, length_chromosome-1)
	return left, right

# um crossover simples
def onepoint(mate1, mate2):
	left, right= pick_pivots()
	child1 = mate1[:left] + mate2[left:]
	child2 = mate2[:left] + mate1[left:]
	return child1, child2

def convert_to_decimal(binary_number):
	str_of_interest = str1 = ''.join(str(e) for e in binary_number)
	return int(str_of_interest, 2)

def calculate_function(param):
	y = param*param
	return y

def calculate_fitness(param):
	result = 1 / float((calculate_function(param) + 1))
	return result

def best_fitness_population(population):
	min = 0
	for individual in population:
		if calculate_fitness(convert_to_decimal(individual)) >= min:
			print "Fenotipo"
			print individual
			print "Genotipo"
			print convert_to_decimal(individual)
			print "\n"
			min = calculate_fitness(convert_to_decimal(individual))
			best_individual = individual
	return min


def tournament(size, choose_best, population):
	competidors = [random.choice(population) for i in range(size)]
	competidors.sort()
	if random.random() < choose_best:
		return competidors[0]
	else:
		return random.choice(competidors[1:])


def generate_new_population(population):
	next_population = []
	while (len(next_population) < len(population)):
		mate1 = tournament(8, 0.90, population)
		mate2 = tournament(8, 0.90, population)
		child1, child2 = onepoint(mate1, mate2)
		mutate(3, (0,1),child1)
		next_population.append(child1)
		next_population.append(child2)
	return next_population


def step(population):
	population.sort()
	new_population = generate_new_population(population)
	return new_population

def goal(generation, max_generation, desirable_fitness, best_individual):
	desirable_fitness = 1
	return generation > max_generation or desirable_fitness >= best_fitness_population

def run(population):
	generation = 0
	max_generation = 100
	best_individual = 100
	desirable_fitness = 0
	while (not goal(generation, max_generation, desirable_fitness, best_individual)):
		new_population = step(population)
		print "Populacao: "
		print new_population
		print "\n\n"
		best_individual = best_fitness_population(new_population)
		print "Melhor fitness da populacao"
		print best_individual
		generation += 1



if __name__ == "__main__":
	alleles = (0,1)
	length_chromosome = 5
	population_size = 10
	all_population = makepopulation(population_size, alleles, length_chromosome)
	run(all_population)	

	
	

