from django import forms

class ProductForm(forms.Form):
    name=forms.CharField(label='Product Name')
    sold=forms.IntegerField(label='Sold Quantity')
    total=forms.IntegerField(label='Total Quantity')
    price=forms.FloatField(label="Price")
    review=forms.FloatField(label="Review")