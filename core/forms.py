from django import forms

CHOICES = (
    ("3", "A* - Manhattan Distance"),
)


class HomeForm(forms.Form):
    initial_state = forms.CharField(label='Start From separated by ( , ):')
    Goal_state = forms.CharField(label='Goal State separated by ( , ) :')
    search_algorithm = forms.ChoiceField(label="A* Algorithm : ",choices=CHOICES,required=True)