#coding:utf-8

import random

def makechromosome(alleles, length_chromosome):
	return [random.choice(alleles) for gene in range(length_chromosome)]

def mutate(gene, alleles, chromosome):
	chromosome[gene] = random.choice(alleles)

def makepopulation(population_size, alleles, length_chromosome):
	return [makechromosome(alleles, length_chromosome) for individual in range(population_size)]


if __name__ == "__main__":
	alleles = (0,1)
	length_chromosome = 5
	population_size = 10
	all_population = makepopulation(population_size, alleles, length_chromosome)
	print "Populacao: "
	print all_population
	

