from .models import DPA
from .models import DPB

def compute(weights,distances,maxweight):
    n=len(weights)
    anslst=[]

    maxmusk=2 ** n
    #slno=serialno
    serialno=0
    #print("This is the dpB table")
    for i in range(maxmusk):
        wt=0
        print(i)
        #to calculate the total weight of destinations present in a subset
        for z in range(n):
            if i&(1<<z) > 0:
                wt+=weights[z]


        if wt > maxweight :
            continue

        mincostsub=999999999999999
        cnt=0
        for y in range(n):
            if i&(1<<y) > 0:
                cnt+=1
                mincostsub=min(mincostsub,distances[n][y]+DPA.objects.get(subsetno=i ,vertexno=y).cost)
        #print(str(i)+" "+str(mincostsub))
        if mincostsub!=999999999999999:
            newobj=DPB(subsetno=i,cost=mincostsub,slno=serialno)
            anslst.append((i,mincostsub/cnt))
            #print("DPB:"+str(serialno)+" "+str(i)+" "+str(mincostsub))
            serialno+=1
            newobj.save()

        #to add '1' wherever it finds a '0'
        for j in range(n):
            if i&(1<<j) == 0:
                newgrp=i|(1<<j)
                nwt=wt+weights[j]
                if nwt > maxweight :
                    continue
                #here newgroup in newgrp starting with j
                mincost=999999999999999
                for k in range(n):
                    if i&(1<<k) > 0:
                        cost=distances[j][k] + DPA.objects.get(subsetno=i ,vertexno=k).cost
                        mincost=min(mincost,cost)
                if mincost == 999999999999999:
                    mincost=distances[j][n]
                #add newgrp j mincost
                #print("DPA:"+str(newgrp)+" "+str(j)+" "+str(mincost))
                nrow=DPA(subsetno=newgrp,vertexno=j,cost=mincost)
                nrow.save()

    mini=compute2(serialno,n,distances,anslst)
    #print("Its working")
    return (mini,serialno)

#print(DPB.objects.get(subsetno=1).id)

def compute2(total,n,ditances,anslst):
    ival=0
    flst=[]
    anslst=sorted(anslst,key=lambda x:x[1])
    for (i,j) in anslst:
        if ival+i == ival^i :
            flst.append(i)
            ival=ival+i
            if ival == (2**n -1):
                break

    return flst

    '''
    maxmusk= 2**total
    min=-1
    minval=999999999999999
    for i in list(reversed(range(maxmusk))):
        #print(i)
        tempval=0
        cost=0
        for j in range(total):
            if i&(1<<j)>0 :
                tempval+=DPB.objects.get(slno=j).subsetno
                cost+=DPB.objects.get(slno=j).cost
        if tempval==(2**n -1) and cost<minval :
            min=i;
            minval=cost
            break
    print("The min ie i="+str(min))
    return min
    #for j in range(total):
    #    if min&(1<<j)>0 :
    #        print(j)
    '''
