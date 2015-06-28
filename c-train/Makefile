train: train.c
	gcc -o train -l fann -I/opt/local/include -L/opt/local/lib train.c

test: test.c 
	gcc -o test -l fann -I/opt/local/include -L/opt/local/lib test.c

test.h:
	python ./gen-test.py > test.h
