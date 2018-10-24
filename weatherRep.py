from weather import Weather, Unit
from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler

def weather():
    # get weather infrmation
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location('shanghai')
    condition = location.condition
    forecasts = location.forecast

    text = 'Good morning! Here is weather report from februarysea! ' + 'Today is ' \
           + forecasts[0].date + '. ' + 'Now the weather is ' \
           + condition.text + '. ' + 'The highest temperature is ' \
           + forecasts[0].high + '. ' + 'The lowest temperature is ' \
           + forecasts[0].low + '. ' + 'Today the forecast is ' \
           + forecasts[0].text + '. ' + 'Have a nice day! :)'
    print(text)

    # send message
    account_sid = '' #here is your account_sid from twilio
    auth_token = '' #here is your auth_token from twilio
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='', #here is your phonenumber get from twilio
        body=text,
        to='' #here is your phonenumber when you sign in writing
    )

scheduler = BlockingScheduler()
scheduler.add_job(weather, 'cron', day_of_week='0-6', hour=7, minute=00)
scheduler.start()
