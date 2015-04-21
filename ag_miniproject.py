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
	min = 100000.0
	for individual in population:
		if calculate_fitness(convert_to_decimal(individual)) < min:
			min = calculate_fitness(convert_to_decimal(individual))
			test = individual
	return min


def tournament(size, choose_best, population):
	competidors = [random.choice(population) for i in range(size)]
	competidors.sort()
	if random.random() < choose_best:
		return competidors[0]
	else:
		return random.choice(competidors[1:])


if __name__ == "__main__":
	alleles = (0,1)
	length_chromosome = 5
	population_size = 10
	all_population = makepopulation(population_size, alleles, length_chromosome)
	print "Populacao: "
	print all_population
	print "\n\n\n"
	print "Melhor Fitness da Populacao"
	print best_fitness_population(all_population)

	

