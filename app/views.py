from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from app.models import *
def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='cricket')
    #LOW=Webpage.objects.get(topic_name='kabaddi')
    LOW=Webpage.objects.exclude(topic_name='cricket')
    LOW=Webpage.objects.all()[:2:]
    LOW=Webpage.objects.all().order_by(Length('name'))
    #LOW=Webpage.objects.all()
    LOW=Webpage.objects.all().order_by(Length('topic_name').desc())


    d={'webpages':LOW}
    return render(request,'display_webpage.html',d)




def display_access(request):
    LOA=AccessRecord.objects.all()

    LOA=AccessRecord.objects.filter(date__gt='2023-03-12')

    LOA=AccessRecord.objects.filter(date__gte='2023-03-12')

    LOA=AccessRecord.objects.filter(date__lt='2023-03-12')

    LOA=AccessRecord.objects.filter(date__lte='2023-03-12')
    d={'access':LOA}
    return render(request,'display_access.html',d)