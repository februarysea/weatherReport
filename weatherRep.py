from weather import Weather, Unit
from twilio.rest import Client

import weatherCode

weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('shanghai')
condition = location.condition
print(condition.text)
forecasts = location.forecast
print(forecasts[0].text)
print(forecasts[0].date)
print(forecasts[0].high)
print(forecasts[0].low)

text = 'Good morning! Here is weather report from februarysea! ' + 'Today is '\
       + forecasts[0].date + '. ' + 'The high temperature is '\
       + forecasts[0].high + '. ' + 'The low temperature is '\
       + forecasts[0].low + '. ' + 'The forecast is '\
       + forecasts[0].text + '. ' + 'Have a nice day! :)'

print(text)



#send message
account_sid = '#'
auth_token = '#'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='#',
    body=text,
    to='#'
)
print(message.sid)
