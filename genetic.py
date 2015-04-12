#coding:utf-8

import random

MAXIMIZE, MINIMIZE = 11, 12

class Individual(object):
	alleles = (0,1)
	length = 30
	separator = ''
	optimization = MINIMIZE

	def __init__(self, chromossome=None):
		self.chromossome = chromossome or self._makechromossome()
		self.score = None # vai ser setado durante a avaliação

	def _makechromossome(self):
		"cria um cromossomo a partir de alelos selecionados randomicamente"
		return [random.choice(self.alleles) for gene in range(self.length)]

	def evaluate(self, optimum=None):
		pass

	def crossover(self, other):
		"sobrescrever esse método para escolher o tipo de crossover preferido"
		return self._twopoint(other)

	def mutate(self, gene):
		"sobrescrever esse método para escolher o tipo de mutação preferido"
		return self._pick(gene)

	# uma mutação simples
	def _pick(self, gene):
		"escolhe um alelo aleatoriamente e altera esse alelo"
		self.chromossome[gene] = random.choice(self.alleles)

	# crossover simples
	def _twopoint(self, other):
		"gera os filhos por dois pontos do cromossomo dos pais"
		left, right = self._pickpivots()
		def mate(p0, p1):
			chromossome = p0.chromossome[:]
			chromossome[left:right] = p1.chromossome[left:right]
			child = p0.__class__(chromossome)
			child._repair(p0, p1)
			return child
		return mate(self, other), mate(other, self)

	

	# alguns helpers pro crossover

	def _repair(self, parent1, parent2):
		pass

	def _pickpivots(self):
		left = random.randrange(1, self.length-2)
		right = random.randrange(left, self.length-1)
		return left, right


	# restante dos métodos

	def __repr__(self):
		return '<%s chromossome="%s" score=%s' % (self.__class__.__name__, self.separator.join(map(str, self.chromossome)), self.score)

	def __cmp__(self, other):
		if self.optimization == MINIMIZE:
			return cmp(self.score, other.score)
		else:
			return cmp(other.score, self.score)


	def copy(self):
		twin = self.__class__(self.chromossome[:])
		twin.score = self.score
		return twin


class Environment(object):
	def __init__(self, kind, population=None, size=100, maxgenerations=100, crossover_rate=0.90, mutation_rate=0.01, optimum=None):
		self.kind = kind
		self.size = size
		self.optimum = optimum
		self.population = population or self._makepopulation()
		for individual in self.population:
			individual.evaluate(self.optimum)
		self.crossover_rate = crossover_rate
		self.mutation_rate = mutation_rate
		self.maxgenerations = maxgenerations
		self.generation = 0
		self.report = 0


	def _makepopulation(self):
		return [self.kind() for individual in range(self.size)]

	def run(self):
		while not self._goal():
			self.step()

	def _goal(self):
		return self.generation > self.maxgenerations or self.best.score == self.optimum

	def step(self):
		self.population.sort()
		self._crossover()
		self.generation += 1
		self.report()

	def _crossover(self):
		next_population = [self.best.copy()]
		while len(next_population) < self.size():
			mate1 = self._select()
			if random.random() < self.crossover_rate:
				mate2 = self._select()
				offspring = mate1.crossover(mate2)
			else:
				offspring = mate1.copy()
			for individual in offspring:
				self._mutate(individual)
				individual.evaluate(self.optimum)
				next_population.append(individual)
		self.population = next_population[:self.size]

	def _select(self):
		"sobrescrever para usar com o método de seleção preferido"
		return self._tournament()

	def _tournament(self, size=8, choosebest=0.90):
		competidors = [random.choice(self.population) for i in range(size)]
		competidors.sort()
		if random.random() < choosebest:
			return competidors[0]
		else:
			return random.choice(competidors[1:])

	def best():
		doc = "individuo com o melhor fitness na populacao"
		def fget(self):
			return self.population[0]
		return locals()
	best = property(**best())

	def report(self):
		print "="*70
		print "geracao: ", self.generation
		print "melhor da geracao: ", self.best













