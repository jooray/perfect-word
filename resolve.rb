require 'eval.rb';

a=Evaluator.new()
db=a.get_db
h=db.execute("select word from evals where domainfree is null and neural>0 order by neural desc");
h.each do |n|
	puts n
	a.eval_domain_free(n[0])
end
