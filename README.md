# Billionaires 2021
A study of the world's Billionaire based on geographical location, net worth, industry, gender and other metrics.

<p align="center">
  <img src="https://github.com/mnperic/billionaires-2021/blob/main/images/billionaires_hero.png" alt="hero"/>
</p>

## Team

Anh Huong, Daniela Cornea and Mino Peric

## Overview

The premise of this project was to analyse and visualise data which showed the world's Billionaires based on their geographical location and net worth. Further metrics included industry/sector, gender, age and whether each Billionaire was or wasn't self-made. 

The datasets used for this project included:

* Forbes Billionaires of 2021 – Version 1
https://www.kaggle.com/roysouravcu/forbes-billionaires-of-2021
* Forbes Billionaires of 2021 – Version 2
https://www.kaggle.com/alexanderbader/forbes-billionaires-2021-30/version/3
* Forbes Real-time Billionaires
https://www.forbes.com/real-time-billionaires/#178d85b83d78

## How to execute application

The application can be executed in as follows:

1 – Update the <b>config.js</b> file in the folder <b>/static/js</b> with the valid <b>API key</b><br></br>
2 – In terminal <b>(python kernel)</b> type command:  <b>python bills_app.py</b>/b><br></br>
3 – Click on the link that appears in the terminal, e.g. <b>http://127.0.01:5000/</b></b>

## Method
### Applications

The project utilised a wide range of platforms, libraries, languages and databases, including;

* Python/Flask API
* MongoDB
* HTML/CSS
* Javascript
  * D3.js
  * Leaflet
  * Dimple

#### Python/Flask API

A <b>Python/Flask-powered API</b> was used to push data onto the database. Python was also used to perform ETL tasks to manipulate and clean datasets (via Jupyter Notebook).

#### MongoDB

<b>MongoDB</b> was utilised to capture real-time information of the world’s richest billionaire (including image, name and net-worth). This information was used as an interactive dashboard that is searchable and allows the user to filter and sort billionaire information.

#### HMTL/CSS

<b>HTML/CSS</b> was utlised to design and build an interactive dashboard that will allow users to choose billionaire profiles from a range of drop-down menus and text boxes, revealing summary information of each billionaire.

#### Javascript/D3.js

Multiple <b>JavaScript</b> libraries were used to plot the data in an interactive way. 

#### Leaflet (*requires user API key)

<b>Leaflet</b> was used to plot Billiionaire information on a global map. When hovered, front-end information is revealed, showing billionaire names and their respective net-worth based on their geographical location. 

#### Dimple

<b>Dimple</b> was also selected as an additional Javascript library to provide an interactive visualisation and aspect to the project. When hovered, the chart shows the number of billionaires per country simulataneously. 

## Visualisations

### Interactive Dashboard – Python/Flask API, MongoDB

 <p align="center">
  <img src="https://github.com/mnperic/billionaires-2021/blob/main/images/billionaires_dashboard.png" alt="dashboard"/>
</p>

### Interactive Map – Leaflet

<p align="center">
  <img src="https://github.com/mnperic/billionaires-2021/blob/main/images/Billionaires_Leaflet_1.PNG" alt="leaflet"/>
</p>

### Interactive Graph – Dimple

<p align="center">
  <img src="https://github.com/mnperic/billionaires-2021/blob/main/images/dimple.png" alt="dimple"/>
</p>

## Summary

<p align="center">
  <img src="https://github.com/mnperic/billionaires-2021/blob/main/images/Top_10_countries_DC_Fig4.png" alt="top_10"/>
</p>

In 2021, <b>USA</b> had the most billionaires in the world – home to <b>57.6%</b> of global billionaires.

<p align="center">
  <img src="https://github.com/mnperic/billionaires-2021/blob/main/images/Top10_DC_Fig1.png" alt="fig_1"/>
</p>

Additionally, in 2021 <b>Jeff Bezos</b> had the highest net worth of all billionaires across the world. 

<p align="center">
  <img src="https://github.com/mnperic/billionaires-2021/blob/main/images/World_Billionaires_DC_Fig2.png" alt="fig_2"/>
</p>

Finally, in 2021 <b>USA</b> had the highest number of billionaires across the world. 

## References

Forbes, 2021, <i>Forbes Billionaires – Version 1</i>, https://www.kaggle.com/roysouravcu/forbes-billionaires-of-2021<br></br>
Forbes, 2021, <i>Forbes Billionaires – Version 2</i>, https://www.kaggle.com/alexanderbader/forbes-billionaires-2021-30/version/3<br></br>
Forbes, 2021, <i>Forbes Real-Time Billionaires</i>, https://www.forbes.com/real-time-billionaires/#178d85b83d78
