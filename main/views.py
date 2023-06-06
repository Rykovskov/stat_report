import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .models import History
from .models import Report_tags
from .models import Values_tags
from .models import Infrastructure_sp
from .models import Roles_sp
from .models import Services_sp
from .models import Priority_tags
from .models import Trcking_tags
from .forms import ReportConfigForms
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin
from pyzabbix import ZabbixAPI
import time
import json
from .applogic import *


# Create your views here.
@xframe_options_sameorigin
def index(request):
    dt_request = datetime.datetime.now()
    Priority_tags_table = Priority_tags.objects.all()
    Trcking_tags_table = Trcking_tags.objects.all()
    Report_tag_table = Report_tags.objects.all()
    Values_tags_table = Values_tags.objects.all()
    Infrastructure_sp_table = Infrastructure_sp.objects.all()
    Services_sp_table = Services_sp.objects.all()
    history_table = History.objects.filter(
        dt_zap__year=dt_request.year,
        dt_zap__month=dt_request.month,
        dt_zap__day=dt_request.day)
    host_sp =[]
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        ReportConfigForm = ReportConfigForms(request.POST)
        print("POST recive")
        print(ReportConfigForm.is_valid())
        # check whether it's valid:
        if ReportConfigForm.is_valid():
            ReportConfigForm.save()
            return HttpResponse('<h1>Maxim Rykovskov (c)</H1>')
    else:
        ReportConfigForm = ReportConfigForms()
        host_sp = get_zabbix_host_by_tags(Trcking_tags_table)
        #--------------------------------------------------------

    context = {
        'ReportConfigForm': ReportConfigForm,
        'report_tag_table': Report_tag_table,
        'values_tags_table':Values_tags_table,
        'Infrastructure_sp_table':Infrastructure_sp_table,
        'services_sp_table': Services_sp_table,
        'priority_tags_table': Priority_tags_table,
        'trcking_tags_table': Trcking_tags_table,
        "host_sp": host_sp,
        "history_table": history_table
    }
    return render(request,'main/index.html', context)

def about(request):
    return HttpResponse('<h1>Maxim Rykovskov (c)</H1>')


def select_tag(request):
    report_tag_table = Report_tags.objects.all()
    values_tags_table = Values_tags.objects.all()
    return render(request,'main/select_tag.html', {'report_tag_tab':report_tag_table, 'values_tags_table':values_tags_table})

