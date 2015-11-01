from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json
import base64
from models import *
import random,hashlib

def test(request):
    ret_method = dict()
    ret_method['message']="hey";
    return HttpResponse(json.dumps(ret_method), content_type="application/json")


@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            if 'username' in request.POST:
                username = request.POST['username']
                password = request.POST['password']
            else:
                data = json.loads(request.body)
                username = data['username']
                password = data['password']
            try:
                dataFields = Users.objects.get(username=username,password=hashlib.sha512(password).hexdigest())
                token=hashlib.sha512(username+str(datetime.datetime.now())+str(random.randint(00000,99999))).hexdigest()
                id=dataFields.user_id
                try:
                    tokens = TokenUsers.objects.create(user_id=id,
                                                               token=token,created=datetime.datetime.now().isoformat())

                    ret = dict()
                    ret['message'] = 'login successfull'
                    ret['error_code'] = '000'
                    ret['success'] = 'True'
                    ret['token'] = tokens.token
                    ret['user_id']=tokens.user_id
                    ret['created_at']=tokens.created
                    return HttpResponse(json.dumps(ret), content_type="application/json")
                except:
                    ret = dict()
                    ret['message'] = 'internal server error'
                    ret['error_code'] = '500'
                    ret['success'] = 'False'
                    return HttpResponse(json.dumps(ret), content_type="application/json")
            except:
                ret = dict()
                ret['message'] = 'username or password is not correct.'
                ret['error_code'] = '103'
                ret['success'] = 'False'
                return HttpResponse(json.dumps(ret), content_type="application/json")
        except:
            ret = dict()
            ret['message'] = 'Values missing in post requests'
            ret['error_code'] = '101'
            ret['success'] = 'False'
            return HttpResponse(json.dumps(ret), content_type="application/json")
    else:
        ret = dict()
        ret['message'] = 'method not supported'
        ret['error_code'] = '102'
        ret['success'] = 'False'
        return HttpResponse(json.dumps(ret), content_type="application/json")



@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            if 'username' in request.POST:
                username = request.POST['username']
                password = request.POST['password']
                name=request.POST['name']
                email=request.POST['email']
            else:
                data = json.loads(request.body)
                username = data['username']
                password = data['password']
                name=data['name']
                email=data['email']
            flag=0
            try:
                dataFields = Users.objects.get(email=email)
                flag=flag+1
            except Users.DoesNotExist:
                flag=flag
            try:
                dataFields = Users.objects.get(username=username)
                flag=flag+2
            except Users.DoesNotExist:
                flag=flag
            ret = dict()
            if  flag==1:
                ret['message'] = 'email already exists'
                ret['error_code'] = '001'

            if  flag==2:
                ret = dict()
                ret['message'] = 'username already exists'
                ret['error_code'] = '002'

            if  flag==3:
                ret = dict()
                ret['message'] = 'email and username both already exists'
                ret['error_code'] = '003'


            if flag!=0:
                ret['success'] = 'false'
                return HttpResponse(json.dumps(ret), content_type="application/json")
            try:
                data = Users.objects.create(username=username,password=hashlib.sha512(password).hexdigest(),name=name,email=email,created=datetime.datetime.now().isoformat())
            except Exception,e:
                print e
                ret['success'] = 'false'
                ret['message'] = 'internal error'
                return HttpResponse(json.dumps(ret), content_type="application/json")
            ret = dict()
            ret['message'] = 'registration succesfull'
            ret['error_code'] = '000'
            ret['success'] = 'True'
            ret['user_id']=data.user_id
            ret['created_at']=data.created
            return HttpResponse(json.dumps(ret), content_type="application/json")

        except:
            ret = dict()
            ret['message'] = 'Values missing in post requests'
            ret['error_code'] = '101'
            ret['success'] = 'False'
            return HttpResponse(json.dumps(ret), content_type="application/json")
    else:
        ret = dict()
        ret['message'] = 'method not supported'
        ret['error_code'] = '102'
        ret['success'] = 'False'
        return HttpResponse(json.dumps(ret), content_type="application/json")



