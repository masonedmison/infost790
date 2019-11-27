# Milwaukee Crime Watch
### Infost790 Capstone Project by Mason Edmison, Katie Gates, and Joel Vojta 

A proof-of-concept for a Milwaukee Crime Watch application.

The application can be viewed at: http://192.241.137.249/
> The site has a self-signed certificate so you will likely encounter a security error upon first visit. 

#### Files of interest
- app/templates/user_input.html *html for landing page using jinja and chart.js*
- app/routes.py *logic of application - the 'clicks'*
- crime_score_api.py *functions that generate stats: crime_score and crime_score breakdown*
- app/\__init\__.py *set basic params for flask and establish connection to db using psycopg2*