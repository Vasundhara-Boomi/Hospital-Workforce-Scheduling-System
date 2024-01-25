import pymongo

mongo_uri = 'mongodb://localhost:27017'
db_name = 'your-database-name'

client = pymongo.MongoClient(mongo_uri)
db = client[db_name]

requests_collection = db['requests']
requests_collection.delete_many({})

requests=[{
    "id":"D1",
    "Name": "Dr. Rajesh Gupta",
    "Dept": "Cardiology",
    "Day": ["Monday","Wednesday"],
    "Status":"Approved",
    "Email":"rajeshgupta@gmail.com",
    "No of days": 1,
    "Dates": ["2023-11-27","2023-11-29"],
    "replacement": []
},
{
    "id":"N1",
    "Name": "Aarti Gupta",
    "Dept": "Cardiology",
    "Day": ["Friday"],
    "Status":"Approved",
    "Email":"aartigupta@gmail.com",
    "No of days": 1,
    "Dates": ["2023-11-24"],
    "replacement": []
}]

for i in requests:
    requests_collection.insert_one(i)


# import pymongo

# mongo_uri = 'mongodb://localhost:27017'
# db_name = 'your-database-name'

# client = pymongo.MongoClient(mongo_uri)
# db = client[db_name]

# requests_collection = db['requests']

# # Find documents where Status is "Pending"
# pending_requests = requests_collection.find({"Status": "Pending"})

# # Extract names, departments, and IDs of people with "Pending" status
# pending_info = [{"Name": req["Name"], "Dept": req["Dept"], "ID": req["id"], "Dates":req["Dates"]} for req in pending_requests]

# print(pending_info)
# doc={}
# print("People with 'Pending' status, their departments, and IDs:")
# #for info in pending_info:
# #    print(f"Name: {info['Name']}, Department: {info['Dept']}, ID: {info['ID']}")
# for i in pending_info:
#     doc[i['ID']]=[i['Name'],i['Dates']]
# print(doc)    
    
