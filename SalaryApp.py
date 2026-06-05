import streamlit as st
import numpy as np 
import pandas as pd
import joblib
model = joblib.load('Lpipe.joblib')
st.title('Salary Pridection Using 2022 Dataset From Stackoverflow ')
st.write("""We need some information""")
countries=(
"India",                                                   
"Brazil",                                                  
"Italy",                                              
"Turkey",                                                  
"Poland",                                                  
"Spain",                                                   
"Russian Federation",
"France",                                                  
"Mexico",                                                  
"Greece",                                                  
"Portugal",                                                
"Argentina" ,                                              
"Hungary" ,                                                 
"Germany",                                                
"Pakistan",                                               
"Colombia",                                                 
"Bangladesh"                                               
"Czech Republic",                                        
"Romania",                                                  
"United Kingdom of Great Britain and Northern Ireland" ,    
"United States of America" ,                                
"Iran, Islamic Republic of..." ,                            
"South Africa",                                             
"Ukraine",                                                  
"Belgium",                                                  
"Netherlands",                                              
"Austria" ,                                                
"Canada",                                                   
"Japan",                                                    
"Switzerland" ,                                             
"Australia",                                               
"Israel"   ,                                                 
"Sweden"   ,                                                 
"Finland"  ,                                                 
"Ireland"  ,                                                 
"Denmark" ,                                                  
"New Zealand" ,                                             
"Norway"                                                   
)

education=(
    "Less than a Bachelors",
    "Bachelor’s degree",
    "Master’s degree",
    "Post grad",
)

employment=(
    "Full-Time",
    "Part-time",
    "Freelance/Contract",
    "Retired"
)

country = st.selectbox("Country", countries)
employment = st.selectbox("Employment", employment)
education = st.selectbox("Education", education)
experience = st.slider("Years Of Experience",0,50,3)

columns = ['Country', 'EdLevel', 'YearsCodePro', 'Employment']

ok = st.button("Calculate Salary")

if ok:
    X_new = np.array([country, education, experience, employment])
    X_new_df= pd.DataFrame([X_new], columns=columns)
    Salary = model.predict(X_new_df)
    st.subheader(f"The estimated salary is ${Salary[0]:0.2f}")