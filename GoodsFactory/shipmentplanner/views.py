from django.shortcuts import render
from . import forms
from .models import Shipments
from .models import DPA
from .models import DPB
from .MyFunc import compute
from .scripts import getDist
from .scripts import getOrigin
#from PredLog.models import PlannedShipments
import json
# Create your views here.
way=[]
def FirstPageHandler(request):
    global way
    formInp=forms.AddShipmentsForm()
    ow=forms.fform()
    if request.method=='POST':
        if 'AddShipment' in request.POST :
            formInp =forms.AddShipmentsForm(request.POST)
            l=len(Shipments.objects.all())
            T=Shipments(slno=l,destination=formInp['destination'].value(),weight=formInp['weight'].value())
            T.save()
            formInp=forms.AddShipmentsForm()

        elif 'ClearThem' in request.POST:
            Shipments.objects.all().delete()


        elif 'PlanShipment' in request.POST:
            DPA.objects.all().delete()
            DPB.objects.all().delete()
            ow=forms.fform(request.POST)
            weights=list(ship.weight for ship in Shipments.objects.all())
            #weights=weights[0:-1]
            #print(weights)
            destinations=list(ship.destination for ship in Shipments.objects.all())
            #print(destinations)
            destinations.append(ow['origin'].value())
            t=Shipments(slno=len(Shipments.objects.all()),destination=ow['origin'].value(),weight=0)
            t.save()
            distances=getDist()
            #print(distances)
            #weights=[30,12,34,40]
            #distances=[[10,23,45,43,22],[22,44,67,12,43],[98,54,43,66,33],[23,66,77,88,44],[55,34,77,55,44]]
            maxweight=int(ow['weight'].value())
            (min,total) = compute(weights,distances,maxweight)
            subsetnolist=min
            '''for j in range(total):
               if min&(1<<j)>0 :
                    subsetnolist.append(DPB.objects.get(slno=j).subsetno)'''
            fans=[]
            fans2=[]
            fans3=[]
            for j in subsetnolist:
                    ro=[]
                    ro1=[]
                    wt=0
                    n=len(weights)
                    for k in range(n):
                        if j&(1<<k) > 0:
                            ro.append(Shipments.objects.get(slno=k).destination)
                            ro1.append(Shipments.objects.get(slno=k).destination)
                            wt+=Shipments.objects.get(slno=k).weight
                            fans2.append({ 'location':Shipments.objects.get(slno=k).destination})

                    fans3.append(ro1)
                    len(fans3)
                    ro.append(wt)
                    fans.append(ro)
                    fans2.append({ 'location':Shipments.objects.get(slno=n).destination})

            n=len(weights)
            lst=[]
            way=fans2
            lst.append({'waypoints':fans2,'origin':Shipments.objects.get(slno=n).destination,'destination':Shipments.objects.get(slno=n).destination,'travelMode':'DRIVING'})
            j_s=json.dumps(lst)
            j_s2=json.dumps(fans3)

            origi=json.dumps(getOrigin(Shipments.objects.get(slno=n).destination))
            originame=json.dumps([Shipments.objects.get(slno=n).destination])
            fans2.insert(0,{'location':Shipments.objects.get(slno=n).destination})
            #for z in range(len(fans2)-2):
            #    T=PlannedShipments(ShipmentId=len(PlannedShipments.objects.all()),StartLocation=fans2[z]['location'],EndLocation=fans2[z+1]['location'])
            #    T.save()

            return render(request,'output2.html',{'fans':fans,'j':j_s ,'wp':j_s2,'org':origi,'orgname':originame})




    return render(request,'index.html',{'form1':formInp,'ow':ow, 'data':Shipments.objects.all()})
