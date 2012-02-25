import random
import optimization
import pprint

castles = [
  #                   % of fighting
  #Name            Arrow   Close Combat  Brothers
  ['eastwatch',       0.2,    0.8,         []],
  ['castleblack',     0.4,    0.6,         []],
  ['shadowtower',     0.2,    0.8,         []]
]

brothers = [
  #Name            Arrow  Close Combat
  ['jonsnow',         8,    8],
  ['samtarly',        1,		5],
  ['dolorousedd',     5,		4],
  ['eddisontollett',  5,		3],
  ['cotterpyke',      6,		6],
  ['clydas',          2,		4],
  ['bowenmarsh',      4,		1],
  ['hobb',            3,		7],
  ['donalnoye',       6,		0],
  ['owen',            3,		3],
  ['yarwick',         2,		5],
  ['cellador',        4,		3],
  ['jackbulwer',      3,		2],
  ['emmett',          5,		7],
  ['denys',           5,		4],
  ['wallace',         6,		2],
  ['mullin',          3,		1],
  ['halfhand',        9,		9],
  ['stonesnake',      7,		8],
  ['harmune',         2,		5],
  ['tattersalt',      2,		5],
  ['glendon',         4,		6],
  ['hewett',          6,		1],
  ['maynard',         2,		1],
  ['barleycorn',      2,		5],
  ['robb',            9,		9],
  ['bran',            2,		7],
  ['rickon',          2,		2],
  ['barristan',      10,	 10],
  ['lordmormont',     7,		8],
  ['arya',            4,		6],
  ['brienne',         9,		9],
  ['tyrion',          4,		8],
  ['ned',            10,   10]
]

#What a solution looks like:
# [0,1,2,0,2,0,1,0,0,2,1,2,0,0,1,0,2,1,1,0,2,1,0...]
#where each list slot represents a particular brother
#from the brothers list, and the value of a slot 
#represents the castle that brother is assigned to

#So, there are len(castles)**len(brothers) possibilities,
#which at the time of writing = 3**34 = A SHITLOAD (like trillions)

#What the domain looks like
# [(0,2),(0,2),(0,2),(0,2),(0,2),(0,2),(0,2)...]
domain = [(0,2)] * len(brothers)

#This is just used for informal testing of the cost fn
randomvec = [random.randint(domain[i][0],domain[i][1])
             for i in range(len(domain))]

#Add up the total strength for each skill possessed by a brother
totarrowstrength = sum([i[1] for i in brothers])
totclosestrength = sum([i[2] for i in brothers])

#Ideal arrow and close strength value at each castle.
#This is simple right now becuase we're just dividing total
#strengths by # of castles. It will get more difficult
#when we have to determine the fighting conditions of each
#castle (i.e. how much is arrow fighting and how much close combat)
optimalarrowstrength = int(totarrowstrength) / len(castles)
optimalclosestrength = int(totclosestrength) / len(castles)

def defendcost(vec):
  cost = 0

  #Start by just being happy to evenly distribute brothers among
  #the castles. After that, maybe consider the fighting style 
  #of each castle.

  #Make sure castles are empty
  for c in range(len(castles)):
    castles[c][3] = []

  #Add brothers to the castles based on the solution vector passed in
  for b in range(len(vec)):
    castles[vec[b]][3].append(b)

  #Loop through the castles and determine how strength was 
  #distributed and calculate cost
  for c in range(len(castles)):
    castlebrothers = [brothers[i] for i in castles[c][3]]
    #Add up all the strength of the brothers in the castle
    solutionarrowstrength = sum([i[1] for i in castlebrothers])
    solutionclosestrength = sum([i[2] for i in castlebrothers])

    #Normalize the number to be always non-negative: abs(). B/C whether 
    #the solution over or under supplies the castle is irrelevant (I think)
    cost += abs(optimalarrowstrength - solutionarrowstrength)
    cost += abs(optimalclosestrength - solutionclosestrength)

  return cost

#Print out a solution (w/ names of brothers and castles, etc)
def printdefense(vec):

  #Make sure castles are empty
  for c in range(len(castles)):
    castles[c][3] = []

  for b in range(len(vec)):
    castles[vec[b]][3].append(b)
  for castle in castles:
    print "=== Castle: %s ===" % castle[0]
    for bro in castle[3]:
      print "%15s A: %2s  S: %2s" % (brothers[bro][0], brothers[bro][1], brothers[bro][2])
    tarrow = sum([brothers[i][1] for i in castle[3]])
    tclose = sum([brothers[i][2] for i in castle[3]])
    print "Arrow strength at castle: %s" % tarrow
    print "Close strength at castle: %s" % tclose

#optimization.geneticoptimize(domain, defendcost)
#optimization.annealingoptimize(domain, defendcost)
#optimization.hillclimb(domain, defendcost)
#optimization.randomoptimize(domain, defendcost)

def main():
  s = optimization.geneticoptimize(domain, defendcost)
  printdefense(s)

if __name__ == "__main__":
    import profile
    profile.run("main()")
