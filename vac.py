import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

vac_df=pd.read_csv("covid_vaccine_statewise.csv")
print(vac_df.head(10))
print(vac_df.describe())
india_covid_df=pd.read_csv("covid_19_india.csv")
print(india_covid_df.head(10))
print(india_covid_df.describe())
#deleting column of not uses
del india_covid_df["Sno"]
del india_covid_df["Time"]
del india_covid_df["ConfirmedIndianNational"]
del india_covid_df["ConfirmedForeignNational"]
# india_covid_df["State/UnionTerritory"]=india_covid_df['State/UnionTerritory'].replace("Andaman and Nicobar Islands","Andaman Island")
# india_covid_df['State/UnionTerritory']=india_covid_df['State/UnionTerritory'].replace('Maharashtra***',"Maharashtra")
# india_covid_df['State/UnionTerritory']=india_covid_df['State/UnionTerritory'].replace('Madhya Pradesh***',"Madhya Pradesh")
# india_covid_df['State/UnionTerritory']=india_covid_df['State/UnionTerritory'].replace('Bihar****',"Bihar")
# india_covid_df["State/UnionTerritory"]=india_covid_df['State/UnionTerritory'].replace("Dadra and Nagar Haveli and Daman and Diu","Daman & Diu")
# india_covid_df['State/UnionTerritory']=india_covid_df['State/UnionTerritory'].replace('Karanataka',"Karnataka")
# # Delete these row indexes from dataFrame
# Unwanted = india_covid_df[ (india_covid_df['State/UnionTerritory'] == 'Unassigned' )| 
# (india_covid_df['State/UnionTerritory'] == 'Cases being reassigned to states') ].index
# india_covid_df.drop(Unwanted , inplace=True)
india_covid_df['Date']=pd.to_datetime(india_covid_df['Date'],format='%Y-%m-%d')
aCases=[]
for index, row in india_covid_df.iterrows():
    val= row["Confirmed"]-(row["Cured"]+row["Deaths"])
    aCases.append(val)
india_covid_df['Active Cases'] = aCases
#Growth Trend
fig=plt.figure(figsize=(13,8),facecolor="black")
grow = india_covid_df.loc[(india_covid_df['State/UnionTerritory'] =="Maharashtra" )|
(india_covid_df['State/UnionTerritory'] =="Uttar Pradesh")| 
(india_covid_df['State/UnionTerritory'] =="Karnataka") |
(india_covid_df['State/UnionTerritory'] =="Kerala") |
(india_covid_df['State/UnionTerritory'] =="Tamil Nadu")
]
print(grow.head(10))
ax4=sns.lineplot(grow ,x='Date',y='Active Cases',hue='State/UnionTerritory')
ax4.tick_params(color='white')
for spine in ax4.spines.values():
        spine.set_edgecolor('white')
ax4.set_facecolor('black')
ax4.set_title("Top 5 Affected States in India",size=30,color="white")
ax4.grid(linewidth=0.4, color='silver')
plt.xticks(color='white')
plt.yticks(color='white')
plt.xlabel("Date",size=25 ,color="white")
plt.ylabel("Active Cases",size=25,color="white")
plt.legend(loc='best')
plt.savefig("growth.jpeg")

# vaccination work
vac_df.rename(columns={'Updated On':'Vaccine_Date'},inplace=True)
vac_df.isnull().sum()
vac=vac_df
del vac["Sputnik V (Doses Administered)"]
del vac["AEFI"]
del vac["18-44 Years (Doses Administered)"]
del vac["45-60 Years (Doses Administered)"]
del vac["60+ Years (Doses Administered)"]
print(vac.head())

vaccine=vac_df[vac_df.State!='India']
print(vaccine.head())
vaccine.rename(columns={'Total Individuals Vaccinated':"Total"},inplace=True)
print(vaccine.head())

# Least vaccinated State
vaccine["State"]=vaccine['State'].replace("Dadra and Nagar Haveli and Daman and Diu","Damand & Diu")
vaccine["State"]=vaccine['State'].replace("Andaman and Nicobar Islands","Andaman Island")
stv1=vaccine.groupby('State')["Total"].sum()
stv1=stv1.to_frame("Total") #use to_frame() to convert stv into dataframe 
stv1=stv1.sort_values(by='Total',ascending=True)
print(stv1)
fig=plt.figure(figsize=(70,50),facecolor="black")
data=stv1.iloc[:10]
x_axis=data.index
y_axis=data.Total
ax2=plt.axes()
ax2.set_facecolor('black')
ax2.grid(linewidth=1,color="snow")
for spine in ax2.spines.values():
        spine.set_edgecolor('white')
        spine.set_linewidth(4)
plt.xticks(size='50',color='white')
plt.yticks(size='50',color='white')
ax2.set_xlabel('State/UnionTerritory',size="70",color="white")
ax2.set_ylabel('Vaccinated People',size="70",color="white")
ax2.set_title('Top 10 states with least vaccinated people in India',size=80,color="white")
mycol=["royalblue","darkseagreen","violet","gold","coral","bisque","pink","chocolate","lime","aqua"]
plt.bar(x_axis,y_axis,color=mycol,linewidth=8,edgecolor='white')
for i,height in zip(x_axis,y_axis):
    ax2.annotate(str(int(height)),
                xy=(i,height+3),
                color='white',size='50'
                ,xytext=(i,height),ha='center')
plt.savefig("lessvac10.jpeg")

#Top 10 states with Most vaccinated  people 
stv=vaccine.groupby('State')["Total"].sum()
stv=stv.to_frame("Total") #use to_frame() to convert stv into dataframe 
stv=stv.sort_values(by='Total',ascending=False)
print(stv)
fig=plt.figure(figsize=(70,40),facecolor="black")
# plt.title("Top 10 states with most vaccinated people in India",size=30,color='white')
data=stv.iloc[:10]
x_axis=data.index
y_axis=data.Total
ax2=plt.axes()
ax2.set_facecolor('black')
for spine in ax2.spines.values():
        spine.set_edgecolor('white')
        spine.set_linewidth(4)
ax2.grid(linewidth=1,color="snow")
plt.xticks(size='50',color='white')
plt.yticks(size='50',color='white')
ax2.set_xlabel('State/UnionTerritory',size="70",color="white")
ax2.set_ylabel('Vaccinated People',size="70",color="white")
ax2.set_title('Top 10 states with most vaccinated people in India',size=80,color="white")
mycol=["royalblue","darkseagreen","violet","gold","coral","bisque","pink","chocolate","lime","aqua"]
plt.bar(x_axis,y_axis,color=mycol,linewidth=8,edgecolor='white')
for i,height in zip(x_axis,y_axis):
    ax2.annotate(str(int(height)),
                xy=(i,height+3),
                color='white',size='50'
                ,xytext=(i,height),ha='center')
plt.savefig("vacmost10.jpeg")

#Comparision of Male vs Female vacccination 
male=vac['Male(Individuals Vaccinated)'].sum()
female=vac['Female(Individuals Vaccinated)'].sum()
gen=[]
gen.append(male)
gen.append(female)
label=["MALE","FEMALE"]
piecol=["red","blue"]
ax2 = plt.axes()
plt.figure(figsize=(12,6))
plt.title("Male vs Female vaccination", size=30)
plt.pie(gen,labels=label, colors=piecol,
autopct='%1.1f%%',textprops={'fontsize': 14}, shadow=True)
plt.xlabel("Male",size=2 ,color="white")
for spine in ax2.spines.values():
        spine.set_edgecolor('orange')
        spine.set_linewidth(4)
plt.ylabel("female",size=2,color="white")
plt.legend(label,loc="best")
plt.savefig("pievac.jpeg")