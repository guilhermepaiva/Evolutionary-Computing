#coding:utf-8

# um exemplo pra testar - o melhor individuo (considerando pra testar) vai ter seu cromossomo consistindo com 30 1's

import genetic

class OneMax(genetic.Individual):
	optimization = genetic.MAXIMIZE
	def evaluate(self, optimum=None):
		self.score = sum(self.chromossome)
	def mutate(self, gene):
		self.chromossome[gene] = not self.chromossome[gene] #bit flip


	if __name__ == "__main__":
		env = genetic.Environment(OneMax, maxgenerations=100, optimum=30)
		env.run()