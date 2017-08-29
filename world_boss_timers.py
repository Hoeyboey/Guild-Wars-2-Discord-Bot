from datetime import datetime
from threading import Timer
import asyncio

@asyncio.coroutine
def start_timers(message, client):
	print("start_timers has run")
	yield from tequatl_timer(message, client)

@asyncio.coroutine
def alarm_message_send(message_to_send, message, client):
	print("alarm_message_send has run")
	yield from testing_thing(client, message, message_to_send)
	print("message sent")

@asyncio.coroutine
def hello_world():
    yield from print("hello world")
    #...

@asyncio.coroutine
def tequatl_timer(message, client):
	print("tequatl_timer has run")
	message_to_send = "Tequatl the Sunless is now live! Recommended level of 65, on Sparkfly Fen. Nearest waypoint is Splintered Coast, far South West."
	tequatl_timer_day = datetime.today()
	tequatl_timer_time_to_go_off = tequatl_timer_day.replace(day=tequatl_timer_day.day, hour=17, minute=1, second=0, microsecond=0)
	tequatl_timer_difference = tequatl_timer_time_to_go_off - tequatl_timer_day
	tequatl_secs = tequatl_timer_difference.seconds+1
	yield from tequatl_timer_obj = Timer(tequatl_secs, alarm_message_send, [message_to_send, message, client])
	print(tequatl_timer_obj)
	tequatl_timer_obj.start()

@asyncio.coroutine
def testing_thing(client, message, message_to_send):
	yield from client.send_message(message.channel, message_to_send)

# 
#, tequatl_alarm_message_string=tequatl_alarm_message_string, channel_destination=channel_destination, client=client 
#
#alarm_message_send, [tequatl_alarm_message_string, channel_destination, client]
# x=datetime.today()
# y=x.replace(day=x.day, hour=12, minute=30, second=0, microsecond=0)
# delta_t=y-x
#message_to_send, channel_destination, client
# secs=delta_t.seconds+1

# def hello_world():
#     print("hello world")
#     #...

# t = Timer(secs, hello_world)
# t.start()

