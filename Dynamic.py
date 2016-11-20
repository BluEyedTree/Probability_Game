


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# initial plot_matrix code from: 
#   http://stackoverflow.com/questions/31998226/how-to-change-color-bar-to-align-with-main-plot-in-matplotlib

#note that we are forcing width:height=1:1 here, 
#as 0.9*8 : 0.9*8 = 1:1, the figure size is (8,8)
#if the figure size changes, the width:height ratio here also need to be changed
def update_matrix(mat, im, ax, title='example'):
    im.set_array(mat)
    ax.set_title(title)
    plt.pause(.5)

def plot_matrix(mat, im, ax, goal, sink, figsize, title='example'):
    for (x,y) in goal:
        rect = patches.Rectangle((y-.500,x-.500),1,1,edgecolor='lime',facecolor='lime')
        ax.add_patch(rect)
    for (x,y) in sink:
        rect = patches.Rectangle((y-.500,x-.500),1,1,edgecolor='r'   ,facecolor='r'   )
        ax.add_patch(rect)

    ax.grid(False)
    cax = plt.axes([0.85, 0.05, 0.05,0.9 ])
    plt.colorbar(mappable=im, cax=cax)
    update_matrix(mat, im, ax, title)
    return ax


def adjCubeList(x,y):
    if(x<19 and y <19 and x>0 and y>0):
        adjCubes = [(x,y+1), (x+1,y), (x,y-1), (x-1,y)]
        return adjCubes
    
    elif (x<19 and x>0 and y==19):
        adjCubes = [(x-1,y), (x,y-1), (x+1,y)]
        return adjCubes
    
    elif (x<19 and x>0 and y==0):
        adjCubes = [(x-1,y), (x+1,y), (x,y+1)]
        return adjCubes
    
    elif(y<19 and y>0 and x==0):
        adjCubes = [(x,y-1),(x+1,y), (x,y+1)]
        return adjCubes
    
    elif(y<19 and y>0 and x==19):
        adjCubes = [(x,y-1), (x-1,y), (x,y+1)]
        return adjCubes
    
    elif(x==19 and y==19):
        adjCubes=[(x-1,y),(x,y-1)]
        return adjCubes
        
    elif(x==0 and y==19):
        adjCubes=[(x,y-1), (x+1,y)]
        return adjCubes
        
    elif(x==0 and y==0):
        adjCubes=[(x,y+1),(x+1,y)]
        return adjCubes
    
    elif(x==19 and y==0):
        adjCubes=[(x-1,y),(x,y+1)]
        return adjCubes
        
def highestProb(inputList):
    #input list in the following format (probability, (x,y))

    highestProbNum = 0
    #probLocation = (0,0)
    for i in inputList:
        if i > highestProbNum:
            highestProbNum = i
            #probLocation = (i[1][0],i[1][1])
    return highestProbNum

  

def main():
    #data = np.random.random((20, 20))
    plt.show()
    ax = plt.axes([0, 0.05, 0.9, 0.9 ]) #left, bottom, width, height
    pCorrectMove = .40; # otherwise completely scatters with the remaining probability (with correct move still a possibility)
    data = np.zeros((20, 20))
    goal = [(17,17)]
    sink = [(12,18),(14,18),(13,18),(13,17),(13,16),(13,15),(13,14),(9,10),(10,10),(11,10),(12,10),(13,10),(14,10),(15,10),(7,11),(7,11),(7,13),(7,14),(7,15),(3,10),(4,9),(5,8),(6,7),(7,6),(8,5),(9,4),(10,3),(11,2),(12,1)]
    for (x,y) in goal:
        data[x,y]=1
    im = ax.imshow(data, interpolation='nearest', cmap=plt.get_cmap('Blues'))
        
    ax = plot_matrix(data, im, ax, goal, sink, (10, 10)) 
    for x in range(20):
        for y in range(20):
            data[x,y]=0
    
    for (x,y) in sink: 
        data[x,y]=0    
    for(x,y) in goal:
        data[x,y]=1

    for i in range(200):
        data0 = np.copy(data)
        for x in range(20):
            for y in range(20):
                adjacentCubes = adjCubeList(x,y)
                if (x,y) not in sink and (x,y) not in goal:
                    if(len(adjacentCubes)==4): 
                        prob1 = data[adjacentCubes[0][0],adjacentCubes[0][1]]
                        prob2 = data[adjacentCubes[1][0],adjacentCubes[1][1]]
                        prob3 = data[adjacentCubes[2][0],adjacentCubes[2][1]]
                        prob4 = data[adjacentCubes[3][0],adjacentCubes[3][1]]
                        probList = [prob1,prob2,prob3,prob4]
                        highestprob = highestProb(probList)
                        probList.remove(highestprob)     
                        x1 = 0.55*highestprob
                        x2 = 0.15*probList[0]
                        x3 = 0.15*probList[1]
                        x4 = 0.15*probList[2]
                        total = x1+x2+x3+x4
                        data[x,y] = total
                        
                        
                    elif(len(adjacentCubes)==3):
                        prob1 = data[adjacentCubes[0][0],adjacentCubes[0][1]]
                        prob2 = data[adjacentCubes[1][0],adjacentCubes[1][1]]
                        prob3 = data[adjacentCubes[2][0],adjacentCubes[2][1]]
                        probList = [prob1,prob2,prob3]
                        highestprob = highestProb(probList)
                        probList.remove(highestprob)
                        x1 = 0.6*highestprob
                        x2 = 0.2*probList[0]
                        x3 = 0.2*probList[1]
                        total = x1+x2+x3
                        data[x,y] = total
                    
                    elif(len(adjacentCubes)==2):
                        prob1 = data[adjacentCubes[0][0],adjacentCubes[0][1]]
                        prob2 = data[adjacentCubes[1][0],adjacentCubes[1][1]]
                        probList = [prob1,prob2]
                        highestprob = highestProb(probList)
                        probList.remove(highestprob)
                        x1 = 0.7*highestprob
                        x2 = 0.3*probList[0]
                        total = x1+x2
                        data[x,y] = total
                        
        for (x,y) in goal:
            data[x,y]=1 # This is the probability of a win if you are at (x,y) that is part of "goal"
        for (x,y) in sink:
            data[x,y]=0 # This is the probability of a win if you are at (x,y) that is part of "sink"
        update_matrix(data, im, ax,"iteration ("+str(i+1)+")")
        #ax, cax = plot_matrix(data, goal, sink, (10, 10), "iteration ("+str(i+1)+")") 
    ax = plot_matrix(data, im, ax, goal, sink, (10, 10), "iteration (FINAL)") 
    plt.pause(600)
    


main()
