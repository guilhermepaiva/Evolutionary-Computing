#coding:utf-8

import random

def makechromosome(alleles, length_chromosome):
	return [random.choice(alleles) for gene in range(length_chromosome)]

def mutate(gene, alleles, chromosome):
	chromosome[gene] = random.choice(alleles)


if __name__ == "__main__":
	alleles = (0,1)
	length_chromosome = 5
	a = makechromosome(alleles, length_chromosome)
	print "Cromossomo: " 
	print a
	print "\n"
	print "Depois da Mutacao:"
	mutate(2, alleles, a)
	print a