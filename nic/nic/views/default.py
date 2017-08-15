from pyramid.response import Response
from pyramid.view import view_config
from pyramid.renderers import render_to_response

from sqlalchemy.exc import DBAPIError
import os
import uuid
import shutil
import datetime


from pyramid.httpexceptions import (
    HTTPForbidden,
    HTTPFound,
    HTTPNotFound,
    )
from ..models import login, savGrossAmt, savingsMax, AssessA, AssessB, employee_master,DesigTable, employee_salary, UserRoles, RoleMap, UserView, ProofStatus, savingsdoc

username = 0
stype = ''
amount = 0
camefrom = 0
rem = 150000
sav = 0
var1 = 0
var2 = 0
c = 0
date = ''

def fun(amnt):
    global rem
    if amount <= rem:
        rem -= amnt
        return True
    else:
        return False




@view_config(route_name='home', renderer='../templates/pages/page1.pt')
def home(request):
    return{}
  #  username = request.params['username']
   # pwd = request.params['pswd']
    #return Response(username + pwd)


@view_config(route_name='login', renderer='../templates/pages/page2.pt')
def Login(request):
    global username
    for key in request.params:
        print( key + '\t' + request.params[key] + '\n\n\n')
    username = request.params['username']
    pwd = request.params['pswd']
    query = request.dbsession.query(login)
    
    name = query.filter(login.id == username, login.password == pwd).first()
    if name is None:
        raise HTTPForbidden
    query = request.dbsession.query(UserRoles)
    
    name = query.filter(UserRoles.id == username).all()
    user = False
    ddo = False
    for i in name:
        if i.role_id == 1:
            user = True
        if i.role_id == 2:
            ddo = True
    
    if ddo == True:
        return render_to_response('../templates/pages/page2a.pt', {'username':username}, request=request)
    return render_to_response('../templates/pages/page2.pt', {'username':username}, request=request)
    
    

@view_config(route_name='submit1', renderer='../templates/pages/page3.pt')
def submit1(request):
    #print('hi')
    query = request.dbsession.query(employee_master)
    
    obj = query.filter(employee_master.id == username).first()
    if obj is None:
        raise HTTPForbidden
    n = obj.name
    addr = obj.address
    query = request.dbsession.query(DesigTable)
    query = query.order_by(DesigTable.date.desc())
    name1 = query.filter(DesigTable.id == username).first()
    des = name1.designation
    pop = name1.place_of_posting
    return{'msg':'', 'name': n, 'id':username, 'desig':des , 'post':pop, 'address':addr}

@view_config(route_name='submit2')
def submit2(request):
    global var1, var2, c
    d = request.params
    
    flag = True
    workflag = True
    #if request.params["work"] == "yes":
    #    if d["org"] == "" or d["addr"] == "":
    #        workflag = False 
    stdate = '2015-03-31'
    enddate = '2016-04-01'
    query = request.dbsession.query(employee_salary)
    name = query.filter(employee_salary.id == username, employee_salary.date > stdate, employee_salary.date < enddate).all() 
    count = 0
    totsal= 0
    ta = 0
    c = 0
    for i in name:
        totsal += int(i.salary) + i.da
        ta += i.ta
        count+=1
        
    print('##########')
    diff = totsal - ta
    print(count, totsal, ta, diff )
    
    #query1 = query(func.count(employee_master.id))
    
    if count < 12:
        c = 12 - count
    
    totsal += c * int(name[0].salary)
    print('#######')
    print(name[0].salary)
      
    for key in d:
        if key != 'org' and key != 'addr':
            if d[key] == "":
                flag = False
    var1 = totsal
    var2 = ta
    if flag and workflag:
        return render_to_response('../templates/pages/page4.pt', {'msg':'', 'amt' : '', 'ainc': var1 , 'tra': var2}, request=request)
    return render_to_response('../templates/pages/page3.pt', {'msg':'Please fill all the fields'}, request=request)
    
@view_config(route_name='submit3')
def submit3(request):
    global var1, var2
    d = {}
    for key in request.params:
        d[key] = request.params[key]
        print( key + '\t' + request.params[key] + '\n\n\n')
    #print("##########")
    for key in d:
        print(key + '\t' + d[key] + '\n\n\n')
    flag = True  
    #print(username)  
    #if d['k'] == "yes":
    #    if d["rent"] == "" or d["hra"] == "":
    #        flag = False 
    for key in d:
        if key == 'aincome' or key == 'ptax':
            if d[key] == "":
                flag = False
    
    
    for key in d:
        if d[key] == "":
            d[key] = 0  
    #print("####")
    grossincome = int(d['aincome']) + int(d['oincome']) - int(d['ta'])  - int(d['ptax']) + int(d['hincome']) 
    #print(username, grossincome)
    query = request.dbsession.query(savGrossAmt)
    obj = query.filter(savGrossAmt.id == username, savGrossAmt.year == 2015).first()
    #print(obj.gamount)
    obj.gamount = grossincome
    request.dbsession.add(obj)
    if flag:
        return render_to_response('../templates/pages/page5.pt', {}, request=request)
    return render_to_response('../templates/pages/page4.pt', {'msg':'Please fill all the fields', 'amt' : grossincome, 'ainc': var1, 'tra': var2}, request=request)

@view_config(route_name='submit3a', renderer='../templates/pages/page5a.pt')
def submit3a(request):
    global amount, at, sav
#    for key in request.params:
#        print( key + '\t' + request.params[key] + '\n\n\n')
    amount = int(request.params['amt'])
    docno = int(request.params['docno'])
    tdy = datetime.date.today()
    print ("%%%%%%%%%%%%%%%%")
    print (tdy,amount,docno)
    print('amount is ',amount)
    
    # ``filename`` contains the name of the file in string format.
    #
    # WARNING: this example does not deal with the fact that IE sends an
    # absolute file *path* as the filename.  This example is naive; it
    # trusts user input.

    filename = request.POST['jpg'].filename

    # ``input_file`` contains the actual file data which needs to be
    # stored somewhere.
	
    input_file = request.POST['jpg'].file
    ph_id = uuid.uuid4()
    print (ph_id)

    # Note that we are generating our own filename instead of trusting
    # the incoming filename since that might result in insecure paths.
    # Please note that in a real application you would not use /tmp,
    # and if you write to an untrusted location you will need to do
    # some extra work to prevent symlink attacks.

    file_path = os.path.join('/media/seenivas/Seeni', '%s.jpg' % ph_id)
    print (file_path)
    ph_path = "/media/seenivas/Seeni/"+str(ph_id)
    #print (ph_path)
    # We first write to a temporary file to prevent incomplete files from
    # being used.
	
    

    # Finally write the data to a temporary file
    input_file.seek(0)
    with open(file_path, 'wb') as output_file:
        shutil.copyfileobj(input_file, output_file)

    # Now that we know the file has been fully saved to disk move it into place.

    


    
    
    #print(request.params)
#    for key in request.params:
#        print( key + '\t' + request.params[key] + '\n\n\n')
    query = request.dbsession.query(savingsMax)
    obj = query.filter(savingsMax.year == 2015).first()
    #print(obj.c)
    a = int(obj.checkmax(stype)) 
    if stype == 'c':
        
        if fun(amount):
            sav += amount
            #print(a)
            
            
            obj = savingsdoc(phpath=ph_path,document_no=docno,savings_amount=amount,submitted_date=tdy,userid=username)
            request.dbsession.add(obj)
            return render_to_response('../templates/pages/page5a.pt', {}, request=request)
        else:
            a = rem       
    elif amount <= a:   
        sav += amount
        obj = savingsdoc(phpath=ph_path,document_no=docno,savings_amount=amount,submitted_date=tdy,userid=username,status=0)
        request.dbsession.add(obj)
        return render_to_response('../templates/pages/page5a.pt', {}, request=request)
    m = 'Amount exceeds maximum limit.Please enter a value below ' + str(a)
    return render_to_response('../templates/pages/page' + camefrom +'.pt', {'msg' : m }, request=request)
@view_config(route_name='submit4', renderer='../templates/pages/page6.pt')
def submit4(request):
    global stype, camefrom
    stype = 'c'
    camefrom = '6'
      
	
    return{'msg' : ''}
    
@view_config(route_name='submit4a', renderer='../templates/pages/page6a.pt')
def submit4a(request):
    global stype, camefrom
    stype = 'c'
    camefrom = '6a'
    return{'msg' : ''}

@view_config(route_name='submit4c', renderer='../templates/pages/page6c.pt')
def submit4c(request):
    global stype, camefrom
    stype = 'c'
    camefrom = '6c'
    return{'msg' : ''}
    
    
@view_config(route_name='submit4d', renderer='../templates/pages/page6d.pt')
def submit4d(request):
    global stype, camefrom
    stype = 'c'
    camefrom = '6d'
    return{'msg' : ''}
        
@view_config(route_name='submit4e', renderer='../templates/pages/page6e.pt')
def submit4e(request):
    global stype, camefrom
    stype = 'c'
    camefrom = '6e'
    return{'msg' : ''}
    
@view_config(route_name='submit4f', renderer='../templates/pages/page6f.pt')
def submit4f(request):
    global stype, camefrom
    stype = 'c'
    camefrom = '6f'
    return{'msg' : ''}
        
@view_config(route_name='submit4g', renderer='../templates/pages/page6g.pt')
def submit4g(request):
    global stype, camefrom
    stype = 'c'
    camefrom = '6g'
    return{'msg' : ''}    
    
@view_config(route_name='submit4h', renderer='../templates/pages/page6h.pt')
def submit4h(request):
    global stype, camefrom
    stype = 'd1'
    camefrom = '6h'
    return{'msg' : ''}
    
@view_config(route_name='submit4i', renderer='../templates/pages/page6i.pt')
def submit4i(request):
    global stype, camefrom
    stype = 'dd'
    camefrom = '6i'
    return{'msg' : ''}        
    
@view_config(route_name='submit4k', renderer='../templates/pages/page6k.pt')
def submit4k(request):
    global stype, camefrom
    stype = 'e'
    camefrom = '6k'
    return{'msg' : ''}
 
@view_config(route_name='submit4l', renderer='../templates/pages/page6l.pt')
def submit4l(request):
    global stype, camefrom
    stype = 'g'
    camefrom = '6l'
    return{'msg' : ''}
    
@view_config(route_name='submit4m', renderer='../templates/pages/page6m.pt')
def submit4m(request):
    global stype, camefrom
    stype = 'u1'
    camefrom = '6m'
    return{'msg' : ''} 
    
@view_config(route_name='submit5', renderer='../templates/pages/finalpage.pt')
def submit5(request):
    global sav, c
    query = request.dbsession.query(savGrossAmt)
    obj = query.filter(savGrossAmt.id == username, savGrossAmt.year == 2015).first()
    inc = obj.gamount
    inc -= sav
    query = request.dbsession.query(AssessB)
    obj = query.filter(AssessB.year == '2015-2016').first()
    tds = obj.calculateTds(inc, c)
	
    #return Response(str(inc) + '\t' + str(tds))  
    return {'income':inc,'tds':tds}
    
@view_config(route_name='ddo1', renderer='../templates/pages/page7.pt')
def ddo1(request):  

    return {}
    
    
@view_config(route_name='ddo2', renderer='../templates/pages/testpage.pt')
def ddo2(request):
    #print(year) 
    year = request.params['year']
    date = str(year+'-12-31')
    print('#@$@#$@#$#@'+ date)
    query = request.dbsession.query(UserRoles)
    allusers = query.filter(UserRoles.role_id == 1).all()
    #for i in name:
    #	z = request.dbsession.query(savingsdoc).filter(savingsdoc.userid == i.id,savingsdoc.submitted_date < '2016-12-31' ).first()
    length = len(allusers)
    return {'all_users':allusers,'length':length}
    """p_id = str(obj.proof_id)
    e_id = str(obj.emp_id)
    d_id = str(obj.deduction_id)
    am = str(obj.amount)
    date = str(obj.date)
    status = str(obj.status)
    return Response(p_id + '\t\t\t' + e_id + '\t\t\t' + d_id + '\t\t\t' + am + '\t\t\t' + date + '\t\t\t' + status)"""
    
@view_config(route_name='ddo3', renderer='../templates/pages/testpage1.pt')
def ddo3(request):
    usertag = request.params['value1']  
    #print('@#$#@%^#$@%#@#'+usertag)
    obj=request.dbsession.query(savingsdoc).filter(savingsdoc.userid == usertag,savingsdoc.submitted_date < 'date',savingsdoc.status == 0 ).all()
    ph=obj[1].phpath+".jpg" 
	
    input_file=open('im.jpg','wb+')
    output_file=open(ph,'rb')
    shutil.copyfileobj(output_file, input_file)
    input_file.close()
    #input_file=open('im.jpg','rb')
    print(output_file)
    print('#$@#%@#%'+ph)   
    #for i in obj:
     #   print(i.phpath)
    #print(obj.phpath)'''
    return {'userdocs':obj,'ph':output_file}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
