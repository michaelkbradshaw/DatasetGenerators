import random
import json




def createPerson():
    person = {}    
    setSex(person)
    setAge(person)
    setIncome(person)
    setChildren(person)
    setBloodType(person)
    setExperiment(person)
    setWeights(person)
    return person


def setSex(person):
    person["sex"] = random.choice(["male","female"])


def setAge(person):
    base = 55
    if(random.random()<.65):
        base = 30

    person["age"] = int(random.normalvariate(base,5))


def setBloodType(person):

    types = ["A","B","AB","O"]
    weights = [40,11,4,45]

    person["bloodType"] = random.choices(types,weights=weights)[0]

def setIncome(person):
    base = 10
    ageAdjusted = base+ random.random()*person["age"]*1.25
    if(person["sex"]=="female"):
        ageAdjusted *=.9

    person["income"] = f'{int(ageAdjusted)*1000:,}'
    

def getIncome(person):
    return int(person["income"].replace(",",""))


def setChildren(person):
    ageBase = .25
    if(person["age"]>50):
        ageBase = 2
    elif(person["age"]>30):
        ageBase = 1

    income = getIncome(person)
    incomeBase = 0
    if(income<20000):
        incomeBase=2
    elif(incomeBase<50000):
        incomeBase=1


    person["children"]= int(random.weibullvariate(ageBase+incomeBase,4))


def setExperiment(person):
    person["experiment"] = random.choice(["Control","Drug A","Drug B"])

def getWeightBase(person):
    base = 88
    if(person["sex"] == "female"):
        base = 76

    ageBase = (person["age"]-25)*.25

    if(ageBase<1):
        ageBase=1

    income = getIncome(person)

    if(income>100000):
        ageBase = ageBase*.25
    elif(income>60000):
        ageBase=ageBase*.5

    if(person["children"]==1):
        ageBase *= 1.1
    elif(person["children"]==2):
        ageBase*=1.3
    elif(person["children"]>2):
        ageBase*=1.6


 #   mean = (base+ageBase)*1.3
   # print(1/mean,mean)
#    return random.gammavariate(2,mean/2);
    mean = 1/(base*ageBase*.05)

    return base*1.1+random.expovariate(mean)




def getEffectiveness(person):
    exp = person["experiment"]

    if(exp == "control"):
        return -.1

    if(exp == "Drug A"):
        return -.2

    if(exp == "Drug B"):
        if(person["bloodType"]=="B" or person["bloodType"]=="AB"):
            return 1
        else:
            return -.5

        
    
def setWeights(person):
    base = getWeightBase(person)
    weight = base;
    weights = [weight,]

    eff = getEffectiveness(person)

    for i in range(15):
        weight = weight+random.normalvariate(eff,1)
        weights.append(weight)
    
    
    person["weights"]=weights

        
    
    
    

#for i in range(100):
#    print(createPerson()["children"])
data = []
for i in range(100):
    data.append(createPerson())

    #print(createPerson()["weights"][0])
    #print( json.dumps(createPerson()) )

text = json.dumps(data,indent=1)
out = open("weightLoss.json","w")
out.write(text)
out.close();

    
