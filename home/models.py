from django.db import models
# Create your models here.


class Applications(models.Model):
    id = models.AutoField(primary_key=True)
    upiid = models.CharField(max_length=200, null=True)
    amount = models.IntegerField(null=True)
    paymentdate = models.DateField(null=True)
    transactionstatus = models.CharField(
        null=True, max_length=200, default='Pending')
    Paymentss = models.FileField(null=True)
    cname = models.CharField(max_length=200, null=True)
    fname = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
    photo = models.ImageField(null=True)
    mob = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.TextField(max_length=500, null=True)
    tsubmit = models.CharField(max_length=200, null=True)
    ftsubmit = models.CharField(max_length=200, null=True)
    equalexam = models.CharField(max_length=200, null=True)
    university = models.CharField(max_length=200, null=True)
    monthyear = models.CharField(max_length=200, null=True)
    supname = models.CharField(max_length=200, null=True)
    supdept = models.CharField(max_length=200, null=True)
    supwadd = models.CharField(max_length=200, null=True)
    admissionorder = models.FileField(null=True)
    supreport = models.FileField(null=True)
    titlethesis = models.CharField(null=True, max_length=200)
    tthesis = models.FileField(null=True)
    yearofadd = models.IntegerField(null=True)
    time = models.CharField(max_length=200,null=True)
    ptime = models.CharField(max_length=90,null=True)
    onTime = models.CharField(max_length=200,null=True)
    onTimef = models.FileField(null=True)
    prephd = models.CharField(max_length=200, null=True)
    article = models.IntegerField(null=True)
    synopsis = models.FileField(null=True)
    fullthesis = models.FileField(null=True)
    dateofsubmission = models.DateField(null=True)
    pc = models.FileField(null=True)
    noc = models.FileField(null=True)
    myDate = models.CharField(max_length=20,null=True)
    sign = models.FileField(null=True)
    status = models.CharField(max_length=200, null=True, default='Pending')
    S_Reason = models.TextField(
        max_length=500, null=True, default="Checking transaction")

    def __str__(self):
        return str(self.id)+" "+self.cname


class Approved(models.Model):
    id = models.AutoField(primary_key=True)
    upiid = models.CharField(max_length=200, null=True)
    amount = models.IntegerField(null=True)
    paymentdate = models.DateField(null=True)
    Paymentss = models.FileField(null=True)
    cname = models.CharField(max_length=200, null=True)
    fname = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
    photo = models.ImageField(null=True)
    mob = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.TextField(max_length=500, null=True)
    tsubmit = models.CharField(max_length=200, null=True)
    ftsubmit = models.CharField(max_length=200, null=True)
    equalexam = models.CharField(max_length=200, null=True)
    university = models.CharField(max_length=200, null=True)
    monthyear = models.CharField(max_length=200, null=True)
    supname = models.CharField(max_length=200, null=True)
    supdept = models.CharField(max_length=200, null=True)
    supwadd = models.CharField(max_length=200, null=True)
    admissionorder = models.FileField(null=True)
    supreport = models.FileField(null=True)
    titlethesis = models.CharField(null=True, max_length=200)
    tthesis = models.FileField(null=True)
    yearofadd = models.IntegerField(null=True)
    time = models.CharField(max_length=200,null=True)
    ptime = models.CharField(max_length=90,null=True)
    onTime = models.CharField(max_length=90,null=True)
    onTimef = models.FileField(null=True)
    prephd = models.CharField(max_length=200, null=True)
    article = models.IntegerField(null=True)
    synopsis = models.FileField(null=True)
    fullthesis = models.FileField(null=True)
    dateofsubmission = models.DateField(null=True)
    pc = models.FileField(null=True)
    noc = models.FileField(null=True)
    myDate = models.CharField(max_length=20,null=True)
    sign = models.FileField(null=True)
    status = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)+" "+self.cname
class Authenticate(models.Model):
    id = models.AutoField(primary_key=True)
    mob=models.CharField(max_length=10,null=True)
    password = models.CharField(max_length=200,null=True)
    sq=models.CharField(max_length=200,null=True) 

    