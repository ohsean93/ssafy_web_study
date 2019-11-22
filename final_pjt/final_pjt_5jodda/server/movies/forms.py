from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content', 'score', )

    content = forms.CharField(
        label='리뷰 작성하기',
        max_length=140,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control review-content',
                'placeholder': '리뷰 내용을 입력해주세요.',
                'rows': 4,
            }
        )
    )

