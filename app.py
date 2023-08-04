import random
import streamlit as st
import pandas as pd
def get_percentage(length:int,range_start:int,range_end:int):
    success = False
    percentage = []
    while success is False:
        left = 100
        percentage = []
        for _ in range(length-1):
            rand_sd = random.randint(range_start,range_end)
            percentage.append(rand_sd)
            left -= rand_sd
        percentage.append(left)
        if percentage[-1] > 0:
            success = True
    print(percentage)
    return percentage


def random_number(total:float,size:int,range_start:int,range_end:int):
    success = False
    numbers=[]
    while success is False:
        percentage=get_percentage(size,range_start,range_end)
        numbers=[]
        for i in range(size):
            num = round(total * (percentage[i]/100),2)
            numbers.append(num)
        final_number = sum(numbers)
        if str(total) == str(final_number):
            success = True
        print(f"sum:{final_number},success:{success}")
    print(numbers)
    return numbers


# numbers = random_number(897.54,7)
# sum(numbers)
st.title("随机数生成器")
col1,col2,col3=st.columns(3)
number_list=[]
with st.form("calc"):
    with col1:
        random_value = st.number_input("输入需要随机分配的数值",value=879.54)
        select_range = st.slider("每份随机的百分比",1,30,(5,20))
    with col2:
        size = st.number_input("输入需要分配的数量",value=7)
    with col3:
        batch = st.number_input("输入生成的组数",value=10)
    if st.form_submit_button("生成"):
        for i in range(batch):
            numbers = random_number(random_value,int(size),range_start=int(select_range[0]),range_end=int(select_range[1]))
            number_list.append(numbers)
df = pd.DataFrame(number_list)
df = df.round(2)
st.table(df)


