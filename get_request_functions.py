import urllib.request
import json

def collect_daily_quests():
	current_dailies_httpreqestobj = urllib.request.urlopen("https://api.guildwars2.com/v2/achievements/daily")
	current_dailies = json.loads(current_dailies_httpreqestobj.read().decode('utf-8'))
	return current_dailies

def format_current_dailies_to_your_level(current_dailies, current_level):
	list_of_available_daily_quests = []
	for x in current_dailies["pve"]:
		if x["level"]["min"] <= current_level and x["level"]["max"] >= current_level:
			list_of_available_daily_quests.append(x["id"])
	return list_of_available_daily_quests

def parse_achievement_ids_into_descriptions(ids):
	ids_list_converted_to_string = [str(x) for x in ids]
	ids_into_string = ",".join(ids_list_converted_to_string)
	available_daily_quests_httprequestobj = urllib.request.urlopen("https://api.guildwars2.com/v2/achievements?ids={0}".format(ids_into_string))
	available_daily_quests_full = json.loads(available_daily_quests_httprequestobj.read().decode('utf-8'))
	return available_daily_quests_full

def available_quest_rewards(available_quests):
	formatted_quest_rewards = []
	formatted_quest_rewards_dictionary = {}
	#FIX THIS STUFF
	for quest in available_quests:
		reward_ids = []
		reward_items_formatted_for_one_quest = ""
		for x in quest["rewards"]:
			reward_ids.append(str(x["id"]))
		reward_ids_into_string = ",".join(reward_ids)
		reward_item_objects_httprequestobj = urllib.request.urlopen("https://api.guildwars2.com/v2/items?ids={0}".format(reward_ids_into_string))
		reward_item_objects = json.loads(reward_item_objects_httprequestobj.read().decode('utf-8'))
		for y in reward_item_objects:
			output = "Item name: {0}\nItem Description: {1}\nItem image: {2}\n".format(y["name"], y["description"],y["icon"])
			reward_items_formatted_for_one_quest = reward_items_formatted_for_one_quest + output
		formatted_quest_rewards_dictionary[quest["id"]] = reward_items_formatted_for_one_quest
	return formatted_quest_rewards_dictionary