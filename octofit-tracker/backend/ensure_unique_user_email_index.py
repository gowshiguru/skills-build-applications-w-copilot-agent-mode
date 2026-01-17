# This script ensures a unique index on the email field in the users collection in octofit_db
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['octofit_db']
users = db['octofit_tracker_user']
users.create_index([('email', 1)], unique=True)
print('Unique index on email field ensured for users collection.')
