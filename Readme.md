###Defend the Wall from White Walkers using optimization algorithms

This Game of Thrones inspired optimization exercise tries to find an even distribution of resources to defend three castles based on the cumulative skill ratings of the individual resouces. Out of trillions of possible configurations, the algorithm uses an optimization technique inspired by genetics/evolution to quickly find an almost perfect combination of resources. The algorithm starts with a random configuration each time it is run, so sometimes the results are more optimal than others. Due to the nature of this particular problem, perfect solutions are frequently produced.

###To run in python shell:

> import defend  
> solution = defend.optimization.geneticoptimize(defend.domain, defend.defendcost)  
> defend.printdefense(solution)  
