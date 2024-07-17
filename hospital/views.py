from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
import cx_Oracle
import random
import string
from django.core.mail import send_mail 

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.pdfgen import canvas


# Your code here...

em=''
pwd=''
ran=''  
user=None
def loginaction(request):
     global em,pwd,ran
     if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
 
        if key=="lemail":
                em=value
        if key=="lpsw":
                pwd=value
      c="SELECT * FROM user_login where email='{}' and password='{}'".format(em,pwd)
      cursor.execute(c)
      t=tuple(cursor.fetchall())
      print(t)
    #   request.session['pname'] = t[0][0]
      request.session['username']=t[0][1]
      print("piddddddddddddddddd",request.session['username'])
      request.session.save()
      with open('username_file.txt', 'w') as file:
            file.write(t[0][0])

      if t==(): 
            return render(request,'login_page.html',{'openlogin':True,'msg':'Invalid Credentials'})
      else:
            
            

            request.session['islogged']=True
            return render(request,"patientdetails.html",{'loggedin': request.session['islogged'],'name':t[0][1] ,'em':t[0][2],'ph':t[0][3] ,'age':t[0][4],'gen':t[0][5] ,'bg':t[0][6]},)

     return render(request,'login_page.html')

def aboutusaction(request):
      return render(request,'aboutus.html')
fn=''
ln=''
em=''
pwd=''
cpwd=''
phone=''
age=''
gender=''
bloodGroup=''
def signaction(request):
     global fn,ln,em,pwd,cpwd
     if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
        if key=="rfname":
                fn=value
        if key=="remail":
                em=value

        if key=="phone":
                phone=value
        if key=="age":
                age=value
        if key=="gender":
                gender=value
        if key=="bloodGroup":
                bloodGroup=value
        if key=="rpsw":
                pwd=value
        if key=="rcpsw":
                cpwd=value
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits,k =6)) 
        request.session['pnr']=ran




      c="INSERT INTO user_login VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(ran,fn,em,phone,age,gender,bloodGroup,pwd,cpwd)
      print("****************************************************************************",c)

      cursor.execute(c)
      m.commit() 
     return render(request,'signup_page.html',{'openregister':True}) 
def signup_login(request):
  return render(request,"login_page.html",{'openlogin':True})  

def logout(request):
      request.session['islogged']=False
      return redirect('/login')

from django.shortcuts import render
import cx_Oracle
# Create your views here.
email=''
name=''
country=''
phno=''
def contactusaction(request):
     global email,name,country,phno
     if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
        if key=="conem":
                email=value
        if key=="conname":
                name=value
        if key=="concountry":
                country=value
        if key=="conphno":
                phno=value        
      c="INSERT INTO contact_us VALUES('{}','{}','{}',{})".format( email,name,country,phno)
      print(c)
      
      cursor.execute(c)
      m.commit() 
      
     return render(request,'contactus.html')


def passqueries(request):
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      #m.close()
      c="SELECT * FROM contact_us "
      cursor.execute(c)
      t=list(cursor.fetchall())
      print(t)
      print(c)
      #l=t
      oid1 = request.session.get('pid1', None)
      print("pid1 value in checkdisease:", oid1)
      
      #for i in range(len(t)):
       # l.append(t[i])

      return render(request,'pass_queries.html',{'qu':t,'sname':request.session ['name']})

# def disease(request):
#       return render(request,'disease.html')


import joblib as jb
model = jb.load('trained_model')


def checkdisease(request):
  

  diseaselist=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction','Peptic ulcer diseae','AIDS','Diabetes ',
  'Gastroenteritis','Bronchial Asthma','Hypertension ','Migraine','Cervical spondylosis','Paralysis (brain hemorrhage)',
  'Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D',
  'Hepatitis E', 'Alcoholic hepatitis','Tuberculosis', 'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
  'Heart attack', 'Varicose veins','Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',
  'Arthritis', '(vertigo) Paroymsal  Positional Vertigo','Acne', 'Urinary tract infection', 'Psoriasis', 'Impetigo']


  symptomslist=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
  'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination',
  'fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy',
  'patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating',
  'dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes',
  'back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
  'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
  'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
  'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
  'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
  'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
  'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
  'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
  'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
  'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
  'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
  'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
  'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
  'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
  'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
  'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
  'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
  'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
  'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
  'yellow_crust_ooze']

  alphabaticsymptomslist = sorted(symptomslist)

  


  if request.method == 'GET':
    
     return render(request,'checkdisease.html', {"list2":alphabaticsymptomslist})




  elif request.method == 'POST':
       
      ## access you data by playing around with the request.POST object
      
      inputno = int(request.POST["noofsym"])
      print(inputno)
      if (inputno == 0 ) :
          return JsonResponse({'predicteddisease': "none",'confidencescore': 0 })
  
      else :

        psymptoms = []
        psymptoms = request.POST.getlist("symptoms[]")
       
        print(psymptoms)

      
        """      #main code start from here...
        """
      

      
        testingsymptoms = []
        #append zero in all coloumn fields...
        for x in range(0, len(symptomslist)):
          testingsymptoms.append(0)


        #update 1 where symptoms gets matched...
        for k in range(0, len(symptomslist)):

          for z in psymptoms:
              if (z == symptomslist[k]):
                  testingsymptoms[k] = 1
        inputtest = [testingsymptoms]
        print(inputtest)
        predicted = model.predict(inputtest)
        print("predicted disease is : ")
        print(predicted)

        y_pred_2 = model.predict_proba(inputtest)
        confidencescore=y_pred_2.max() * 100
        print(" confidence score of : = {0} ".format(confidencescore))

        confidencescore = format(confidencescore, '.0f')
        predicted_disease = predicted[0]

        Rheumatologist = [  'Osteoarthristis','Arthritis']
       
        Cardiologist = [ 'Heart attack','Bronchial Asthma','Hypertension ']
       
        ENT_specialist = ['(vertigo) Paroymsal  Positional Vertigo','Hypothyroidism' ]

        Orthopedist = []

        Neurologist = ['Varicose veins','Paralysis (brain hemorrhage)','Migraine','Cervical spondylosis']

        Allergist_Immunologist = ['Allergy','Pneumonia',
        'AIDS','Common Cold','Tuberculosis','Malaria','Dengue','Typhoid']

        Urologist = [ 'Urinary tract infection',
         'Dimorphic hemmorhoids(piles)']

        Dermatologist = [  'Acne','Chicken pox','Fungal infection','Psoriasis','Impetigo']

        Gastroenterologist = ['Peptic ulcer diseae', 'GERD','Chronic cholestasis','Drug Reaction','Gastroenteritis','Hepatitis E',
        'Alcoholic hepatitis','Jaundice','hepatitis A',
         'Hepatitis B', 'Hepatitis C', 'Hepatitis D','Diabetes ','Hypoglycemia']
         
        if predicted_disease in Rheumatologist :
           consultdoctor = "Rheumatologist"
           
        if predicted_disease in Cardiologist :
           consultdoctor = "Cardiologist"
           

        elif predicted_disease in ENT_specialist :
           consultdoctor = "ENT specialist"
     
        elif predicted_disease in Orthopedist :
           consultdoctor = "Orthopedist"
     
        elif predicted_disease in Neurologist :
           consultdoctor = "Neurologist"
     
        elif predicted_disease in Allergist_Immunologist :
           consultdoctor = "Allergist/Immunologist"
     
        elif predicted_disease in Urologist :
           consultdoctor = "Urologist"
     
        elif predicted_disease in Dermatologist :
           consultdoctor = "Dermatologist"
     
        elif predicted_disease in Gastroenterologist :
           consultdoctor = "Gastroenterologist"
     
        else :
           consultdoctor = "other"
        request.session['doctortype'] = consultdoctor 
        connStr = 'system/password@localhost:1521/xe'
        connection = cx_Oracle.connect(connStr)
        cursor = connection.cursor()


        with open('username_file.txt', 'r') as file:
             stored_value = file.read().strip()

        query = "SELECT name, age FROM user_login WHERE id = :id"
        cursor.execute(query, id=stored_value)
        result_set = cursor.fetchall()

        # Check if there is at least one row in the result set
        if result_set:
            # Iterate over each row in the result set
            for result in result_set:
                # Convert each row (tuple) to a list
                result_list = list(result)
                namee = result_list[0]
                agee = result_list[1]





        

        
        dran = ''.join(random.choices(string.ascii_uppercase + string.digits,k =6))
        request.session['dran']=dran 

        with open('dran.txt', 'w') as file:
            file.write(dran)

        cursor.execute("""
    INSERT INTO diseaseinfo (dis_id, name, diseasename, no_of_symp, symptomsname, confidence, consultdoctor,patient_id)
    VALUES (:dis_id, :name, :diseasename, :no_of_symp, :symptomsname, :confidence, :consultdoctor,:patient_id)
""", {
    'dis_id': dran,  # Use 'dis_id' instead of 'id'
    'name':namee,
    'diseasename': predicted_disease,
    'no_of_symp': inputno,
    'symptomsname': ', '.join(psymptoms),
    'confidence': confidencescore,
    'consultdoctor': consultdoctor,
    'patient_id': stored_value
})
        connection.commit()
        cursor.close()
        connection.close()
        print({'predicteddisease': predicted_disease, 'confidencescore': confidencescore, 'consultdoctor': consultdoctor, 'namee': namee})
        return JsonResponse({'predicteddisease': predicted_disease, 'confidencescore': confidencescore, 'consultdoctor': consultdoctor, 'namee': namee,'agee':agee})


def bookingaction(request):
 if request.method == 'GET':
      doctortype = request.session['doctortype']      
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()          
      c = '''
      select hospital,specialization from doctor where specialization=:doctortype

        '''
      cursor.execute(c, {'doctortype': doctortype})
      print(doctortype)
      t=list(cursor.fetchall())
      print(t)

     
      l=[]
      for i in range(len(t)):
        l.append(t[i])
      print(l)
      
      return render(request,'dum.html',{'se':l})
 


# def appaction(request):
#     if request.method == 'GET':
#         # doctortype = request.session['doctortype']    
#         doctortype = request.session.get('doctortype')
  
#         connStr = 'system/password@localhost:1521/xe'
#         m = cx_Oracle.connect(connStr)
#         cursor = m.cursor()

#         c = '''
#             SELECT d.name AS doctor_name, a.appointment_date
#             FROM doctor d
#             JOIN appointment a ON d.doc_id = a.doc_id
#             WHERE d.hospital = 'Manipal Hospitals, Bangalore' AND d.specialization=:doctortype
#         '''
       

#         cursor.execute(c, {'doctortype': doctortype})
#         t = list(cursor.fetchall())
#         print(t)
#         l = []
#         for i in range(len(t)):
#             l.append(t[i])
#         print(l)
#         return render(request, 'passenger.html', {'se': l})



em=''
pwd=''
# Create your views here.
def staffloginaction(request):
     global em,pwd
     if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
 
        if key=="semail":
                em=value
        if key=="spsw":
                pwd=value
    
      c="SELECT * FROM admin where email='{}' and password='{}'".format(em,pwd)
      cursor.execute(c)
      t=cursor.fetchone()
      print(t)
      if not t:
            return render(request,'login_page.html',{'sf':'Invalid credentials','stafflogin':True})
      request.session['name']=t[2]
#       ph="SELECT * FROM staff_ph where staff_id='{}'".format(t[0])
#       cursor.execute(ph)
#       ph=tuple(cursor.fetchone())
      
      return render(request,"staff_welcome.html",{'sname':t[2],'c':t,'ema':t[1]+" "+t[2]})

     return render(request,'staff_page.html')

def passqueries(request):
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      #m.close()
      c="SELECT * FROM contact_us "
      cursor.execute(c)
      t=list(cursor.fetchall())
      print(t)
      print(c)
      #l=t
      
      #for i in range(len(t)):
       # l.append(t[i])

      return render(request,'pass_queries.html',{'qu':t,'sname':request.session ['name']})

doc_id = ''
doc_name = ''
doc_dob = ''
address = ''
mobile_no = ''
gender = ''
registration_no = ''
year_of_registration = ''
qualification = ''
state_medical_council = ''
specialization = ''
password = ''
hospital = ''
def addflightaction(request):
    global doc_id, doc_name, doc_dob, address, mobile_no, gender, registration_no, year_of_registration, qualification, state_medical_council, specialization, password, hospital

    if request.method == "POST":
        conn_str = 'system/password@localhost:1521/xe'
        m = cx_Oracle.connect(conn_str)
        cursor = m.cursor()
        d = request.POST

        for key, value in d.items():
            if key == "dname":
                doc_name = value
            elif key == "dob":
                doc_dob = value
            elif key == "add":
                address = value
            elif key == "mobno":
                mobile_no = value
            elif key == "gen":
                gender = value
            elif key == "regno":
                registration_no = value
            elif key == "yor":
                year_of_registration = value
            elif key == "qua":
                qualification = value
            elif key == "med":
                state_medical_council = value
            elif key == "spe":
                specialization = value
            elif key == "pass":
                password = value
            elif key == "hos":
                hospital = value

        doc_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        c = """
            INSERT INTO doctor 
            VALUES (
                :doc_id, 
                :doc_name, 
                TO_DATE(:doc_dob, 'YYYY-MM-DD'), 
                :address, 
                :mobile_no, 
                :gender, 
                :registration_no, 
                TO_DATE(:year_of_registration, 'YYYY'), 
                :qualification, 
                :state_medical_council, 
                :specialization, 
                :password, 
                :hospital
            )
        """

        cursor.execute(c, {
            'doc_id': doc_id,
            'doc_name': doc_name,
            'doc_dob': doc_dob,
            'address': address,
            'mobile_no': mobile_no,
            'gender': gender,
            'registration_no': registration_no,
            'year_of_registration': year_of_registration,
            'qualification': qualification,
            'state_medical_council': state_medical_council,
            'specialization': specialization,
            'password': password,
            'hospital': hospital
        })

        m.commit()
        cursor.close()
        m.close()

        return render(request, 'newflight.html', {'sname': request.session['name'], 'fadd': 'Doctor details are added successfully'})

    return render(request, 'newflight.html', {'sname': request.session['name']})
    


secem=''
secpwd=''
# Create your views here.
def securityloginaction(request):
     global secem,secpwd
     if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
 
        if key=="secemail":
                secem=value
        if key=="secpsw":
                secpwd=value
    
      c="SELECT * FROM doctor WHERE registration_no='{}' and password='{}'".format(secem,secpwd)
      cursor.execute(c)
      t=cursor.fetchone()
      if not t:
            return render(request,'login_page.html',{'secf':'Invalid credentials','seclogin':True})
      request.session['secname']=t[0]
      
      print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",t)
    
      return render(request,"security_welcome.html",{'sname':t[1],'c':t})

     return render(request,'login_page.html')   


def consul_his(request):
    connStr = 'system/password@localhost:1521/xe'
    m = cx_Oracle.connect(connStr)
    cursor = m.cursor()

    doc_id = request.session['secname']
    print(doc_id)

    c = '''
        SELECT
            ul.name AS user_name,
            ul.email AS user_email,
            di.diseasename,
            c.consultation_date,
            c.status
        FROM
            user_login ul
        JOIN
            consultation c ON ul.id = c.patient_id
        JOIN    
            diseaseinfo di ON c.diseaseinfo_id = di.dis_id
        WHERE
            c.doctor_id = :doc_id
    '''

    cursor.execute(c, {'doc_id': doc_id})
    t = list(cursor.fetchall())
    print(t)
    print(c)

    # l = t

    return render(request, 'consultation_his.html', {'se': t})



def patientchat(request):
     oid1 = request.session.get('pid1', None)
     print("pid1 value in checkdisease:", oid1)
     return render(request,'hos_doc.html')



# def extractflytno(request):
#     flightid1=''
#     flightid2=''
#     if request.method=="GET":
#       connStr = 'system/password@localhost:1521/xe'
#       m = cx_Oracle.connect(connStr)
#       cursor=m.cursor()
#       d=request.GET
#       print("--------------------ext----------------------------------------------------------",d)
#       #m.close()
#       for key,value in d.items():
#         if key=="flightid1":
#                 flightid1=value
#         if key=="flightid2":
#                 flightid2=value
#         print("-*********************1st idigo**************************************************",flightid1)       
#         print("-**********************2nd idigo*************************************************",flightid2)       

#       #c="SELECT * FROM Flight where from_='{}' and to_='{}' and to_char(cast(Arrival as date),'YYYY-MM-DD')='{}'".format(fr,to,arr_date)
#       #cursor.execute(c)
#       return render(request,'doctors.html',{'flightid1':flightid1})
#     return render(request,'dum.html') 

# def extractflytno(request):
#     hospital_name = request.GET.get('hospital_name', '')
#     specialization = request.GET.get('specialization', '')

#     if hospital_name and specialization:
#         connStr = 'system/password@localhost:1521/xe'
#         m = cx_Oracle.connect(connStr)
#         cursor = m.cursor()

#         # Use the flightid1 and flightid2 in your database queries or processing
#         print("hospital_name:", hospital_name)
#         print("specialization", specialization)

#         cursor.close()
#         m.close()

#         return render(request, 'doctors.html', {'flightid1': hospital_name})
#     else:
#         return render(request, 'dum.html')
def extractflytno(request):
    hospital_name = request.GET.get('hospital_name', '')
    specialization = request.GET.get('specialization', '')
    request.session['hos_name']=hospital_name
    request.session['spec']=specialization


    if hospital_name and specialization:
        connStr = 'system/password@localhost:1521/xe'
        m = cx_Oracle.connect(connStr)
        cursor = m.cursor()

        # Use the hospital_name and specialization in your database queries or processing
        print("hospital_name:", hospital_name)
        print("specialization", specialization)

        # SQL Query to retrieve doctor names and appointment dates
        query = """
        SELECT d.name AS doctor_name, a.appointment_date,d.doc_id
        FROM doctor d
        JOIN appointment a ON d.doc_id = a.doc_id
        WHERE d.hospital = :hospital_name AND d.specialization = :specialization
        """
        
        # Bind parameters and execute the query
        cursor.execute(query, {'hospital_name': hospital_name, 'specialization': specialization})
        
        # Fetch the results
        results = cursor.fetchall()
        print(results)
        cursor.close()
        m.close()


        return render(request, 'doctors.html', {'results': results})
    else:
        return render(request, 'dum.html')


# def extractflytno1(request):
#     doc_name = request.GET.get('doc_name', '')
#     slot = request.GET.get('slot', '')
#     # print("Doctor name:", doc_name)
#     # print("slot", slot)

#     if doc_name and slot:
#         connStr = 'system/password@localhost:1521/xe'
#         m = cx_Oracle.connect(connStr)
#         cursor = m.cursor()

#         print("Doctor name:", doc_name)
#         print("slot", slot)

#         cursor.close()
#         m.close()

#         return render(request, 'dummy.html')

#     # Add a return statement in case the conditions are not met
#     return HttpResponse("Invalid parameters")
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render
import cx_Oracle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render
import cx_Oracle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph

# def extractflytno1(request):
#     doc_name = request.GET.get('doc_name', '')
#     slot = request.GET.get('slot', '')

#     hospital_name = request.session['hos_name']
#     specialization = request.session['spec']
#     print("hos", hospital_name)
#     print('spe', specialization)

#     if doc_name and slot:
#         connStr = 'system/password@localhost:1521/xe'
#         m = cx_Oracle.connect(connStr)
#         cursor = m.cursor()

#         with open('username_file.txt', 'r') as file:
#             stored_value = file.read().strip()

#         # SQL Query to retrieve user details
#         query = """
#             SELECT id, name, email, phoneno, age, gender, bloodgroup
#             FROM user_login
#             WHERE id = :stored_value
#         """

#         cursor.execute(query, {'stored_value': stored_value})

#         # Fetch the results
#         results = cursor.fetchall()

#         # Create a PDF document with letter size
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = f'inline; filename="{doc_name}_{slot}_confirmation.pdf"'
#         pdf = SimpleDocTemplate(response, pagesize=letter)

#         # Define styles
#         styles = getSampleStyleSheet()
#         title_style = ParagraphStyle('Title', parent=styles['Title'], textColor=colors.blue, fontSize=18, spaceAfter=12)
#         heading_style = ParagraphStyle('Heading1', parent=styles['Heading1'], textColor=colors.black, fontSize=14, spaceBefore=12)
#         content_style = ParagraphStyle('BodyText', parent=styles['BodyText'], spaceBefore=12, fontSize=12)

#         # Add a border to the whole page
#         pdf.leftMargin = 20
#         pdf.rightMargin = 20
#         pdf.topMargin = 20
#         pdf.bottomMargin = 20

#         # Add title to the PDF with a colored background and border
#         title_text = "HealthHub"
#         title_paragraph = Paragraph(title_text, title_style)
#         title_paragraph.border = colors.black
#         title_paragraph.backgroundColor = colors.lightblue
#         pdf.build([title_paragraph])

#         # Add a border around the content
#         content = []

#         # Add user details to the PDF with a colored background and border
#         if results:
#             content.append(Paragraph("<b>User Details:</b>", heading_style))
#             user_details = []
#             for result in results:
#                 user_details.extend([
#                     f"<b>Registration Id:</b> {result[0]}",
#                     f"<b>Name:</b> {result[1]}",
#                     f"<b>Email:</b> {result[2]}",
#                     f"<b>Mobile No:</b> {result[3]}",
#                     f"<b>Age:</b> {result[4]}",
#                     f"<b>Gender:</b> {result[5]}",
#                     f"<b>Blood Group:</b> {result[6]}",
#                 ])
#             user_details_paragraphs = [Paragraph(detail, content_style) for detail in user_details]
#             for paragraph in user_details_paragraphs:
#                 paragraph.border = colors.black
#                 paragraph.backgroundColor = colors.lightgrey
#             content.extend(user_details_paragraphs)

#         # Add a line break between user details and doctor/slot details
#         content.append(Paragraph("<br/><br/>", content_style))

#         # Add Doctor and Slot details to the PDF with a colored background and border
#         content.append(Paragraph(f"<b>Doctor Name:</b> {doc_name}", heading_style))
#         content.append(Paragraph(f"<b>Specialization:</b> {specialization}", heading_style))
#         content.append(Paragraph(f"<b>Slot:</b> {slot}", heading_style))
#         content.append(Paragraph(f"<b>Hospital Name:</b> {hospital_name}", heading_style))

#         for paragraph in content:
#             paragraph.border = colors.black
#             paragraph.backgroundColor = colors.lightgrey

#         pdf.build(content)

#         cursor.close()
#         m.close()

#         return response

#     # Add a return statement in case the conditions are not met
#     return HttpResponse("Invalid parameters")



        
from datetime import datetime

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import io
import cx_Oracle

def extractflytno1(request):
    doc_name = request.GET.get('doc_name', '')
    slot = request.GET.get('slot', '')
    doc_id = request.GET.get('doc_id', '')
    print("doccccccccccidd",doc_id)
    print('name',doc_name)
    print(slot)


    hospital_name = request.session['hos_name']
    specialization = request.session['spec']
    print("hos", hospital_name)
    print('spe', specialization)

    if doc_name and slot:

        connStr = 'system/password@localhost:1521/xe'
        m = cx_Oracle.connect(connStr)
        cursor = m.cursor()
        con_ran = ''.join(random.choices(string.ascii_uppercase + string.digits,k =6)) 
        with open('dran.txt', 'r') as file:
            dran = file.read().strip()
        print('dran', dran)


        with open('username_file.txt', 'r') as file:
            stored_value = file.read().strip()

        # SQL Query to retrieve user details
        query = """
            SELECT id, name, email, phoneno, age, gender, bloodgroup
            FROM user_login
            WHERE id = :stored_value
        """

        cursor.execute(query, {'stored_value': stored_value})

        # Fetch the results
        results = cursor.fetchall()

        # Load HTML template
        template = get_template('pdf_template.html')

        # Define context for the template
        context = {
            'results': results,
            'doc_name': doc_name,
            'specialization': specialization,
            'slot': slot,
            'hospital_name': hospital_name,
        }
      

       


        def parse_date_time(time_data):
            # Remove the period from the month abbreviation
            time_data = time_data.replace('.', '')
            try:
                # Try parsing with the first format
                formatted_time = datetime.strptime(time_data, '%b %d, %Y, %I %p')
            except ValueError:
                try:
                    # If the first format fails, try the second format
                    formatted_time = datetime.strptime(time_data, '%b %d, %Y, %I:%M %p')
                except ValueError:
                    # If both formats fail, raise an error or handle it as needed
                    raise ValueError(f"Unable to parse the date and time: {time_data}")

            return formatted_time

        # Example usage:
        # time_data = 'Dec. 15, 2023, 10 a.m.'
        formatted_time = parse_date_time(slot)

        insert_values = {
            'consultation_id': con_ran,
            'patient_id': stored_value,
            'doctor_id': doc_id,
            'diseaseinfo_id': dran,
            'consultation_date': formatted_time.strftime('%Y-%m-%d %H:%M:%S'),  # Convert datetime to string
        }

        insert_query = """
            INSERT INTO consultation (
                consultation_id,
                patient_id,
                doctor_id,
                diseaseinfo_id,
                consultation_date,
                status
            ) VALUES (
                :consultation_id,
                :patient_id,
                :doctor_id,
                :diseaseinfo_id,
                TO_TIMESTAMP(:consultation_date, 'YYYY-MM-DD HH24:MI:SS'),
                'Booked'
            )
        """

        cursor.execute(insert_query, insert_values)
        email_body = (
        f"Hello, {results[0][1]}\n\n"
        f"Your appointment with {doc_name} on {slot} at {hospital_name} is confirmed.\n"
        f"For any assistance, please call Team {hospital_name} at +91 1234567892\n\n"
        "Thank you for choosing HEALTHHUB. We look forward to seeing you at your appointment."
    )

     


        send_mail(
        "HEALTHHUB",
        email_body,
        "sairebelstar22@gmail.com",
        [results[0][2]],
        fail_silently=False,
        )
            

                        










        # Render the template with the context
        html_content = template.render(context)

        # Create a PDF document
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{doc_name}_{slot}_confirmation.pdf"'

        # Create PDF from HTML content
        pdf_buffer = io.BytesIO()
        pisa.pisaDocument(io.StringIO(html_content), pdf_buffer)
        pdf = pdf_buffer.getvalue()
        pdf_buffer.close()

        response.write(pdf)

        m.commit()
        cursor.close()
        m.close()
        

        return response

    # Add a return statement in case the conditions are not met
    return HttpResponse("Invalid parameters")







    
    















