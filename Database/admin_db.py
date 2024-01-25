import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Hospitaldb"]
admin_collection = db["Admin"]
admin_collection.delete_many({})

def insert_admin(data):
    admin_collection.insert_one(data)

admin_data = [
    {
        'id': 1,
        'name': 'Aryan M',
        'experience': 8,
        'education': 'MBA in Healthcare Management',
        'nationality': 'Indian',
        'department': 'Administration',
        'password': '2309'
    },
    {
        'id': 2,
        'name': 'Ananya Kapoor',
        'experience': 6,
        'education': "Master's in Hospital Administration",
        'nationality': 'Indian',
        'department': 'Administration',
        'password': '1973'
    },
    {
        'id': 3,
        'name': 'Rajat Verma',
        'experience': 10,
        'education': 'Healthcare Management Degree',
        'nationality': 'Indian',
        'department': 'Administration',
        'password': '1893'
    },
    {
        'id': 4,
        'name': 'Sanya D',
        'experience': 7,
        'education': "Master's in Health Administration",
        'nationality': 'Indian',
        'department': 'Administration',
        'password': '4829'
    },
    {
        'id': 5,
        'name': 'Akshay P',
        'experience': 9,
        'education': 'Health Services Administration',
        'nationality': 'Indian',
        'department': 'Administration',
        'password': '7389'
    }
]


for i in admin_data:
    insert_admin(i)