#!/usr/bin/env python3

import pandas as pd

def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    date = df["Päivämäärä"].str.split(expand=True)
    date[[4,5]] = date[4].str.split(":",expand=True)
    date = date.drop(5,axis=1)
    date = date.dropna()
    date = date.rename(columns={0:"Weekday",1:"Day",2:"Month",3:"Year",4:"Hour"})
    weekdayDic = {"ma":"Mon","ti":"Tue","ke":"Wed","to":"Thu","pe":"Fri","la":"Sat","su":"Sun"}
    monthDic = {"tammi":1,"helmi":2,"maalis":3,"huhti":4,"touko":5,"kesä":6,"heinä":7,"elo":8,
                "syys":9,"loka":10,"marras":11,"joulu":12}
    date['Weekday'] = date["Weekday"].map(weekdayDic)
    date['Month'] = date["Month"].map(monthDic).astype(int)
    date[['Day','Year','Hour']] = date[['Day','Year','Hour']].astype(int)
    # print(date)
    # print(date.dtypes)
    return date,df

def split_date_continues():
    date,df = split_date()
    df.dropna(axis=0,how="all",inplace=True)
    df.dropna(axis=1,how="all",inplace=True)
    df.drop(["Päivämäärä"],axis=1,inplace=True)
    # print(df)
    result = pd.concat([date,df],axis=1)
    # result["Weekday"] = result["Weekday"].astype(object)
    #print(result)
    return result

def cycling_weather():
    df_cyc = split_date_continues()
    df_weather = pd.read_csv("src/kumpula-weather-2017.csv")
    #print(df_weather)
    result = pd.merge(df_cyc,df_weather,left_on=['Day','Month','Year'],right_on=['d','m','Year'])
    result.drop(['m','d','Time','Time zone'],axis=1,inplace=True)
    print(result.dtypes)
    return result

def main():
    print(cycling_weather())
    return

if __name__ == "__main__":
    main()
