#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv")
    df.drop(['year','sex','age'],axis = 1,inplace=True)
    df['rate'] = df['suicides_no'] / df['population']
    group = df.groupby('country')
    # print(list(group)[0]) //if needs to access group by index
    result = group['rate'].mean()
    return result
    
def suicide_weather():
    df_weather = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html",index_col=0)[0]
    # convert negative sign in string to float
    df_weather.iloc[:,0] = df_weather.iloc[:,0].str.replace("\u2212", "-").astype(float)
    df_suicide = suicide_fractions()
    # print(df_suicide)
    # print(df_weather)
    
    df_sw = pd.merge(df_weather,df_suicide,how="inner",right_index=True,left_index=True)
    # print(df_sw)
    
    correlation = df_sw.corr(method="spearman")
    # print(correlation)
    anwser = [df.shape[0] for df in [df_suicide,df_weather,df_sw]]
    anwser.append(correlation.iloc[0,1])
    # print(anwser)
    return tuple(anwser)

def main():
    suicide_rows, temperature_rows, common_rows, correlation = suicide_weather()
    print(f"Suicide DataFrame has {suicide_rows} rows")
    print(f"Temperature DataFrame has {temperature_rows} rows")
    print(f"Common DataFrame has {common_rows} rows")
    print(f"Spearman correlation: {correlation}")
    return

if __name__ == "__main__":
    main()
