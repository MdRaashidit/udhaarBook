from django.shortcuts import render
from .models import Party,Transactions

def udhari(request):
    if request.method == "POST":
        party = request.POST.get("party")
        parties, _ = Party.objects.get_or_create(name=party)
        amount=request.POST.get('amount')
        des=request.POST.get('des')
        date=request.POST.get('date')
        tsave = Transactions(party=parties,amount=amount,description=des,date=date)
        tsave.save()
                
    return render(request,'index.html')
