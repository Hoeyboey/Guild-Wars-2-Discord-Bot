import discord
import asyncio
from bot_credentials import secret_token
from get_request_functions import *
from on_message_functions import *

client = discord.Client()



@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith("!daily"):
		available_quests_to_your_level_ids = await daily_achievement_function(message, client)
		if available_quests_to_your_level_ids != None:
			available_quests_full_description = parse_achievement_ids_into_descriptions(available_quests_to_your_level_ids)
			formatted_quest_rewards =  available_quest_rewards(available_quests_full_description)
			final_output_for_available_daily_quests = format_daily_quest_output(available_quests_full_description, formatted_quest_rewards)
			for x in final_output_for_available_daily_quests:
				await client.send_message(message.channel, x)

client.run(secret_token)

