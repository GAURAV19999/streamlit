import seaborn as sns
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

# Set Page Layout
st.set_page_config(layout='wide')

#Load the dataset*

df = pd.read_excel(r"C:\Users\Admin\Downloads\Dashboard_Code\Cleaned_UBL_Data.xlsx")

# SIDEBAR

st.sidebar.subheader('Select to Filter the data')

# By Gender

st.sidebar.text('By Gender')

filter_gender = st.sidebar.radio('Filter by Gender', options=['Both','Female','Male'])

if filter_gender == 'Both':
    
    pass

else:
    
    df = df.query('gender == @filter_gender')

#By PC

PC_select = st.sidebar.selectbox('Select Parliament',options=['All','Chittoor','Hindupur','Kadapa','Narasaraopet','Narsapuram','Nellore','Ongole','Vijayawada'])

if PC_select == 'All':
    pass

else:
    
    df = df.query('Parliament == @PC_select')

#By AC
AC_select = st.sidebar.selectbox('Select Assembly',options=['All','Darsi','Gurzala','Jaggayyapet','Kamalapuram','Kovur','Kuppam','Mylavaram','Nellore City','Penukonda','Undi'])

if AC_select == 'All':
    pass

else:
    
    df = df.query('Assembly == @AC_select')    
    
#By ULB

ULB_select = st.sidebar.selectbox('Select ULB',options=['All','Corporation','Municipality','Nagara Panchayath'])

if ULB_select == 'All':
    pass

else:
    
    df = df.query('ULB == @ULB_select')
#By Occupation

Occupation_select = st.sidebar.selectbox('Select occupation',options=['All','Businessman/ Trader','Daily Wage Workers','Farmer','Fisherman','Government Employee','Housewife','Private employee','Retired','Self Employed','Small business owner (Shop, vendor etc)','Student','Teacher/Professor','Unemployed','Village Volunteer'])

if Occupation_select == 'All':
    pass

else:
    df = df.query('Respondent_Occupation==@Occupation_select')
    
                     
# Title
st.title('ULB Election Dashboard')

#Separator
st.markdown('---')

# Columns Summary

st.subheader('| QUICK SUMMARY')

col1, col2, col3,col4 = st.columns(4)

# column 1
with col1:
    st.title(df.Parliament.nunique())
    st.text('Parliament')
# coloumn 2    
with col2:
    st.title(df.Assembly.nunique())
    st.text('Assembly')
# coloumn 3    
with col3:
    st.title(df.ULB.nunique())
    st.text('ULB')
# coloumn 4    
with col4:
    st.title(df.Name_of_the_Urban_Local_Body.nunique())
    st.text('Overall Urban Local Body')    
    
# Graphics
col1, col2, col3 = st.columns(3)

#Opinion on drugs

with col1:
    ind1 = pd.DataFrame(df.groupby('Recent_drugs_smuggling_article_in_AP_newspaper').Recent_drugs_smuggling_article_in_AP_newspaper.count()).rename(columns={'Recent_drugs_smuggling_article_in_AP_newspaper':'count'}).reset_index()
    g1 = px.pie(ind1,
                values='count',
                names='Recent_drugs_smuggling_article_in_AP_newspaper',
                color='Recent_drugs_smuggling_article_in_AP_newspaper',
                color_discrete_map={'Yes, there is an increase': 'green','No': 'red','''Don't know''':'grey','Maybe':'dark grey'},
                title='| OPINION ON DRUGS')
    g1.update_traces(textposition='inside',
                     textinfo='percent+label',
                     showlegend=False)
    st.plotly_chart(g1,use_container_width=True)

#Do you think that Govt is being negligible towards drug smuggling

with col3:
    ind3 = pd.DataFrame(df.groupby('Govt_is_being_negligible_towards_drug_smuggling').Govt_is_being_negligible_towards_drug_smuggling.count()).rename(columns={'Govt_is_being_negligible_towards_drug_smuggling':'count'}).reset_index()
    g1 = px.pie(ind3,
                values='count',
                names='Govt_is_being_negligible_towards_drug_smuggling',
                color='Govt_is_being_negligible_towards_drug_smuggling',
                color_discrete_map={'Yes': 'green','No': 'red','''Don't Know''':'grey','Maybe':'dark grey'},
                title='| Govt_is_being_negligible_towards_drug_smuggling')
    g1.update_traces(textposition='inside',
                     textinfo='percent+label',
                     showlegend=False)
    st.plotly_chart(g1,use_container_width=True)

# Who will win the upcoming election

with col1:
    ind1 = pd.DataFrame(df.groupby('who_will_win_in_the_upcoming_Municipality_Nagar_Panchayat_elections_in_your_area').who_will_win_in_the_upcoming_Municipality_Nagar_Panchayat_elections_in_your_area.count()).rename(columns={'who_will_win_in_the_upcoming_Municipality_Nagar_Panchayat_elections_in_your_area':'count'}).reset_index()
    g1 = px.pie(ind1,
                values='count',
                names='who_will_win_in_the_upcoming_Municipality_Nagar_Panchayat_elections_in_your_area',
                color='who_will_win_in_the_upcoming_Municipality_Nagar_Panchayat_elections_in_your_area',
                color_discrete_map={'TDP':'yellow','YSRCP':'blue','''Didn't Answer''':'grey','BJP & Jenasena':'orange','Others':'dark grey'},
                title='| Upcoming Election Winner')
    g1.update_traces(textposition='inside',
                     textinfo='percent+label',
                     showlegend=False)
    st.plotly_chart(g1,use_container_width=True)

# Whom will you vote 

with col3:
    ind3 = pd.DataFrame(df.groupby('Whom_will_you_vote_in_the_upcoming_Municipality_Nagar_Panchayat_elections_in_your_area').Whom_will_you_vote_in_the_upcoming_Municipality_Nagar_Panchayat_elections_in_your_area.count()).rename(columns={'Whom_will_you_vote_in_the_upcoming_Municipality_Nagar_Panchayat_elections_in_your_area':'count'}).reset_index()
    g1 = px.pie(ind3,
                values='count',
                names='Whom_will_you_vote_in_the_upcoming_Municipality_Nagar_Panchayat_elections_in_your_area',
                color='Whom_will_you_vote_in_the_upcoming_Municipality_Nagar_Panchayat_elections_in_your_area',
                color_discrete_map={'TDP':'yellow','YSCRP':'blue','''Didn't Answer''':'grey','BJP & Jenasena':'orange','Others':'dark grey'},
                title='| Whom will you vote')
    g1.update_traces(textposition='inside',
                     textinfo='percent+label',
                     showlegend=False)
    st.plotly_chart(g1,use_container_width=True)
    
# DO you think upcoming election reflaction 


with col1:
    ind1 = pd.DataFrame(df.groupby('Do_you_think_that_the_upcoming_Municipality_Nagar_Panchayat_elections_in_your_area_will_be_a_reflection_in_the_next_assembly_election').Do_you_think_that_the_upcoming_Municipality_Nagar_Panchayat_elections_in_your_area_will_be_a_reflection_in_the_next_assembly_election.count()).rename(columns={'Do_you_think_that_the_upcoming_Municipality_Nagar_Panchayat_elections_in_your_area_will_be_a_reflection_in_the_next_assembly_election':'count'}).reset_index()
    g1 = px.pie(ind1,
                values='count',
                names='Do_you_think_that_the_upcoming_Municipality_Nagar_Panchayat_elections_in_your_area_will_be_a_reflection_in_the_next_assembly_election',
                color='Do_you_think_that_the_upcoming_Municipality_Nagar_Panchayat_elections_in_your_area_will_be_a_reflection_in_the_next_assembly_election',
                color_discrete_map={'Yes': 'green','No':'red','''Don't Know''':'grey','Maybe':'dark grey','''Didn't Answer''':'grey'},
                title='| Upcoming election reflection')
    g1.update_traces(textposition='inside',
                     textinfo='percent+label',
                     showlegend=False)
    st.plotly_chart(g1,use_container_width=True)
#If YCP loses the election. Will decrease the taxes 

with col3:
    ind3 = pd.DataFrame(df.groupby('If_YCP_loses_the_upcoming_Municipality_Nagar_Panchayat_elections_will_the_government_decrease_taxes').If_YCP_loses_the_upcoming_Municipality_Nagar_Panchayat_elections_will_the_government_decrease_taxes.count()).rename(columns={'If_YCP_loses_the_upcoming_Municipality_Nagar_Panchayat_elections_will_the_government_decrease_taxes':'count'}).reset_index()
    g1 = px.pie(ind3,
                values='count',
                names='If_YCP_loses_the_upcoming_Municipality_Nagar_Panchayat_elections_will_the_government_decrease_taxes',
                color='If_YCP_loses_the_upcoming_Municipality_Nagar_Panchayat_elections_will_the_government_decrease_taxes',
                color_discrete_map={'Yes': 'green','No': 'red','''Don't Know''':'grey','Maybe':'dark grey'},
                title='| Taxes will decrease')
    g1.update_traces(textposition='inside',
                     textinfo='percent+label',
                     showlegend=False)
    st.plotly_chart(g1,use_container_width=True)
 
    
 
ind3 = pd.DataFrame(df.groupby('Common_issues').Common_issues.count()).rename(columns={'Common_issues':'count'}).reset_index()
g3 = px.bar(ind3,
x='Common_issues',
y='count',
title='| COMMON ISSUES')
st.plotly_chart(g3, use_container_width=True)
    


