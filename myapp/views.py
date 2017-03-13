from django.shortcuts import render
from django.views.generic.edit import CreateView
from models import Activity
from myapp.forms import ActivityForm

# Create your views here.
def home(request):
	return render(request, 'home.html', {'key': "value" })

def hike(request):
	return render(request, 'hike.html', {'key': "value" })

def all_activity(request):
	return render(request, 'AllAc.html',{'key': "value"})

def vote(request):
	score = request.GET.get("day")
	print(score)
	##return redirect('home')
	return render(request, 'home.html', {'key': "value" })

class CreateActivity(CreateView):
	queryset = Activity()
	template_name='activity.html'
	form_class = ActivityForm
	success_url = '/'
