
# coding: utf-8

# ## Generrating the ordering for diferrent strategies

import random
import numpy as np
random.seed(2018)

def ordering(nrows, ncols, groups, methods, percentFamily = [0.2, 0.4]):
    ''' 
    inputs:
        nrows, ncols:  integer, number of rows and columns of the airplane
        groups: integer, number of groups
        methods: string, different strategies
                 'BTF': Back-to-Front with ordering
                 'BLOCK': Back-to-Front with Blocks
                 'WILMA': Window-Middle-Asile
                 'RASS': Random-with-AssignSeats
                 'RFOALL': Random-Free-for-All
                 'STFOPT': Steffan-optimal
                 'STFMOD': Steffan-Modified-Optimal
                 'Amigos': Amigos-Steffan method
                 'REVPYR': Reverse Pyramid

    return: a list of the ordering
    '''
    ordering = []

    if methods == "BTF":
        for i in range(nrows-1, -1, -1):
            for j in range(ncols//2):
                ordering.append([i, ncols - j - 1])
                ordering.append([i, j])

    elif methods == 'BLOCK':
        blocRows = nrows // groups
        for i in range(0, groups, 2):
            lower = nrows - blocRows*(i + 1)
            upper = nrows - blocRows*i
            blocks = [[j, k] for j in range(lower, upper) for k in range(ncols)]
            random.shuffle(blocks)
            ordering = ordering + blocks
        for i in range(1, groups, 2):
            lower = nrows - blocRows*(i + 1)
            upper = nrows - blocRows*i
            blocks = [[j, k] for j in range(lower, upper) for k in range(ncols)]
            random.shuffle(blocks)
            ordering = ordering + blocks

    elif methods == 'WILMA':
        # 3 groups: windows, midlle, asile
        for j in range(groups):
            blocks = [[k, j] for k in range(nrows)] + [[k, ncols - j - 1] for k in range(nrows)]
            random.shuffle(blocks) 
            ordering = ordering + blocks

    elif methods == 'RASS':
        ordering = [[i, j] for i in range(nrows) for j in range(ncols)]
        random.shuffle(ordering)


    elif methods == 'STFOPT':
        for i in range(ncols//2):
            even1 = [[j, ncols - i - 1] for j in range(nrows-1, -1, -2)]
            even2 = [[j, i] for j in range(nrows-1, -1, -2)]

            odd1 = [[j, ncols - i - 1] for j in range(nrows-2, -1, -2)]
            odd2 = [[j, i] for j in range(nrows-2, -1, -2)]
            ordering = ordering + even1 + even2 + odd1 + odd2

    elif methods == 'STFMOD':
        for i in range(groups//2):
            # four groups: right even -> left even -> right odd -> left odd
            blocks1 = [[j, k] for j in range(nrows-1-i, -1, -groups//2) for k in range(ncols-1, (ncols-1)//2, -1)]
            random.shuffle(blocks1)
            blocks2 = [[j, k] for j in range(nrows-1-i, -1, -groups//2) for k in range((ncols-1)//2, -1, -1)]
            random.shuffle(blocks2)
            ordering = ordering + blocks1 + blocks2
            
    elif methods == 'RFOALL':
        total = ncols*nrows
        col_prob = [0.175, 0.025, 0.3, 0.3,0.025, 0.175]
        
        while len(ordering) < total:
            j = np.random.choice(ncols, 1, p=col_prob, replace=True)
            if j[0] == 0 or j[0] == 5:
                # ind = np.random.choice(nrows,1)
                ind = int(np.random.gamma(1,nrows/6))
                person = [ind, j[0]]
            elif j[0] ==1 or j[0] ==4:
                ind = int(np.random.gamma(1,nrows/6))
                person = [ind, j[0]]
            elif j[0] ==2 or j[0] ==3:
                ind = int(np.random.gamma(1,nrows/6))
                person = [ind, j[0]]
            
            if person in ordering or person[0] >= nrows:
                continue
            else:
                ordering.append(person)
    
    elif methods == 'REVPYR':
        ncols = 6                    # only works for 6 columns and 4 or 5 groups
        
        if groups == 4:
            cut1 = nrows // 4        # group 1 starts here
            
            group1 = [[j,k] for j in range(cut1,nrows) for k in [0,5]]
            random.shuffle(group1)
#             print(group1)
            
            b = 2*cut1               # group 2 middle ends here
            group2A = [[j,k] for j in range(0,cut1) for k in [0,5]]
            group2B = [[j,k] for j in range(b,nrows) for k in [1,4]]
            group2 = group2A + group2B
            random.shuffle(group2)

            c = 3*cut1               # group 3 aisle ends here (also size group 4)
            group3A = [[j,k] for j in range(0,b) for k in [1,4]]
            group3B = [[j,k] for j in range(c,nrows) for k in [2,3]]
            group3 = group3A + group3B
            random.shuffle(group3)

            group4 = [[j,k] for j in range(0,c) for k in [2,3]]
            random.shuffle(group4)

            ordering = ordering + group1 + group2 + group3 + group4
            
        elif groups == 5:
            cut1 = 2*nrows // 5 

            group1 = [[j,k] for j in range(cut1,nrows) for k in [0,5]]
            random.shuffle(group1)
            print(group1)
            
            cut2 = 2*cut1 // 5                      
            b = 2*cut1 - cut2                   # group 2 middle comes up to here 
            group2A = [[j,k] for j in range(cut2,cut1) for k in [0,5]]
            group2B = [[j,k] for j in range(b,nrows) for k in [1,4]]
            group2 = group2A + group2B
            random.shuffle(group2)
            
            c = 3*cut1 - nrows                  # group 3 middle comes up to here
            group3A = [[j,k] for j in range(0,cut2) for k in [0,5]]
            group3B = [[j,k] for j in range(c,b) for k in [1,4]]
            group3 = group3A + group3B
            random.shuffle(group3)

            d = 4*cut1 - nrows                  # size group 5
            group4A = [[j,k] for j in range(0,c) for k in [1,4]]
            group4B = [[j,k] for j in range(d,nrows) for k in [2,3]]
            group4 = group4A + group4B
            random.shuffle(group4)
                         
            group5 = [[j,k] for j in range(0,d) for k in [2,3]]
            random.shuffle(group5)
            ordering = ordering + group1 + group2 + group3 + group4 + group5
            
        else:
            print('Number of groups should be 4 or 5.')
            
    elif methods == 'Amigos':
        percentFamSize_3 = percentFamily[0]
        percentFamSize_2 = percentFamily[1]/(1 - percentFamily[0])
        ordering = initial_distribution(nrows, ncols, groups, percentFamSize_3, percentFamSize_2)
                
                
#     print('Length of the ordering:', len(ordering))
    
    if len(ordering) != nrows*ncols:
        print(len(ordering))
        print('The total number of passengers is not correct!')
    
    return ordering



## Amigos ordering:

def initial_distribution(nrows,ncols,groups,percentFamily3,percentFamily2):

    ordering = []
    
    for i in range(ncols//2):
        even1 = [[j, ncols - i - 1] for j in range(nrows-1, -1, -2)]
        even2 = [[j, i] for j in range(nrows-1, -1, -2)]

        odd1 = [[j, ncols - i - 1] for j in range(nrows-2, -1, -2)]
        odd2 = [[j, i] for j in range(nrows-2, -1, -2)]
        ordering = ordering + even1 + even2 + odd1 + odd2
            
#     ordering = ordering(nrows, ncols, groups, 'STFOPT')
    sampling = [[i, j] for i in range(nrows) for j in [0, 3]]
    families3 = random.sample(sampling, int(2*nrows*percentFamily3))
    
    for x in families3:
        sampling.remove(x)

    
    families2 = random.sample(sampling,int((2*nrows - len(families3))*percentFamily2))
    for x in families2:
        x[1] = x[1] + int(np.asarray(random.sample([0,1],1)))
    
    row = families2[0]
    
    print('Families of size 3:', families3)
    print('Families of szie 2:', families2)
    
    families3_copy = families3[:]
    families2_copy = families2[:]
    
    for row in families3:
        families3_copy.append([row[0],row[1]+1])
        families3_copy.append([row[0],row[1]+2])

    for row in families2:
        families2_copy.append([row[0],row[1]+1])
     
    
    families3 = families3_copy
    families2 = families2_copy


    for row in ordering:
        if row in families3:
            row.append(3)
        if row in families2:
            row.append(2)
        if len(row) == 2:
            row.append(1)
    
    i = 0
    
    while i < len(ordering):
        x = ordering[i]
        
        if x[2] == 3:
            p = (int(x[1] < 3) - 0.5)*2
            p1 = [x[0],x[1] + int(p),x[2]]
            p2 = [x[0],x[1] + int(2*p),x[2]]
            ordering.remove(p1)
            ordering.remove(p2)
            ordering.insert(ordering.index(x) + 1,p1)
            ordering.insert(ordering.index(x) + 2,p2)
            i = i + 3
            
        elif x[2] == 2:
            p = (int(x[1]<3) - 0.5)*2
            p1 = [x[0],x[1] + int(p),x[2]]
            ordering.remove(p1)
            ordering.insert(ordering.index(x) + 1,p1)
            i = i + 2
            
        else:
            i = i + 1
        
    a = [(x[1] == 0 or x[1] == 5) for x in ordering]
    group1 = max([index for index, value in enumerate(a) if value == True])
    
    group1_no = group1 + ordering[group1][2]
    
    # Now group1_no is the number of the first group
    ordering1 = ordering[:(group1_no)]
   
    ordering_rest = ordering[group1_no:]
    
    #print("ordering1 is of length", len(ordering1),"at the beginning")
    i = 0
    bumplist = ["initial"]
    # Start shuffling
    while i < (group1_no - 1):
        #print("ordering1 at",i,"is",ordering1)
        #print("and group1_no is",group1_no,"and length of ordering1 is",len(ordering1))
        w = ordering1[i]
        
        if w[2] == 3 and (i + 3) < (group1_no-1):
            
            x = ordering1[i+3]
            if x not in bumplist:
                if x[0] not in [0,nrows-1,nrows-2]:
                    if x[2] > 1:
                        
                        ordering1 = rotate_family(ordering1,i+3,bumplist)
                        
                        bumplist = ordering1[-1]
                        ordering1 = ordering1[:-1]
                    else:
                        
                        if (nrows - x[0] - 1)%2 == 0:
                            #print("case1")
                            bumplist.append(x)
                            ordering1.remove(x)
                            ordering1_del = [[row[0],row[1]] for row in ordering1]
                            index1 = ordering1_del.index([x[0]+1,x[1]])
                            index2 = index1 + ordering1[index1][2]
                            ordering1.insert(index2,x)
                        else:
                            ordering1_del = [[row[0],row[1]] for row in ordering1]
                            ordering_rest_del = [[row[0],row[1]] for row in ordering_rest]
                            brother = [x[0]+1,x[1]+ int(2*(int(x[1]<3)-0.5))]
                            if brother in ordering1_del:
                                #print("case3")
                                # The place I want to put him to has a family and has been moved
                                ordering1.remove(x)
                                ordering1.append(x)
                                bumplist.append(x)
                                
                            else:
                                #print("case4")
                                ordering1.remove(x)
                                group1_no = group1_no - 1
                                
                                index1 = ordering_rest_del.index(brother)
                                index2 = index1 + ordering_rest[index1][2]
                                ordering_rest.insert(index2,x)
 
        i = i + w[2]
    #print("ordering1 is",ordering1)
    #print("ordering_rest is",ordering_rest)
    preordering = ordering1 + ordering_rest
    
    ordering = [[x[0],x[1]] for x in preordering]
            
        
    return ordering


# In[4]:


def rotate_family(ordering1,i,bumplist):
    family_no = ordering1[i][2]
    
    p0 = ordering1[i]
    
    p1 = ordering1[i+1]
    
    if family_no == 3:
        p2 = ordering1[i+2]
        
    ordering1.remove(p0)
    ordering1.remove(p1)
    ordering1.append(p0)
    ordering1.append(p1)
    bumplist.append(p0)
    bumplist.append(p1)
    if family_no == 3:
        ordering1.remove(p2)
        ordering1.append(p2)
        bumplist.append(p2)
        
    ordering1.append(bumplist)    
    return ordering1
