from instabot import Bot

user_ = 'user@example'
pass_ = 'pass@example'

bot = Bot()

bot.login(username=user_, password=pass_)
bot.upload_photo('pic.jpg', caption='caption of post here')
