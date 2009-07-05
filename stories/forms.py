from django import forms

class AddFragmentForm(forms.Form):
    fragment_text = forms.fields.CharField(
        label="Three words",
        widget=forms.TextInput()
    )
    def clean_fragment_text(self):
    
        # Taken from models.Story.add_fragment:
        word_list = [
            word.strip()
            for word
            in self.cleaned_data['fragment_text'].split()
            if word.strip() != ""
        ]
        
        if len(word_list) > 3:
            raise forms.ValidationError("We can only have three words here!")
            
        return " ".join(word_list)
        
class NewStoryForm(forms.Form):
    story_name = forms.fields.CharField(
        label="Story name",
        widget=forms.TextInput()
    )
