#skincrawlerbot 


import praw
import os
import time
print("started")

reddit = praw.Reddit(client_id=os.getenv("clid"),
                          client_secret=os.getenv("sec"),
                          username="skincrawlerbot",
                          password=os.getenv("password"),
                          user_agent=os.getenv("agent"))




subreddit = reddit.subreddit("distressingmemes")
bot = reddit.redditor("skincrawlerbot")



while(1):
  for submission in subreddit.new(limit = None):
    yep = 0
    comments = submission.comments
    for comment in comments:
      if comment.author.name.lower() == "skincrawlerbot":
        yep = 1
        break

    if yep == 1:
      break
    else:
      stickycomment = submission.reply("`upvote` this comment if this post is distressing, `downvote` this comment if it isnt.\n\n ^(dont check your closet tonight  (◣\_◢))")
      stickycomment.mod.distinguish(sticky=True)
      print("stickied a comment on new post")
      time.sleep(5)

      continue


    

  for comment in bot.comments.new(limit = None):
    if "removed" in comment.body:
      continue
    elif "`upvote`" in comment.body:
      if comment.removed == True:
        continue
      #print("yes")
      #print(comment.score)
      elif comment.score < -3:
        try:
          comment.submission.mod.remove()
          comment.submission.flair.select("0341b710-4066-11ec-8e52-4a54370f5687")
          removalcomment = comment.submission.reply("Your post has been removed as the users voted that it was not distressing, if you have any doubts, contact the moderators of this community [here](https://i.imgur.com/or5lKlg.png)")
          removalcomment.mod.distinguish(sticky=True)
          print(f"removed a post, link: https://reddit.com{comment.submission.permalink}\n")
          comment.mod.remove()


        except Exception as a:
          print(a)
          comment.mod.remove()
          continue

      elif comment.score > 7:
        try:
          if submission.mod:
              continue

          comment.submission.mod.approve()
          approvalcomment = comment.submission.reply("users voted that your post was distressing, your soul wont be harvested tonight")
          approvalcomment.mod.distinguish(sticky=True)

          print(f"approved a post, link: https://reddit.com{comment.submission.permalink}\n")
          
          comment.mod.remove()

        except Exception as a:
          print(a)
          comment.mod.remove()
          continue





          
        
  
  
  #print("sleeping for 15s")
  time.sleep(15)
  




