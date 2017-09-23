import praw
import config
import pdb
import re
import os

reddit = praw.Reddit(
    username      = config.username,
    password      = config.password,
    client_id     = config.client_id,
    client_secret = config.client_secret,
    user_agent    = config.user_agent
)

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=10):
    if submission.id not in posts_replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("AyeeDwaynee Python Bot Says: Everyone Loves Python")
            print("Bot Replying To : ", submission.title)

            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
