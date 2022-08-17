import telegram.ext

def gettgid(update, context):
    user = update.message.from_user
    print('You talk with user {} and his user ID: {} '.format(user['username'], user['id']))

ge