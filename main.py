import streamlit as st
import csv, pathlib
from pathlib import Path

#----------- read data ------------#
fp = Path.cwd()/"boston_data.csv"

# read csv 
with fp.open("r", newline="") as file:
    data = csv.reader(file)
    next(data) # skip header
    details = [] # to store details of each runner
    all_name = [] # to store just the name of runners 
    all_time = [] # to store just the time of runners

    for line in data:
        details.append(line)
        all_name.append(line[1])
        all_time.append(int(line[5]))

#----------- create title and header for dashboard ------------#

st.title("Boston Marathon Data 2018") # create a title for the dashboard
st.header("Runner's Finishing Time") # create a header 

#----------- display runner's finishing time based on selection widget ------------#
# allow user to select names to display finishing time
selection = st.multiselect(label="You may select more than one runner : ", options=all_name)

# iterate based on the length of details 
for index in range(len(details)):
    # if runners name is found in selection
    if details[index][1] in selection:

        time = round(int(details[index][5])/60, 2) # store time and divide by 60 
        name = details[index][1] # store the name
        country = details[index][3] # store the country
        age = details[index][2] # store the age
       
        #create 3 column in the dashboard
        col1, col2, col3 = st.columns(3)
        # use metric function to display each runner's detail from the variables.
        col1.metric(label="Participant", value=name)
        col2.metric(label="Age", value=age)
        col3.metric(label="Finishing Time (Hours)", value=time)

#----------- display runner's finishing time based on slider widget  ------------#

# use select_slider function to allow user to select runners by finishing time
time_selection = st.select_slider("Select a range of finishing time", options=all_time, value=(min(all_time), max(all_time)))

# select_slider return a tuple of min and max values 
time1 = time_selection[0] # store min value 
time2= time_selection[1] # store max value

# create 4 columns to display runner's details based min and max values
col5, col6, col7, col8 = st.columns(4)
# iterate over details 
for line in details:
    # if finishing time is >= to min time and <= max time
    if int(line[5]) >= time1 and int(line[5]) <= time2:
        name = line[1] # store runner's name
        country = line[3] # store runner's country
        gender = line[4] # store runner's gender
        time = line[5] # store runner's completion time

        # write the data to each columns
        col5.write(name)
        col6.write(country)
        col7.write(gender)
        col8.write(time)


#"""
#Create Streamlit App in 2 steps
#STEP 1 
#- Write the code and test out on local host.
#- To run streamlit in terminal: streamlit run filename.py
#
#STEP 2
#- Create a new repo in GitHub to hose the app.
#- Create a new streamlit app in streamlit cloud.
#(For first time user in GitHub and Streamlit, 
#signup GitHub account then sign up Streamlit with GitHub)
#
#GITHUB
#- To work seamlessly between VS code and GitHub, make sure you link up
#GitHub in VS Code, authorisation is required.
#
#- Install GitHub Pull Requests Extensions in VS Code.
#- Use Command Palette (CTRL + SHIFT + P) to "initialize" and "add remote" to GitHub.
#- Finally stage, commmit and push to the repo.
#
#"""





