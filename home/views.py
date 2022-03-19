from os import P_NOWAIT
from pickletools import read_uint1
import re
from django.core.files.storage import FileSystemStorage
from django.db.models.fields import EmailField
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from home.models import Applications, Approved, Authenticate
from django.contrib import messages


def instruction(request):
    if request.session['var'] == 0:
        request.session['var'] = 1
        return render(request, 'instruction.html')
    return HttpResponseRedirect("/")


def register(request):
    return render(request, 'register.html')


def login(request):
    if(request.session['var'] == 1 or request.session['var'] == 2):
        request.session['var'] = 2
        return render(request, 'login.html', {'andy': request.session['phno1']})
    return HttpResponseRedirect("/")


def validate(request):
    if(request.session['var'] != 2):
        return HttpResponseRedirect("/")
    if request.method == "POST":
        request.session['var'] = 2
        request.session['upiid'] = request.POST.get('upiid')
        request.session['amount'] = request.POST.get('amount')
        request.session['paymentdate'] = request.POST.get('paymentdate')
        payss = request.FILES['payss']
        fs = FileSystemStorage()
        file = fs.save(payss.name, payss)
        request.session['payss'] = file
        request.session['cname'] = request.POST.get('cname')
        request.session['fname'] = request.POST.get('fname')
        request.session['dob'] = request.POST.get('dob')
        photo = request.FILES['photo']
        file = fs.save(photo.name, photo)
        request.session['photo'] = file
        request.session['mob'] = request.POST.get('mob')
        request.session['email'] = request.POST.get('email')
        request.session['address'] = request.POST.get('address')
        request.session['tsubmit'] = request.POST.get('tsubmit')
        request.session['ftsubmit'] = request.POST.get('ftsubmit')
        request.session['equalexam'] = request.POST.get('equalexam')
        request.session['university'] = request.POST.get('university')
        request.session['monthyear'] = request.POST.get('monthyear')
        request.session['supname'] = request.POST.get('supname')
        request.session['supdept'] = request.POST.get('supdept')
        request.session['supwadd'] = request.POST.get('supwadd')
        admissionorder = request.FILES['admissionorder']
        file = fs.save(admissionorder.name, admissionorder)
        request.session['ador'] = file
        supreport = request.FILES['supreport']
        file = fs.save(supreport.name, supreport)
        request.session['supre'] = file
        tthesis = request.FILES['tthesis']
        file = fs.save(tthesis.name, tthesis)
        request.session['th'] = file
        request.session['titlethesis'] = request.POST.get('titlethesis')
        request.session['yearofadd'] = request.POST.get('yearofadd')
        request.session['time'] = request.POST.get('time')
        request.session['ptime'] = ptime = request.POST.get('ptime')
        request.session['otf'] = onTimef = 0
        request.session['onTime'] = onTime = request.POST.get('onTime')
        if(ptime == 'false' and onTime == 'true'):
            onTimef = request.FILES['onTimef']
            file = fs.save(onTimef.name, onTimef)
            request.session['otf'] = file
        request.session['prephd'] = request.POST.get('prephd')
        request.session['article'] = request.POST.get('article')
        synopsis = request.FILES['synopsis']
        file = fs.save(synopsis.name, synopsis)
        request.session['syn'] = file
        uploadthesis = request.FILES['uploadthesis']
        file = fs.save(uploadthesis.name, uploadthesis)
        request.session['fthesis'] = file
        pc = request.FILES['pc']
        file = fs.save(pc.name, pc)
        request.session['pc'] = file
        request.session['dateofsubmission'] = request.POST.get(
            'dateofsubmission')
        noc = request.FILES['noc']
        file = fs.save(noc.name, noc)
        request.session['noc'] = file
        request.session['myDate'] = request.POST.get('myDate')
        Sign = request.FILES['Sign']
        file = fs.save(Sign.name, Sign)
        request.session['sign'] = file

    return render(request, 'validate.html', {'sign': request.session['sign'], 'mydate': request.session['myDate'], 'pc': request.session['pc'], 'noc': request.session['noc'], 'date': request.session['dateofsubmission'], 'fthesis': request.session['fthesis'], 'syn': request.session['syn'], 'article': request.session['article'], 'prephd': request.session['prephd'], 'otf': request.session['otf'], 'otime': request.session['onTime'], 'ptime': request.session['ptime'], 'time': request.session['time'], 'photo': request.session['photo'], 'yearofadd': request.session['yearofadd'], 'th': request.session['th'], 'supre': request.session['supre'], 'ador': request.session['ador'], 'supwadd': request.session['supwadd'], 'supdept': request.session['supdept'], 'supname': request.session['supname'], 'monthyear': request.session['monthyear'], 'univer': request.session['university'], 'equalexam': request.session['equalexam'], 'fsubmit': request.session['ftsubmit'], 'tsubmit': request.session['tsubmit'], 'addr': request.session['address'], 'mail': request.session['email'], 'mob': request.session['mob'], 'dob': request.session['dob'], 'fname': request.session['fname'], 'cname': request.session['cname'], 'payss': request.session['payss'], 'paymt': request.session['paymentdate'], 'amount': request.session['amount'], 'upiid': request.session['upiid'], 'titlethesis': request.session['titlethesis'], 'photo': request.session['photo']})


def success(request):
    if(request.session['var'] == 2):
        app = Applications(
            upiid=request.session['upiid'],
            amount=request.session['amount'],
            paymentdate=request.session['paymentdate'],
            Paymentss=request.session['payss'],
            cname=request.session['cname'],
            fname=request.session['fname'],
            dob=request.session['dob'],
            photo=request.session['photo'],
            mob=request.session['mob'],
            email=request.session['email'],
            address=request.session['address'],
            tsubmit=request.session['tsubmit'],
            ftsubmit=request.session['ftsubmit'],
            equalexam=request.session['equalexam'],
            university=request.session['university'],
            monthyear=request.session['monthyear'],
            supname=request.session['supname'],
            supdept=request.session['supdept'],
            supwadd=request.session['supwadd'],
            admissionorder=request.session['ador'],
            supreport=request.session['supre'],
            titlethesis=request.session['titlethesis'],
            tthesis=request.session['th'],
            yearofadd=request.session['yearofadd'],
            time=request.session['time'],
            ptime=request.session['ptime'],
            onTime=request.session['onTime'],
            onTimef=request.session['otf'],
            prephd=request.session['prephd'],
            article=request.session['article'],
            synopsis=request.session['syn'],
            fullthesis=request.session['fthesis'],
            pc=request.session['pc'],
            dateofsubmission=request.session['dateofsubmission'],
            noc=request.session['noc'],
            myDate=request.session['myDate'],
            sign=request.session['sign']
        )
        app.save()
        request.session['var'] = 0
        return render(request, 'success.html', {'cname': app.cname, 'id': app.id})
    return HttpResponseRedirect("/")


def check(request):
    if request.method == "POST":
        phno = request.POST.get('mob')
        passwd = request.POST.get('password')
        sq = request.POST.get('sq')
        try:
            obj = Authenticate.objects.get(mob=phno)
            return HttpResponseRedirect("/")
        except:
            authenticate = Authenticate(
                mob=phno,
                password=passwd,
                sq=sq
            )
            authenticate.save()
    request.session['var'] = 0
    return render(request, 'check.html', {'message': ""})


def status(request):
    if request.method == "POST":
        if request.session['var'] == 0:
            phno = request.POST.get('phno')
            count = 0
            for i in phno:
                if(i < '0' or i > '9'):
                    break
                count += 1
            if(count != 10):
                return render(request, 'check.html', {'message': "Enter Valid Mobile Number"})
            request.session['phno1'] = phno
            password = request.POST.get('password')
            try:
                obj = Authenticate.objects.get(mob=phno)
            except:
                return render(request, 'check.html', {'message': "Create New User"})
            try:

                if obj.password == password:

                    obj = Applications.objects.get(mob=phno)

                    name = getattr(obj, 'cname')
                    fname = getattr(obj, 'fname')
                    mobile = getattr(obj, 'mob')
                    photo = getattr(obj, 'photo')
                    sta = getattr(obj, 'status')
                    tsta=getattr(obj,'transactionstatus')
                    bsta = rej = False
                    tstabool=False
                    if sta == 'Approved':
                        request.session['fmobile'] = mobile
                        bsta = True
                    elif sta == 'Rejected':
                        request.session['fmobile'] = mobile
                        rej = True
                    if tsta=="Approved":
                        tstabool=True
                    srea = getattr(obj, 'S_Reason')
                    return render(request, 'status.html', {'paystatus':tstabool,'photo': photo, 'cname': name, 'fname': fname, 'mobile': mobile, 'bstatus': bsta, 'status': sta, 'Sreason': srea, 'Rstatus': rej})
                return render(request, 'check.html', {'message': "Incorrect Password"})
            except:
                return HttpResponseRedirect("/instruction")

        else:
            return HttpResponseRedirect("/")
    return HttpResponseRedirect("/")


def forgot(request):
    return render(request, 'forgot.html')


def change(request):
    if request.method == "POST":
        mob = request.POST.get("phno")
        sq = request.POST.get("sq")
        passwd = request.POST.get("password")
    try:
        obj = Authenticate.objects.get(mob=mob)
        print(obj.password)
        if obj.sq == sq:
            Authenticate.objects.filter(mob=mob).update(password=passwd)
        else:
            return HttpResponse("<h1>Incorrect Security Answer</h1>")
        return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/register')


def certificate(request):
    mobile = request.session['fmobile']
    obj = Approved.objects.get(mob=mobile)
    return render(request, 'certify.html', {'obj': obj})


def delete(request):
    Applications.objects.get(mob=request.session['fmobile']).delete()
    return HttpResponseRedirect("/instruction")


def paylogin(request):
    request.session['var'] = 1
    return render(request, 'paylogin.html')


def logverify(request):
    if(request.session['var'] == 1):
        request.session['var'] = 2
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            if(user == "PaymentOfficer" and password == "1829"):
                return HttpResponseRedirect('payverify')
            elif(user == "VerifyOfficer" and password == "1839"):
                return HttpResponseRedirect("test")
        return HttpResponseRedirect('paylogin')
    return HttpResponseRedirect('paylogin')


def payverify(request):
    if(request.session['var'] == 2):
        request.session['var'] = 3
        if request.method == "POST":
            val = request.POST.get('stat')
            obje = Applications.objects.get(mob=request.session['verfphno'])
            if(val != "Approved"):
                setattr(obje, 'status', val)
                setattr(obje, 'S_Reason', request.POST.get('rstat'))
            setattr(obje, 'transactionstatus', val)
            obje.save()
        obj = Applications.objects.filter(transactionstatus='Pending')
        return render(request, 'payverify.html', {'objs': obj})
    return HttpResponseRedirect('paylogin')


def paydetails(request):
    if(request.session['var'] == 3):
        request.session['var'] = 0
        if request.method == "POST":
            phno = request.POST.get('persel')
            try:
                obj = Applications.objects.get(mob=phno)
                request.session['verfphno'] = phno
                request.session['var'] = 2
                return render(request, 'payaproval.html', {'objs': obj})
            except:
                return HttpResponseRedirect('payverify')
        return render(request, "payverify")
    return HttpResponseRedirect('payverify')


def test(request):
    if request.method == "POST":
        if request.POST.get('stat') == 'Approved':
            apprv = request.session['apprv']
            Applications.objects.filter(mob=apprv).update(status='Approved')
            try:
                obj = Approved.objects.get(mob=request.session['apprv'])
            except:
                obj = Applications.objects.get(mob=request.session['apprv'])
                approve = Approved(
                    upiid=obj.upiid,
                    amount=obj.amount,
                    paymentdate=obj.paymentdate,
                    Paymentss=obj.Paymentss,
                    cname=obj.cname,
                    fname=obj.fname,
                    dob=obj.dob,
                    photo=obj.photo,
                    mob=obj.mob,
                    email=obj.email,
                    address=obj.address,
                    tsubmit=obj.tsubmit,
                    ftsubmit=obj.ftsubmit,
                    equalexam=obj.equalexam,
                    university=obj.university,
                    monthyear=obj.monthyear,
                    supname=obj.supname,
                    supdept=obj.supdept,
                    supwadd=obj.supwadd,
                    admissionorder=obj.admissionorder,
                    supreport=obj.supreport,
                    titlethesis=obj.titlethesis,
                    tthesis=obj.tthesis,
                    yearofadd=obj.yearofadd,
                    time=obj.time,
                    ptime=obj.ptime,
                    onTime=obj.onTime,
                    onTimef=obj.onTimef,
                    prephd=obj.prephd,
                    article=obj.article,
                    synopsis=obj.synopsis,
                    fullthesis=obj.fullthesis,
                    pc=obj.pc,
                    dateofsubmission=obj.dateofsubmission,
                    noc=obj.noc,
                    myDate=obj.myDate,
                    sign=obj.sign,
                    status=obj.status
                )
                approve.save()
                return HttpResponseRedirect("/test")
        elif request.POST.get('stat') == 'Rejected':
            apprv = request.session['apprv']
            Applications.objects.filter(mob=apprv).update(status='Rejected')
            Applications.objects.filter(mob=apprv).update(
                S_Reason=request.POST.get('rstat'))
    a = []
    andy = Applications.objects.filter(
        status='Pending', transactionstatus='Approved')
    for i in andy:
        a.append(i.mob)
    return render(request, 'test.html', {'andy': a})


def adminlogin(request):
    if request.method == "POST":
        sandy = request.POST.get('nithin')
        try:
            obj = Applications.objects.get(mob=sandy)
            request.session['apprv'] = sandy

            return render(request, 'adminlogin.html', {'obj': obj})
        except:
            return HttpResponseRedirect('/test')
    return HttpResponseRedirect('/')


def printform(request):
    if request.method == "POST":
        id = request.POST.get('nithin')
        obj = Approved.objects.get(id=id)
    return render(request, 'printform.html', {'obj': obj})


def ApprovedList(request):
    a = []
    obj = Approved.objects.all()
    for i in obj:
        a.append(i.id)
    return render(request, 'ApprovedList.html', {'andy': a})


def home(request):
    return render(request, 'Home.html    ')


def bcvdlogin(request):
    request.session['advar'] = 1
    return render(request, 'bcvdlogin.html')


def bcvdverify(request):
    if(request.session['advar'] == 1):
        request.session['advar'] = 2
        if request.method == "POST":
            user = request.POST.get('user')
            print(user)
            password = request.POST.get('pass')
            if(user == "BOSKU" and password == "1829"):
                print(password)
                return HttpResponseRedirect('bosfill')
            elif(user == "VCKU" and password == "1839"):
                return HttpResponseRedirect("vclogin")
            elif(user == "COEKU" and password == "1853"):
                return HttpResponseRedirect("coelogin")
            elif(user == "DeptKU" and password == "1833"):
                return HttpResponseRedirect("deptlogin")
        return HttpResponseRedirect('bcvdlogin')
    return HttpResponseRedirect('bcvdlogin')


def bosfill(request):
    return render(request, 'bosfill.html')


def vclogin(request):
    return render(request, 'vclogin.html')


def coelogin(request):
    return render(request, 'coelogin.html')


def deptlogin(request):
    return render(request, 'deptlogin.html')
