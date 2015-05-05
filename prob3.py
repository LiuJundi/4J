import os
import multiprocessing
import time
import Queue
import random

def preprocess():
    f = open(os.path.join(BASE_DIR,'train.txt'),"r")
    j = 0
    subprob = []
    qA = Queue.PriorityQueue()
    qB = Queue.PriorityQueue()
    for j in range(1,76):
        a = "train" + str(j)
        file_path = os.path.join(BASE_DIR, a)
        subprob +=[open(file_path,'wb')]
    for line in f:
        if line[0] == 'A':
            qA.put(line)
        else:
            qB.put(line)
    while not qA.empty():
        i_a = random.randint(1,5)
        patA = qA.get()
        for num in range((i_a-1)*15,i_a*15):
            subprob[num].write(patA)
    while not qB.empty():
        i_b = random.randint(0,14)
        patB = qB.get()
        for m in [i_b,i_b+15,i_b+30,i_b+45,i_b+60]:
            subprob[m-1].write(patB)
    for i in range(0,75):
        subprob[i].close()
    f.close()

def train(train_name):
    a = './train'+' '+train_name
    p1 = os.popen(a)

def predict(model_name, test_name, output_name):
    b = './predict'+' '+test_name+' '+model_name+' '+output_name
    p2 = os.popen(b)
    print p2.read()

if __name__ == "__main__":
    time_start = time.time()
    BASE_DIR = os.getcwd()
    preprocess()
    time_middle = time.time()
    p = []
    q = []
    for i in range(0,75):
        p += [multiprocessing.Process(target=train, args=(os.path.join(BASE_DIR,'train'+str(i+1)),))]
        p[i].start()
    for i in range(0,75):
        p[i].join()
    for i in range(0,75):
        q += [multiprocessing.Process(target=predict, args=(os.path.join(BASE_DIR,'train'+str(i+1)+'.model'),os.path.join(BASE_DIR,'test.txt'),os.path.join(BASE_DIR,'output'+str(i+1))))]
        q[i].start()
    for i in range(0,75):
        q[i].join()
    time_end = time.time()
    print time_end-time_middle,time_middle-time_start
