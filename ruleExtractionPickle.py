import pickle

dataset = 'TitanicHakankBinary'
split = '1'

name = dataset + '_' + split

def showBio(name):
    with open('obj/bio_' + name + '.pkl','rb') as f:
        return pickle.load(f)

def showBNN(name):
    with open('obj/BNN_' + name + '.pkl','rb') as f:
        return pickle.load(f)

def showEx(name):
    with open('obj/example_cond_dict_' + name + '.pkl','rb') as f:
        return pickle.load(f)

def showIndex(name):
    with open('obj/index_list_' + name + '.pkl','rb') as f:
        return pickle.load(f)

def showIndexTrain(name):
    with open('indexes/' + name + '_train.pkl','rb') as f:
        return pickle.load(f)

def showIndexTest(name):
    with open('indexes/' + name + '_test.pkl','rb') as f:
        return pickle.load(f)

print('Datatype Bio: ' + str(type(showBio(name))))
print('Datatype BNN: ' + str(type(showBNN(name))))
print('Datatype Ex: ' + str(type(showEx(name))))
print('Datatype Index: ' + str(type(showIndex(name))))
print('Datatype IndexTrain: ' + str(type(showIndexTrain(name))))
print('Datatype IndexTest: ' + str(type(showIndexTest(name))))
print('')

#print(len(showBio(name)))
print(len(showBNN(name)))
print(len(showEx(name)))
print(len(showIndex(name)))
print(len(showIndexTrain(name)))
print(len(showIndexTest(name)))
print('')
print('Bio:')
print(showBio(name))
print('BNN:') 
print(showBNN(name))
print('Ex:')
print(showEx(name))
print('Index:')
print(showIndex(name))
print('IndexTrain:')
print(showIndexTrain(name))
print('IndexTest:')
print(showIndexTest(name))
