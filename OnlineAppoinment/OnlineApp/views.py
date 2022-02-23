from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import *
from .forms import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


# Create your views here.

name = [' ']


def sendmail_confirm(name,purp,date,depart,mail):
    print('goods')
    var = 'Good Day MR/MS '+ name + '\n'+ '\n' + 'This is to confirm your appointment for '+ purp + ' on ' + str(date) + '\n' + '\n' + 'If you have any queries feel free to reply to this email.'+'\n'+ '\n' +'Thank You!!!'+'\n'+depart+'\n'+'TUP Cavite'
    message_sent = var
    subject_sent = 'TUPC ONLINE APPOINTMENT'
    recipient_sent = [mail,]
    send_mail(subject_sent, message_sent, 'tupc.online.appointment@gmail.com', recipient_sent, fail_silently=False,)
    print('goods')

def sendmail_denied(name,purp,date,depart,mail):
    print('goods')
    var = 'Good Day MR/MS '+ name + '\n'+ '\n' +  'We would like to inform you on your appointment for' + depart + ' on ' + str(date) +  '\n'+ '\n' + 'has been declined for some reason.' + '\n'+ '\n''If you have any queries feel free to reply to this email.'+'\n' + '\n' +'Thank You!!!'+'\n'+ depart +'\n'+'TUP Cavite'
    message_sent = var
    subject_sent = 'TUPC ONLINE APPOINTMENT'
    recipient_sent = [mail,]
    send_mail(subject_sent, message_sent, 'tupc.online.appointment@gmail.com', recipient_sent, fail_silently=False,)
    print('goods')



def oaa (request):
    getalumni = AlumniBook.objects.filter(Adep = 'Office of Academic Affairs').values()
    getstudent = StudentBook.objects.filter(Sdep = 'Office of Academic Affairs').values()
    getguardian = GuardianBook.objects.filter(Gdep = 'Office of Academic Affairs').values()

    data = {
        'alumnidata': getalumni,
        'studentdata': getstudent,
        'guardiandata': getguardian
    }
    return render (request, 'temp/oaa.html', data)

def confirm1(request,oaa_id):
    yes = AlumniBook.objects.get(id=oaa_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('oaa')
def denied1(request,oaa_id):
    yes = AlumniBook.objects.get(id=oaa_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('oaa')

def confirm2(request,oaa_id):
    yes = StudentBook.objects.get(id=oaa_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('oaa')
def denied2(request,oaa_id):
    yes = StudentBook.objects.get(id=oaa_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('oaa')

def confirm3(request,oaa_id):
    yes = GuardianBook.objects.get(id=oaa_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('oaa') 
def denied3(request,oaa_id):
    yes = GuardianBook.objects.get(id=oaa_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('oaa')

def ocr (request):
    getalumni = AlumniBook.objects.filter(Adep = 'Office of Campus Registrar').values()
    getstudent = StudentBook.objects.filter(Sdep = 'Office of Campus Registrar').values()
    getguardian = GuardianBook.objects.filter(Gdep = 'Office of Campus Registrar').values()


    data = {
        'alumnidata': getalumni,
        'studentdata': getstudent,
        'guardiandata': getguardian
    }

    return render (request, 'temp/ocr.html', data)

def confirm4(request,ocr_id):
    yes = AlumniBook.objects.get(id=ocr_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('ocr')
def denied4(request,ocr_id):
    yes = AlumniBook.objects.get(id=ocr_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('ocr')

def confirm5(request,ocr_id):
    yes = StudentBook.objects.get(id=ocr_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('ocr')
def denied5(request,ocr_id):
    yes = StudentBook.objects.get(id=ocr_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('ocr')

def confirm6(request,ocr_id):
    yes = GuardianBook.objects.get(id=ocr_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('ocr') 
def denied6(request,ocr_id):
    yes = GuardianBook.objects.get(id=ocr_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('ocr')


def landingpage (request):
    print('landingpage')
    return render (request, 'temp/landingpage.html')

def alumni (request): 
    getalumni = AlumniBook.objects.filter(Adep = 'Alumni Office').values()
    getstudent = StudentBook.objects.filter(Sdep = 'Alumni Office').values()
    getguardian = GuardianBook.objects.filter(Gdep = 'Alumni Office').values()


    data = {
        'alumnidata': getalumni,
        'studentdata': getstudent,
        'guardiandata': getguardian
    }

    return render (request, 'temp/alumni.html', data)
def confirm7(request,alumni_id):
    yes = AlumniBook.objects.get(id=alumni_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('alumni')
def denied7(request,alumni_id):
    yes = AlumniBook.objects.get(id=alumni_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('alumni')

def confirm8(request,alumni_id):
    yes = StudentBook.objects.get(id=alumni_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('alumni')
def denied8(request,alumni_id):
    yes = StudentBook.objects.get(id=alumni_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('alumni')

def confirm9(request,alumni_id):
    yes = GuardianBook.objects.get(id=alumni_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('alumni') 
def denied9(request,alumni_id):
    yes = GuardianBook.objects.get(id=alumni_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('alumni')

def adminlogin (request):
    sell = AccDepartment.objects.all()
    len1 = len(sell)
    print(sell)
    print('-----------------')
    if len1 == 0:
        print('NO DATA')
    else:
        if request.method == 'POST':
            sel = request.POST.get('choice')
            pas = request.POST.get('passwords')
            print(sel)
            print(pas)
            if pas == '':
                print('change')
                return redirect ('adminlogin')
            else:
                for i in sell:
                    if i.Department == sel and i.Depass == pas:
                        if i.Department == 'Office of Academic Affairs':
                            return redirect ('oaa')
                        elif i.Department == 'Office of Campus Registrar':
                            return redirect ('ocr')
                        elif i.Department == 'Office of the Guidance Services':
                            return redirect ('ogs')
                        elif i.Department == 'Campus Library':
                            return redirect ('library')
                        elif i.Department == 'Office of Health Services':
                            return redirect ('ohs')
                        elif i.Department == 'University Information Technology Center':
                            return redirect ('uitc')
                        elif i.Department == 'University Student Government':
                            return redirect ('usg')
                        elif i.Department == 'Office of Student Affairs':
                            return redirect ('osa')
                        elif i.Department == 'Alumni Office':
                            return redirect ('alumni')
                        elif i.Department == 'Security Department':
                            return redirect ('securitydept')
                        
                
    return render (request, 'temp/adminlogin.html')

def bookappointment (request):
    return render (request, 'temp/bookappointment.html')

def library (request):
    getalumni = AlumniBook.objects.filter(Adep = 'Campus Library').values()
    getstudent = StudentBook.objects.filter(Sdep = 'Campus Library').values()
    getguardian = GuardianBook.objects.filter(Gdep = 'Campus Library').values()


    data = {
        'alumnidata': getalumni,
        'studentdata': getstudent,
        'guardiandata': getguardian
    }

    return render (request, 'temp/library.html', data)

def confirm10(request,library_id):
    yes = AlumniBook.objects.get(id=library_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('library')
def denied10(request,library_id):
    yes = AlumniBook.objects.get(id=library_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('library')

def confirm11(request,library_id):
    yes = StudentBook.objects.get(id=library_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('library')
def denied11(request,library_id):
    yes = StudentBook.objects.get(id=library_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('library')

def confirm12(request,library_id):
    yes = GuardianBook.objects.get(id=library_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('library') 
def denied12(request,library_id):
    yes = GuardianBook.objects.get(id=library_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('library')

    

def ogs (request):
    getalumni = AlumniBook.objects.filter(Adep = 'Office of the Guidance Services').values()
    getstudent = StudentBook.objects.filter(Sdep = 'Office of the Guidance Services').values()
    getguardian = GuardianBook.objects.filter(Gdep = 'Office of the Guidance Services').values()


    data = {
        'alumnidata': getalumni,
        'studentdata': getstudent,
        'guardiandata': getguardian
    }
    return render (request, 'temp/ogs.html', data)

def confirm13(request,ogs_id):
    yes = AlumniBook.objects.get(id=ogs_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('ogs')
def denied13(request,ogs_id):
    yes = AlumniBook.objects.get(id=ogs_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('ogs')

def confirm14(request,ogs_id):
    yes = StudentBook.objects.get(id=ogs_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('ogs')
def denied14(request,ogs_id):
    yes = StudentBook.objects.get(id=ogs_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('ogs')

def confirm15(request,ogs_id):
    yes = GuardianBook.objects.get(id=ogs_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('ogs') 
def denied15(request,ogs_id):
    yes = GuardianBook.objects.get(id=ogs_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('ogs')



def ohs (request):
    getalumni = AlumniBook.objects.filter(Adep = 'Office of Health Services').values()
    getstudent = StudentBook.objects.filter(Sdep = 'Office of Health Services').values()
    getguardian = GuardianBook.objects.filter(Gdep = 'Office of Health Services').values()


    data = {
        'alumnidata': getalumni,
        'studentdata': getstudent,
        'guardiandata': getguardian
    }
    return render (request, 'temp/ohs.html', data)

def confirm16(request,ohs_id):
    yes = AlumniBook.objects.get(id=ohs_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('ohs')
def denied16(request,ohs_id):
    yes = AlumniBook.objects.get(id=ohs_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('ohs')

def confirm17(request,ohs_id):
    yes = StudentBook.objects.get(id=ohs_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('ohs')
def denied17(request,ohs_id):
    yes = StudentBook.objects.get(id=ohs_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('ohs')

def confirm18(request,ohs_id):
    yes = GuardianBook.objects.get(id=ohs_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('ohs') 
def denied18(request,ohs_id):
    yes = GuardianBook.objects.get(id=ohs_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('ohs')

def osa (request):
    getalumni = AlumniBook.objects.filter(Adep = 'Office of Student Affairs').values()
    getstudent = StudentBook.objects.filter(Sdep = 'Office of Student Affairs').values()
    getguardian = GuardianBook.objects.filter(Gdep = 'Office of Student Affairs').values()


    data = {
        'alumnidata': getalumni,
        'studentdata': getstudent,
        'guardiandata': getguardian
    }
    return render (request, 'temp/osa.html', data)

def confirm19(request,osa_id):
    yes = AlumniBook.objects.get(id=osa_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('osa')
def denied19(request,osa_id):
    yes = AlumniBook.objects.get(id=osa_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('osa')

def confirm20(request,osa_id):
    yes = StudentBook.objects.get(id=osa_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('osa')
def denied20(request,osa_id):
    yes = StudentBook.objects.get(id=osa_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('osa')

def confirm21(request,osa_id):
    yes = GuardianBook.objects.get(id=osa_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('osa') 
def denied21(request,ohs_id):
    yes = GuardianBook.objects.get(id=osa_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('osa')


def securitydept (request):
    if request.method == 'POST':
        val = request.POST.get('search')
        getalumni = AlumniBook.objects.filter(Aname = val,status = 'CONFIRMED').values()
        getstudent = StudentBook.objects.filter(Sname = val, status = 'CONFIRMED').values()
        getguardian = GuardianBook.objects.filter(Ggname = val, status = 'CONFIRMED').values()
    else:
        getalumni = AlumniBook.objects.filter(status = 'CONFIRMED').values()
        getstudent = StudentBook.objects.filter(status = 'CONFIRMED').values()
        getguardian = GuardianBook.objects.filter(status = 'CONFIRMED').values()

    print(getstudent)
    print(getalumni)
    print(getguardian)

    data = {
        'alumnidata': getalumni,
        'studentdata': getstudent,
        'guardiandata': getguardian
    }
    return render (request, 'temp/securitydept.html', data)

def signupadmin (request):
    if request.method == 'POST':
        sel = request.POST.get('choice')
        pas = request.POST.get('passwords')
        print(sel)
        print(pas)
        if pas == '':
            print('change')
            return redirect ('signupadmin')
        else:
            dep = AccDepartment.objects.all()
            x = len(dep)
            if x == 0:
                s = AccDepartment(Department=sel,Depass=pas)
                s.save()
                return redirect ('adminlogin')
            else:
                for deps in dep:
                    print(deps.Department)
                    if deps.Department == sel:
                        print('INVALID')
                        return redirect ('signupadmin')
                    else:
                        s = AccDepartment(Department=sel,Depass=pas)
                        s.save()
                        return redirect ('adminlogin')

    return render (request, 'temp/signupadmin.html')

def signupstudent (request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if email == '' or pass1 == '' or pass2 == '':
            print('change')
            return redirect ('signupstudent')
        else:
            if pass1 == pass2:
                stu = AccStudent.objects.all()
                x = len(stu)
                if x == 0:
                    s = AccStudent(Semail=email,Spass=pass1)
                    s.save()
                    return redirect ('studentlogin')
                else:
                    for studs in stu:
                        if studs.Semail == email:
                            print('INVALID')
                            return redirect ('signupstudent')
                        else:
                            s = AccStudent(Semail=email,Spass=pass1)
                            s.save()
                            return redirect ('studentlogin')
            else:
                return redirect ('signupstudent')
    return render (request, 'temp/signupstudent.html')

def studentlogin (request):
    stu = AccStudent.objects.all()
    len1 = len(stu)
    if len1 == 0:
        print('NO DATA')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            pas = request.POST.get('pass')
            if pas == '' or email == '':
                print('change')
                return redirect ('studentlogin')
            else:
                for i in stu:
                    if i.Semail == email and i.Spass == pas:
                        name[0] = i.Semail
                        return redirect ('bookappointment')


    return render (request, 'temp/studentlogin.html')

def uitc (request):
    getalumni = AlumniBook.objects.filter(Adep = 'University Information Technology Center').values()
    getstudent = StudentBook.objects.filter(Sdep = 'University Information Technology Center').values()
    getguardian = GuardianBook.objects.filter(Gdep = 'University Information Technology Center').values()


    data = {
        'alumnidata': getalumni,
        'studentdata': getstudent,
        'guardiandata': getguardian
    }
    return render (request, 'temp/uitc.html', data)

def confirm22(request,uitc_id):
    yes = AlumniBook.objects.get(id=uitc_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('uitc')
def denied22(request,uitc_id):
    yes = AlumniBook.objects.get(id=uitc_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('uitc')

def confirm23(request,uitc_id):
    yes = StudentBook.objects.get(id=uitc_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('uitc')
def denied23(request,uitc_id):
    yes = StudentBook.objects.get(id=uitc_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('uitc')

def confirm24(request,uitc_id):
    yes = GuardianBook.objects.get(id=uitc_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('uitc') 
def denied24(request,uitc_id):
    yes = GuardianBook.objects.get(id=uitc_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('uitc')


def usg (request): 
    getalumni = AlumniBook.objects.filter(Adep = 'University Student Government').values()
    getstudent = StudentBook.objects.filter(Sdep = 'University Student Government').values()
    getguardian = GuardianBook.objects.filter(Gdep = 'University Student Government').values()


    data = {
        'alumnidata': getalumni,
        'studentdata': getstudent,
        'guardiandata': getguardian
    }
    return render (request, 'temp/usg.html', data)

def confirm25(request,usg_id):
    yes = AlumniBook.objects.get(id=usg_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('usg')
def denied25(request,usg_id):
    yes = AlumniBook.objects.get(id=usg_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Aname,yes.Apurp,yes.Adate,yes.Adep,yes.Amail)
    return redirect('usg')

def confirm26(request,usg_id):
    yes = StudentBook.objects.get(id=usg_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('usg')
def denied26(request,usg_id):
    yes = StudentBook.objects.get(id=usg_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Sname,yes.Spurp,yes.Sdate,yes.Sdep,yes.Smail)
    return redirect('usg')

def confirm27(request,usg_id):
    yes = GuardianBook.objects.get(id=usg_id)
    yes.status = 'CONFIRMED'
    yes.save()
    sendmail_confirm(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('usg') 
def denied27(request,usg_id):
    yes = GuardianBook.objects.get(id=usg_id)
    yes.status = 'DENIED'
    yes.save()
    sendmail_denied(yes.Ggname,yes.Gpurp,yes.Gdate,yes.Gdep,yes.Gmail)
    return redirect('usg')

def alumniform (request):
    formAlumni = alumnus(request.POST or None)
    print('change')
    if formAlumni.is_valid():
        print('change')
        formAlumni.save()

        return redirect ('bookappointment')

    context = {
        'formAlumni': formAlumni
    }
    return render (request, 'temp/alumniform.html', context)

def studentform (request): 
    formStudent = student(request.POST or None)
    if formStudent.is_valid():
        formStudent.save()
        return redirect ('bookappointment')

    context = {
        'formStudent': formStudent
    }

    return render (request, 'temp/studentform.html', context)

def guardianform (request): 
    formGuardian = guardian(request.POST or None)
    if formGuardian.is_valid():
        formGuardian.save()
        return redirect ('bookappointment')

    context = {
        'formGuardian': formGuardian
    }

    return render (request, 'temp/guardianform.html', context)


def delete1(request,sec_id):
    yes = StudentBook.objects.get(id=sec_id)
    yes.delete()
    return redirect('securitydept')

def delete2(request,sec_id):
    yes = AlumniBook.objects.get(id=sec_id)
    yes.delete()
    return redirect('securitydept')

def delete3(request,sec_id):
    yes = GuardianBook.objects.get(id=sec_id)
    yes.delete()
    return redirect('securitydept')

def refresh(request):
    
    return redirect('securitydept')

def logout(request):
    return redirect('adminlogin')



