import pandas as pd
import matplotlib.pyplot as plt


def avg_data_2015():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/data_2015.csv',chunksize=30):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='' and i!=' ':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/30
        temp_i=temp_i+1
        
        average.append(avg)
    return average
    
def avg_data_2016():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/data_2016.csv',chunksize=30):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='' and i!=' ':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/30
        temp_i=temp_i+1
        
        average.append(avg)
    return average
    
def avg_data_2017():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/data_2017.csv',chunksize=30):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='' and i!=' ':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/30
        temp_i=temp_i+1
        
        average.append(avg)
    return average
   
def avg_data_2018():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/data_2018.csv',chunksize=30):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='' and i!=' ':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/30
        temp_i=temp_i+1
        
        average.append(avg)
    return average
   
def avg_data_2019():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/data_2019.csv',chunksize=30):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='' and i!=' ':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/30
        temp_i=temp_i+1
        
        average.append(avg)
    return average
   
def avg_data_2020():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/data_2020.csv',chunksize=30):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='' and i!=' ':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/30
        temp_i=temp_i+1
        
        average.append(avg)
    return average

def avg_data_2021():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/data_2021.csv',chunksize=30):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='' and i!=' ':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/30
        temp_i=temp_i+1
        
        average.append(avg)
    return average
      
def avg_data_2022():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/data_2022.csv',chunksize=30):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='' and i!=' ':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/30
        temp_i=temp_i+1
        
        average.append(avg)
    return average
   
def avg_data_2023():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/data_2023.csv',chunksize=30):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='' and i!=' ':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/30
        temp_i=temp_i+1
        
        average.append(avg)
    return average
   

if __name__ == "__main__":
    lst2015 = avg_data_2015()
    lst2016 = avg_data_2016()
    lst2017 = avg_data_2017()
    lst2018 = avg_data_2018()
    lst2019 = avg_data_2019()
    lst2020 = avg_data_2020()
    lst2021 = avg_data_2021()
    lst2022 = avg_data_2022()
    lst2023 = avg_data_2023()

    plt.plot(range(len(lst2015)), lst2015, label="2015")
    plt.plot(range(len(lst2016)), lst2016, label="2016")
    plt.plot(range(len(lst2017)), lst2017, label="2017")
    plt.plot(range(len(lst2018)), lst2018, label="2018")
    plt.plot(range(len(lst2019)), lst2019, label="2019")
    plt.plot(range(len(lst2020)), lst2020, label="2020")
    plt.plot(range(len(lst2021)), lst2021, label="2021")
    plt.plot(range(len(lst2022)), lst2022, label="2022")
    plt.plot(range(len(lst2023)), lst2023, label="2023")

    plt.xlabel('Ay')
    plt.ylabel('PM 2.5 Ortalaması')
    plt.legend(loc='upper right')
    plt.show()



