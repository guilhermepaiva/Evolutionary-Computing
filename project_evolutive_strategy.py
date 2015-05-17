import random
import math

def makechromosome():
	length_chromosome = 31
	chromosome = [random.uniform(-15.0,15.0) for gene in range(length_chromosome-1)]
	chromosome.append(1.0)
	return chromosome

def makepopulation(population_size):
	return [makechromosome() for individual in range(population_size)]

def calculate_fitness(chromosome):
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



if __name__ == "__main__":
	my_population = makepopulation(10)
	for individual in my_population:
		print calculate_fitness(individual)