import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Hospitaldb"]
nurse_collection = db["Nurse"]
nurse_collection.delete_many({})

def insert_nurse(data):
    nurse_collection.insert_one(data)

nurses_data = [
    {
        'id': "N1",
        'name': 'Aarti Gupta',
        'experience': 5,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Cardiology',
        'password': '7890'
    },
    {
        'id': "N2",
        'name': 'Priya Singh',
        'experience': 4,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Cardiology',
        'password': '1234'
    },
    {
        'id': "N3",
        'name': 'Sunil V',
        'experience': 3,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Cardiology',
        'password': '7235'
    },
    {
        'id': "N4",
        'name': 'Meera Kapoor',
        'experience': 6,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Cardiology',
        'password': '5784'
    },
    {
        'id': "N5",
        'name': 'Rajesh Sharma',
        'experience': 4,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Cardiology',
        'password': '6488'
    },
    {
        'id': "N6",
        'name': 'Preeti Y',
        'experience': 5,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Cardiology',
        'password': '7589'
    },
    {
        'id': "N7",
        'name': 'Sunita Verma',
        'experience': 4,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Orthopedics',
        'password': '8095'
    },
    {
        'id': "N8",
        'name': 'Anil Kumar',
        'experience': 5,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Orthopedics',
        'password': '1234'
    },
    {
        'id': "N9",
        'name': 'Ram Yadav',
        'experience': 4,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Orthopedics',
        'password': '5678'
    },
    {
        'id': "N10",
        'name': 'Anil Jain',
        'experience': 3,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Orthopedics',
        'password': '9012'
    },
    {
        'id': "N11",
        'name': 'Karthik L',
        'experience': 5,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Orthopedics',
        'password': '1234'
    },
    {
        'id': "N12",
        'name': 'Meera S',
        'experience': 6,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Orthopedics',
        'password': '5678'
    },
    {
        'id': "N13",
        'name': 'Harish M',
        'experience': 5,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Nephrology',
        'password': '1234'
    },
    {
        'id': "N14",
        'name': 'Deepika M',
        'experience': 4,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Nephrology',
        'password': '7890'
    },
    {
        'id': "N15",
        'name': 'Ruchi Dev',
        'experience': 3,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Nephrology',
        'password': '4627'
    },
    {
        'id': "N16",
        'name': 'Suresh Verma',
        'experience': 6,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Nephrology',
        'password': '6430'
        
    },
    {
        'id': "N17",
        'name': 'Gita Yadav',
        'experience': 4,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Nephrology',
        'password': '5784'
    },
    {
        'id': "N18",
        'name': 'Sanjay G',
        'experience': 5,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Nephrology',
        'password': '6284'
    },
    {
        'id': "N19",
        'name': 'Divya Sharma',
        'experience': 4,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Endocrinology',
        'password': '1234'
    },
    {
        'id': "N20",
        'name': 'Pooja S',
        'experience': 3,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Endocrinology',
        'password': '1234'
    },
    {
        'id': "N21",
        'name': 'Varsha Nair',
        'experience': 6,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Endocrinology',
        'password': '9890'
    },
    {
        'id': "N22",
        'name': 'Sangeeta P',
        'experience': 4,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Endocrinology',
        'password': '1234'
    },
    {
        'id': "N23",
        'name': 'Akshaya J',
        'experience': 5,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Endocrinology',
        'password': '7173'
    },
    {
        'id': "N24",
        'name': 'Sonia Singh',
        'experience': 5,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Neurology',
        'password': '6328'
    },
    {
        'id': "N25",
        'name': 'Rajesh Kumar',
        'experience': 4,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Neurology',
        'password': '8493'
    },
    {
        'id': "N26",
        'name': 'Poonam P',
        'experience': 3,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Neurology',
        'password': '7289'
    },
    {
        'id': "N27",
        'name': 'Sarita Sharma',
        'experience': 6,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Neurology',
        'password': '4728'
    },
    {
        'id': "N29",
        'name': 'Amit Verma',
        'experience': 4,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Neurology',
        'password': '7382'
    },
    {
        'id': "N30",
        'name': 'Anjali S',
        'experience': 5,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Neurology',
        'password': '2934'
    },
    {
        'id': "N31",
        'name': 'Dhruv M',
        'experience': 4,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Oncology',
        'password': '9138'
    },
    {
        'id': "N32",
        'name': 'Aparna Sharma',
        'experience': 5,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Oncology',
        'password': '7193'
    },
    {
        'id': "N33",
        'name': 'Poonam Shetty',
        'experience': 3,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Oncology',
        'password': '5143'
    },
    {
        'id': "N34",
        'name': 'Samyukta Jain',
        'experience': 6,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Oncology',
        'password': '2456'
    },
    {
        'id': "N35",
        'name': 'Rohan J',
        'experience': 4,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Oncology',
        'password': '1340'
    },
    {
        'id': "N36",
        'name': 'Harini D',
        'experience': 5,
        'education': 'B.Sc Nursing',
        'nationality': 'Indian',
        'department': 'Oncology',
        'password': '5784'
    }
]
    

for i in nurses_data:
    insert_nurse(i)