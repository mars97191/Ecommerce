from django import forms
from product.models import ProductReview


class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'reviews__comment--reply__textarea', 'placeholder': 'Напиши отзыв'}))

    class Meta:
        model = ProductReview
        fields = ['review', 'rating']
