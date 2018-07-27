from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from myapp.model.models_alpha import patientregModel,docregModel,hospitalregModel,p_checkuserModel,h_checkuserModel,pf_checkuserModel,p_updatepassModel,hospital_listModel,doc_listModel,appointmentModel,getAppointmentDetailsModel,df_checkuserModel,d_updatepassModel,d_checkuserModel
# Create your views here.
@csrf_exempt
def preg(request):
    return render(request,'patientReg.html')
@csrf_exempt
def dreg(request):
    return render(request,'addDoctor.html')
@csrf_exempt
def hreg(request):
    return render(request,'addHospital.html')
@csrf_exempt
def patientlog(request):
    return render(request,'patientLogin.html')
@csrf_exempt
def hospitalog(request):
    return render(request,'hospitalLogin.html')
@csrf_exempt
def doctorlog(request):
    return render(request,'doctorLogin.html')
@csrf_exempt
def forgotpass(request):
    return render(request,'forgotpass.html')
@csrf_exempt
def hforgotpass(request):
    return render(request,'h_forgotpass.html')
@csrf_exempt
def dforgotpass(request):
    return render(request,'d_forgotpass.html')
@csrf_exempt
def patient_dashboard(request):
    return render(request,'patientDashboard.html')

@csrf_exempt
def patientreg(request):
    if request.method=="POST":
        p_name=request.POST["pname"]
        p_mob=request.POST["pmob"]
        p_img=request.POST["pimg"]
        p_add=request.POST["padd"]
        p_email=request.POST["pemail"]
        p_pass=request.POST["pass"]
        rid=patientregModel(p_name,p_mob,p_img,p_add,p_email,p_pass)
        return HttpResponse(rid)
@csrf_exempt
def docreg(request):
    if request.method=="POST":
        h_name=request.POST["hname"]
        d_name=request.POST["dname"]
        d_img=request.POST["dimg"]
        d_spcl=request.POST["dspcl"]
        d_con=request.POST["dcon"]
        rid=docregModel(h_name,d_name,d_img,d_spcl,d_con)
        return HttpResponse(rid)
@csrf_exempt
def hospitalreg(request):
    if request.method=="POST":
        h_name=request.POST["hname"]
        h_add=request.POST["hadd"]
        h_email=request.POST["hemail"]
        h_pass=request.POST["hpass"]
        h_sec=request.POST["hsecurity"]
        h_ans=request.POST["hans"]
        rid=hospitalregModel(h_name,h_add,h_email,h_pass,h_sec,h_ans)
        return HttpResponse(rid)
    
@csrf_exempt
def patientlogin(request):
    user=request.POST["username"]
    password=request.POST["pas"]
    checkuserExist=p_checkuserModel(user,password)

    if checkuserExist >= 1:
        request.session['user_name']=user
        return HttpResponseRedirect('/p_dashboard/')
    else:
        return render(request,'patientLogin.html',{"message":"User does not exist"})
@csrf_exempt
def p_dashboard(request):
    userName=request.session['user_name']

    if 'user_name' in request.session:
        return render(request,'patientDashboard.html')
    else:
        return HttpResponseRedirect('/patientlog/')
@csrf_exempt
def patientlogout(request):
    del request.session['user_name']
    return HttpResponseRedirect('/patientlog/')

@csrf_exempt
def hospitalogin(request):
    user=request.POST["username"]
    password=request.POST["pas"]
    checkuserExist=h_checkuserModel(user,password)

    if checkuserExist >= 1:
        request.session['user_name']=user
        return HttpResponseRedirect('/h_dashboard/')
    else:
        return render(request,'hospitalLogin.html',{"message":"User does not exist"})
@csrf_exempt
def h_dashboard(request):
    userName=request.session['user_name']

    if 'user_name' in request.session:
        return render(request,'dashboard.html',{"user_name":userName})
    else:
        return HttpResponseRedirect('/hospitalog/')
@csrf_exempt
def hospitalogout(request):
    del request.session['user_name']
    return HttpResponseRedirect('/hospitalog/')

#patient
@csrf_exempt
def p_confirm(request):
    user=request.POST["username"]
    checkuserExist=pf_checkuserModel(user)

    if checkuserExist >= 1:
        request.session['user_name']=user
        return HttpResponseRedirect('/p_editpass/')
    else:
        return render(request,'patientLogin.html',{"message":"User does not exist"})
@csrf_exempt
def p_editpass(request):
    user=request.session['user_name']
    if 'user_name' in request.session:
        return render(request,'changePass.html')
    else:
        return render(request,'forgotpass.html',{"message":"Invalid username"})
@csrf_exempt
def p_changepass(request):
    if request.method=="POST":
        p_password=request.POST["pass"]
        username = request.session['user_name']
        p_updatepassModel(p_password,username)
        return render(request,'changePass.html',{"message":"your password has been changed successfully"})
@csrf_exempt
def appointments(request):
    hospital_list=hospital_listModel()
    doc_list=doc_listModel()
    return render(request,'appointments.html',{"data":hospital_list,
                                               "data1":doc_list})
@csrf_exempt
def bookappointment(request):
    if request.method=="POST":
        h_name=request.POST["hospitalname"]
        d_name=request.POST["doctorname"]
        dept=request.POST["deptname"]
        date=request.POST["date"]
        time=request.POST["time"]
        rid=appointmentModel(h_name,d_name,dept,date,time)
        return HttpResponse(rid)
@csrf_exempt
def manage_appointment(request):
    getAppointmentDetails=getAppointmentDetailsModel()
    return render(request,'manage_appointment.html',{"data2":getAppointmentDetails})

#doctor
@csrf_exempt
def doctorlogin(request):
    user=request.POST["username"]
    password=request.POST["pas"]
    checkuserExist=d_checkuserModel(user,password)

    if checkuserExist >= 1:
        request.session['user_contact']=user
        return HttpResponseRedirect('/d_dashboard/')
    else:
        return render(request,'doctorLogin.html',{"message":"User does not exist"})
@csrf_exempt
def d_dashboard(request):
    userName=request.session['user_contact']

    if 'user_contact' in request.session:
        return render(request,'doctorDashboard.html')
    else:
        return HttpResponseRedirect('/doctorlog/')
@csrf_exempt
def d_confirm(request):
    user=request.POST["username"]
    checkuserExist=df_checkuserModel(user)

    if checkuserExist >= 1:
        request.session['user_contact']=user
        return HttpResponseRedirect('/d_editpass/')
    else:
        return render(request,'doctorLogin.html',{"message":"User does not exist"})
@csrf_exempt
def d_editpass(request):
    user=request.session['user_contact']
    if 'user_contact' in request.session:
        return render(request,'dchangePass.html')
    else:
        return render(request,'dforgotpass.html',{"message":"Invalid username"})
@csrf_exempt
def d_changepass(request):
    if request.method=="POST":
        d_password=request.POST["pass"]
        username = request.session['user_contact']
        d_updatepassModel(d_password,username)
        return render(request,'dchangePass.html',{"message":"your password has been changed successfully"})


   


    
