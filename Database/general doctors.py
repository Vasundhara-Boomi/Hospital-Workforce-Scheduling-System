import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["general_doctors_db"]
gdoc_collection = db["general_doctors"]
gdoc_collection.delete_many({})

def insert_gdoc(data):
    gdoc_collection.insert_one(data)

gdoc_data=[
    {"name": "Dr. Aryan Sharma G1", "department": "Cardiology", "Assigned": False},
    {"name": "Dr. Riya Patel G2", "department": "Cardiology", "Assigned": False},
    {"name": "Dr. Aditi Singh G3", "department": "Cardiology", "Assigned": False},
    {"name": "Dr. Arjun Gupta G4", "department": "Cardiology", "Assigned": False},
    {"name": "Dr. Ishaan Kumar G5", "department": "Nephrology", "Assigned": False},
    {"name": "Dr. Anaya Reddy G6", "department": "Nephrology", "Assigned": False},
    {"name": "Dr. Avni Choudhary G7", "department": "Nephrology", "Assigned": False},
    {"name": "Dr. Dev Sharma G8", "department": "Nephrology", "Assigned": False},
    {"name": "Dr. Kabir Malhotra G9", "department": "Neurology", "Assigned": False},
    {"name": "Dr. Meera Menon G10", "department": "Neurology", "Assigned": False},
    {"name": "Dr. Arnav Khanna G11", "department": "Neurology", "Assigned": False},
    {"name": "Dr. Nisha Ahuja G12", "department": "Neurology", "Assigned": False},
    {"name": "Dr. Anika Verma G13", "department": "Orthopedics", "Assigned": False},
    {"name": "Dr. Shaurya Gupta G14", "department": "Orthopedics", "Assigned": False},
    {"name": "Dr. Yash Kapoor G15", "department": "Orthopedics", "Assigned": False},
    {"name": "Dr. Riya Mehta G16", "department": "Orthopedics", "Assigned": False},
    {"name": "Dr. Diya Singh G17", "department": "Oncology", "Assigned": False},
    {"name": "Dr. Advik Patel G18", "department": "Oncology", "Assigned": False},
    {"name": "Dr. Saanvi Sharma G19", "department": "Oncology", "Assigned": False},
    {"name": "Dr. Aaradhya Reddy G20", "department": "Oncology", "Assigned": False},
    {"name": "Dr. Arya Banerjee G21", "department": "Dermatology", "Assigned": False},
    {"name": "Dr. Ishanvi Singh G22", "department": "Dermatology", "Assigned": False},
    {"name": "Dr. Aarav Sharma G23", "department": "Dermatology", "Assigned": False},
    {"name": "Dr. Nandini Joshi G24", "department": "Dermatology", "Assigned": False},
    {"name": "Dr. Sia Mishra G25", "department": "Endocrinology", "Assigned": False},
    {"name": "Dr. Kabir Patel G26", "department": "Endocrinology", "Assigned": False},
    {"name": "Dr. Tanvi Gupta G27", "department": "Endocrinology", "Assigned": False},
    {"name": "Dr. Ishaan Verma G28", "department": "Endocrinology", "Assigned": False}
  ]

for i in gdoc_data:
    insert_gdoc(i)