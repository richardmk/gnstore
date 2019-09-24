from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('state',)
        #que use todos los campos pero exluya es state del general

        widgets = {
            'name':forms.TextInput(
                attrs = {
                    'class' :' form-control stext-111 cl2 plh3 size-90 p-l-62 p-r-30',
                    'placeholder': 'Your Name'
            
                }
            ),
           
            'email':forms.EmailInput(
                attrs = {
                    'class': 'form-control stext-111 cl2 plh3 size-90 p-l-62 p-r-30',
                    'placeholder' : 'Your Email Address'
                }
            ),
            'message':forms.Textarea(
                attrs = {
                    'class': ' form-control stext-111 cl2 plh3 p-lr-28 p-tb-25'
                }
            )

        }