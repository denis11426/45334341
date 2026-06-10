# Interactive Fuel Prices Application

This project was created by Martin Beránek and Denis Pščolka for the course Data Processing in Python (JEM207) in the summer semester of the academic year 2025/2026.

THIS IS STILL A **WORK IN PROGRESS**!


## What is this project about

This project's goal is to create an interactive application in which the user can explore current and historical fuel prices in the countries of the European Union and get a simple prediction of what the fuel price might be in the next period.

The application downloads the newest version of the document "Price developments 2005 onwards" from the [Weekly Oil Bulletin](https://energy.ec.europa.eu/data-and-analysis/weekly-oil-bulletin_en), which is published by the European Commission.

Then the data is cleaned, transformed, merged and displayed in the interactive application. In the app, the user can specify the following information:

* whether the prices shown are for Euro95 or Diesel
* tank size for which some calculations will be done
* countries for which they want to see the comparison of historical prices
* country for which they want to see the prediction of the future price
* maximum order of p, d and q parameters in the ARIMA(p,d,q) models that will be estimated as candidate models in the prediction section

The following tables, statistics and figures are shown:

* interactive map of Europe, where countries are colored according to the current price of the selected fuel
* table of 10 countries currently with the cheapest selected fuel, with the price for 1000 liters of selected fuel and the price for the tank size specified by the user
* bar chart showing 10 countries currently with the cheapest selected fuel
* bar chart showing 5 countries currently with the cheapest selected fuel and 5 countries currently with the most expensive selected fuel
* graph showing historical prices of selected fuel in selected countries since the year 2005 until today
* bar chart showing prices of selected fuel in selected countries with and without tax
* table with the price of selected fuel in selected countries with and without tax, including how much of the price is tax in both absolute terms and relative terms
* table with prediction of the future price of selected fuel in the selected country, created in the following way:
  * user specifies the highest possible orders of p, d and q parameters in an ARIMA(p,d,q) process
  * the app estimates ARIMA models with all possible combinations of p, d and q and chooses the best model according to AIC (Akaike information criterion) and the best model according to BIC (Bayesian information criterion)
  * the app then creates a table with the last observed price, the orders of the best models according to AIC and BIC, each model's prediction for the next price and how large this change is in relative terms

The prediction table is not estimated automatically every time the app changes. The user first chooses the ARIMA settings in the sidebar and then starts the prediction by clicking the prediction button.


## How to proceed with launching the app

This is our recommended procedure for launching the app for the first time. This procedure worked on our computers.

* Open Anaconda Prompt.
* Run the following commands in this specific order, line by line. You only have to change the path to where this project's folder is on your computer:
  * conda create -n fuel_app python=3.11 -y
  * conda activate fuel_app
  * cd C:\path\to\the\downloaded\repository\project
  * python -m pip install -r requirements.txt
  * python run_project.py
