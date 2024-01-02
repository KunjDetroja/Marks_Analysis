from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from .models import *
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
import matplotlib.pyplot as plt
from .forms import Marks
from django.urls import reverse
import base64
from io import BytesIO

def main(request):
    return render ( request , 'main.html' )

def home(request):
    searchTerm1 = request.GET.get('search1')
    searchTerm2 = request.GET.get('search2')
    Filter = request.GET.get('filter')
    Order = request.GET.get('order')
    Sort = request.GET.get('sort')
    Norder = ''
    if Sort == '0' and Order:
        Norder = '-'+Order
    if searchTerm1 or searchTerm2:
        if searchTerm1 == "":
            searchTerm1 = searchTerm2
        if searchTerm2 == "":
            searchTerm2 = searchTerm1
    if Order:
        if searchTerm1 or searchTerm2:
            if 'All' == Filter:
                marks = Marksheet.objects.filter(Name__icontains=searchTerm1).order_by(
                    Order) | Marksheet.objects.filter(Div__icontains=searchTerm1).order_by(
                    Order) | Marksheet.objects.filter(Roll_No__icontains=searchTerm1).order_by(
                    Order) | Marksheet.objects.filter(Mentor__icontains=searchTerm1).order_by(
                    Order) | Marksheet.objects.filter(Enrollment__icontains=searchTerm1).order_by(
                    Order) | Marksheet.objects.filter(Branch__icontains=searchTerm1).order_by(Order)|Marksheet.objects.filter(Name__icontains=searchTerm2).order_by(
                    Order) | Marksheet.objects.filter(Div__icontains=searchTerm2).order_by(
                    Order) | Marksheet.objects.filter(Roll_No__icontains=searchTerm2).order_by(
                    Order) | Marksheet.objects.filter(Mentor__icontains=searchTerm2).order_by(
                    Order) | Marksheet.objects.filter(Enrollment__icontains=searchTerm2).order_by(
                    Order) | Marksheet.objects.filter(Branch__icontains=searchTerm2).order_by(Order)
            elif 'Name' == Filter:
                marks = Marksheet.objects.filter(
                    Name__icontains=searchTerm1).order_by(Order) | Marksheet.objects.filter(
                    Name__icontains=searchTerm2).order_by(Order)
            elif 'Div' == Filter:
                marks = Marksheet.objects.filter(
                    Div__icontains=searchTerm1).order_by(Order)|Marksheet.objects.filter(
                    Div__icontains=searchTerm2).order_by(Order)
            elif 'Roll_No' == Filter:
                marks = Marksheet.objects.filter(
                    Roll_No__icontains=searchTerm1).order_by(Order)|Marksheet.objects.filter(
                    Roll_No__icontains=searchTerm2).order_by(Order)
            elif 'Mentor' == Filter:
                marks = Marksheet.objects.filter(
                    Mentor__icontains=searchTerm1).order_by(Order)|Marksheet.objects.filter(
                    Mentor__icontains=searchTerm2).order_by(Order)
            elif 'Enrollment' == Filter:
                marks = Marksheet.objects.filter(
                    Enrollment__icontains=searchTerm1).order_by(Order)|Marksheet.objects.filter(
                    Enrollment__icontains=searchTerm2).order_by(Order)
            elif 'Branch' == Filter:
                marks = Marksheet.objects.filter(
                    Branch__icontains=searchTerm1).order_by(Order)|Marksheet.objects.filter(
                    Branch__icontains=searchTerm2).order_by(Order)
        else:
            marks = Marksheet.objects.all().order_by(Order)

    else:
        marks = Marksheet.objects.all().order_by("Roll_No")
    if Sort == '0' and Order:
        marks = marks.order_by(Norder)
    return render(request, 'home.html', {'marks': marks, 'Filter': Filter, 'Order': Order, 'Norder': Norder})
    # return HttpResponse('<h1>Welcome to Home Page</h1>')


def detail(request, marks_id):
    student = Marksheet.objects.all()
    marks = get_object_or_404(Marksheet, pk=marks_id)
    Test = request.GET.get('test')
    Subject = request.GET.get('subject')
    test1 = 0
    test2 = 0
    test3 = 0
    test4 = 0
    Title = ''
    rank = 1
    if Subject == 'All':
        Title = ''
        rank = 1
        if Test == 'All':
            dm = marks.DM_T1+marks.DM_T2+marks.DM_T3+marks.DM_T4
            coa = marks.COA_T2+marks.COA_T1+marks.COA_T3+marks.COA_T4
            toc = marks.TOC_T2+marks.TOC_T1+marks.TOC_T3+marks.TOC_T4
            fsd = marks.FSD_2_T2+marks.FSD_2_T1+marks.FSD_2_T3+marks.FSD_2_T4
            fcsp = marks.FCSP_2_T2+marks.FCSP_2_T1+marks.FCSP_2_T3+marks.FCSP_2_T4
            for i in range(len(student)):
                dms = student[i].DM_T1+student[i].DM_T2+student[i].DM_T3+student[i].DM_T4
                coas = student[i].COA_T2+student[i].COA_T1+student[i].COA_T3+student[i].COA_T4
                tocs = student[i].TOC_T2+student[i].TOC_T1+student[i].TOC_T3+student[i].TOC_T4
                fsds = student[i].FSD_2_T2+student[i].FSD_2_T1+student[i].FSD_2_T3+student[i].FSD_2_T4
                fcsps = student[i].FCSP_2_T2+student[i].FCSP_2_T1+student[i].FCSP_2_T3+student[i].FCSP_2_T4
                if ( dms+coas+tocs+fsds+fcsps> dm+coa+toc+fsd+fcsp):
                    rank += 1
            Title = 'All Test Marks(Out of 100) Rank: ' + str(rank) + '/' + str(len(student))

        elif Test == 'T2':
            dm = marks.DM_T2
            coa = marks.COA_T2
            toc = marks.TOC_T2
            fsd = marks.FSD_2_T2
            fcsp = marks.FCSP_2_T2
            for i in range(len(student)):
                if (student[i].DM_T2+student[i].COA_T2+student[i].TOC_T2+student[i].FSD_2_T2+student[i].FCSP_2_T2 > dm+coa+toc+fsd+fcsp):
                    rank += 1
            Title = 'T2 Marks(Out of 25) Rank: ' + str(rank) + '/' + str(len(student))
        elif Test == 'T3':
            dm = marks.DM_T3
            coa = marks.COA_T3
            toc = marks.TOC_T3
            fsd = marks.FSD_2_T3
            fcsp = marks.FCSP_2_T3
            for i in range(len(student)):
                if (student[i].DM_T3+student[i].COA_T3+student[i].TOC_T3+student[i].FSD_2_T3+student[i].FCSP_2_T3 > dm+coa+toc+fsd+fcsp):
                    rank += 1
            Title = 'T3 Marks(Out of 25) Rank: ' + str(rank) + '/' + str(len(student))
        elif Test == 'T4':
            dm = marks.DM_T4
            coa = marks.COA_T4
            toc = marks.TOC_T4
            fsd = marks.FSD_2_T4
            fcsp = marks.FCSP_2_T4
            for i in range(len(student)):
                if (student[i].DM_T4+student[i].COA_T4+student[i].TOC_T4+student[i].FSD_2_T4+student[i].FCSP_2_T4 > dm+coa+toc+fsd+fcsp):
                    rank += 1
            Title = 'T4 Marks(Out of 25) Rank: ' + str(rank) + '/' + str(len(student))
        else:
            dm = marks.DM_T1
            coa = marks.COA_T1
            toc = marks.TOC_T1
            fsd = marks.FSD_2_T1
            fcsp = marks.FCSP_2_T1
            for i in range(len(student)):
                if (student[i].DM_T1+student[i].COA_T1+student[i].TOC_T1+student[i].FSD_2_T1+student[i].FCSP_2_T1 > dm+coa+toc+fsd+fcsp):
                    rank += 1
            Title = 'T1 Marks(Out of 25) Rank: ' + \
                str(rank) + '/' + str(len(student))
    elif Subject == 'DM':
        test1 = marks.DM_T1
        test2 = marks.DM_T2
        test3 = marks.DM_T3
        test4 = marks.DM_T4
        for i in range(len(student)):
            if (student[i].DM_T1+student[i].DM_T2+student[i].DM_T3+student[i].DM_T4 > test1+test2+test3+test4):
                rank += 1
        Title = "DM Marks(Out of 25) Rank: " + str(rank) + \
            '/' + str(len(student))
    elif Subject == 'TOC':
        test1 = marks.TOC_T1
        test2 = marks.TOC_T2
        test3 = marks.TOC_T3
        test4 = marks.TOC_T4
        for i in range(len(student)):
            if (student[i].TOC_T1+student[i].TOC_T2+student[i].TOC_T3+student[i].TOC_T4 > test1+test2+test3+test4):
                rank += 1
        Title = "TOC Marks(Out of 25) Rank: " + \
            str(rank) + '/' + str(len(student))
    elif Subject == 'COA':
        test1 = marks.COA_T1
        test2 = marks.COA_T2
        test3 = marks.COA_T3
        test4 = marks.COA_T4
        for i in range(len(student)):
            if (student[i].COA_T1+student[i].COA_T2+student[i].COA_T3+student[i].COA_T4 > test1+test2+test3+test4):
                rank += 1
        Title = "COA Marks(Out of 25) Rank: " + \
            str(rank) + '/' + str(len(student))
    elif Subject == 'FSD':
        test1 = marks.FSD_2_T1
        test2 = marks.FSD_2_T2
        test3 = marks.FSD_2_T3
        test4 = marks.FSD_2_T4
        for i in range(len(student)):
            if (student[i].FSD_2_T1+student[i].FSD_2_T2+student[i].FSD_2_T3+student[i].FSD_2_T4 > test1+test2+test3+test4):
                rank += 1
        Title = "FSD-2 Marks(Out of 25) Rank: " + \
            str(rank) + '/' + str(len(student))
    elif Subject == 'FCSP':
        test1 = marks.FCSP_2_T1
        test2 = marks.FCSP_2_T2
        test3 = marks.FCSP_2_T3
        test4 = marks.FCSP_2_T4
        for i in range(len(student)):
            if (student[i].FCSP_2_T1+student[i].FCSP_2_T2+student[i].FCSP_2_T3+student[i].FCSP_2_T4 > test1+test2+test3+test4):
                rank += 1
        Title = "FCSP-2 Marks(Out of 25) Rank: " + \
            str(rank) + '/' + str(len(student))

    def addlabels(x, y):
        for i in range(len(x)):
            plt.text(i-0.1, y[i]+0.2, y[i])

    def get_graph1():
        data1 = {'DM': dm, 'COA': coa, 'TOC': toc,
                 'FSD-2': fsd, 'FCSP-2': fcsp}
        c = ['Blue', 'Blue', 'Blue', 'Blue', 'Blue']
        courses1 = list(data1.keys())
        values1 = list(data1.values())
        for i in range(len(values1)):
            if int(values1[i]) < 9:
                c[i] = 'Red'
        plt.figure(figsize=(10, 5))
        plt.bar(courses1, values1, color=c, width=0.4)
        addlabels(courses1, values1)
        plt.xlabel("Subjects")
        plt.ylabel("Marks")
        plt.title(Title)
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        return string.decode('utf-8')

    def get_graph2():
        c = ['Blue', 'Blue', 'Blue', 'Blue']
        data2 = {'T1': test1, 'T2': test2, 'T3': test3, 'T4': test4}
        courses2 = list(data2.keys())
        values2 = list(data2.values())
        for i in range(len(values2)):
            if int(values2[i]) < 9:
                c[i] = 'Red'
        plt.figure(figsize=(10, 5))
        plt.bar(courses2, values2, color=c, width=0.4)
        addlabels(courses2, values2)
        plt.xlabel("Tests")
        plt.ylabel("Marks")
        plt.title(Title)
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        return string.decode('utf-8')
    if Subject == "All":
        graph = get_graph1()
    else:
        graph = get_graph2()
    marks = get_object_or_404(Marksheet, pk=marks_id)
    return render(request, 'detail.html', {'marks': marks, 'graph': graph, "Rank": rank})


def marksupdate(request, pk):
    student = Marksheet.objects.get(pk=pk)
    if request.method == 'POST':
        form = Marks(request.POST, instance=student)
        if form.is_valid():
            form.save()
            detail_url = reverse('detail', args=[pk])
            return redirect(detail_url)
    else:
        form = Marks(instance=student)
    return render(request, 'updateform.html', {'form': form, 'pk': pk, 'Name': student.Name})


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request,'signup.html',{'form':UserCreationForm,'error':'Username already taken. Choosenew username.'})
        else:
            return render(request, 'signup.html',{'form':UserCreationForm,'error':'Passwords do not match'})

def loginacc(request):
    if request.method == 'GET':
        return render(request, 'login.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'login.html',{'form': AuthenticationForm(),'error': 'username and password donot match'})
        else:
            login(request,user)
            return redirect('home')
        
def logoutacc(request):
    logout(request)
    return redirect('main')

def search(request):
    if request.method == 'GET':
        search = request.GET.get('Roll_No')
        if search:
            detail_url = reverse('detail', args=[search])
            return redirect(detail_url)
        else:
            return render(request, 'search.html')