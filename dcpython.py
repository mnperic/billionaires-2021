import pandas as pd
import plotly.express as px
import numpy as np
import geopandas as gpd
from bs4 import BeautifulSoup
import requests
import pymongo
from pymongo import MongoClient
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import psycopg2

import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Float

    # %load_ext sql
    # %sql sqlite://

# new_func()
from config import user, password
user = user
password = password
import json
import config
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# data file path
billionaires2_path = "./data/billionaires2.csv"
# read the billionaires csv file
billionaires2_df = pd.read_csv(billionaires2_path)
# display the data
# billionaires2_df
# Name	NetWorth	Country	Source	Rank	Age	Residence	Citizenship	Status	Children	Education	Self_made	geometry
# 0	Jeff Bezos	177.0	United States	Amazon	1	57.0	Seattle, Washington	United States	In Relationship	4.0	Bachelor of Arts/Science, Princeton University	True	POINT (-122.3300624 47.6038321)
# 1	Elon Musk	151.0	United States	Tesla, SpaceX	2	49.0	Austin, Texas	United States	In Relationship	7.0	Bachelor of Arts/Science, University of Pennsy...	True	POINT (-97.74369950000001 30.2711286)
# 2	Bernard Arnault & family	150.0	France	LVMH	3	72.0	Paris, France	France	Married	5.0	Bachelor of Arts/Science, Ecole Polytechnique ...	False	POINT (2.3514616 48.8566969)
# 3	Bill Gates	124.0	United States	Microsoft	4	65.0	Medina, Washington	United States	Divorced	3.0	Drop Out, Harvard University	True	POINT (-122.2264453 47.620548)
# 4	Mark Zuckerberg	97.0	United States	Facebook	5	36.0	Palo Alto, California	United States	Married	2.0	Drop Out, Harvard University	True	POINT (-122.1598465 37.4443293)
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 2750	Daniel Yong Zhang	1.0	China	e-commerce	2674	49.0	Hangzhou, China	China	NaN	NaN	NaN	True	POINT (120.2052342 30.2489634)
# 2751	Zhang Yuqiang	1.0	China	Fiberglass	2674	65.0	Tongxiang, China	China	NaN	NaN	NaN	True	POINT (120.5610365 30.6316971)
# 2752	Zhao Meiguang	1.0	China	gold mining	2674	58.0	Jilin, China	China	NaN	NaN	NaN	True	POINT (125.9816054 42.9995032)
# 2753	Zhong Naixiong	1.0	China	conglomerate	2674	58.0	Foshan, China	China	NaN	NaN	NaN	True	POINT (113.1146335 23.0247687)
# 2754	Zhou Wei family	1.0	China	Software	2674	54.0	Shanghai, China	China	Married	NaN	NaN	True	POINT (121.4692071 31.2322758)
# 2755 rows × 13 columns

# billionaires2_df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 2755 entries, 0 to 2754
# Data columns (total 13 columns):
#  #   Column       Non-Null Count  Dtype  
# ---  ------       --------------  -----  
#  0   Name         2755 non-null   object 
#  1   NetWorth     2755 non-null   float64
#  2   Country      2755 non-null   object 
#  3   Source       2755 non-null   object 
#  4   Rank         2755 non-null   int64  
#  5   Age          2630 non-null   float64
#  6   Residence    2715 non-null   object 
#  7   Citizenship  2739 non-null   object 
#  8   Status       2090 non-null   object 
#  9   Children     1552 non-null   float64
#  10  Education    1409 non-null   object 
#  11  Self_made    2737 non-null   object 
#  12  geometry     2755 non-null   object 
# dtypes: float64(3), int64(1), object(9)
# memory usage: 279.9+ KB
billionaires2_df_dc = billionaires2_df.dropna(how='any',axis=0)
billionaires2_df_dc.isnull().sum()
# Name           0
# NetWorth       0
# Country        0
# Source         0
# Rank           0
# Age            0
# Residence      0
# Citizenship    0
# Status         0
# Children       0
# Education      0
# Self_made      0
# geometry       0
# dtype: int64
# billionaires2_df_dc
# Name	NetWorth	Country	Source	Rank	Age	Residence	Citizenship	Status	Children	Education	Self_made	geometry
# 0	Jeff Bezos	177.0	United States	Amazon	1	57.0	Seattle, Washington	United States	In Relationship	4.0	Bachelor of Arts/Science, Princeton University	True	POINT (-122.3300624 47.6038321)
# 1	Elon Musk	151.0	United States	Tesla, SpaceX	2	49.0	Austin, Texas	United States	In Relationship	7.0	Bachelor of Arts/Science, University of Pennsy...	True	POINT (-97.74369950000001 30.2711286)
# 2	Bernard Arnault & family	150.0	France	LVMH	3	72.0	Paris, France	France	Married	5.0	Bachelor of Arts/Science, Ecole Polytechnique ...	False	POINT (2.3514616 48.8566969)
# 3	Bill Gates	124.0	United States	Microsoft	4	65.0	Medina, Washington	United States	Divorced	3.0	Drop Out, Harvard University	True	POINT (-122.2264453 47.620548)
# 4	Mark Zuckerberg	97.0	United States	Facebook	5	36.0	Palo Alto, California	United States	Married	2.0	Drop Out, Harvard University	True	POINT (-122.1598465 37.4443293)
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 2736	Surin Upatkoon	1.0	Thailand	telecom, lotteries, insurance	2674	72.0	Kuala Lumpur, Malaysia	Thailand	Married	3.0	High School	True	POINT (101.6942371 3.1516964)
# 2737	Ruben Vardanyan	1.0	Russia	investment banking	2674	52.0	Moscow, Russia	Russia	Married	4.0	Master of Science, Moscow State University	True	POINT (37.6174943 55.7504461)
# 2742	J. Wayne Weaver	1.0	United States	Shoes	2674	85.0	Jacksonville, Florida	United States	Married	2.0	Bachelor of Science, University of Florida	True	POINT (-81.65565100000001 30.3321838)
# 2743	Sandy Weill	1.0	United States	Citigroup	2674	88.0	Sonoma, California	United States	Married	2.0	Bachelor of Arts/Science, Cornell University	True	POINT (-122.8473388 38.5110803)
# 2746	Vadim Yakunin	1.0	Russia	pharmacy	2674	58.0	Moscow, Russia	Russia	Married	3.0	Bachelor of Arts/Science, Moscow Institute of ...	True	POINT (37.6174943 55.7504461)
# 995 rows × 13 columns

# generate HTML table from billionaires dataframe

# billionaires2_table=(billionaires2_df_dc.to_html())
# generate the data HTML file for the billionaires dataframe

# billionaires2_df_dc.to_html('output/billionaires2_table_dc.html') renamed billionaires_profile_2021 when copied under templates
billionaires2_geo_dc = billionaires2_df_dc[["Name", "Country", "geometry", "NetWorth", "Age", "Source", "Rank"]]
# billionaires2_df_dc.to_json(r'output/billionaires2_geo_dc.json')
b_df = billionaires2_df_dc.sort_values(by = ['NetWorth'],ascending = False).reset_index().head(10)

fig = px.bar(b_df, x= 'Name', y ='NetWorth', color = 'NetWorth',
             color_continuous_scale = 'magma',
             hover_data = ['Source','Age'],
             labels= {"NetWorth":"Networth(Billions)"})

fig.update_xaxes(tickangle=45, tickfont=dict(color='darkBlue'))

fig.update_layout(title = 'Top 10 Billionaires in the world',
                  title_font = dict(size = 20, family = 'Arial', color = 'darkBlue'),
                  title_x = 0.4)
# savefig('Images/Top10_DC_Fig1.png')
fig.show()
b_country_df = billionaires2_df_dc['Country'].value_counts().reset_index()
b_country_df = b_country_df.rename(columns = {"index":"country"}) 
b_country_df = b_country_df.rename(columns = {"Country":"Billionaires"}) 

fig = px.choropleth(b_country_df, 
                    locations = 'country',
                    locationmode = 'country names',
                    color = 'Billionaires',
                    color_continuous_scale = 'picnic')

fig.update_layout(title = 'World - Billionaires',
                  title_x = 0.5,
                  title_font = dict(size = 22, family = 'Arial', color = 'darkBlue'),
                  geo = dict(showframe = False,
                             showcoastlines = True,
                             projection_type = 'natural earth'))
# savefig('Images/World_Billionaires_DC_Fig2.png')
fig.show()
b_networth_df = billionaires2_df_dc.groupby("Country")['NetWorth'].sum().sort_values(ascending = False).reset_index().head(20)


fig = px.choropleth(b_networth_df, 
                    locations = 'Country',
                    locationmode = 'country names',
                    color = 'NetWorth',
                    color_continuous_scale = 'viridis')

fig.update_layout(title = 'Billionaires NetWorth',
                  title_x = 0.5,
                  title_font = dict(size = 22, family = 'Arial', color = 'darkBlue'),
                  geo = dict(showframe = False,
                             showcoastlines = True,
                             projection_type = 'natural earth'))
# savefig('Images/Billionaires_NetWorth_DC_Fig3.png')
# fig.write_html("output/Billionaires_NetWorth_DC.html")
fig.show()
b_by_country = billionaires2_df_dc['Country'].value_counts().reset_index().head(10)
fig = px.pie(b_by_country,
             values = 'Country', 
             names = 'index', 
             labels = {"index":"Country","Country":"Count"}
            )

fig.update_traces(textposition = 'inside', textinfo = 'label+percent')

fig.update_layout(title = 'Top 10 Countries',
                  title_x = 0.5,

                  font = dict(size = 16, color = '#4c8486'))
# savefig('Images/Top_10_countrues_DC_Fig4.png')
fig.show()
billionaires2_geo_dc1 = billionaires2_df_dc[["Name", "Country", "geometry", "NetWorth", "Age", "Source", "Rank"]]
 
billionaires2_geo_dc1[['point', 'latlng']] = billionaires2_geo_dc1['geometry'].str.split('(', expand=True)
billionaires2_geo_dc1





# Name	Country	geometry	NetWorth	Age	Source	Rank	point	latlng
# 0	Jeff Bezos	United States	POINT (-122.3300624 47.6038321)	177.0	57.0	Amazon	1	POINT	-122.3300624 47.6038321)
# 1	Elon Musk	United States	POINT (-97.74369950000001 30.2711286)	151.0	49.0	Tesla, SpaceX	2	POINT	-97.74369950000001 30.2711286)
# 2	Bernard Arnault & family	France	POINT (2.3514616 48.8566969)	150.0	72.0	LVMH	3	POINT	2.3514616 48.8566969)
# 3	Bill Gates	United States	POINT (-122.2264453 47.620548)	124.0	65.0	Microsoft	4	POINT	-122.2264453 47.620548)
# 4	Mark Zuckerberg	United States	POINT (-122.1598465 37.4443293)	97.0	36.0	Facebook	5	POINT	-122.1598465 37.4443293)
# ...	...	...	...	...	...	...	...	...	...
# 2736	Surin Upatkoon	Thailand	POINT (101.6942371 3.1516964)	1.0	72.0	telecom, lotteries, insurance	2674	POINT	101.6942371 3.1516964)
# 2737	Ruben Vardanyan	Russia	POINT (37.6174943 55.7504461)	1.0	52.0	investment banking	2674	POINT	37.6174943 55.7504461)
# 2742	J. Wayne Weaver	United States	POINT (-81.65565100000001 30.3321838)	1.0	85.0	Shoes	2674	POINT	-81.65565100000001 30.3321838)
# 2743	Sandy Weill	United States	POINT (-122.8473388 38.5110803)	1.0	88.0	Citigroup	2674	POINT	-122.8473388 38.5110803)
# 2746	Vadim Yakunin	Russia	POINT (37.6174943 55.7504461)	1.0	58.0	pharmacy	2674	POINT	37.6174943 55.7504461)
# 995 rows × 9 columns

billionaires2_geo_dc1[['longitude', 'latitude']] = billionaires2_geo_dc1['latlng'].str.split(' ', expand=True)
billionaires2_geo_dc1


# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead

# See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

# Name	Country	geometry	NetWorth	Age	Source	Rank	point	latlng	longitude	latitude
# 0	Jeff Bezos	United States	POINT (-122.3300624 47.6038321)	177.0	57.0	Amazon	1	POINT	-122.3300624 47.6038321)	-122.3300624	47.6038321)
# 1	Elon Musk	United States	POINT (-97.74369950000001 30.2711286)	151.0	49.0	Tesla, SpaceX	2	POINT	-97.74369950000001 30.2711286)	-97.74369950000001	30.2711286)
# 2	Bernard Arnault & family	France	POINT (2.3514616 48.8566969)	150.0	72.0	LVMH	3	POINT	2.3514616 48.8566969)	2.3514616	48.8566969)
# 3	Bill Gates	United States	POINT (-122.2264453 47.620548)	124.0	65.0	Microsoft	4	POINT	-122.2264453 47.620548)	-122.2264453	47.620548)
# 4	Mark Zuckerberg	United States	POINT (-122.1598465 37.4443293)	97.0	36.0	Facebook	5	POINT	-122.1598465 37.4443293)	-122.1598465	37.4443293)
# ...	...	...	...	...	...	...	...	...	...	...	...
# 2736	Surin Upatkoon	Thailand	POINT (101.6942371 3.1516964)	1.0	72.0	telecom, lotteries, insurance	2674	POINT	101.6942371 3.1516964)	101.6942371	3.1516964)
# 2737	Ruben Vardanyan	Russia	POINT (37.6174943 55.7504461)	1.0	52.0	investment banking	2674	POINT	37.6174943 55.7504461)	37.6174943	55.7504461)
# 2742	J. Wayne Weaver	United States	POINT (-81.65565100000001 30.3321838)	1.0	85.0	Shoes	2674	POINT	-81.65565100000001 30.3321838)	-81.65565100000001	30.3321838)
# 2743	Sandy Weill	United States	POINT (-122.8473388 38.5110803)	1.0	88.0	Citigroup	2674	POINT	-122.8473388 38.5110803)	-122.8473388	38.5110803)
# 2746	Vadim Yakunin	Russia	POINT (37.6174943 55.7504461)	1.0	58.0	pharmacy	2674	POINT	37.6174943 55.7504461)	37.6174943	55.7504461)
# 995 rows × 11 columns

billionaires2_geo_dc1[['latitude', 'x']] = billionaires2_geo_dc1['latitude'].str.split(')', expand=True)
billionaires2_geo_dc1


# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead

# See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

# Name	Country	geometry	NetWorth	Age	Source	Rank	point	latlng	longitude	latitude	x
# 0	Jeff Bezos	United States	POINT (-122.3300624 47.6038321)	177.0	57.0	Amazon	1	POINT	-122.3300624 47.6038321)	-122.3300624	47.6038321	
# 1	Elon Musk	United States	POINT (-97.74369950000001 30.2711286)	151.0	49.0	Tesla, SpaceX	2	POINT	-97.74369950000001 30.2711286)	-97.74369950000001	30.2711286	
# 2	Bernard Arnault & family	France	POINT (2.3514616 48.8566969)	150.0	72.0	LVMH	3	POINT	2.3514616 48.8566969)	2.3514616	48.8566969	
# 3	Bill Gates	United States	POINT (-122.2264453 47.620548)	124.0	65.0	Microsoft	4	POINT	-122.2264453 47.620548)	-122.2264453	47.620548	
# 4	Mark Zuckerberg	United States	POINT (-122.1598465 37.4443293)	97.0	36.0	Facebook	5	POINT	-122.1598465 37.4443293)	-122.1598465	37.4443293	
# ...	...	...	...	...	...	...	...	...	...	...	...	...
# 2736	Surin Upatkoon	Thailand	POINT (101.6942371 3.1516964)	1.0	72.0	telecom, lotteries, insurance	2674	POINT	101.6942371 3.1516964)	101.6942371	3.1516964	
# 2737	Ruben Vardanyan	Russia	POINT (37.6174943 55.7504461)	1.0	52.0	investment banking	2674	POINT	37.6174943 55.7504461)	37.6174943	55.7504461	
# 2742	J. Wayne Weaver	United States	POINT (-81.65565100000001 30.3321838)	1.0	85.0	Shoes	2674	POINT	-81.65565100000001 30.3321838)	-81.65565100000001	30.3321838	
# 2743	Sandy Weill	United States	POINT (-122.8473388 38.5110803)	1.0	88.0	Citigroup	2674	POINT	-122.8473388 38.5110803)	-122.8473388	38.5110803	
# 2746	Vadim Yakunin	Russia	POINT (37.6174943 55.7504461)	1.0	58.0	pharmacy	2674	POINT	37.6174943 55.7504461)	37.6174943	55.7504461	
# 995 rows × 12 columns

billionaires2_geo_dc1['latitude'] = billionaires2_geo_dc1['latitude'].astype(float)
billionaires2_geo_dc1['longitude'] = billionaires2_geo_dc1['longitude'].astype(float)


billionaires2_geo_dc1 = billionaires2_geo_dc1.drop('point', 1)
billionaires2_geo_dc1 = billionaires2_geo_dc1.drop('latlng', 1)
billionaires2_geo_dc1 = billionaires2_geo_dc1.drop('x', 1)
billionaires2_geo_dc1
# Name	Country	geometry	NetWorth	Age	Source	Rank	longitude	latitude
# 0	Jeff Bezos	United States	POINT (-122.3300624 47.6038321)	177.0	57.0	Amazon	1	-122.330062	47.603832
# 1	Elon Musk	United States	POINT (-97.74369950000001 30.2711286)	151.0	49.0	Tesla, SpaceX	2	-97.743700	30.271129
# 2	Bernard Arnault & family	France	POINT (2.3514616 48.8566969)	150.0	72.0	LVMH	3	2.351462	48.856697
# 3	Bill Gates	United States	POINT (-122.2264453 47.620548)	124.0	65.0	Microsoft	4	-122.226445	47.620548
# 4	Mark Zuckerberg	United States	POINT (-122.1598465 37.4443293)	97.0	36.0	Facebook	5	-122.159847	37.444329
# ...	...	...	...	...	...	...	...	...	...
# 2736	Surin Upatkoon	Thailand	POINT (101.6942371 3.1516964)	1.0	72.0	telecom, lotteries, insurance	2674	101.694237	3.151696
# 2737	Ruben Vardanyan	Russia	POINT (37.6174943 55.7504461)	1.0	52.0	investment banking	2674	37.617494	55.750446
# 2742	J. Wayne Weaver	United States	POINT (-81.65565100000001 30.3321838)	1.0	85.0	Shoes	2674	-81.655651	30.332184
# 2743	Sandy Weill	United States	POINT (-122.8473388 38.5110803)	1.0	88.0	Citigroup	2674	-122.847339	38.511080
# 2746	Vadim Yakunin	Russia	POINT (37.6174943 55.7504461)	1.0	58.0	pharmacy	2674	37.617494	55.750446
# 995 rows × 9 columns

def df_to_geojson(df, properties, lat='latitude', lon='longitude'):
    # create a new python dict to contain our geojson data, using geojson format
    geojson = {'type':'FeatureCollection', 'features':[]}

    # loop through each row in the dataframe and convert each row to geojson format
    for _, row in df.iterrows():
        # create a feature template to fill in
        feature = {'type':'Feature',
                   'properties':{},
                   'geometry':{'type':'Point',
                               'coordinates':[]}}

        # fill in the coordinates
        feature['geometry']['coordinates'] = [row[lon],row[lat]]

        # for each column, get the value and add it as a new feature property
        for prop in properties:
            feature['properties'][prop] = row[prop]
        
        # add this feature (aka, converted dataframe row) to the list of features inside our dict
        geojson['features'].append(feature)
    
    return geojson
cols = ['Name', 'Country', 'NetWorth']
geojson = df_to_geojson(billionaires2_geo_dc1, cols)
output_filename = 'dataset.js'
with open("./output/bgeojsondc.js", 'w') as output_file:
    output_file.write('var dataset = ')
    json.dump(geojson, output_file, indent=2) 
output_filename = 'dataset.js'
with open("./output/bgeojsondc.geojson", 'w') as output_file:
    output_file.write('var dataset = ')
    json.dump(geojson, output_file, indent=2) 
API_KEY="API_KEY"
# density map by net worth
fig = px.density_mapbox(billionaires2_geo_dc1, lat='latitude', lon='longitude', z='NetWorth', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-terrain")
# savefig('Images/Density_Map_NetWorth_DC_Fig5.png')
fig.show()
# density map by age
fig = px.density_mapbox(billionaires2_geo_dc1, lat='latitude', lon='longitude', z='Age', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-toner")
# savefig('/Images/Density_Map_Age_DC_Fig6.png')
# fig.write_html("output/Density_Map_Age_DC.html")
fig.show()
billionaires2_geo_dc1
# Name	Country	geometry	NetWorth	Age	Source	Rank	longitude	latitude
# 0	Jeff Bezos	United States	POINT (-122.3300624 47.6038321)	177.0	57.0	Amazon	1	-122.330062	47.603832
# 1	Elon Musk	United States	POINT (-97.74369950000001 30.2711286)	151.0	49.0	Tesla, SpaceX	2	-97.743700	30.271129
# 2	Bernard Arnault & family	France	POINT (2.3514616 48.8566969)	150.0	72.0	LVMH	3	2.351462	48.856697
# 3	Bill Gates	United States	POINT (-122.2264453 47.620548)	124.0	65.0	Microsoft	4	-122.226445	47.620548
# 4	Mark Zuckerberg	United States	POINT (-122.1598465 37.4443293)	97.0	36.0	Facebook	5	-122.159847	37.444329
# ...	...	...	...	...	...	...	...	...	...
# 2736	Surin Upatkoon	Thailand	POINT (101.6942371 3.1516964)	1.0	72.0	telecom, lotteries, insurance	2674	101.694237	3.151696
# 2737	Ruben Vardanyan	Russia	POINT (37.6174943 55.7504461)	1.0	52.0	investment banking	2674	37.617494	55.750446
# 2742	J. Wayne Weaver	United States	POINT (-81.65565100000001 30.3321838)	1.0	85.0	Shoes	2674	-81.655651	30.332184
# 2743	Sandy Weill	United States	POINT (-122.8473388 38.5110803)	1.0	88.0	Citigroup	2674	-122.847339	38.511080
# 2746	Vadim Yakunin	Russia	POINT (37.6174943 55.7504461)	1.0	58.0	pharmacy	2674	37.617494	55.750446
# 995 rows × 9 columns

# create dataframes for updating tables in a database

billionaires2_geo_dc1.to_csv("output/billionaires2_geo_dc1.csv")
rank = billionaires2_geo_dc1[["Rank", "NetWorth"]]
rank = rank.rename({'Rank': 'rank', 'NetWorth': 'networth'}, axis=1) 
rank = rank.drop_duplicates(subset=["networth"], keep=False)
rank
# rank	networth
# 0	1	177.0
# 1	2	151.0
# 2	3	150.0
# 3	4	124.0
# 4	5	97.0
# ...	...	...
# 325	323	7.7
# 389	384	6.8
# 419	418	6.4
# 471	472	5.9
# 498	496	5.6
# 85 rows × 2 columns

rank.to_csv("output/rank.csv")
country = billionaires2_geo_dc1[["Country", "geometry" , "longitude","latitude"]]
country = country.rename({'Country': 'country','geometry': 'geometry', 'longitude': 'longitude', 'latitude': 'latitude'}, axis=1) 
country = country.drop_duplicates(subset=["country"], keep=False)
country.to_csv("output/country.csv")
details = billionaires2_geo_dc1[["Name", "Age" , "Source","Country"]]
details = details.rename({'Name': 'name','Age': 'age', 'Source': 'source', 'Country': 'country'}, axis=1) 
details.to_csv("output/details.csv")
annualdata = billionaires2_geo_dc1[["Name", "NetWorth" , "Rank"]]
annualdata['year'] = 2021



annualdata
# Name	NetWorth	Rank	year
# 0	Jeff Bezos	177.0	1	2021
# 1	Elon Musk	151.0	2	2021
# 2	Bernard Arnault & family	150.0	3	2021
# 3	Bill Gates	124.0	4	2021
# 4	Mark Zuckerberg	97.0	5	2021
# ...	...	...	...	...
# 2736	Surin Upatkoon	1.0	2674	2021
# 2737	Ruben Vardanyan	1.0	2674	2021
# 2742	J. Wayne Weaver	1.0	2674	2021
# 2743	Sandy Weill	1.0	2674	2021
# 2746	Vadim Yakunin	1.0	2674	2021
# 995 rows × 4 columns

annualdata = annualdata.rename({'Name': 'name','NetWorth': 'networth','Rank': 'rank', 'year': 'year', }, axis=1) 
annualdata.to_csv("output/annualdata.csv")
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
# billionaires2_geo_dc1.to_numpy()
latlngnetworth = billionaires2_geo_dc1[["latitude", "longitude", "NetWorth"]]
latlngnetworth.info()
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 995 entries, 0 to 2746
# Data columns (total 3 columns):
#  #   Column     Non-Null Count  Dtype  
# ---  ------     --------------  -----  
#  0   latitude   995 non-null    float64
#  1   longitude  995 non-null    float64
#  2   NetWorth   995 non-null    float64
# dtypes: float64(3)
# memory usage: 63.4 KB
latlngnetworth
# latitude	longitude	NetWorth
# 0	47.603832	-122.330062	177.0
# 1	30.271129	-97.743700	151.0
# 2	48.856697	2.351462	150.0
# 3	47.620548	-122.226445	124.0
# 4	37.444329	-122.159847	97.0
# ...	...	...	...
# 2736	3.151696	101.694237	1.0
# 2737	55.750446	37.617494	1.0
# 2742	30.332184	-81.655651	1.0
# 2743	38.511080	-122.847339	1.0
# 2746	55.750446	37.617494	1.0
# 995 rows × 3 columns

# latlngnetworth.to_numpy()
# latlngnetworth.to_json(r'output/latlngnetworth.json')
latlngnetworth.to_json(r'output/latlngnetworth2.json', orient='index', indent=2 )
# latlngnetworth.to_dict(orient='records')
# data file path
countriesloc = "./data/countriescoordinates.csv"
# read the csv file
countriesloc = pd.read_csv(countriesloc)
countriesloc.isnull().sum()
# country      1
# latitude     1
# longitude    1
# name         0
# dtype: int64
countriesloc = countriesloc.dropna(how='any',axis=0)
countriesloc
# country	latitude	longitude	name
# 0	AD	42.546245	1.601554	Andorra
# 1	AE	23.424076	53.847818	United Arab Emirates
# 2	AF	33.939110	67.709953	Afghanistan
# 3	AG	17.060816	-61.796428	Antigua and Barbuda
# 4	AI	18.220554	-63.068615	Anguilla
# ...	...	...	...	...
# 240	YE	15.552727	48.516388	Yemen
# 241	YT	-12.827500	45.166244	Mayotte
# 242	ZA	-30.559482	22.937506	South Africa
# 243	ZM	-13.133897	27.849332	Zambia
# 244	ZW	-19.015438	29.154857	Zimbabwe
# 243 rows × 4 columns

# data file path
countrieshdi = "./data/hdicsvData1.csv"
# read the csv file
countrieshdi = pd.read_csv(countrieshdi)
countrieshdi.isnull().sum()
# country    0
# hdi        0
# pop2022    0
# dtype: int64
countrieshdi
# country	hdi	pop2022
# 0	Norway	0.954	5511.370
# 1	Switzerland	0.946	8773.637
# 2	Ireland	0.942	5020.199
# 3	Hong Kong	0.939	7604.299
# 4	Germany	0.939	83883.596
# ...	...	...	...
# 181	Burundi	0.423	12624.840
# 182	South Sudan	0.413	11618.511
# 183	Chad	0.401	17413.580
# 184	Central African Republic	0.381	5016.678
# 185	Niger	0.377	26083.660
# 186 rows × 3 columns

cdf = countriesloc.merge(countrieshdi, left_on='name', right_on='country')
cdf
# country_x	latitude	longitude	name	country_y	hdi	pop2022
# 0	AD	42.546245	1.601554	Andorra	Andorra	0.857	77.463
# 1	AE	23.424076	53.847818	United Arab Emirates	United Arab Emirates	0.866	10081.785
# 2	AF	33.939110	67.709953	Afghanistan	Afghanistan	0.496	40754.388
# 3	AG	17.060816	-61.796428	Antigua and Barbuda	Antigua and Barbuda	0.776	99.509
# 4	AL	41.153332	20.168331	Albania	Albania	0.791	2866.374
# ...	...	...	...	...	...	...	...
# 171	VU	-15.376706	166.959158	Vanuatu	Vanuatu	0.597	321.832
# 172	YE	15.552727	48.516388	Yemen	Yemen	0.463	31154.867
# 173	ZA	-30.559482	22.937506	South Africa	South Africa	0.705	60756.135
# 174	ZM	-13.133897	27.849332	Zambia	Zambia	0.591	19470.234
# 175	ZW	-19.015438	29.154857	Zimbabwe	Zimbabwe	0.563	15331.428
# 176 rows × 7 columns

cdf = cdf.drop('country_y', 1)
cdf.to_json(r'output/cdf.json')
cols = ['latitude', 'longitude', 'name', 'hdi', 'pop2022']
geojson = df_to_geojson(cdf, cols)
output_filename = 'dataset.js'
with open("./output/cdf1.js", 'w') as output_file:
    output_file.write('var dataset = ')
    json.dump(geojson, output_file, indent=2) 
billionaires2_geo_dc1
# Name	Country	geometry	NetWorth	Age	Source	Rank	longitude	latitude
# 0	Jeff Bezos	United States	POINT (-122.3300624 47.6038321)	177.0	57.0	Amazon	1	-122.330062	47.603832
# 1	Elon Musk	United States	POINT (-97.74369950000001 30.2711286)	151.0	49.0	Tesla, SpaceX	2	-97.743700	30.271129
# 2	Bernard Arnault & family	France	POINT (2.3514616 48.8566969)	150.0	72.0	LVMH	3	2.351462	48.856697
# 3	Bill Gates	United States	POINT (-122.2264453 47.620548)	124.0	65.0	Microsoft	4	-122.226445	47.620548
# 4	Mark Zuckerberg	United States	POINT (-122.1598465 37.4443293)	97.0	36.0	Facebook	5	-122.159847	37.444329
# ...	...	...	...	...	...	...	...	...	...
# 2736	Surin Upatkoon	Thailand	POINT (101.6942371 3.1516964)	1.0	72.0	telecom, lotteries, insurance	2674	101.694237	3.151696
# 2737	Ruben Vardanyan	Russia	POINT (37.6174943 55.7504461)	1.0	52.0	investment banking	2674	37.617494	55.750446
# 2742	J. Wayne Weaver	United States	POINT (-81.65565100000001 30.3321838)	1.0	85.0	Shoes	2674	-81.655651	30.332184
# 2743	Sandy Weill	United States	POINT (-122.8473388 38.5110803)	1.0	88.0	Citigroup	2674	-122.847339	38.511080
# 2746	Vadim Yakunin	Russia	POINT (37.6174943 55.7504461)	1.0	58.0	pharmacy	2674	37.617494	55.750446
# 995 rows × 9 columns

bcount_df = billionaires2_geo_dc1['Country'].value_counts()
bcount_df
# United States           471
# Russia                  100
# India                    72
# China                    46
# South Korea              33
# Taiwan                   25
# Hong Kong                20
# Brazil                   18
# Canada                   16
# Germany                  16
# Australia                15
# Japan                    11
# Switzerland              10
# Malaysia                 10
# United Kingdom            9
# Sweden                    9
# Turkey                    8
# Italy                     8
# Philippines               7
# Spain                     7
# Mexico                    7
# Thailand                  6
# Ukraine                   6
# Israel                    6
# Indonesia                 5
# France                    5
# Egypt                     5
# Czechia                   5
# Lebanon                   3
# Chile                     3
# Singapore                 3
# Nigeria                   2
# South Africa              2
# Morocco                   2
# Netherlands               2
# Ireland                   2
# Kazakhstan                2
# Peru                      2
# Austria                   2
# Colombia                  2
# Eswatini (Swaziland)      1
# Venezuela                 1
# Denmark                   1
# Vietnam                   1
# United Arab Emirates      1
# Zimbabwe                  1
# Greece                    1
# Poland                    1
# Iceland                   1
# Romania                   1
# Norway                    1
# Argentina                 1
# Name: Country, dtype: int64
billionaires2_geo_dc1['Counts'] = billionaires2_geo_dc1.groupby(['Country'])['Rank'].transform('count')
billionaires2_geo_dc1
# Name	Country	geometry	NetWorth	Age	Source	Rank	longitude	latitude	Counts
# 0	Jeff Bezos	United States	POINT (-122.3300624 47.6038321)	177.0	57.0	Amazon	1	-122.330062	47.603832	471
# 1	Elon Musk	United States	POINT (-97.74369950000001 30.2711286)	151.0	49.0	Tesla, SpaceX	2	-97.743700	30.271129	471
# 2	Bernard Arnault & family	France	POINT (2.3514616 48.8566969)	150.0	72.0	LVMH	3	2.351462	48.856697	5
# 3	Bill Gates	United States	POINT (-122.2264453 47.620548)	124.0	65.0	Microsoft	4	-122.226445	47.620548	471
# 4	Mark Zuckerberg	United States	POINT (-122.1598465 37.4443293)	97.0	36.0	Facebook	5	-122.159847	37.444329	471
# ...	...	...	...	...	...	...	...	...	...	...
# 2736	Surin Upatkoon	Thailand	POINT (101.6942371 3.1516964)	1.0	72.0	telecom, lotteries, insurance	2674	101.694237	3.151696	6
# 2737	Ruben Vardanyan	Russia	POINT (37.6174943 55.7504461)	1.0	52.0	investment banking	2674	37.617494	55.750446	100
# 2742	J. Wayne Weaver	United States	POINT (-81.65565100000001 30.3321838)	1.0	85.0	Shoes	2674	-81.655651	30.332184	471
# 2743	Sandy Weill	United States	POINT (-122.8473388 38.5110803)	1.0	88.0	Citigroup	2674	-122.847339	38.511080	471
# 2746	Vadim Yakunin	Russia	POINT (37.6174943 55.7504461)	1.0	58.0	pharmacy	2674	37.617494	55.750446	100
# 995 rows × 10 columns

billionaires2_geo_dc1.to_csv("output/bdc.csv")
def df_to_geojson(df, properties, lat='latitude', lon='longitude'):
    # create a new python dict to contain our geojson data, using geojson format
    geojson = {'type':'FeatureCollection', 'features':[]}

    # loop through each row in the dataframe and convert each row to geojson format
    for _, row in df.iterrows():
        # create a feature template to fill in
        feature = {'type':'Feature',
                   'properties':{},
                   'geometry':{'type':'Point',
                               'coordinates':[]}}

        # fill in the coordinates
        feature['geometry']['coordinates'] = [row[lon],row[lat]]

        # for each column, get the value and add it as a new feature property
        for prop in properties:
            feature['properties'][prop] = row[prop]
        
        # add this feature (aka, converted dataframe row) to the list of features inside our dict
        geojson['features'].append(feature)
    
    return geojson
cols = ['Name', 'Country', 'NetWorth', 'Counts', 'Rank', 'Age', "geometry"]
geojson = df_to_geojson(billionaires2_geo_dc1, cols)
output_filename = 'dataset.js'
with open("./output/bgeojsoncountdc1.geojson", 'w') as output_file:
    output_file.write('var dataset = ')
    json.dump(geojson, output_file, indent=2) 
# data_source = './output/bgeojsoncountdc1.geojson'
# gdf = gpd.read_file(data_source)

# gdf = gpd.GeoDataFrame(gdf, geometry=gdf['geometry'])
# gdf.crs = {'init' :'epsg:2154'}
# gdf = gdf.to_crs({'init' :'epsg:4326'}) 
# Import the SQL database into Pandas
engine = create_engine(f'postgresql://{user}:{password}@localhost:5432/bdc')

conn = engine.connect()
# read salaries file
bsql_df = pd.read_sql('Billionaires', conn)
bsql_df.head()
# ID	Name	Country	geometry	NetWorth	Age	Source	Rank	longitude	latitude	Counts
# 0	0	Jeff Bezos	United States	POINT (-122.3300624 47.6038321)	177.0	57.0	Amazon	1.0	-122.330062	47.603832	471.0
# 1	1	Elon Musk	United States	POINT (-97.74369950000001 30.2711286)	151.0	49.0	Tesla, SpaceX	2.0	-97.743700	30.271129	471.0
# 2	2	Bernard Arnault & family	France	POINT (2.3514616 48.8566969)	150.0	72.0	LVMH	3.0	2.351462	48.856697	5.0
# 3	3	Bill Gates	United States	POINT (-122.2264453 47.620548)	124.0	65.0	Microsoft	4.0	-122.226445	47.620548	471.0
# 4	4	Mark Zuckerberg	United States	POINT (-122.1598465 37.4443293)	97.0	36.0	Facebook	5.0	-122.159847	37.444329	471.0
counts_df = bsql_df[["Country", "Counts", "geometry", "latitude", "longitude"]]
counts_df
# Country	Counts	geometry	latitude	longitude
# 0	United States	471.0	POINT (-122.3300624 47.6038321)	47.603832	-122.330062
# 1	United States	471.0	POINT (-97.74369950000001 30.2711286)	30.271129	-97.743700
# 2	France	5.0	POINT (2.3514616 48.8566969)	48.856697	2.351462
# 3	United States	471.0	POINT (-122.2264453 47.620548)	47.620548	-122.226445
# 4	United States	471.0	POINT (-122.1598465 37.4443293)	37.444329	-122.159847
# ...	...	...	...	...	...
# 990	Thailand	6.0	POINT (101.6942371 3.1516964)	3.151696	101.694237
# 991	Russia	100.0	POINT (37.6174943 55.7504461)	55.750446	37.617494
# 992	United States	471.0	POINT (-81.65565100000001 30.3321838)	30.332184	-81.655651
# 993	United States	471.0	POINT (-122.8473388 38.5110803)	38.511080	-122.847339
# 994	Russia	100.0	POINT (37.6174943 55.7504461)	55.750446	37.617494