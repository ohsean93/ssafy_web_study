from django import forms
from .models import Article, Comment


# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=20,
#         label='제목',
#         help_text='제목은 20글자 이내로 입력해 주세요',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-contral my-content',
#                 'placeholder': '제목을 입력해 주세요.',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-contral my-content',
#                 'placeholder': '내용을 입력해 주세요.',
#                 'rows': 5,
#             }
#         ),
#     )


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)  # '__all__': 모두 다 , 이떄 자동인거 들어가면 에러에러
        # exclude = ('title',)

    # 방식 1(권장 X)
        # widgets = {
        #     # '필드(칼럼)': form속성
        #     'title': forms.TextInput(attrs={
        #                             'class': 'form-contral title-class',
        #                             'placeholder': '제목을 입력해 주세요.',
        #                             'id': 'title'
        #                         })
        # }
        # label={
        #     'title': '제목',
        # }
        # help_text={
        #     'title': '제목은 20글자 이내로 입력해 주세요',
        # }

    # 방식 2(장고 권장)
    title = forms.CharField(
        max_length=20,
        label='제목',
        help_text='제목은 20글자 이내로 입력해 주세요',
        widget=forms.TextInput(
            attrs={
                'class': 'form-contral my-content',
                'placeholder': '제목을 입력해 주세요.',
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-contral my-content',
                'placeholder': '내용을 입력해 주세요.',
                'rows': 5,
            }
        ),
    )
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
    content = forms.CharField(
        label='댓글',
        widget=forms.TextInput(
            attrs={
                'class': 'form-contral my-content col-7 ml-3',
                'placeholder': '댓글을 입력해 주세요.',
                'rows': 3,
            }
        ),
    )
    article = forms.ModelChoiceField(
        widget=forms.TextInput(
            attrs={
                'style': 'display:hidden',
            }
        ),
    )

    # def __init__(self, *args, **kwargs):
    #     super(ArticleForm, self).__init__(*args, **kwargs)
    #     self.fields['article'].queryset = Article.objects.all()