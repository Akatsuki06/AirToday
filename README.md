# AirToday
A web app to alert the users daily through email/sms about air quality in/around their area :)

## Screenshots

![screenshot from 2018-02-15 18-27-45](https://user-images.githubusercontent.com/16136908/37600206-b0cf6ad0-2bac-11e8-9d1c-ed9800fa55a2.png )


![screenshot from 2018-02-15 18-28-35](https://user-images.githubusercontent.com/16136908/37600209-b244ff60-2bac-11e8-9fa1-4003f0f61df7.png)

## Note 
Create a `credentials.py` file inside `AirToday` folder with following content.


AIRPOLLUTION_APPID = APP ID given by api.airpollutionapi.com <br>
AIRPOLLUTION_APPURL = 'http://api.airpollutionapi.com/1.0/aqi'<br>
EMAIL_HOST = 'smtp.sendgrid.net'<br>
EMAIL_HOST_USER = Sendgrid API Key ID<br>
EMAIL_HOST_PASSWORD = Sendgrid API Key<br>
EMAIL_PORT = 587<br>
EMAIL_USE_TLS = True<br>
ADMIN_EMAIL = Admin Email Address<br> 
TWILIO_ACC = Twilio Account Key<br>
TWILIO_TOKEN = Twilio Account Token<br>
TWILIO_PHONE = Twilio Phone Number<br>
GOOGLEAPIKEY = Google Map API key<br>
TEMP_IP = A temporary ip address to run on localhost