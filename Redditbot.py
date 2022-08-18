# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 17:20:26 2021

@author: Roshan Nadavi
"""

import praw
import random 
import time
reddit = praw.Reddit(
    client_id="", #hidden for privacy reasons
    client_secret="", #hidden for privacy reasons
    user_agent="", #hidden for privacy reasons
    username="", #hidden for privacy reasons
    password="", #hidden for privacy reasons
    check_for_async=False
)

arr_nba = reddit.subreddit("nba").hot(limit=10)
Lebron_nickname = ["LeBronze", "LeGod", "LeLegend", "LeGoat"]
upvoted_take = ["good take", "big fax", 'I agree']
downvoted_take = ["bruh", "bad take", "downvoted you"]
for post in arr_nba:
    print(post.title)
    print('------------')
    if post.pinned == False:
        for comment in post.comments:
            if hasattr(comment, "body") and "lebron" in comment.body.lower() and comment.score>25:
                selected_index1 = Lebron_nickname[random.randrange(len(Lebron_nickname))] 
                #print(comment.body)
                #print(selected_index1)
                #print("***********")
                comment.reply("LeBron more like " + selected_index1)
                time.sleep(630)
            elif hasattr(comment, "score") and comment.score>750:
                selected_index2 =upvoted_take[random.randrange(len(upvoted_take))]   
                #print(comment.body)
                #print(selected_index2)
                #print("***********")
                comment.reply(selected_index2)
                time.sleep(630)
            elif hasattr(comment, "score") and comment.score<-10:
                selected_index3 = downvoted_take[random.randrange(len(downvoted_take))]
                #print(comment.body)
                #print(selected_index3)
                #print("***********")
                comment.reply(selected_index3)
                time.sleep(630)
