from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Project
from django.core.mail import send_mail, BadHeaderError
from portfolio.settings import EMAIL_HOST_USER



# Create your views here.





def home(request):
    project = Project.objects.all()[:3]
    # if request.method == 'POST':
    #         name = request.POST['sender-name']
    #         from_email = request.POST['from-email']
    #         message = request.POST['from-message']
    #         message_sent = 'Your message was sent'
    #         sent = "Thank you. I got you Email"
    #         error = "Please check the form"
    #         missing_email = " "
    #
    #         if from_email == missing_email:
    #             return render(request, 'projects/home.html', {"error":error}, {'project': project})
    #         else:
    #
    #             try:
    #                 send_mail([from_email, name], message, from_email, [EMAIL_HOST_USER])
    #             except BadHeaderError:
    #                 return HttpResponse('Invalid header found.')
    #         return render(request, 'projects/home.html',   {'project': project},)
    return render(request, 'projects/home.html', {'project': project})


def sendemail(request):
    if request.method == 'POST':
        name = request.POST['senderName']
        from_email = request.POST['email']
        message = request.POST['fromMessage']

        try:
            send_mail([from_email, name], message, from_email, [EMAIL_HOST_USER])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    return HttpResponse()




#
# def contact(request):
#     project = Project.objects.all()[:3]
#     if request.method == 'POST':
#             name = request.POST['sender-name']
#             from_email = request.POST['from-email']
#             message = request.POST['from-message']
#             message_sent = 'Your message was sent'
#             error = "Please check the form"
#             missing_email = ""
#             if from_email == missing_email:
#                 return render(request, 'projects/home.html', {"error":error})
#             else:
#
#                 try:
#                     send_mail([from_email, name], message, from_email, [EMAIL_HOST_USER])
#                 except BadHeaderError:
#                     return HttpResponse('Invalid header found.')
#             return render(request, 'projects/home.html', {'message_sent':message_sent} )
#     return render(request, 'projects/home.html', {'project': project})
