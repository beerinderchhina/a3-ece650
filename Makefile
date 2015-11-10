all: Graph rgen driver

Graph: Graph.c
    gcc -Wall -std=c89 Graph.c -o Graph

rgen: rgen.c
    gcc -Wall -std=c89 rgen.c -o rgen
	
driver: driver.c
    gcc -Wall -std=c89 driver.c -o a3-ece650
clean:
	rm -f a3-ece650
