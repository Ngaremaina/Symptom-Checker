import streamlit as st
import csv
from sklearn.tree import _tree
from train import x, cols
from model import le, clf

precautionDictionary=dict()

symptoms_dict = {}

for index, symptom in enumerate(x):
       symptoms_dict[symptom] = index

def getprecautionDict():
    global precautionDictionary
    with open('data/Precautions.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            _prec={row[0]:[row[1],row[2],row[3],row[4]]}
            precautionDictionary.update(_prec)

def print_disease(node): 
    node = node[0]
    val  = node.nonzero() 
    disease = le.inverse_transform(val[0])
    return disease


def tree_to_code(tree, feature_names):
    tree_ = tree.tree_
    
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]

    symptoms_present = []
    def recurse(node, depth):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            try:
                ans = 'yes'
                
                if ans == yes:
                    val = 1
                else:
                    val = 0
                
                if  val <= threshold:
                    recurse(tree_.children_left[node], depth + 1)
                else:
                    symptoms_present.append(name)
                    recurse(tree_.children_right[node], depth + 1)
            except:
                st.write("No illness")
        else:
            present_disease = print_disease(tree_.value[node])
            st.write("You may have " , present_disease[0])

            precution_list=precautionDictionary[present_disease[0]]
            st.write("Take following measures : ")
            for  i,j in enumerate(precution_list):
                st.write(i+1,j)

    recurse(0, 1)
getprecautionDict()

st.header('Virtual Health Assistant')
st.write("Please reply Yes or No for the following symptoms")

with st.container():
    col1, col2=st.columns(2)
    with col1: 
        st.write("")
        st.write("")
        st.write('Are you experiencing a headache?')
  
    with col2:        
        headache = st.radio("",('Yes', 'No'),horizontal=True, key="1")

        if headache == 'Yes':
            yes=headache
        else:
            no=headache

with st.container():
    col1, col2=st.columns(2)
    with col1: 
        st.write("")
        st.write("")
        st.write('Are you experiencing a cough?')
  
    with col2:
        cough= st.radio("",('Yes', 'No'),horizontal=True, key="2")

        if cough == 'Yes':
            yes=cough
        else:
            no=cough
with st.container():
    col1, col2=st.columns(2)
    with col1: 
        st.write("")
        st.write("")
        st.write('Are you experiencing high fever?')
  
    with col2:
        fever= st.radio("",('Yes', 'No'),horizontal=True, key="3")

        if fever == 'Yes':
            yes=fever
        else:
            no=fever
with st.container():
    col1, col2=st.columns(2)
    with col1: 
        st.write("")
        st.write("")
        st.write('Are you experiencing vomiting?')
  
    with col2:
        vomiting= st.radio("",('Yes', 'No'),horizontal=True, key="4")

        if vomiting == 'Yes':
            yes=vomiting
        else:
            no=vomiting

with st.container():
    col1, col2=st.columns(2)
    with col1: 
        st.write("")
        st.write("")
        st.write('Are you experiencing appetite loss?')
  
    with col2:
        appetite= st.radio("",('Yes', 'No'),horizontal=True, key="5")

        if appetite == 'Yes':
            yes=appetite
        else:
            no=appetite

with st.container():
    col1, col2=st.columns(2)
    with col1: 
        st.write("")
        st.write("")
        st.write('Are you experiencing sweating?')
  
    with col2:
        sweating= st.radio("",('Yes', 'No'),horizontal=True, key="6")

        if sweating == 'Yes':
            yes=sweating
        else:
            no=sweating

with st.container():
    col1, col2=st.columns(2)
    with col1: 
        st.write("")
        st.write("")
        st.write('Are you experiencing chest pains?')
  
    with col2:
        chest= st.radio("",('Yes', 'No'),horizontal=True, key="7")

        if chest == 'Yes':
            yes=chest
        else:
            no=chest

with st.container():
    col1, col2=st.columns(2)
    with col1: 
        st.write("")
        st.write("")
        st.write('Are you experiencing fatigue?')
  
    with col2:
        fatigue= st.radio("",('Yes', 'No'),horizontal=True, key ="8")

        if fatigue == 'Yes':
            yes=fatigue
        else:
            no=fatigue

submitresponse=st.button("Validate")

if submitresponse:
    tree_to_code(clf,cols)