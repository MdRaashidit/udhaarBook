from django.shortcuts import render
from .models import Party,Transactions

def udhari(request):
    
    if request.method == "POST":
        Balance=0
        party = request.POST.get("party")
        parties, _ = Party.objects.get_or_create(name=party)
        amount=request.POST['amount']
        des=request.POST.get('des')
        date=request.POST.get('date')
        tsave = Transactions(party=parties,amount=amount,description=des,date=date)
        tsave.save()
        party.Balance=party.Balance+amount
        print('...........................')
        print(party.Balance)
        party.save()
                
    return render(request,'index.html')

 