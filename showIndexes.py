import pickle

dataset = 'C'
split = 'cv2-0'

name = dataset + '_' + split

def showIndex(name):
    with open('obj/index_list_' + name + '.pkl','rb') as f:
        return pickle.load(f)

def showIndexTrain(name):
    with open('indexes/' + name + '_train.pkl','rb') as f:
        return pickle.load(f)

def showIndexRaw(name):
    with open('indexes/' + name + '.pkl','rb') as f:
        return pickle.load(f)

def showIndexTest(name):
    with open('indexes/' + name + '_test.pkl','rb') as f:
        return pickle.load(f)
"""
print('Index:')
print(showIndex(name))
print('IndexTrain:')
print(showIndexTrain(name))
print('IndexTest:')
print(showIndexTest(name))
"""
print(showIndexRaw(name))
print(len(showIndexRaw(name)))