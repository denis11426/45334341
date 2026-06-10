# Interactive Fuel Prices Application

This project was created by Martin Beránek and Denis Pščolka for the course Data Processing in Python (JEM207) in the summer semester of the academic year 2025/2026.

THIS IS STILL A **WORK IN PROGRESS**!


## What is this project about

This project's goal was to create an interactive application in which the user could explore current and historic prices of fuel in the countries of the European Union. And get a simple prediction of what the price might me in the future.

The application downloads newest version of the document "Price developments 2005 onwards" from the [Weekly Oil bulletin](https://energy.ec.europa.eu/data-and-analysis/weekly-oil-bulletin_en), which is published by the European Comisson.

Then the data is cleaned, transformed etc. and can be viewed by the user. In the environment the user can specify following information: 

* if the prices shown are of Euro95 or Diesel
* tank size for which some salculations will be done
* countries of which they want to see the comparison of historic prices
* for which country they want to see the prediction of future price
* what is the maximum order of p, d and q parameters in the ARIMA(p,d,q) models that will be estimated as candidate models in the prediction section

Following tables, statistics and figures are shown:

* table of 10 countries currently with the cheapest selected fuel, with the price for 1000l of seleted fuel and the price for the tank size specified by the user
* bar chart showing 10 countries currently with the cheapest selected fuel
* bar chart showing 5 countries currently with the cheapest selected fuel and 5 countries currently with the most expensive selected fuel
* graph showing historical prices of selected fuel in selected countries since the year 2005 until today
* bar chart showing prices of selected fuel in selected countries with and without tax
* table with price of selected fuel in selected countries with and without tax, how much of the price is tax in both absolute and relative terms
* table with prediction of future (this week's) price of selected fuel in the selected country created in the following way:
  * user specifies the highest possible orders of p, d and q parameters in an ARIMA(p.d.q) process
  * the app estimates ARIMA models with all possible combinations of p, d and q and chooses the best model according to AIC (Akaike information criterion) and the best model according to BIC (Bayesian information criterion)
  * the app then creates the table with last week's price, the orders of the best models according to AIC and BIC, each model's prediction for this weeks price and how large this change is in relative terms


## How to proceed with launching the app

This is our recommended procedure (it worked on our computers) of how to launch the app if you are trying to launch it for the first time ever:


1. Open Anaconda Prompt.
2. Run the following commands in this specific order, line by line (you only have to change the path to where this project's folder is on your computer):
  * conda create -n fuel_app python=3.11 -y
  * conda activate fuel_app
  * cd C:\path\to\the\downloaded\repository\project
  * python -m pip install -r requirements.txt
  * python run_project.py

The app should open in an internet browser window and you are free to explore the data.

If you are trying to launch the app and have previously already done the steps above, you can skip some of them. You would only need to do the following:

1. Open Anaconda Prompt.
2. Run the following commands in this specific order, line by line (you only have to change the path to where this project's folder is on your computer, also you can skip lines 3-6 if you already ran these lines this week, since there are no new data, so you would just download the same data again):

  * conda activate fuel_app
  * cd C:\path\to\the\downloaded\repository\project
  * python run_project.pys

The app should open in an internet browser window and you are free to explore the data.

