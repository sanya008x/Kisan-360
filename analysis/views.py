from django.shortcuts import render
from twilio.rest import Client

# Create your views here.
from django.shortcuts import render

# Create your views here.
def season(request):
    return render(request, 'pages/season.html')
    
def send_report_via_sms():
    account_sid = 'AC9e7bc37bfa0b0e27a3ea6158ff213466'

    auth_token = '67084154965dc7ab8d1109c059740caf'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+13412095896',
            body = f'''नमस्ते, Harsh
                    उत्पाद का नाम: मक्का 🌽
                    समाप्ति तिथि: कल, 16-05-2025

                    उत्पाद का नाम: ज्वार 🌱
                    समाप्ति तिथि: कल, 16-05-2025

                    उत्पाद का नाम: गेहूं 🌾
                    समाप्ति तिथि: कल, 16-05-2025

                    उत्पाद का नाम: चावल 🌾
                    समाप्ति तिथि: कल, 16-05-2025

                    कृपया इन्हें जल्द से जल्द उपयोग करें या बाजार में बेचने के लिए विचार करें। धन्यवाद!''',
  to='+916202603974'
    )

    print(message.sid)




def crops(request):
    return render(request, 'pages/crops.html')

def fertilizer(request):
    return render(request, 'pages/fertilizer.html')

def seed(request):
    return render(request, 'pages/seed.html')

def profit(request):
    return render(request, 'pages/profit.html')

def utilized(request):
    return render(request, 'pages/utilized.html')

def table(request):
    return render(request, 'pages/table.html')