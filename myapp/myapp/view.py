from django.http import HttpResponse

def home(request):
    response = HttpResponse()
    response.write("Akhil HH")
    response.status_code = 400
    return response