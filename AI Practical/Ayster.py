dict_hn={'Aurangabad':336,'Ausa':0,'Beed':160,'Bidar':242,'Carepur':161,
'Dhayri':176,'Fulkapur':77,'Gav':151,'Hinjewadi':226,'Ichalkaranji':244,
'Jayantpur':241,'Karepur':234,'Kolhapur':380,'Lonawala':100,'Moregaon':193,
'Narhe':253,'Navle':329,'Parali':80,'Renapur':199,'Talni':374}

dict_gn=dict(
Aurangabad=dict(Talni=75,Navle=118,Narhe=140),
Ausa=dict(Parali=85,Fulkapur=90,Lonawala=101,Fagaras=211),
Beed=dict(Bidar=120,Lonawala=138,Moregaon=146),
Bidar=dict(Jayantpur=75,Beed=120),
Carepur=dict(Gav=86),
Dhayri=dict(Narhe=99,Ausa=211),
Fulkapur=dict(Ausa=90),
Gav=dict(Carepur=86,Parali=98),
Hinjewadi=dict(Karepur=87,Renapur=92),
Ichalkaranji=dict(Jayantpur=70,Navle=111),
Jayantpur=dict(Ichalkaranji=70,Bidar=75),
Karepur=dict(Hinjewadi=87),
Kolhapur=dict(Talni=71,Narhe=151),
Lonawala=dict(Moregaon=97,Ausa=101,Beed=138),
Moregaon=dict(Narhe=80,Lonawala=97,Beed=146),
Narhe=dict(Moregaon=80,Dhayri=99,Aurangabad=140,Kolhapur=151),
Navle=dict(Ichalkaranji=111,Aurangabad=118),
Parali=dict(Ausa=85,Gav=98,Renapur=142),
Renapur=dict(Hinjewadi=92,Parali=142),
Talni=dict(Kolhapur=71,Aurangabad=75)
)
import queue as Q
start='Aurangabad'
goal='Ausa'
result=''
def get_fn(citystr):
    cities=citystr.split(" , ")
    hn=gn=0
    for ctr in range(0, len(cities)-1):
        gn=gn+dict_gn[cities[ctr]][cities[ctr+1]]
    hn=dict_hn[cities[len(cities)-1]]
    return(hn+gn)

def expand(cityq):
    global result
    tot, citystr, thiscity=cityq.get()
    if thiscity==goal:
        result=citystr+" : : "+str(tot)
        return
    for cty in dict_gn[thiscity]:
        cityq.put((get_fn(citystr+" , "+cty), citystr+" , "+cty, cty))
    expand(cityq)

def main():
    cityq=Q.PriorityQueue()
    thiscity=start
    cityq.put((get_fn(start),start,thiscity))
    expand(cityq)
    print("The A* path with the total is: ")
    print(result)
main()
