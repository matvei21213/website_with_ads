from django import forms

class AdvForm(forms.Form):# наследую класс Model для создания таблицы в БД
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control form-control-lg"})) #  текстовое поле
    description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control form-control-lg"}))  # нет TextField
    price = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control form-control-lg"}))
    auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class":"form-check-input"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control form-control-lg"}))