import praw
import config

reddit = praw.Reddit(
    username      = config.username,
    password      = config.password,
    client_id     = config.client_id,
    client_secret = config.client_secret,
    user_agent    = config.user_agent
)

subreddit = reddit.subreddit("pythonforengineers")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
