# WeatherReport

I use this repository on a vps to send a message on time everyday.


The repository use 3 python modules: 
 
weather-api: https://github.com/AnthonyBloomer/weather-api
 
twilio: https://github.com/twilio/twilio-python
 
apscheduler: https://github.com/agronholm/apscheduler
 
***

# Enviroment build

* Virtualenv

Install virtualenv:

    pip3 install virtualenv
    
Make project:

    mkdir myproject
    
    cd myproject/
    
Make virtual python3 environment:

    virtualenv --no-site-packages venv

Actvivate environment:

    soruce source venv/bin/activate
    
By the way, quit environment:

    deactivate
    
* Modules

Install weather-api:

    pip3 install weather-api

Install twilio:

    pip3 install twilio

Instal apscheduler:

    pip3 install apscheduler
    
***

# Coding

* Get weather from yahoo

      weather = Weather(unit=Unit.CELSIUS)
      location = weather.lookup_by_location('shanghai') 
      condition = location.condition
      forecasts = location.forecast 
      
  Location.forecast returns a forecast list, forecast[0] is today.
      
* Send message

      account_sid = '' 
      auth_token = ''  
      client = Client(account_sid, auth_token)

      message = client.messages.create(
          from_='', 
          body=text,
          to='' # the number when you sign in, trial account can only send this number
      )
      
   Variable account_sid and auth_token are you get from twilio.com.
   
   Variable from_ is the number that twilio.com gives you.
   
   Variable to is the number when you sign in, trial account can only send this number.
      

* Autorun

      scheduler = BlockingScheduler()
      scheduler.add_job(function, 'cron', day_of_week='0-6', hour=7, minute=00) 
      scheduler.start()
      
  Function is you want to do on time. 
  
  Cron means period.
  
  For example
                
      day_of_week='0-6', hour=7, minute=00
  
  It means we will do the function everyday at 7:00am.
  
Finally, we can receive the weather message on our phones everymoring at 7:00am.
