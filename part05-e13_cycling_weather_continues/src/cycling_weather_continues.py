#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model
import numpy as np

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
    # print(result)
    return result

def cycling_weather_continues(station):
    df_weather = pd.read_csv('src/kumpula-weather-2017.csv')
    df = split_date_continues()

    new_df = pd.merge(df.loc[:, 'Weekday':'Hour'], df.loc[:, station], left_index=True, right_index=True)
    new_df = new_df[new_df.Year == 2017]
    a = new_df.groupby(['Month', 'Day'])[station].sum()
    print(a)
    merged_df = pd.merge(df_weather, a, right_on=['Day', 'Month'], left_on=['d', 'm'])
    merged_df.fillna(method='ffill', inplace=True)
    print(merged_df)
    model = linear_model.LinearRegression(fit_intercept=True)
    x = merged_df.loc[:, ['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
    y = merged_df.loc[:, station]
    model.fit(x, y)
    score = model.score(x, y)
    return model.coef_, score
    
def main():
    coef, score = cycling_weather_continues("Baana")
    print(f"Measuring station: Baana")
    print(f"Regression coefficient for variable 'precipitation': {coef[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]:.1f}")
    print(f"Score: {score:.2f}")

if __name__ == "__main__":
    main()
