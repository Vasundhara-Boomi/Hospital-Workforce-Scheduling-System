import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["general_nurses_db"]
gnurse_collection = db["general_nurses"]
gnurse_collection.delete_many({})

def insert_gnurse(data):
    gnurse_collection.insert_one(data)

gnurse_data = [
    {"name": "Alisha G1", "department": "Cardiology", "Assigned": False},
    {"name": "Riddhi G2", "department": "Cardiology", "Assigned": False},
    {"name": "Shivani G3", "department": "Cardiology", "Assigned": False},
    {"name": "Diya G4", "department": "Cardiology", "Assigned": False},
    {"name": "Aarav G5", "department": "Nephrology", "Assigned": False},
    {"name": "Avantika G6", "department": "Nephrology", "Assigned": False},
    {"name": "Yuvraj G7", "department": "Nephrology", "Assigned": False},
    {"name": "Ishika G8", "department": "Nephrology", "Assigned": False},
    {"name": "Kabir G9", "department": "Neurology", "Assigned": False},
    {"name": "Myra G10", "department": "Neurology", "Assigned": False},
    {"name": "Kavya G11", "department": "Neurology", "Assigned": False},
    {"name": "Zara G12", "department": "Neurology", "Assigned": False},
    {"name": "Maya G13", "department": "Orthopedics", "Assigned": False},
    {"name": "Rohan G14", "department": "Orthopedics", "Assigned": False},
    {"name": "Priya G15", "department": "Orthopedics", "Assigned": False},
    {"name": "Aryan G16", "department": "Orthopedics", "Assigned": False},
    {"name": "Tanisha G17", "department": "Oncology", "Assigned": False},
    {"name": "Armaan G18", "department": "Oncology", "Assigned": False},
    {"name": "Kiara G19", "department": "Oncology", "Assigned": False},
    {"name": "Aditya G20", "department": "Oncology", "Assigned": False},
    {"name": "Aaradhya G21", "department": "Endocrinology", "Assigned": False},
    {"name": "Advait G22", "department": "Endocrinology", "Assigned": False},
    {"name": "Anushka G23", "department": "Endocrinology", "Assigned": False},
    {"name": "Riyaan G24", "department": "Endocrinology", "Assigned": False}
]

for nurse in gnurse_data:
    insert_gnurse(nurse)