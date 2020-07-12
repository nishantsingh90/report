from django.shortcuts import render,redirect
from .forms import ReportForm
from django.contrib import messages

# Create your views here.
def report(request):
    if request.method == 'POST':
        # user_form = UserForm(request.POST, instance=request.user)
        form = ReportForm(request.POST)
        if form.is_valid():



            form.save()
            messages.success(request,"Report was successfully updated!")
            return redirect('/')
        else:
            messages.error(request,'Please correct the error below.')
    else:

        form = ReportForm()
    return render(request, 'index.html', {

        'form': form
    })