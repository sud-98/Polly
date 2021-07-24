from django.forms import ModelForm
from .models import Poll

class CreatePoll(ModelForm):
	class Meta:
		model = Poll
		fields = ['topic', 'option1', 'option2', 'option3']