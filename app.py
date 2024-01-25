from flask import Flask, jsonify, render_template, request,render_template_string, url_for, flash
import pymongo
import os,json
from datetime import datetime, timedelta, date 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string


app = Flask(__name__)
client = pymongo.MongoClient("mongodb://localhost:27017/")


db = client["Hospitaldb"]

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(8))
    return password

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        role = request.form['role']
        print(role)
        if role == 'Doctor':
            collection = db.doctors
            redirect_page = 'doctor_home.html'
        elif role == 'Nurse':
            collection = db.Nurse
            redirect_page = 'nurse_home.html'
        elif role == 'Admin':
            collection = db.Admin
            redirect_page = 'admin.html'
        elif role == 'Receptionist':
            collection = db.Receptionist
            redirect_page = 'welcome.html'
        else:
        # Handle an invalid or unknown role here
            return render_template('index.html')

        user = collection.find_one({'name': name, 'password': password})
        print(user)
        if user:
        # User authenticated successfully
        # Implement your authentication logic here
           #return redirect(url_for('welcome'))  # Redirect to the appropriate page
           return render_template(redirect_page,nurse_name=name)

        # User authentication failed
        return render_template('index.html')
    
def scheduling(name):
        db_name1=name
        db = client["Hospitaldb"]
        collections = db[db_name1] 
        cursor = collections.find()
        # count=0
        # for document in cursor:
        #     print(document)
        #     count+=1
        # print(count)    
        departments={"Cardiology":[],"Nephrology":[],"Neurology":[],"Orthopedics":[],"Oncology":[],"Endocrinology":[]}
        doctors=list(collections.find({"department":"Cardiology"}))
        for i in departments:
            doctors=list(collections.find({"department":i}))
            for j in doctors:
                departments[i].append([j["name"],j["experience"]])
            departments[i].sort(key=lambda x:x[1],reverse=True)
            departments[i]=[k[0] for k in departments[i]]
        # for i in departments:
        #     print(departments[i])

        doctors=["A","B","C","D","E"]
        day_rest={"A":"Tuesday","B":"Wednesday","C":"Sunday","D":"Saturday","E":"Monday"}
        shift_rest={"A":1,"B":2,"C":1,"D":2,"E":1}
        total=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        exp={"A":5,"B":6,"C":10,"D":3,"E":6}
        total1=[]
        for i in total:
            total1.append(i+"1")
            total1.append(i+"2")
        schedule={"Cardiology":[],"Nephrology":[],"Neurology":[],"Orthopedics":[],"Oncology":[],"Endocrinology":[]}
        def csp(name, dept, new, stack):
            while set(new) != {False}:
                added = False  # Track whether a doctor was added in this iteration
                for i in dept:
                    for j in range(len(new)):
                        if new[j]:
                            if "1" in new[j]:
                                req = new[j].strip("1")
                                k = 1
                            else:
                                req = new[j].strip("2")
                                k = 2
                            if shift_rest[i[1]] != k and day_rest[i[1]] != req:
                                stack.append([i, new[j]])
                                new[j] = False
                                added = True
                                break
                if not added:
                    break  # Break the loop if no doctor was added in this iteration
            schedule[name] = stack
        for i in departments:
            # print("error for loop", departments[i])
            new = total1.copy()
            dept = []
            for dept_name, doctor in zip(departments[i], doctors):
                # print([dept_name, doctor])
                dept.append([dept_name, doctor])

            # print("Length of doctors:", len(doctors))
            # print("Length of departments[i]:", len(departments[i]))

            csp(i, dept, new, [])

        for i in schedule:
            for j in range(len(schedule[i])):
                req1=[schedule[i][j][0][0],schedule[i][j][1]]
                schedule[i][j]=req1
        #print(schedule)
        f=open("schedule.json","w")
        json.dump(schedule,f)
        f=open("schedule.json","r")
        f1=json.load(f)
        print(f1)
        # departments = list(schedule.keys())
        # days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        # shifts = ['1', '2']

        # # Initialize an empty schedule_data dictionary
        # schedule_data = {dept: {day: {} for day in days} for dept in departments}

        # # Populate schedule_data based on the existing schedule
        # for dept, shifts_info in schedule.items():
        #     for shift_info in shifts_info:
        #         doctor_name, day_and_shift = shift_info
        #         day, shift = day_and_shift[:-1], day_and_shift[-1]
        #         schedule_data[dept][day][shift] = doctor_name
        # print(schedule_data)
        # return schedule_data
        
def schedule_mongodb(coll_schedule):
    print("schedule_mongodb")
    f=open("schedule.json","r")
    data=json.load(f)

    client = pymongo.MongoClient('mongodb://localhost:27017/')  

    db = client['medical_data']  

    collection = db[coll_schedule]  
    collection.delete_many({})

    collection.insert_one(data)

    print("Data inserted successfully into MongoDB.")

    all_schedule = collection.find()
    print(all_schedule[0])
      
def manage_leave(schedule_coll,staff,general_database,general_staff,json_file):
    print("manage_leave")
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['medical_data']
    collection = db[schedule_coll]


    today = date.today()  

    day_name = today.strftime("%A")
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    mongo_uri = 'mongodb://localhost:27017'
    db_name = 'your-database-name'
    client = pymongo.MongoClient(mongo_uri)
    db = client[db_name]
    requests_collection = db['requests']
    request = requests_collection.find({})

    check_flag = True
    leave=[]
    current_date = datetime.now()
    for i in request:
        print(len(i["replacement"]))
        if i["Status"]=="Approved" and len(i["replacement"])==0 and i["id"][0]==staff:
            c=0
            off=[]
            for j in range(len(i["Dates"])):
                given_date = datetime.strptime(i["Dates"][j], '%Y-%m-%d')
                date_diff=abs(current_date-given_date)
                if date_diff<timedelta(days=6):
                    c=c+1
                    off.append(i["Day"][j])
            if c>=1:
                leave.append([i["Name"],i["Dept"],off])
                check_flag=False     
    request.rewind()
    list_days=[]
    first=week.index(day_name)
    second=(first-2)%len(week)
    third=(first-1)%len(week)
    for i in range(first+1,len(week)):
        list_days.append(week[i])
    for i in range(first):
        list_days.append(week[i])
    if check_flag==False:
        schedule = collection.find({}, {'_id': 0})[0]
        old_schedule={}
        for i in schedule:
            old_schedule[i]=[]
            for j in schedule[i]:
                if "1" in j[1]:
                    m=j[1].strip("1")
                else:
                    m=j[1].strip("2")
                if week.index(m)!=third:
                    old_schedule[i].append(j)
        f=open(json_file,"r")
        confirm_schedule=json.load(f)
        for i in old_schedule:
            for j in confirm_schedule[i]:
                if "1" in j[1]:
                    m=j[1].strip("1")
                else:
                    m=j[1].strip("2")
                if week.index(m)==third:
                    old_schedule[i].append(j)
        for i in leave:
            name=i[0]
            dept=i[1]
            shift_one=[]
            shift_two=[]
            working=[]
            for j in range(len(old_schedule[dept])):
                if old_schedule[dept][j][0]==name:
                    if "1" in old_schedule[dept][j][1]:
                        new=old_schedule[dept][j][1].strip("1")
                        working.append(new)
                    else:
                        new=old_schedule[dept][j][1].strip("2")
                        working.append(new)
            if len(i[2])==1:
                for j in old_schedule[dept]:
                    if "1" in j[1]:
                        if j[0] not in shift_one:
                            shift_one.append(j[0])
                    else:
                        if j[0] not in shift_two:
                            shift_two.append(j[0])
                if name in shift_one:
                    need=shift_one
                    m="1"
                else:
                    need=shift_two
                    m="2"
                for j in need:
                    total=False
                    if j!=name:
                            req=j
                            break
                flag1=0
                flag2=0
                min1=float("inf")
                req2=0
                req1=0
                for j in range(len(old_schedule[dept])):
                    if flag1+flag2==2:
                                break
                    else:
                        if old_schedule[dept][j][0]==name and old_schedule[dept][j][1].strip(m)==i[2][0]:
                            req1=j
                        if old_schedule[dept][j][0]==req:
                            if "1" in old_schedule[dept][j][1]:
                                n=old_schedule[dept][j][1].strip("1")
                            else:
                                n=old_schedule[dept][j][1].strip("2")
                            if n in list_days and list_days.index(n)<min1 and n not in working:
                                min1=list_days.index(n)
                                req2=j
                k=old_schedule[dept][req1][0]
                l=old_schedule[dept][req2][0]
                old_schedule[dept][req1][0]=l
                old_schedule[dept][req2][0]=k
                filter_query={"Name":name}
                update_query = {"$set": {"replacement": [l]}}
                requests_collection.update_one(filter_query, update_query)
                collection.replace_one({},old_schedule)
            else:
                client = pymongo.MongoClient("mongodb://localhost:27017/")
                general_db = client[general_database]
                general_doctors_collection = general_db[general_staff]
                gd=general_doctors_collection.find({})
                for doctor in gd:
                    if doctor["Assigned"]==False and doctor["department"]==dept:
                        assgn=doctor["name"]
                        break
                for j in range(len(old_schedule[dept])):
                    if old_schedule[dept][j][0]==name:
                        if "1" in old_schedule[dept][j][1]:
                            d1=old_schedule[dept][j][1].strip("1")
                        else:
                            d1=old_schedule[dept][j][1].strip("2")
                        if d1 in i[2]:
                            old_schedule[dept][j][0]=assgn
                filter_query={"name":assgn}
                update_query = {"$set": {"Assigned":True}}
                general_doctors_collection.update_one(filter_query, update_query)
                filter_query={"Name":name}
                update_query = {"$set": {"replacement": [assgn]}}
                requests_collection.update_one(filter_query, update_query)
                collection.replace_one({},old_schedule)
        # else:
              
def retrieval(collect_schedule):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["medical_data"]
    collection = db[collect_schedule]

    # Retrieve data from the collection
    schedule_document = collection.find({})[0]
    schedule_data = {key: value for key, value in schedule_document.items() if key != '_id'}
    return schedule_data
 
def set_replacement():
    mongo_uri = 'mongodb://localhost:27017'
    db_name = 'your-database-name'

    client = pymongo.MongoClient(mongo_uri)
    db = client[db_name]

    requests_collection = db['requests']
    requests_collection.update_many({}, {"$set": {"replacement": []}}) 

def set_assigned():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["general_doctors_db"]
    gdoc_collection = db["general_doctors"]

    # Update all documents to set "Assigned" field to False
    gdoc_collection.update_many({}, {"$set": {"Assigned": False}})

@app.route('/nurse_get_leave_dates/<userName>')    
def nurse_requestleave(userName):
    scheduling("Nurse")
    dates=leave_schedule(userName,'nurses_schedule',"confirm_schedule_n.json")
    print('my dates are  ',dates)
    return jsonify(dates) 

@app.route('/doctor_get_leave_dates/<userName>')    
def doctor_requestleave(userName):
    scheduling("doctors")
    dates=leave_schedule(userName,'doctors_schedule',"confirm_schedule_d.json")
    print('my dates are  ',dates)
    print(userName)
    return jsonify(dates) 

def leave_schedule(staff_name, collect_schedule,json_file):
    try: 
        db_name=collect_schedule
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['medical_data']
        collection = db[db_name]
        req = collection.find({}) 
        print("Data inserted successfully into MongoDB.")

        name = staff_name

        all_schedule = collection.find()
        val = list(all_schedule[0].values())[1:]
        day = []
        for i in val:
            for j in i:
                if j[0] == name:
                    day.append(j[1])

        days_list = [i[:-1] for i in day]
        current_date = datetime.now()

        # Calculate dates within a week (excluding today)
        start_date = current_date + timedelta(days=1)  # Starting from tomorrow
        date_list = [start_date + timedelta(days=x) for x in range(7)]
        formatted_dates = [date.strftime('%Y-%m-%d') for date in date_list]

        with open(json_file, "r") as file:
            req = json.load(file)
            month_days = []
            for i in req:
                for j in req[i]:
                    if j[0] == name:
                        c = j[1].strip("12")
                        month_days.append(c)
        
        # Get matching dates within a week based on specific criteria
        matching_dates = []
        for date in formatted_dates:
            if datetime.strptime(date, '%Y-%m-%d').strftime('%A') in month_days:
                matching_dates.append(datetime.strptime(date, '%Y-%m-%d'))

        # Extract first four days and their dates
        matching_days = [date.strftime('%A') for date in matching_dates[:4]]
        matching_dates_final = [date.strftime('%Y-%m-%d') for date in matching_dates[:4]]

        print(matching_days)
        print(matching_dates_final)
        return matching_dates_final

    except Exception as e:
        print("Error:", e)
        return [] # Return empty list or handle error case as required

@app.route('/nurse_submit_leave', methods=['POST'])
def nurse_submit_leave():
    if request.method == 'POST':
        try:
            data = request.get_json()  # Get the JSON data from the request
            username = data.get('username')  # Extract username
            date = data.get('date')  # Extract selected date

            # Call your function to handle leave submission here
            user_id, user_department = get_nurse_info(username)

            result = submit_leave(username,date,user_id,user_department)
            print('result of result',result)
            return 'Leave submitted successfully' if result else 'Failed to submit leave'

        except Exception as e:
            return f'Error: {str(e)}'
        
def get_nurse_info(username):
    db = client['Hospitaldb']
    collection = db['Nurse']  

    user_info = collection.find_one({'name': username}, {'id': 1, 'department': 1})

    if user_info:
        return user_info.get('id'), user_info.get('department')
    else:
        return None, None
    
@app.route('/doctor_submit_leave', methods=['POST'])
def doctor_submit_leave():
    if request.method == 'POST':
        try:
            data = request.get_json()  # Get the JSON data from the request
            username = data.get('username')  # Extract username
            date = data.get('date')  # Extract selected date

            # Call your function to handle leave submission here
            user_id, user_department = get_doctor_info(username)
            result = submit_leave(username,date,user_id,user_department)
            print('result of result',result)
            return 'Leave submitted successfully' if result else 'Failed to submit leave'

        except Exception as e:
            return f'Error: {str(e)}'
                
def get_doctor_info(username):
    db = client['Hospitaldb']
    collection = db['doctors']  

    user_info = collection.find_one({'name': username}, {'id': 1, 'department': 1})

    if user_info:
        return user_info.get('id'), user_info.get('department')
    else:
        return None, None
                  
def submit_leave(username, udate, user_id, user_department):
    try:
        date_object = datetime.strptime(udate, '%Y-%m-%d')
        day = date_object.strftime('%A')

        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["your-database-name"]
        req_collection = db["requests"]

        existing_record = req_collection.find_one({'Name': username, 'Dates': udate})

        if existing_record:
            print("Leave request already exists for this name and date.")
            return False

        existing_user = req_collection.find_one({'Name': username})

        if existing_user:
            # If user record exists, update it by appending new date and day
            req_collection.update_one(
                {'Name': username},
                {'$push': {'Dates': udate, 'Day': day}}
            )
            print('Data updated successfully.')
            return True

        # If user record doesn't exist, create a new dictionary
        data = {
            'id': user_id,
            'Name': username,
            'Dept': user_department,
            'Day': [day],  # Create a list for the first day
            'Status': 'Pending',
            'Email': (username.replace(" ", "")).replace(".", "") + "@gmail.com",
            'No of days': 1,
            'Dates': [udate],  # Create a list for the first date
            'replacement': []
        }

        req_collection.insert_one(data)
        print('Data added to the database successfully.')
        return True  # Return True upon successful insertion

    except Exception as e:
        print(f'Error: {str(e)}')
        return False  # Return False if an error occurs
    
def retrieval_staff(collect_schedule):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["medical_data"]
    collection = db[collect_schedule]

    # Retrieve data from the collection
    schedule_data = collection.find({}, {'_id': 0})[0]

    # Convert the retrieved data to a dictionary
    schedule= dict(schedule_data)

    # Display or use the retrieved schedule dictionary
    print(schedule)
    departments={"Cardiology":[],"Nephrology":[],"Neurology":[],"Orthopedics":[],"Oncology":[],"Endocrinology":[]}
    departments = list(schedule.keys())
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    shifts = ['1', '2']

    # Initialize an empty schedule_data dictionary
    schedule_data = {dept: {day: {} for day in days} for dept in departments}

    # Populate schedule_data based on the existing schedule
    for dept, shifts_info in schedule.items():
        for shift_info in shifts_info:
            doctor_name, day_and_shift = shift_info
            day, shift = day_and_shift[:-1], day_and_shift[-1]
            schedule_data[dept][day][shift] = doctor_name
    print(schedule_data)
    return schedule_data
      
@app.route('/display_doctors')
def display_doctors():
    try:
        print("doctor method")
        set_assigned()
        set_replacement()
        scheduling("doctors")
        schedule_mongodb('doctors_schedule')
        manage_leave('doctors_schedule',"D","general_doctors_db","general_doctors","confirm_schedule_d.json")
        schedule_data=retrieval('doctors_schedule')
        print(schedule_data)
        role='DOCTOR'
        return render_template('table.html', schedule_data=schedule_data,role=role)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "An error occurred. Check the console for details.", 500
    
@app.route('/display_nurses')
def display_nurses():
    try:
        set_assigned()
        set_replacement()
        scheduling("Nurse")
        schedule_mongodb('nurses_schedule')
        manage_leave('nurses_schedule',"N","general_nurses_db","general_nurses","confirm_schedule_n.json")
        schedule_data=retrieval('nurses_schedule')
        role='NURSE'
        return render_template('table.html', schedule_data=schedule_data,role=role)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "An error occurred. Check the console for details.", 500
    
@app.route('/view_schedule_nurse/<nurse_name>')
def view_schedule_nurse(nurse_name):
    set_assigned()
    set_replacement()
    scheduling("Nurse")
    schedule_mongodb('nurses_schedule')
    manage_leave('nurses_schedule',"N","general_nurses_db","general_nurses","confirm_schedule_n.json")
    schedule_data=retrieval_staff('nurses_schedule')
    nurse_schedule = {dept: schedule for dept, schedule in schedule_data.items() if nurse_name in [shift_info for shifts_info in schedule.values() for shift_info in shifts_info.values()]}
    script_path = os.path.abspath(__file__)
    templates_path = os.path.join(os.path.dirname(script_path), 'templates')
    html_path = os.path.join(templates_path, 'view_schedule.html')
    return render_template_string(open(html_path).read(), doctor_name=nurse_name, doctor_schedule=nurse_schedule)

@app.route('/view_schedule_doctor/<nurse_name>')
def view_schedule_doctor(nurse_name):
    set_assigned()
    set_replacement()
    scheduling("doctors")
    schedule_mongodb('doctors_schedule')
    manage_leave('doctors_schedule',"D","general_doctors_db","general_doctors","confirm_schedule_d.json")
    schedule_data=retrieval_staff('doctors_schedule')
    nurse_schedule = {dept: schedule for dept, schedule in schedule_data.items() if nurse_name in [shift_info for shifts_info in schedule.values() for shift_info in shifts_info.values()]}
    script_path = os.path.abspath(__file__)
    templates_path = os.path.join(os.path.dirname(script_path), 'templates')
    html_path = os.path.join(templates_path, 'view_schedule.html')
    return render_template_string(open(html_path).read(), doctor_name=nurse_name, doctor_schedule=nurse_schedule)
       
@app.route('/add_emp')
def add_emp():
    return render_template('registration.html')

@app.route('/viewschedule')
def viewschedule():
    return render_template('schedule.html')

@app.route("/add_dept")
def add_dept():
    return render_template('add_dept.html')

@app.route('/add_department', methods=['POST'])
def add_department():
    department_data = request.json
    print(department_data)
    client = pymongo.MongoClient('mongodb://localhost:27017/')  
    db = client['Hospitaldb']  
    collection = db['Dept']
    collection.insert_one(department_data) 
    return jsonify({'message': 'Department added successfully'})

@app.route('/approval')
def approval():
    mongo_uri = 'mongodb://localhost:27017'
    db_name = 'your-database-name'

    client = pymongo.MongoClient(mongo_uri)
    db = client[db_name]

    requests_collection = db['requests']

    # Find documents where Status is "Pending"
    pending_requests = requests_collection.find({"Status": "Pending"})

    # Extract names, departments, and IDs of people with "Pending" status
    pending_info = [{"Name": req["Name"], "Dept": req["Dept"], "ID": req["id"], "Dates":req["Dates"]} for req in pending_requests]
    return render_template('req.html', pending_info=pending_info)

@app.route('/register_success')
def register_success():
    return render_template('index.html')

def send_email(subject, body,to_address='vemula2110137@ssn.edu.in'):
    
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'no.reply.hosschman@gmail.com'  
    smtp_password = 'ywwx wykh gkkk bkkd'  

    # Create a connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    
    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = to_address
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Send the email
    server.sendmail(smtp_username, to_address, message.as_string())
    print("sent")
    server.quit()
    
@app.route('/process_request', methods=['POST'])
def process_request():
    mongo_uri = 'mongodb://localhost:27017'
    db_name = 'your-database-name'

    client = pymongo.MongoClient(mongo_uri)
    db = client[db_name]

    requests_collection = db['requests']
    data = request.json
    print('Received request from client:', data)
    Dates=",".join(data.get('Dates'))
    # Extract UserID and action from the received data
    user_id = data.get('userId')
    action = data.get('action')

    # If the action is 'accept', update the user's status to 'Approved'
    if action == 'accept':
        
        user = requests_collection.find_one({'id': user_id})
        if user:
            requests_collection.update_one(
                {'id': user_id},
                {'$set': {'Status': 'Approved'}}
            )
            subject='Update On Your Leave Request '
            toemail="vemula2110137@ssn.edu.in"
            body= f"Dear {user_id},\n\n" \
                "Your leave request has been approved.\n\n" \
                f"Leave Dates: {Dates}\n\n \Your Compensatory date has been scheduled. Kindly view the Updated schedule\n\n"\
                "Thank you.\n\n Have a nice day :)"
            

                
    # If the action is 'deny', update the user's status to 'Denied'
    if action == 'deny':
        user = requests_collection.find_one({'id': user_id})
        if user:
            requests_collection.update_one(
                {'id': user_id},
                {'$set': {'Status': 'Denied'}}
            )
        subject='Update On Your Leave Request '
        toemail="vemula2110137@ssn.edu.in"
        body= f"Dear {user_id},\n\n" \
                    "Unfortunately, your leave request has been rejected.\n\n" \
                    f"Leave Dates: {Dates}\n\n" \
                    "If you have any questions or need more information, please contact the administrator.\n\n" \
                    "Thank you.\n\nHave a nice day :)"
    send_email(subject,body,toemail)
    response = {'status': 'success', 'message': 'Request processed successfully'}
    return jsonify(response)
@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        first_name = request.form['First Name']
        last_name = request.form['Last Name']
        employee_id = request.form['Employee ID']
        phone_number = request.form['phoneNumber']
        email = request.form['EMaIl ID']
        confirm_email = request.form['confirmEMaIl ID']
        department = request.form['department']
        category = request.form['category']
        gender = request.form['gender']
        exp = request.form['experience']
        house_number = request.form['house-number']
        address_lane_1 = request.form['address-lane-1']
        edu = request.form['address-lane-2']
        country = request.form['country']
        state = request.form['state']
        name=first_name+" "+last_name
        print(category)
        if category in ['HOD',"Junior Doctor","Senior Doctor"]:
            name="Dr."+" "+first_name+" "+last_name
            pas=generate_password()
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client["general_doctors_db"]
            subject = 'Registration Details'
            body = f"Dear {name}!\n\n Your Deatails suceccfully register \n\n user name:{email}\nYour password: {pas}\n\nPlease keep it secure."
            send_email(subject,body)
            doctors_collection = db["general_doctors"]
            doctors_collection.insert_one({"id":employee_id,"name":name,"experience":exp,"education":edu,"nationality":country,"department":department,"password":pas,"email_id":email,
                                           "phone":phone_number,"gender":gender,"address":house_number+address_lane_1+state})
        else:
            name=first_name+" "+last_name
            pas=generate_password()
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client["general_nurses_db"]
            subject = 'Registration Details'
            body = f"Dear {name}!\n\n Your Deatails suceccfully register \n\n user name:{email}\nYour password: {pas}\n\nPlease keep it secure."
            send_email(subject,body)
            doctors_collection = db["general_nurses"]
            doctors_collection.insert_one({"id":employee_id,"name":name,"experience":exp,"education":edu,"nationality":country,"department":department,"password":pas,"email_id":email,
                                           "phone":phone_number,"gender":gender,"address":house_number+address_lane_1+state})
                

        return "Form Registered successfully"
    
@app.route('/logout')
def logout():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/past_working_n/<nurse_name>')
def past_working_n(nurse_name):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['Hospitaldb']
    nurses_collection = db['Nurse']
    nurse_info = nurses_collection.find_one({'name': nurse_name}, {'_id': 0, 'id': 1, 'department': 1})
    if nurse_info:
        id = nurse_info.get('id')
        dept = nurse_info.get('department')
    final_other=past_working(id,nurse_name,dept)
    return render_template('past_working.html', final_other=final_other)
    
@app.route('/past_working_d/<nurse_name>')
def past_working_d(nurse_name):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['Hospitaldb']
    doctor_collection = db['doctors']
    doctor_info = doctor_collection.find_one({'name': nurse_name}, {'_id': 0, 'id': 1, 'department': 1})
    if doctor_info:
        id = doctor_info.get('id')
        dept = doctor_info.get('department')
    final_other=past_working(id,nurse_name,dept)
    return render_template('past_working.html', final_other=final_other)
    
def past_working(id,name,dept): 
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['medical_data']
    collection = db['doctors_schedule']


    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['medical_data']
    schedule_collection = db['nurses_schedule']

    mongo_uri = 'mongodb://localhost:27017'
    db_name = 'your-database-name'
    client = pymongo.MongoClient(mongo_uri)
    db = client[db_name]
    requests_collection = db['requests']

    today=datetime.today()


    last_seven=[]

    for i in range(1, 8):
        previous_date = today - timedelta(days=i)
            
        last_seven.append(previous_date.strftime('%Y-%m-%d'))
    date_last_seven =[datetime.strptime(date, '%Y-%m-%d') for date in last_seven]
    if id[0]=="N":
        schedule=schedule_collection.find({})[0]
        leaves=[]
        leave_take=requests_collection.find({})
        taken=[]
        for i in leave_take:
            if i["Name"]==name:
                for j in i["Dates"]:
                    if j in last_seven:
                        leaves.append([j,"Leave"])
                        taken.append(datetime.strptime(j, '%Y-%m-%d'))
        other_days=[]
        for i in date_last_seven:
            if i not in taken:
                other_days.append([i,i.strftime("%A")])
        final_other=[]
        for i in other_days:
            for j in range(len(schedule[dept])):
             if schedule[dept][j][0]==name:
                if "1" in schedule[dept][j][1]:
                    new=schedule[dept][j][1].strip("1")
                else:
                    new=schedule[dept][j][1].strip("2")
                if new==i[1]:
                    final_other.append(i)
        for i in range(len(final_other)):
            final_other[i][0]=str(final_other[i][0]).split()[0]
            final_other[i][1]="Present"
        if leaves:
            final_other.extend(leaves)
        else:
            final_other=other_days
        for i in range(len(final_other)):
            if isinstance(final_other[i][0], datetime):  
                final_other[i][0] = final_other[i][0].strftime('%Y-%m-%d')
        final=[]
        for i in range(len(final_other)):
            if final_other[i][1]=="Present":
                final.append(final_other[i])
        return final
    else:
        schedule=collection.find({})[0]
        leaves=[]
        leave_take=requests_collection.find({})
        taken=[]
        for i in leave_take:
            if i["Name"]==name:
                for j in i["Dates"]:
                    if j in last_seven:
                        leaves.append([j,"Leave"])
                        taken.append(datetime.strptime(j, '%Y-%m-%d'))
        other_days=[]
        for i in date_last_seven:
            if i not in taken:
                other_days.append([i,i.strftime("%A")])
        final_other=[]
        for i in other_days:
            for j in range(len(schedule[dept])):
             if schedule[dept][j][0]==name:
                if "1" in schedule[dept][j][1]:
                    new=schedule[dept][j][1].strip("1")
                else:
                    new=schedule[dept][j][1].strip("2")
                if new==i[1]:
                    final_other.append(i)
        for i in range(len(final_other)):
            final_other[i][0]=str(final_other[i][0]).split()[0]
            final_other[i][1]="Present"
        if leaves:
            final_other.extend(leaves)
        else:
            final_other=other_days
        print(final_other)
        for i in range(len(final_other)):
            if isinstance(final_other[i][0], datetime):  
                final_other[i][0] = final_other[i][0].strftime('%Y-%m-%d')
        final=[]
        for i in range(len(final_other)):
            print(final_other[i][1])
            if final_other[i][1]=="Present":
                final.append(final_other[i])
        return final

if __name__ == '__main__':
    app.run(debug=True)