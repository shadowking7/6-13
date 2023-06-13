import streamlit as st
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as pltt

# import Attrition by Attack csv file
@st.cache_data
def load_csv(file):
    return pd.read_csv(file)

#print all data (AA=Attrition by Attack)
AA = load_csv("Attrition by Attack (Updated).csv")

#columns on the page
col1, col2, col3, col4, = st.columns(4)

#shortens AA dataframe

AirData=AA[["design_point","iteration","AirbaseId","entityTypeName","EntityName","killCriteria", "porthosAttackName"]]
#st.write(AirData)

#dp=design point and iter=iteration
dp=1
iter=1
base="PGUA"
def bar_graph1():
    st.header("average kills by design point")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        #buttons for selecting design point and base
        akdp_dp = int(st.radio("Select a Design Point ", ("1", "2", "3", "4")))
        akdp_base = st.radio("Select a Base ", ("PGUA", "PAED"))

    kkillattrition=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["design_point"]==akdp_dp) & (AirData["AirbaseId"]==akdp_base)]
    killData=kkillattrition[["entityTypeName","killCriteria"]]
    #total kills by design point
    tkdp=killData.groupby(["entityTypeName"]).count()
    # st.header("total kills by design point")
    # st.write(tkdp)
    #average kills by design point. The 10 divides the total by the 10 iterations to give an average
    akdp=tkdp['killCriteria'] = tkdp['killCriteria'].div(10)
    # st.header("average kills by design point")
    # st.write(akdp)
    with col2:
        st.write("design point "+ str(dp))
        st.bar_chart(akdp)

#------------------------------------------------------
def bar_graph2():
    st.header("average kills in each design point")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        akie_base = st.radio("Pick a Base ", ("PGUA", "PAED"))

    #all kkills regardless of design point
    kkills=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["AirbaseId"]==akie_base)]
    AllKillData=kkills[["design_point","killCriteria"]]
    #total kills in each design point
    tkie=AllKillData.groupby(["design_point"]).count()
    # st.header("total kills in each design point")
    # st.write(tkie)
    #average kills in each design point. The 10 divides the total by the 10 iterations to give an average
    akie=tkie['killCriteria'] = tkie['killCriteria'].div(10)
    # st.header("average kills in each design point")
    # st.write(akie)
    with col2:
        st.bar_chart(akie)

#-------------------------------------------------------
#pie charts
#plane kkills
def pie_baby1():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        pk_dp = int(st.radio("Choose a Design Point", ("1", "2", "3", "4")))
        pk_base = st.radio("Choose a Base", ("PGUA", "PAED"))
    st.header("^^Attrition by Design Point " + str(pk_dp))


    #pie chart 1 setup
    kkillattrition_pk1=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["design_point"]==pk_dp) & (AirData["AirbaseId"]==pk_base)]
    pk1=kkillattrition_pk1[(kkillattrition_pk1["entityTypeName"]=="Bomber") | (kkillattrition_pk1["entityTypeName"]=="Fighter") | (kkillattrition_pk1["entityTypeName"]=="Tanker")]
    pk11=pk1[(pk1["porthosAttackName"]=="Attack1")]
    h1=pk11[["entityTypeName"]]
    hh1=h1.count()/10
    p1=hh1.iloc[0]
    hh1["Functioning"]=24-p1
    #actual pie chart
    fig1, ax1 = pltt.subplots()
    labels = 'Attrition','Functioning'
    explode = (0.1, 0)
    ax1.pie(hh1, explode=explode, shadow=True, labels=labels, autopct='%1.1f%%')
    ax1.axis('equal')

    #pie chart 2 setup
    kkillattrition_pk2=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["design_point"]==pk_dp) & (AirData["AirbaseId"]==pk_base)]
    pk2=kkillattrition_pk2[(kkillattrition_pk2["porthosAttackName"]=="Attack1") | (kkillattrition_pk2["porthosAttackName"]=="Attack2")]
    pk22=pk2[(pk2["entityTypeName"]=="Bomber") | (pk2["entityTypeName"]=="Fighter") | (pk2["entityTypeName"]=="Tanker")]
    h2=pk22[["entityTypeName"]]
    hh2=h2.count()/10
    p2=hh2.iloc[0]
    hh2["Functioning"]=24-p2
    #actual pie chart
    fig2, ax2 = pltt.subplots()
    labels = 'Attrition','Functioning'
    explode = (0.1, 0)
    ax2.pie(hh2, explode=explode, shadow=True, labels=labels, autopct='%1.1f%%')
    ax2.axis('equal')

    #pie chart 3 setup
    kkillattrition_pk3=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["design_point"]==pk_dp) & (AirData["AirbaseId"]==pk_base)]
    pk3=kkillattrition_pk3[(kkillattrition_pk3["porthosAttackName"]=="Attack1") | (kkillattrition_pk3["porthosAttackName"]=="Attack2") | (kkillattrition_pk3["porthosAttackName"]=="Attack3")]
    pk33=pk3[(pk3["entityTypeName"]=="Bomber") | (pk3["entityTypeName"]=="Fighter") | (pk3["entityTypeName"]=="Tanker")]
    h3=pk33[["entityTypeName"]]
    hh3=h3.count()/10
    p3=hh3.iloc[0]
    hh3["Functioning"]=24-p3
    #actual pie chart
    fig3, ax3 = pltt.subplots()
    labels = 'Attrition','Functioning'
    explode = (0.1, 0)
    ax3.pie(hh3, explode=explode, shadow=True, labels=labels, autopct='%1.1f%%')
    ax3.axis('equal')

    #diplaying everything
    with col2:
        st.write("After Attack 1")
        st.pyplot(fig1)
        st.write(hh1)
    with col3:
        st.write("After Attack 2")
        st.pyplot(fig2)
        st.write(hh2)
    with col4:
        st.write("After Attack 3")
        st.pyplot(fig3)
        st.write(hh3)

def pie_baby2():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        pk_dp = int(st.radio("Choose a Design Point ", ("1", "2", "3", "4")))
        pk_base = st.radio("Choose a Base ", ("PGUA", "PAED"))
    st.header("^^Attrition by Design Point "+ str(pk_dp))


    #pie chart 1 setup
    kkillattrition_pk1=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["design_point"]==pk_dp) & (AirData["AirbaseId"]==pk_base)]
    pk1=kkillattrition_pk1[(kkillattrition_pk1["entityTypeName"]=="Bomber") | (kkillattrition_pk1["entityTypeName"]=="Fighter") | (kkillattrition_pk1["entityTypeName"]=="Tanker")]
    pk11=pk1[(pk1["porthosAttackName"]=="Attack1")]
    h1=pk11[["entityTypeName"]]
    hh1=h1.count()/10
    p1=hh1.iloc[0]
    hh1["Functioning"]=24-p1
    #actual pie chart
    fig1, ax1 = pltt.subplots()
    labels = 'Attrition','Functioning'
    explode = (0.1, 0)
    ax1.pie(hh1, explode=explode, shadow=True, labels=labels, autopct='%1.1f%%')
    ax1.axis('equal')

    #pie chart 2 setup
    kkillattrition_pk2=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["design_point"]==pk_dp) & (AirData["AirbaseId"]==pk_base)]
    pk2=kkillattrition_pk2[(kkillattrition_pk2["porthosAttackName"]=="Attack1") | (kkillattrition_pk2["porthosAttackName"]=="Attack2")]
    pk22=pk2[(pk2["entityTypeName"]=="Bomber") | (pk2["entityTypeName"]=="Fighter") | (pk2["entityTypeName"]=="Tanker")]
    h2=pk22[["entityTypeName"]]
    hh2=h2.count()/10
    p2=hh2.iloc[0]
    hh2["Functioning"]=24-p2
    #actual pie chart
    fig2, ax2 = pltt.subplots()
    labels = 'Attrition','Functioning'
    explode = (0.1, 0)
    ax2.pie(hh2, explode=explode, shadow=True, labels=labels, autopct='%1.1f%%')
    ax2.axis('equal')

    #pie chart 3 setup
    kkillattrition_pk3=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["design_point"]==pk_dp) & (AirData["AirbaseId"]==pk_base)]
    pk3=kkillattrition_pk3[(kkillattrition_pk3["porthosAttackName"]=="Attack1") | (kkillattrition_pk3["porthosAttackName"]=="Attack2") | (kkillattrition_pk3["porthosAttackName"]=="Attack3")]
    pk33=pk3[(pk3["entityTypeName"]=="Bomber") | (pk3["entityTypeName"]=="Fighter") | (pk3["entityTypeName"]=="Tanker")]
    h3=pk33[["entityTypeName"]]
    hh3=h3.count()/10
    p3=hh3.iloc[0]
    hh3["Functioning"]=24-p3
    #actual pie chart
    fig3, ax3 = pltt.subplots()
    labels = 'Attrition','Functioning'
    explode = (0.1, 0)
    ax3.pie(hh3, explode=explode, shadow=True, labels=labels, autopct='%1.1f%%')
    ax3.axis('equal')

    #diplaying everything
    with col2:
        st.write("After Attack 1")
        st.pyplot(fig1)
        st.write(hh1)
    with col3:
        st.write("After Attack 2")
        st.pyplot(fig2)
        st.write(hh2)
    with col4:
        st.write("After Attack 3")
        st.pyplot(fig3)
        st.write(hh3)

# pie1=st.write(pie_baby1())
# pie2=st.write(pie_baby2())


#12 fighters
#4 bombers
#8 tankers

#-------------------------------------------------------
#Line Charts
#Plane kkills

# #Total Plane Kills in Attack 1 by design point
# pkkills1=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["AirbaseId"]==akie_base) & (AirData["porthosAttackName"]=="Attack1")]
# dppkkills1=pkkills1[(pkkills1["entityTypeName"]=="Bomber") | (pkkills1["entityTypeName"]=="Fighter") | (pkkills1["entityTypeName"]=="Tanker")]
# dpplane_killdata1=dppkkills1[["design_point","killCriteria"]]
# e1=dpplane_killdata1.groupby(["design_point"]).count()
# st.write(e1)
#
# #Total Plane Kills in Attack 2 by design point
# pkkills2=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["AirbaseId"]==akie_base) & (AirData["porthosAttackName"]=="Attack2")]
# dppkkills2=pkkills2[(pkkills2["entityTypeName"]=="Bomber") | (pkkills2["entityTypeName"]=="Fighter") | (pkkills2["entityTypeName"]=="Tanker")]
# dpplane_killdata2=dppkkills2[["design_point","killCriteria"]]
# e2=dpplane_killdata2.groupby(["design_point"]).count()
# st.write(e2)
#
# #Total Plane Kills in Attack 3 by design point
# pkkills3=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["AirbaseId"]==akie_base) & (AirData["porthosAttackName"]=="Attack3")]
# dppkkills3=pkkills3[(pkkills3["entityTypeName"]=="Bomber") | (pkkills3["entityTypeName"]=="Fighter") | (pkkills3["entityTypeName"]=="Tanker")]
# dpplane_killdata3=dppkkills3[["design_point","killCriteria"]]
# e3=dpplane_killdata3.groupby(["design_point"]).count()
# st.write(e3)
#
#
#
#
#
#
# #pk_line_chart=pd.DataFrame([e1,e2,e3],columns=["D1","D2","D3","D4"])
# #pk_line_chart=pd.DataFrame(columns=[e1,e2,e3])
# pk_line_chart=pd.DataFrame(e1)
# st.line_chart(pk_line_chart)




#-------------------------------------------------------

#killCriteria=AirData[["killCriteria"]]
#creating a column of kkills by design point/iteration
#kkillfighter=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["design_point"]==dp) & (AirData["iteration"]==iter) & (AirData["entityTypeName"]=="Fighter")]
#kkillbomber=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["design_point"]==dp) & (AirData["iteration"]==iter) & (AirData["entityTypeName"]=="Bomber")]
#kkilltanker=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["design_point"]==dp) & (AirData["iteration"]==iter) & (AirData["entityTypeName"]=="Tanker")]
#killcount=killCriteria.duplicated().sum()
#st.write(killcount)
#st.write(kkillattrition)

#attempt at making hist (AAH=AA Histogram)
# AAH=AA.hist(column=["iteration", "killCriteria"])
# st.write(AAH)

#prelim filtering code
#kkillattrition=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["design_point"]==dp) & (AirData["iteration"]==iter)]

#original successful bar chart
# kkillattrition=AirData[(AirData["killCriteria"]=="k-kill") & (AirData["design_point"]==dp) & (AirData["iteration"]==iter)]
# killData=kkillattrition[["entityTypeName","killCriteria"]]
# st.write(killData)

##kills by design point
# kbdp=killData.groupby(["entityTypeName"]).count()
# st.write(kbdp)
# st.bar_chart(kbdp)

#original pie chart code
# labels = 'Functioning', 'Attrition'
# sizes = [hh]
# explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
#
# fig1, ax1 = pltt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# st.pyplot(fig1)
#---------------------------------------------------------------

#real stuff
# pie1=st.write(pie_baby1())
# pie2=st.write(pie_baby2())
# bar1=st.write(bar_graph1())
# bar2=st.write(bar_graph2())

st.title("VMI AD-ARM APP")

bar1 = st.checkbox('Bar 1')
if bar1:
    st.write(bar_graph1())

bar2 = st.checkbox('Bar 2')
if bar2:
    st.write(bar_graph2())

pie1 = st.checkbox('Pie 1')
if pie1:
    st.write(pie_baby1())

pie2 = st.checkbox('Pie 2')
if pie2:
    st.write(pie_baby2())