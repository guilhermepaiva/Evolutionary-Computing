#coding:utf-8

import random
import math
import numpy as np
from matplotlib.pyplot import *


def makechromosome(alleles, length_chromosome):
	return [random.choice(alleles) for gene in range(length_chromosome)]

def mutate(gene, alleles, chromosome):
	chromosome[gene] = random.choice(alleles)
	return chromosome[gene]

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

def calculate_dummy_function(param):
	y = param*param
	return y

def calculate_function(x):
	y = 100*(np.power(((x+1) - np.power(x, 2)),2)) + np.power((x - 1),2)
	return y


def calculate_fitness(param):
	result = 1 / float((calculate_function(param) + 1))
	return result


def best_fitness_population(population):
	min = 0.0
	for individual in population:
		if calculate_fitness(convert_to_decimal(individual)) >= min:
			min = calculate_fitness(convert_to_decimal(individual))
			best_individual = individual
	print "Melhor Individuo da Populacao: "
	print best_individual, " --->>> ", convert_to_decimal(best_individual)
	return min

def best_individual_fitness_population(population):
	min = 0.0
	for individual in population:
		if calculate_fitness(convert_to_decimal(individual)) >= min:
			min = calculate_fitness(convert_to_decimal(individual))
			best_individual = individual
	return best_individual

def total_fitness_population(population):
	total = 0.0
	for individual in population:
		total += calculate_fitness(convert_to_decimal(individual))
	return total



def tournament(size, choose_best, population):
	competidors = [random.choice(population) for i in range(size)]
	#competidors.sort()
	if random.random() < choose_best:
	#return competidors[0]
		return best_individual_fitness_population(competidors)
	else:
		return random.choice(competidors)


def generate_new_population(population):
	next_population = []
	while (len(next_population) < len(population)):
		#mate1 = best_individual_fitness_population(population)
		mate1 = tournament(10, 0.8, population)
		mate2 = tournament(10, 0.8, population)
		child1, child2 = onepoint(mate1, mate2)
		if child1 == mate1 or child1 == mate2:
			child1[3] = mutate(3, (0,1),child1)
		elif child2 == mate1 or child2 == mate2:
			child2[4] = mutate(4, (0,1), child2)
		else:
			pass
		next_population.append(child1)
		next_population.append(child2)
	return next_population


def step(population):
	print "Fitness da Populacao como um todo: ", total_fitness_population(population)
	new_population = generate_new_population(population)
	return new_population

def goal(generation, max_generation, desirable_fitness, best_individual):
	return generation > max_generation or desirable_fitness >= best_fitness_population

def run():
	population_now = first_population
	generation = 1
	max_generation = 1000
	best_individual = best_individual_fitness_population(population_now)
	desirable_fitness = 0.4
	list_best_fitness = []
	while (not goal(generation, max_generation, desirable_fitness, best_individual)):
		print "Geracao: ", generation
		new_population = step(population_now)
		population_now = new_population
		print "#"*80
		print "Populacao Atual"
		for i in population_now:
			print i, "|- representacao em decimal -> ", convert_to_decimal(i)
		print "#"*80
		best_fitness = best_fitness_population(new_population)
		list_best_fitness.append(best_fitness)
		print "Melhor fitness da populacao"
		print best_fitness
		print "-"*80
		generation += 1
		best_individual = best_individual_fitness_population(population_now)
	plot_fitness(list_best_fitness)

def plot_fitness(list_fitness):
	x = np.arange(0,1000)
	y = list_fitness
	plot(x,y)
	xlabel('Geracoes')
	ylabel('Melhor Fitness')
	title('Relacao entre o melhor fitness e as geracoes')
	grid(True)
	show()


if __name__ == "__main__":
	alleles = (0,1)
	length_chromosome = 12
	population_size = 50
	first_population = makepopulation(population_size, alleles, length_chromosome)
	run()

	
	

