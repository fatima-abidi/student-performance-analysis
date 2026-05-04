import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#-------------------
#Load Dataset
#-------------------
df=pd.read_csv("student-por.csv")

#-------------------
#App Title
#-------------------
st.title("Student Performance Analysis")

#-------------------
#User Inputs
#-------------------
gender = st.selectbox("Select Gender", df["sex"].unique())
study_hours = st.selectbox("How many hours do you study?", df["studytime"].unique())
internet = st.selectbox("Do you have Internet access?", df["internet"].unique())

#-------------------
#Data Filtering
#-------------------
filter_data = df[(df["sex"]==gender) & 
                 (df["studytime"]==study_hours) & 
                 (df["internet"]==internet)]

if filter_data.empty:
    st.write("No data")
else:
    st.write(filter_data)

#---------------------------
#Visualization 1: Histogram
#---------------------------
st.subheader("Filtered Students Distribution")
fig, ax = plt.subplots()
ax.hist(filter_data["G3"])
ax.set_title("Score Distribution")
ax.set_xlabel("Final Grade")
ax.set_ylabel("Number of Students")
st.pyplot(fig)

#------------------------------------------
#Visualization 2: Study Time VS Performance
#------------------------------------------
st.subheader("Overall Trends")
study_avg = df.groupby("studytime")["G3"].mean()

fig, ax = plt.subplots()
study_avg.plot(kind="bar", ax=ax)
ax.set_title("Study Time vs Average Final Grade")
ax.set_xlabel("Study Time")
ax.set_ylabel("Final Grade")
st.pyplot(fig)

#------------------------------------------
#Visualization 2: Internet VS Performance
#------------------------------------------
internet_avg = df.groupby("internet")["G3"].mean()

fig, ax = plt.subplots()

internet_avg.plot(kind="bar", ax=ax)

ax.set_title("Internet Access vs Performance")
ax.set_xlabel("Internet Access")
ax.set_ylabel("Final Grade")
st.pyplot(fig)
