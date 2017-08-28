from get_request_functions import *

async def daily_achievement_function(message, client):
	split_message_content = message.content.split()
	if len(split_message_content) == 1:
		current_dailies = collect_daily_quests()
		available_quests_to_your_level_ids = format_current_dailies_to_your_level(current_dailies, 80)
		return available_quests_to_your_level_ids
	elif len(split_message_content) == 2:
		try:
			split_message_content[1] = int(split_message_content[1])
			current_dailies = collect_daily_quests()
			if split_message_content[1] > 0 and split_message_content[1] <= 80:
				available_quests_to_your_level_ids = format_current_dailies_to_your_level(current_dailies, split_message_content[1])
				return available_quests_to_your_level_ids
			else:
				await client.send_message(message.channel, "You've put in something that's not a possible character level!")
				return None
		except ValueError:
			await client.send_message(message.channel, "You put in something that's not a number after !daily.")
			return None

def format_daily_quest_output(available_quests, quest_rewards):
	current_available_quests_variable = ""
	formatted_available_quests = []
	for x in available_quests:
		output = "Quest name: {0}\nQuest requirement: {1}\nQuest rewards: {2}\n".format(x["name"], x["requirement"], quest_rewards[x["id"]])
		formatted_available_quests.append(output)
	return formatted_available_quests



