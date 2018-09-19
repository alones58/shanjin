from django.shortcuts import render
from django.shortcuts import HttpResponse
from duty import models

from qcloudsms_py import SmsMultiSender  #短信群发
from qcloudsms_py.httpclient import HTTPError  #腾讯云短信
# Create your views here.


def index(request):
    #return HttpResponse('helllllllo')
    user_list = models.DutyUser.objects.all()
    return render(request, 'index.html', {"data": user_list})


def sms(request):
    appid = 1400099984
    appkey = "ca6d8085b795710f985517b9d7cb66d8"
    template_id = 190316
    sms_sign = "山金矿业"

    dept = models.Dept.objects.all()
    userlist = models.DutyUser.objects.all()

    if request.method == "POST":
        phone_numbers = request.POST.getlist("check_box_list",None)
        print(phone_numbers)
        dx1 = request.POST.getlist("dx", '')
        params = []
        params.append(dx1)
        print(params)
        #短信代码
        msender = SmsMultiSender(appid, appkey)
        try:
            pass
            # result = msender.send_with_param(86, phone_numbers,template_id, params, sign=sms_sign, extend="", ext="")
        except HTTPError as e:
            print(e)
        except Exception as e:
            print(e)
        # print(result)
    return render(request, 'index.html', locals())


# def userlist(request):
#     user_list = models.User.objects.all()
#     return request(request, 'index.html', {"userlist": user_list})
