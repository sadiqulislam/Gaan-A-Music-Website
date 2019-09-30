from django.shortcuts import render

def index(req):
    context= {

    }

    return render(req,'music/index.html',context=context)