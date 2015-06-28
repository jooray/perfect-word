
require "resolv"
require "sqlite3"

class Evaluator < Object

	def initialize
		@db = SQLite3::Database.new( "data/words.db" )
	end

	def insert_or_update(word, argname, value)
		c=@db.get_first_value('select count(*) from evals where word = ?', word) 
		if (!c) or (c==0) or (c=='0')
			@db.execute("insert into evals (word, #{argname}) values (?, ?)", word, value)
		else
			@db.execute("update evals set #{argname}=? where word=?", value, word)
		end

	end

	def eval_neural(word)
		a=@db.get_first_value('select neural from evals where word = ?', word)
		if a == nil
			a=0
			adr=Dir.pwd
			IO.popen("./test #{word}") do |f|
				s=f.gets
				if s
					a=s.chomp.to_f
				end
			end
			self.insert_or_update(word,"neural",a)
		end
		a.to_f
	end

	def get_db
		@db
	end

	def eval_domain_free(s)
		f=@db.get_first_value('select domainfree from evals where word = ?', s)
		if f == nil
		  f=Resolv::DNS.new.getresources(s+".com", Resolv::DNS::Resource::IN::NS).size == 0
		  self.insert_or_update(s,"domainfree", f ? 1 : 0)
		end
		f
	end

	def eval_human(s)
		@db.get_first_value('select human from evals where word = ?', s)
	end

	def eval(word)
		s=self.eval_human(word)
		if (s)
			return s.to_f/10
		else
			return self.eval_neural(word)
		end
	end

end


