"""
parseJSON.py parses the LUIS AI JSON response.
"""

from CalItem import CalItem
from TaskItem import TaskItem
import json

def parseJSON(json):
	scheduling = []
	todo = []
	for j in json:
		query = j["query"]
		intent = j["intents"][0]["intent"]
		action = ""
		actionTarget = ""
		location = ""
		startTime = ""
		for ent in j["entities"]:
			enttype = ent["type"]
			if enttype == "Action":
				action = enttype["entity"] 
			elif enttype == "ActionTarget":
				actionTarget = enttype["entity"]
			elif enttype == "Place":
				location = enttype["entity"]
			else:
				# not all entities have date
				startTime = enttype["resolution"]["date"]

		if intent == "Schedule":
			scheduling.append(CalItem(query, action,actionTarget,location,startTime))
		else:
			todo.append(TaskItem(query, action,actionTarget,location,startTime))
		
	return (scheduling,todo)