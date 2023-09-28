from django import forms
from .models import UploadFile, Comment

class UploadFileForm(forms.ModelForm):
    friend = forms.CharField(help_text="Bu faylı paylaşmaq üçün istifadəçi adını və ya e-mail adressini yazın.", required=False)
    comment_permission = forms.BooleanField(help_text="Comment permission", required=False)
    class Meta:
        model = UploadFile
        fields = ('name', 'description', 'file',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)