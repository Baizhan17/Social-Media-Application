from django.forms import ModelForm
from .models import Post,PostAttachment,PostReport
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("body",)
class AttachmentForm(ModelForm):
    class Meta:
        model = PostAttachment
        fields = ("image",)
        
class PostReportForm(ModelForm):
    class Meta:
        model = PostReport
        fields = ['post', 'text']  # Fields to include in the form

    def clean(self):
        cleaned_data = super().clean()
        post = cleaned_data.get('post')
        text = cleaned_data.get('text')

 
        if not post:
            raise forms.ValidationError("A valid post is required.")

        if not text:
            raise forms.ValidationError("Text for the report is required.")

        return cleaned_data