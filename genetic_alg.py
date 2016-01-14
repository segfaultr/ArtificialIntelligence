#from StringIO import StringIO
import random
import math

letters = "abcdefghijklmnopqrstuvwxyz "




#finds the difference between two strings
#if 0 is returned, the two match
#1 is added for every char they are off in length 'abc', 'a' = 2
#a fraction of 1 is added for the distance between letters
#'a', 'b' = abs(ord('a')-ord('b'))/abs(ord(' ')-ord('z')) = 1/90
def evaluate(parent, target):
    #lengthdif = int(math.fabs(len(parent) - len(target)))
    score = 0.0
    #print lengthdif
    for x in range(len(parent)):
        if parent[x] != target[x]:
            score += float(abs(ord(parent[x])-ord(target[x])))/float(abs(ord(' ')-ord('z')))
            #score = score + 1
        #score += lengthdif
    return score

#generates a random word that is within the
#length of the target by at most +-5
def generate_random(target):
    word = ""
    for y in range(len(target)):
        word += letters[random.randint(0, len(letters) - 1)]
    return word

def next_population(parent1, parent2):
    if random.random() < .9:
        parent1, parent2 = crossover(parent1, parent2)
    bestchild1 = mutation(parent1)
    bestchild2 = mutation(parent2)
    for x in range(6):
        newchild1 = mutation(parent1)
        newchild2 = mutation(parent2)
        if evaluate(bestchild1, target) > evaluate(newchild1, target):
            bestchild1 = "" + newchild1
        if evaluate(bestchild2, target) > evaluate(newchild2, target):
            bestchild2 = "" + newchild2
    return bestchild1, bestchild2

#takes the front half of a parent and adds it to the latter half of a parent
#does it the other way and returns both
def crossover(parent1, parent2):
    crossovervalue = random.randint(1, len(parent1))
    #print crossovervalue
    tempparent1 = parent1[:crossovervalue] + parent2[crossovervalue:]
    tempparent2 = parent2[:crossovervalue] + parent1[crossovervalue:]
    return tempparent1, tempparent2

#takes a word, there is a 5% chance that any given letter will change
#by one space up or down
def mutation(child):
    mutated_child = ""
    for x in child:
        if random.random() < .05:
            if x == ' ':
                if random.random() < .5:
                    mutated_child += 'a'
                else:
                    mutated_child += 'z'
            elif x == 'a':
                if random.random() < .5:
                    mutated_child += ' '
                else:
                    mutated_child += 'b'
            elif x == 'z':
                if random.random() < .5:
                    mutated_child += ' '
                else:
                    mutated_child += 'y'
            else:
                if random.random() < .5:
                    mutated_child += chr(ord(x) + 1)
                else:
                    mutated_child += chr(ord(x) - 1)
            #mutated_child += letters[random.randint(0, len(letters) - 1)]
        else:
            mutated_child += x
    return mutated_child


def genetic_algorithm(target):
    parent1 = generate_random(target)
    parent2 = generate_random(target)
    while True:
        if evaluate(parent1, target) == 0:
            return parent1
        elif evaluate(parent2, target) == 0:
            return parent2

        parent1, parent2 = next_population(parent1, parent2)
        print parent1 + " : " +  parent2
        

target = "methinks it is like a weasel"
#target = "abcdefg"
genetic_algorithm(target)



