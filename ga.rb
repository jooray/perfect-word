require "eval.rb"

class Generator

	def initialize(population,maxsize)
		@e=Evaluator.new
		@p=Array.new
		population.each do |w|
			@p << [w, self.calculate_fitness(w)]
		end
		@maxsize=maxsize
		self.sort_population
	end
	
	def population
		@p
	end

	def eval_population
		a=Array.new
		@p.each do |k|
			if k[1]>0 and @e.eval_domain_free(k[0])
				a << k[0]
			end
		a
		end
	end
	def sort_population
		@p.sort! do |a,b|
			a[1]<=>b[1]
		end
	end

	def calculate_fitness(word)
		@e.eval(word)
	end

	def generate_population(psize)
		while @p.size < psize
			@p << self.generate_random()
		end
	end

	def mutate(s)
		a="abcdefghijklmnopqrstuvwxyz"
		word="#{s}"
		p=rand(word.size)
		word[p]=a[rand(a.size)]
		word
	end

	def crossover(s1,s2)
		cut1=rand(s1.size)
		cut2=rand(s2.size)
		w=s1[0,cut1]+s2[0,cut2]
		if w.size>15
			w=w[0,15]
		end
		w
	end

	def generation
		size=@p.size
		(size/2).to_i.times do 
			w1=@p[rand(size)]
			w2=@p[rand(size)]
			w = self.crossover(w1[0], w2[0])
			if w.size>4
				@p << [w,self.calculate_fitness(w)]
			end
		end
#		(size/10).to_i.times do 
#			w = self.mutate(@p[rand(size)][0])
#			@p << [w,self.calculate_fitness(w)]
#		end	

		self.sort_population
		if @p.size > @maxsize
			@p = @p[@p.size-@maxsize,@p.size-1]
		end
	end

end


# should contain all characters, this is the starting population
a=Generator.new( ['technology','science','business','think','forward','pushing','solutions','services','ultimate','universal','network','max','base','knowledge','intelligence','inter','networking','expert','reasoning','distribute','balance','advanced','essential','connecting','source','trust','architect','digital','experience','high','brain','mind','value','ability','gate','peak','experience','clever','smart','pure','skill','robust','artful','profound','constan','value'], 300 )

15.times do |generation|
	puts generation
	a.generation
end

print a.eval_population
