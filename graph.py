import csv 
import matplotlib.pyplot as plt
#reading csv file of covid 19 india
covidfile="covid_19_india.csv"
covid_india = csv.reader(open(covidfile,"r"), delimiter =",", quotechar='"')
I ={}
m= []
rownum =0
for row in covid_india:
	rownum+=1
	if(rownum == 1):
		for i in range(len(row)):
			I[row[i]]=i
		continue
	elif(len(row)==0):
		continue
	else:
		m.append(row)
for i in range(5):
        print(m[i])
#reading  covid vaccination csv of india 
vacfile="covid_vaccine_statewise.csv"
vac_india = csv.reader(open(vacfile,"r"), delimiter =",", quotechar='"')
I1={}
v= []
rownum =0
for row in vac_india:
	rownum+=1
	if(rownum == 1):
		for i in range(len(row)):
			I1[row[i]]=i
		continue
	elif(len(row)==0):
		continue
	else:
		v.append(row)
for i in range(5):
        print(v[i])
 #removing anamoly from datasets
for i in range(len(m)):
        if m[i][I["State/UnionTerritory"]]=="Andaman and Nicobar Islands":
                m[i][I["State/UnionTerritory"]]="Andaman Island"
        if m[i][I["State/UnionTerritory"]]=="Maharashtra***":
                m[i][I["State/UnionTerritory"]]="Maharashtra"
        if m[i][I["State/UnionTerritory"]]=="Bihar****":
                m[i][I["State/UnionTerritory"]]="Bihar"
        if m[i][I["State/UnionTerritory"]]=="Madhya Pradesh***":
                 m[i][I["State/UnionTerritory"]]="Madhya Pradesh"
        if m[i][I["State/UnionTerritory"]]=="Dadra and Nagar Haveli and Daman and Diu":
          m[i][I["State/UnionTerritory"]]="Daman & Diu"
        if m[i][I["State/UnionTerritory"]]=="Karanataka":
                m[i][I["State/UnionTerritory"]]="Karnataka"
        if m[i][I["State/UnionTerritory"]]=="Himanchal Pradesh":
                m[i][I["State/UnionTerritory"]]="Himachal Pradesh"
#removing unwanted rows &column
for row in m:
        if row[I["State/UnionTerritory"]]=="Unassigned":  
                m.remove(row)
        if row[I["State/UnionTerritory"]]=="Cases being reassigned to states":
                m.remove(row)
g=sorted(m,key=lambda l:l[3])
# Extracting basic Information
my_data=[]
for i in range(len(g)-1):
        if g[i][3]!=g[i+1][3]:
                 row=[]
                 row.extend([g[i][1],g[i][3],int(g[i][6]),int(g[i][7]),int(g[i][8])])
                 my_data.append(row)
for i in range(5):
        print(my_data[i])

for row in my_data:
#finding Recovery rates of states
        x = (row[2]*100)/row[4]
        row.append(x)
 #finding mortality rate of states
        y = (row[3]*100)/row[4]
        row.append(y)
for i in range(5):
        print(my_data[i])
# plotting graph between mortality rate vs recovery rate
colors ={5:'blue', 6:'red'}
lss ={5:'-', 6:'-.'}
label={5:'Recovery Rate', 6:'Mortality Rate'}
x_axis= list(map(lambda r:r[1],my_data))
plt.figure(figsize=(15,8),facecolor="black")
ax2=plt.axes()
ax2.set_facecolor('black')
ax2.tick_params(color='white')
for spine in ax2.spines.values():
        spine.set_edgecolor('white')
ax2.grid(linewidth=0.4,color="snow")
for col in [5,6]:
        y_axis= list(map(lambda r : r[col],my_data))
        plt.plot(x_axis,y_axis,label=label[col],ls= lss[col], color= colors[col],linewidth=2)
plt.title("Mortality Rate VS Recovery Rate of different states of india",size=22)
plt.xticks(rotation='vertical',color="white")
plt.yticks(rotation='horizontal',color="white")
plt.ylabel("Rate",color="white",size=20)
plt.xlabel("State/UnionTerritory",color="white",size=20)
plt.legend(loc='best')
plt.savefig("rate.png", bbox_inches = 'tight')

#finding active cases 
state_active = []
for i in my_data:
        all_cases = 0
        for j in m:
                if i[1] == j[3]: 
                        if all_cases < (int(j[8])-(int(j[6])+int(j[7]))) :
                                all_cases = (int(j[8])-(int(j[6])+int(j[7]))) 
        state_active.append([i[1], all_cases])
state_active=sorted(state_active,key=lambda l:l[1],reverse=True)
for i in range(10):
        print(state_active[i])
x=[]
y=[]
for i in range(10):
        x.append(state_active[i][0])
        y.append(state_active[i][1])

#Plotting graph between  Active cases and States
plt.figure(figsize=(70,50),facecolor="black")
ax2=plt.axes()
ax2.set_facecolor('black')
ax2.grid(linewidth=1,color="snow")
for spine in ax2.spines.values():
        spine.set_edgecolor('white')
        spine.set_linewidth(4)
plt.xticks(size='50',color='white')
plt.yticks(size='50',color='white')
ax2.set_xlabel('State/UnionTerritory',size=75,color="white")
ax2.set_ylabel('Active Cases',size=75,color="white")
ax2.set_title('Active cases vs States',size=80,color="white")
mycol=["royalblue","darkseagreen","violet","gold","coral","bisque","pink","chocolate","lime","aqua"]
plt.bar(x,y,color=mycol,linewidth=8,edgecolor='white')
for i,height in zip(x,y):
    ax2.annotate(str(int(height)),
                xy=(i,height+3),
                color='white',size=50
                ,xytext=(i,height),ha='center')
plt.savefig("active10.jpeg")

#finding growth of covid cases of top 5 states with most active cases
growth = []
for i in my_data:
        for j in m:
                if i[1] == j[3]:
                        growth.append([j[1], int(j[8]) - (int(j[6])+ int(j[7])), i[1]])

# plotting graph betwen growth rate and states
plt.figure(figsize=(15,8),facecolor="black")
ax2=plt.axes()
ax2.set_facecolor('black')
ax2.tick_params(color='white')
for spine in ax2.spines.values():
        spine.set_edgecolor('white')
for i in ['Maharashtra', 'Uttar Pradesh', 'Karnataka', 'Kerala', 'Tamil Nadu']:
        x_axis = [x[0] for x in growth  if x[2] == i]
        y_axis= [x[1] for x in growth if x[2] == i]
        plt.plot(x_axis,y_axis,label =i,linewidth=2)
plt.title("Growth Rate",size=22)
plt.grid(linewidth=0.4, color='silver')
plt.xticks(['2020-05-05',  '2020-07-05',  '2020-09-05',  '2020-11-05', \
        '2021-01-05', '2021-03-05',  '2021-05-05',  '2021-07-05']\
                , labels = ['2020-05', '2020-07', '2020-09', '2020-11', \
                        '2021-01', '2021-03', '2021-05', '2021-07'], color="white", rotation='vertical')
plt.yticks(rotation='horizontal',color="white")
plt.ylabel("Active Cases",color="white",size=20)
plt.xlabel("Date",color="white",size=20)
plt.legend(loc='best')
plt.savefig("growth.png", bbox_inches = 'tight')

#finding  total deaths during coving in each states
state_death = []
for i in my_data:
        all_death = 0
        for j in m:
                if i[1] == j[3]: 
                        if all_death < int(j[7]) :
                                all_death = int(j[7])
        state_death.append([i[1], all_death])
state_death=sorted(state_death,key=lambda l:l[1],reverse=True)
for i in range(10):
        print(state_death[i])

# plotting graph Death cases vs States
x=[]
y=[]
for i in range(10):
        x.append(state_death[i][0])
        y.append(state_death[i][1])
plt.figure(figsize=(70,50),facecolor="black")
ax2=plt.axes()
ax2.set_facecolor('black')
ax2.grid(linewidth=1,color="snow")
for spine in ax2.spines.values():
        spine.set_edgecolor('white')
        spine.set_linewidth(4)
plt.xticks(size='50',color='white')
plt.yticks(size='50',color='white')
ax2.set_xlabel('State/UnionTerritory',size=75,color="white")
ax2.set_ylabel('Deaths',size=75,color="white")
ax2.set_title('Deaths Cases vs States',size=80,color="white")
plt.bar(x,y,color=mycol,linewidth=8,edgecolor='white')
for i,height in zip(x,y):
    ax2.annotate(str(int(height)),
                xy=(i,height+3),
                color='white',size=50
                ,xytext=(i,height),ha='center')
plt.savefig("death10.jpeg")

#finding overall +ve test cases of each states  
overalposCase = []
for i in my_data:
        poscase = 0
        for j in m:
                if i[1] == j[3]: 
                        if poscase < int(j[8]) :
                                poscase = int(j[8])
        overalposCase.append([i[1], poscase])
        
#plotting graph of top 10 states having high no of +ve test cases
overalposCase=sorted(overalposCase,key=lambda l:l[1],reverse=True)
x=[]
y=[]
for i in range(10):
        x.append(overalposCase[i][0])
        y.append(overalposCase[i][1])
plt.figure(figsize=(70,50),facecolor="black")
ax3=plt.axes()
ax3.set_facecolor('black')
ax3.grid(linewidth=1,color="snow")
for spine in ax3.spines.values():
        spine.set_edgecolor('white')
        spine.set_linewidth(4)
plt.xticks(size='50',color='white')
plt.yticks(size='50',color='white')
ax3.set_xlabel('State/UnionTerritory',size=75,color="white")
ax3.set_ylabel('Positive Confirmed Cases',size=75,color="white")
ax3.set_title('Overall +ve Cases vs States',size=80,color="white")
plt.bar(x,y,color=mycol,linewidth=8,edgecolor='white')
for i,height in zip(x,y):
    ax3.annotate(str(int(height)),
                xy=(i,height+3),
                color='white',size=50
                ,xytext=(i,height),ha='center')
plt.savefig("overposcase10.jpeg")

f=sorted(m,key=lambda l:(l[3],int(l[8])))
for i in range(len(f)-1):
        if f[i][3]==f[i+1][3]:
                val = int(f[i+1][8])-int(f[i][8])
                f[i].append(val)
growcnf = []
for i in my_data:
        for j in f:
                if i[1] == j[3]: 
                        if len(j) == 10:
                                growcnf.append([j[1], i[1], j[9]])    
plt.figure(figsize=(15,8),facecolor="black")
ax2=plt.axes()
ax2.set_facecolor('black')
ax2.tick_params(color='white')
for spine in ax2.spines.values():
        spine.set_edgecolor('white')
for i in ['Maharashtra', 'Andhra Pradesh', 'Karnataka', 'Kerala', 'Tamil Nadu']:
        x_axis = [x[0] for x in growcnf  if x[1] == i]
        y_axis= [x[2] for x in growcnf if x[1] == i]
        plt.plot(x_axis,y_axis,label =i,linewidth=2)
plt.title("+VE test case ",size=22)
plt.grid(linewidth=0.4, color='silver')
plt.xticks(['2020-05-05',  '2020-07-05',  '2020-09-05',  '2020-11-05', \
        '2021-01-05', '2021-03-05',  '2021-05-05',  '2021-07-05']\
                , labels = ['2020-05', '2020-07', '2020-09', '2020-11', \
                        '2021-01', '2021-03', '2021-05', '2021-07'], color="white", rotation='vertical')

plt.yticks(rotation='horizontal',color="white")
plt.ylabel("+ve test cases",color="white",size=20)
plt.xlabel("Date",color="white",size=20)
plt.legend(loc='best')
plt.savefig("growpos.png", bbox_inches = 'tight')

#plotting graph of top 10 states having high no of +ve test cases
overalposCase=sorted(overalposCase,key=lambda l:l[1])
x.clear()
y.clear()
for i in range(10):
        x.append(overalposCase[i][0])
        y.append(overalposCase[i][1])
plt.figure(figsize=(70,50),facecolor="black")
ax3=plt.axes()
ax3.set_facecolor('black')
ax3.grid(linewidth=1,color="snow")
for spine in ax3.spines.values():
        spine.set_edgecolor('white')
        spine.set_linewidth(4)
plt.xticks(size='50',color='white')
plt.yticks(size='50',color='white')
ax3.set_xlabel('State/UnionTerritory',size=75,color="white")
ax3.set_ylabel('Positive Confirmed Cases',size=75,color="white")
ax3.set_title('Top 10 States having low Overall +ve Cases ',size=80,color="white")
plt.bar(x,y,color=mycol,linewidth=8,edgecolor='white')
for i,height in zip(x,y):
    ax3.annotate(str(int(height)),
                xy=(i,height+3),
                color='white',size=50
                ,xytext=(i,height),ha='center')
plt.savefig("overposless10.jpeg")

#vaccination work starts
#reducing states name as it stops overlapping of xticks
for i in range(len(v)):
        if v[i][1]=="Andaman and Nicobar Islands":
                v[i][1]="Andaman Island"
        if v[i][I1['State']]=="Dadra and Nagar Haveli and Daman and Diu":
          v[i][I1["State"]]="Daman & Diu"
#extracting info about states only
vaccine= []
for row in v:
        if row[I1['State']]!="India":
                vaccine.append(row)
states= set()
for i in vaccine:
        states.add(i[1])

#finding total vacination done in each state 
state_vac= []
for i in states:
        totvac = 0
        for j in vaccine:
                if i == j[1] and j[2] !='': 
                        if totvac < float(j[2]) :
                                totvac = float(j[2])
        state_vac.append([i, totvac])
for i in range(5):
        print(state_vac[i])

#plotting graph of lowest number of vaccination states
vac10less=sorted(state_vac,key=lambda x:x[1])
fig=plt.figure(figsize=(70,50),facecolor="black")
x_axis=[]
y_axis=[]
for i in range(10):
        x_axis.append(vac10less[i][0])
        y_axis.append(vac10less[i][1])
ax2=plt.axes()
ax2.set_facecolor('black')
ax2.grid(linewidth=1,color="snow")
for spine in ax2.spines.values():
        spine.set_edgecolor('white')
        spine.set_linewidth(4)
plt.xticks(size='50',color='white')
plt.yticks(size='50',color='white')
ax2.set_xlabel('State/UnionTerritory',size="70",color="white")
ax2.set_ylabel('Vaccinated People(in Cr)',size="70",color="white")
ax2.set_title('Top 10 states with least vaccinated people in India',size=80,color="white")
mycol=["bisque","darkseagreen","chocolate","gold","pink","royalblue","lime","coral","violet","aqua"]
plt.bar(x_axis,y_axis,color=mycol,linewidth=8,edgecolor='white')
for i,height in zip(x_axis,y_axis):
    ax2.annotate(str(int(height)),
                xy=(i,height+3),
                color='white',size='50'
                ,xytext=(i,height),ha='center')
plt.savefig("lessvac10.jpeg")

#plotting graph of highest number of vaccination states
vac10top=sorted(state_vac,key=lambda x:x[1],reverse=True)
fig=plt.figure(figsize=(70,40),facecolor="black")
x_axis=[]
y_axis=[]
for i in range(10):
        x_axis.append(vac10top[i][0])
        y_axis.append(vac10top[i][1])
ax2=plt.axes()
ax2.set_facecolor('black')
for spine in ax2.spines.values():
        spine.set_edgecolor('white')
        spine.set_linewidth(4)
ax2.grid(linewidth=1,color="snow")
plt.xticks(size='50',color='white')
plt.yticks(size='50',color='white')
ax2.set_xlabel('State/UnionTerritory',size="70",color="white")
ax2.set_ylabel('Vaccinated People(in Cr)',size="70",color="white")
ax2.set_title('Top 10 states with most vaccinated people in India',size=80,color="white")
plt.bar(x_axis,y_axis,color=mycol,linewidth=8,edgecolor='white')
for i,height in zip(x_axis,y_axis):
    ax2.annotate(str(int(height)),
                xy=(i,height+3),
                color='white',size='50'
                ,xytext=(i,height),ha='center')
plt.savefig("vacmost10.jpeg")

#Comparision Between Male and female vaccination       
male=0
female=0
transgender=0
for row in v:
        if row[I1['State']]=="India":
                if row[I1["Male(Individuals Vaccinated)"]]!="" or row[I1["Female(Individuals Vaccinated)"]]!="" :
                        male += float(row[I1["Male(Individuals Vaccinated)"]])
                        female+= float(row[I1["Female(Individuals Vaccinated)"]])
gen=[]
gen.extend([male,female])
label=["MALE","FEMALE"]
piecol=["orange","green"]
ax2 = plt.axes()
plt.figure(figsize=(12,6))
plt.title("Male vs Female vaccination", size=30)
plt.pie(gen,labels=label, colors=piecol,
autopct='%1.1f%%',textprops={'fontsize': 14}, shadow=True)
plt.xlabel("Male",size=2 ,color="white")
for spine in ax2.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(4)
plt.ylabel("female",size=2,color="white")
plt.legend(label,loc="best")
plt.savefig("pievac.jpeg")























