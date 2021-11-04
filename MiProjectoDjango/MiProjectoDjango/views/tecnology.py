from django.http import HttpResponse
import datetime
from django.template import loader
from django.template import Template, Context

def tecnology(request):
    year = datetime.datetime.now().year
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    hour = datetime.datetime.now().strftime("%X")

    fecha = "%s/%s/%s a las %s" %(day, month, year, hour)

    external_doc = loader.get_template('tecnology.html')
    document = external_doc.render({'fecha': fecha})
    return HttpResponse(document)