import json

funkWords = open('FunctionWords.txt').read().split('\r\n')
funkedHam = [0]*339
funkedMad = [0]*339
funkedDisputed = [[0]*339]*12


disp = 0

def update_the_funk(funkType, word, update):
    global disp
    ind = funkWords.index(word)
    if funkType == 'Hamilton':
        funkedHam[ind] += update
    elif funkType == 'Madison':
        funkedMad[ind] += update
    elif funkType == 'Disputed':
        funkedDisputed[disp][ind] += update



x = open('papers.txt').read()
papers = json.loads(x)

for key in papers.keys():
    boberto = papers[key]
    
    for bob in boberto:
        billy = filter(None, bob.split('\r\n'))
        i = 0
        while i < len(billy):
            billy[i] = ''.join([b for b in billy[i] if not b.isdigit() and b not in '!@#$%&*()?".,;'])
            i += 1

        combo = ' '.join(billy)
        for f in funkWords:
            z = combo.count(f)
            update_the_funk(key, f, z)

        if key == "Disputed":
            disp += 1


# print sum(funkedHam)
# print sum(funkedMad)
# print sum(funkedDisputed)

idealHam = [float(x)/sum(funkedHam) for x in funkedHam]
idealMad = [float(x)/sum(funkedMad) for x in funkedMad]

idealDisputed = [[0]*339]*12


for i in range(0,12):
    idealDisputed[i] = [float(x)/sum(funkedDisputed[i]) for x in funkedDisputed[i]]
    disputedHam = sum([(a-b)*(a-b) for a,b in zip(idealHam, idealDisputed[i])])
    disputedMad = sum([(a-b)*(a-b) for a,b in zip(idealMad, idealDisputed[i])])
    if disputedHam < disputedMad:
        print "Disputed Paper " + str(i+1) + " has been classified as Hamilton"
    else:
        print "Disputed Paper " + str(i+1) + " has been classified as Madison"
