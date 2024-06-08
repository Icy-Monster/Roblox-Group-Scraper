import requests
import json 
import time

GroupID = 1
FilePath = r"" #Set this to the location of the .txt file which will store the user IDs

IDList = open(FilePath, "a")
def RetrieveMembers(Group, Cursor: str): 
    GroupURL = "https://groups.roblox.com/v1/groups/"+ str(Group) +"/users?sortOrder=Asc&limit=100&cursor=" + Cursor

    Members = json.loads(requests.get(GroupURL).content.decode('utf-8'))

    for Member in Members['data']:
        time.sleep(0.12)
        IDList.write(str(Member['user']['userId']) + "\n")

    # Go to the next page
    if Members['nextPageCursor']:
        RetrieveMembers(Group, Members['nextPageCursor'])

RetrieveMembers(GroupID, "")