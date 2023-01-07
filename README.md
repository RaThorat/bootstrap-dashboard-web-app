# bootstrap-dashboard-web-app

This dashboard is an example to design and to style a dashboard app completely in python with Dash Bootstrap. It includes the grid of the page, fonts, colors, rows and columns when designing future dashboard apps.

This is a dashboard app built using Dash and Plotly. It displays various graphs and charts based on the data provided in the file "Example_input_data.xlsx". The app has a responsive layout using Bootstrap. I used the video from charming data: 

https://www.youtube.com/watch?v=0mfIK8zxUds&t=13s

The example input data you can find in the github repository. The data used is about grant applications by the companies.The company names are anonimised for obvious reasons. The other data (money, dates) are heavily modified so as not to be able to trace to its origin.

# You can view dashboard via the link below: 

https://ronirmal.pythonanywhere.com/

How to use: If you want to see the entire dashboard on your laptop or on your external screen, zoom out 67% in your browser with your laptop or with your screen. You can also view the dashboard on your mobile browser. The graphs are interactive. You can use dropdown or checklist. You can also click or hover over the graphs to see more information. The graphs are examples for further development.


## Dependencies
The following libraries are used in this app:

  dash

  dash.dcc

  dash.html

  dash.dependencies

  plotly.express

  dash_bootstrap_components

  pandas

## Features

The app has the following features:

  A pie chart showing the distribution of data based on a dropdown selection

  A pie chart showing the distribution of data based on a dropdown selection

  A line chart showing the top ten applicants per type of organization, based on a multi-select dropdown

  A histogram showing the total subsidy vs type of organization, with application results based on a checklist

  A scatter plot showing the correlation between two variables, based on a dropdown selection
