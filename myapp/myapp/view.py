from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    response = HttpResponse()
    response.write("Akhil HH")
    response.status_code = 400
    return response

def redirectExample(request):
    '''
    redirect example
    '''
    return HttpResponseRedirect('/home')
