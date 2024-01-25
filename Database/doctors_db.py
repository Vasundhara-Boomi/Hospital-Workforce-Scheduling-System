import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Hospitaldb"]
doctors_collection = db["doctors"]
doctors_collection.delete_many({})

def insert_doctor(data):
    doctors_collection.insert_one(data)
doctors_data = [
    {
        'id': "D1",
        'name': 'Dr. Rajesh Gupta',
        'experience': 15,
        'education': 'MBBS, MD, DM (Cardiology)',
        'nationality': 'Indian',
        'department': 'Cardiology',
        'password': '7890',
        'email_id':'rajesh.gupta@gmail.com'
    },
    {
        'id': "D2",
        'name': 'Dr. Priya Singh',
        'experience': 10,
        'education': 'MBBS, MD (Cardiology)',
        'nationality': 'Indian',
        'department': 'Cardiology',
        'password': '6328'
    },
    {
        'id': "D3",
        'name': 'Dr. Sunil Verma',
        'experience': 8,
        'education': 'MBBS, MD (Cardiology)',
        'nationality': 'Indian',
        'department': 'Cardiology',
        'password': '1890'
    },
    {
        'id': "D4",
        'name': 'Dr. Anjali Sharma',
        'experience': 12,
        'education': 'MBBS, MD, DM (Cardiology)',
        'nationality': 'Indian',
        'department': 'Cardiology',
        'password': '3129'
    },
    {
        'id': "D5",
        'name': 'Dr. Sameer Yadav',
        'experience': 9,
        'education': 'MBBS, MD, DM (Cardiology)',
        'nationality': 'Indian',
        'department': 'Nephrology',
        'password': '8293'
    },
    {
        'id': "D6",
        'name': 'Dr. Kara B',
        'experience': 10,
        'education': 'MBBS, MS (Nephrology)',
        'nationality': 'Indian',
        'department': 'Nephrology',
        'password': '6734'
    },
    {
        'id': "D7",
        'name': 'Dr. Shruthi P',
        'experience': 12,
        'education': 'MBBS, MS (Nephrology)',
        'nationality': 'Indian',
        'department': 'Nephrology',
        'password': '7389'
    },
    {
        'id': "D8",
        'name': 'Dr. Sunita B',
        'experience': 9,
        'education': 'MBBS, MS (Nephrology)',
        'nationality': 'Indian',
        'department': 'Nephrology',
        'password': '1902'
    },
    {
        'id': "D9",
        'name': 'Dr. Anil Kumar',
        'experience': 11,
        'education': 'MBBS, MS, DM (Nephrology)',
        'nationality': 'Indian',
        'department': 'Neurology',
        'password': '1923'
    },
    {
        'id': "D10",
        'name': 'Dr. Ramesh Yadav',
        'experience': 8,
        'education': 'MBBS, MD (Nephrology)',
        'nationality': 'Indian',
        'department': 'Neurology',
        'password': '7829'
    },
    {
        'id': "D11",
        'name': 'Dr. Ashish K',
        'experience': 14,
        'education': 'MBBS, MD, DM (Neurology)',
        'nationality': 'Indian',
        'department': 'Neurology',
        'password': '8913'
    },
    {
        'id': "D12",
        'name': 'Dr. Raghu M',
        'experience': 13,
        'education': 'MBBS, MS, DM (Neurology)',
        'nationality': 'Indian',
        'department': 'Neurology',
        'password': '9102'
    },
    {
        'id': "D13",
        'name': 'Dr. Simran J',
        'experience': 7,
        'education': 'MBBS, MD (Neurology)',
        'nationality': 'Indian',
        'department': 'Orthopedics',
        'password': '8912'
    },
    {
        'id': "D14",
        'name': 'Dr. Deepak M',
        'experience': 10,
        'education': 'MBBS, MS, DM (Neurology)',
        'nationality': 'Indian',
        'department': 'Orthopedics',
        'password': '9128'
    },
    {
        'id': "D15",
        'name': 'Dr. Preeti G',
        'experience': 9,
        'education': 'MBBS, MD (Orthopedics)',
        'nationality': 'Indian',
        'department': 'Orthopedics',
        'password': '2938'
    },
    {
        'id': "D16",
        'name': 'Dr. Sangeetha K',
        'experience': 11,
        'education': 'MBBS, MS, DNB (Orthopedics)',
        'nationality': 'Indian',
        'department': 'Orthopedics',
        'password': '1029'
    },
    {
        'id': "D17",
        'name': 'Dr. Sanjay Gupta',
        'experience': 8,
        'education': 'MBBS, MS (Orthopedics)',
        'nationality': 'Indian',
        'department': 'Oncology',
        'password': '1902'
    },
    {
        'id': "D18",
        'name': 'Dr. Deepika M',
        'experience': 9,
        'education': 'MBBS, MS, DNB (Orthopedics)',
        'nationality': 'Indian',
        'department': 'Oncology'
    },
    {
        'id': "D19",
        'name': 'Dr. Surya K',
        'experience': 10,
        'education': 'MBBS, MD (Oncology)',
        'nationality': 'Indian',
        'department': 'Oncology',
        'password': '3910'
    },
    {
        'id': "D20",
        'name': 'Dr. Suresh S',
        'experience': 12,
        'education': 'MBBS, MD, DM (Oncology)',
        'nationality': 'Indian',
        'department': 'Oncology',
        'password': '9201'
    },
    {
        'id': "D21",
        'name': 'Dr. Anita Kumar',
        'experience': 11,
        'education': 'MBBS, MD, DNB (Oncology)',
        'nationality': 'Indian',
        'department': 'Oncology',
        'password': '9103'
    },
    {
        'id': "D22",
        'name': 'Dr. Rohan S',
        'experience': 10,
        'education': 'MBBS, MD, DM (Oncology)',
        'nationality': 'Indian',
        'department': 'Oncology',
        'password': '1829'
    },
    {
        'id': "D23",
        'name': 'Dr. Kavya H',
        'experience': 14,
        'education': 'MBBS, MD (Oncology)',
        'nationality': 'Indian',
        'department': 'Oncology',
        'password': '8109'
    },
    {
        'id': "D24",
        'name': 'Dr. Meena R',
        'experience': 15,
        'education': 'MBBS, MD, DNB (Endocrinology)',
        'nationality': 'Indian',
        'department': 'Endocrinology',
        'password': '1834'
    },
    {
        'id': "D25",
        'name': 'Dr. Priyanka P',
        'experience': 10,
        'education': 'MBBS, MD (Endocrinology)',
        'nationality': 'Indian',
        'department': 'Endocrinology',
        'password': '1783'
    },
    {
        'id': "D26",
        'name': 'Dr. Shankar G',
        'experience': 12,
        'education': 'MBBS, MD, DNB (Endocrinology)',
        'nationality': 'Indian',
        'department': 'Endocrinology',
        'password': '1893'
    },
    {
        'id': "D27",
        'name': 'Dr. Mridhula A',
        'experience': 11,
        'education': 'MBBS, MD, DM (Endocrinology)',
        'nationality': 'Indian',
        'department': 'Endocrinology',
        'password': '1894'
    },
    {
        'id': "D28",
        'name': 'Dr. Shaam D',
        'experience': 8,
        'education': 'MBBS, MD (Endocrinology)',
        'nationality': 'Indian',
        'department': 'Endocrinology',
        'password': '1938'
    }
]


for i in doctors_data:
    insert_doctor(i)
