#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    date = df["Päivämäärä"].str.split(expand=True)
    date[[4,5]] = date[4].str.split(":",expand=True)
    date = date.drop(5,axis=1)
    date = date.dropna()
    date = date.rename(columns={0:"Weekday",1:"Day",2:"Month",3:"Year",4:"Hour"})
    weekdayDic = {"ma":1,"ti":2,"ke":3,"to":4,"pe":5,"la":6,"su":7}
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
    print(result)
    return result

def bicycle_timeseries():
    df = split_date_continues()
    df['Date'] = pd.to_datetime(df[["Year","Month","Day","Hour"]])
    df.drop(["Year","Month","Day","Hour"],axis=1,inplace=True)
    df.set_index("Date",inplace=True)
    return df

def commute():
    df = bicycle_timeseries()
    result = df["2017-08-01":"2017-08-31"].groupby("Weekday").sum()
    return result
    
def main():
    result = commute()
    print(result)
    result.plot()
    # stick mon tue wed on x ticklabels
    # x took the zero point so it will not shown up, only for the place holder
    weekdays = "x mon tue wed thu fri sat sun".title().split()
    plt.gca().set_xticklabels(weekdays)
    plt.show()
    return


if __name__ == "__main__":
    main()
