from operator import itemgetter
import pprint
import random

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

#What the domain looks like
# [(0,2),(0,2),(0,2),(0,2),(0,2),(0,2),(0,2)...]
domain = [(0,2)] * len(brothers)

randomvec = [random.randint(domain[i][0],domain[i][1])
             for i in range(len(domain))]
print randomvec

totarrowstrength = sum([i[1] for i in brothers])
totclosestrength = sum([i[2] for i in brothers])

print totarrowstrength, totclosestrength

def defendcost(vec):
  #Start by just being happy to evenly distribute brothers among
  #the castles.

  #After that, consider fighting style of each castle.

  cost = 0

  #Add brothers to the castles
  for b in range(len(vec)):
    castles[vec[b]][3].append(b)

  #Ideal arrow and close strength at each castle
  optimalarrowstrength = int(totarrowstrength) / len(castles)
  optimalclosestrength = int(totclosestrength) / len(castles)

  print "Optimal arrow strength: %s, optimal close strength: %s " % (optimalarrowstrength, optimalclosestrength)

  #Determine how strength was distributed

  for c in range(len(castles)):
    castlebrothers = [brothers[i] for i in castles[c][3]]
    print castlebrothers
    
    arrowstrength = sum([i[1] for i in castlebrothers])
    closestrength = sum([i[2] for i in castlebrothers])

    print "%s arrow strength: %s" % (castles[c][0], arrowstrength)
    print "%s close strength: %s" % (castles[c][0], closestrength)

  """
  One way to determine cost is to subtract arrow strength from optimal arrow strength.
  So, if we got an arrow strength at eastwatch of 34, and optimal is 54, the cost is 54 - 34 = 20.
  But wait, what if it happens that we allocate too much, so like eastwatch got 74 and optimal is 54.
  54 - 74 is -20. The # 20 shows up again. We could just normalize everything to a +ive int.
  Because (I *think*) whether we over allocated or under allocated doesn't actually matter does it? They're
  both just a mis-allocation of X amount.
  ""


