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

# um crossover simples - rever aqui
def onepoint(mate1, mate2):
	left, right= pick_pivots()
	child1 = mate1[:left] + mate2[left:]
	child2 = mate2[:left] + mate1[left:]
	return child1, child2




if __name__ == "__main__":
	alleles = (0,1)
	length_chromosome = 5
	population_size = 10
	all_population = makepopulation(population_size, alleles, length_chromosome)
	print "Populacao: "
	print all_population
	print "\n\n\n"
	print onepoint(all_population[0], all_population[1])

	

