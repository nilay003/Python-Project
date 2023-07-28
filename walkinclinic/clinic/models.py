from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

# healthcare_app/models.py
from django.db import models

class user(models.Model):
    user_types = (
        ('patient', 'patient'),
        ('staff', 'staff'),
        ('doctor', 'doctor'),
        ('admin', 'admin'),
    )

    userid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthday = models.DateField()
    contactno = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postalcode = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=10, choices=user_types)
    def __str__(self):
        return self.username

class doctor(models.Model):
    doctorid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(user, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    daysavailable = models.CharField(max_length=100)
    def __str__(self):
        return f"Dr. {self.userid.firstname} {self.userid.lastname}"
    

class patient(models.Model):
    patientid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(user, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bpm = models.IntegerField()
    spo2 = models.IntegerField()
    def __str__(self):
        return f"{self.userid.firstname} {self.userid.lastname}"

class appointment(models.Model):
    appointmentid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(user, on_delete=models.CASCADE)
    doctorid = models.ForeignKey(doctor, on_delete=models.CASCADE)
    appointmentdate = models.DateField()
    appointmenttime = models.TimeField()
    patientissue = models.CharField(max_length=500)
    def __str__(self):
        return f"Appointment #{self.appointmentid} - {self.userid.firstname} {self.userid.lastname} with Dr. {self.doctorid.userid.firstname} {self.doctorid.userid.lastname}"



class invoice(models.Model):
    invoiceid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(user, on_delete=models.CASCADE)
    appointmentid = models.ForeignKey(appointment, on_delete=models.CASCADE)
    invoicedate = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentstatus = models.CharField(max_length=20)
    paymentmethod = models.CharField(max_length=50)
    def __str__(self):
        return f"Invoice #{self.invoiceid} - Amount: {self.amount} - Status: {self.paymentstatus}"

class prescription(models.Model):
    prescriptionid = models.AutoField(primary_key=True)
    doctorid = models.ForeignKey(doctor, on_delete=models.CASCADE)
    prescriptiondate = models.DateField()
    prescriptiondetail = models.CharField(max_length=500)
    def __str__(self):
       return f"Prescription #{self.prescriptionid} - Dr. {self.doctorid.userid.firstname} {self.doctorid.userid.lastname}"

class routinecheckup(models.Model):
    checkupid = models.AutoField(primary_key=True)
    patientid = models.ForeignKey(patient, on_delete=models.CASCADE)
    doctorid = models.ForeignKey(doctor, on_delete=models.CASCADE)
    checkupdate = models.DateField()
    detail = models.CharField(max_length=500)
    def __str__(self):
       return f"Checkup #{self.checkupid} - {self.patientid.userid.firstname} {self.patientid.userid.lastname} with Dr. {self.doctorid.userid.firstname} {self.doctorid.userid.lastname}"



class questionnairefacility(models.Model):
    questionid = models.AutoField(primary_key=True)
    questioncontent = models.CharField(max_length=500)
    def __str__(self):
       return self.questioncontent

class answer(models.Model):
    userid = models.ForeignKey(user, on_delete=models.CASCADE)
    questionid = models.ForeignKey(questionnairefacility, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    def __str__(self):
        return f"Answer to Question #{self.questionid.questionid} by {self.userid.username}"

class requestequipment(models.Model):
    requestid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(user, on_delete=models.CASCADE)
    equipmentname = models.CharField(max_length=100)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    def __str__(self):
       return f"Request #{self.requestid} - Equipment: {self.equipmentname} - Quantity: {self.quantity}"




class reporting(models.Model):
    userid = models.ForeignKey(user, on_delete=models.CASCADE)
    sentto = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateField()
    def __str__(self):
        return f"Report by {self.userid.username} - Sent To: {self.sentto}"

class feedback(models.Model):
    feedbackid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(user, on_delete=models.CASCADE)
    date = models.DateField()
    content = models.CharField(max_length=500)
    response = models.IntegerField()
    feedbacktype = models.CharField(max_length=20)
    def __str__(self):
        return f"Feedback #{self.feedbackid} by {self.userid.username} - Type: {self.feedbacktype}"

class promo(models.Model):
    invoiceid = models.ForeignKey(invoice, on_delete=models.CASCADE)
    promocode = models.CharField(max_length=50)
    percentage = models.IntegerField()
    def __str__(self):
       return f"Promo for Invoice #{self.invoiceid.invoiceid} - Code: {self.promocode} - {self.percentage}% Off"
