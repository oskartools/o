from django import forms

class JobApplicationForm(forms.Form):
    full_name = forms.CharField(label="الاسم الكامل", max_length=100, required=True)
    gender = forms.ChoiceField(
        label="الجنس",
        choices=[("male", "ذكر"), ("female", "أنثى")],
        required=True
    )
    country = forms.ChoiceField(
        label="الدولة",
        choices=[
            ("yemen", "اليمن"),
            ("algeria", "الجزائر"),
            ("bahrain", "البحرين"),
            ("comoros", "جزر القمر"),
            ("djibouti", "جيبوتي"),
            ("egypt", "مصر"),
            # أضف بقية الدول هنا
            
        ],
        required=True
    )
    email = forms.EmailField(label="البريد الإلكتروني", required=True)
    phone = forms.CharField(label="رقم الهاتف", max_length=15, required=True)
    portfolio = forms.URLField(label="رابط معرض الأعمال (اختياري)", required=False)
    experience = forms.IntegerField(label="سنوات الخبرة", min_value=0, required=True)
    education = forms.ChoiceField(
        label="المستوى الأكاديمي",
        choices=[
            ("high_school", "ثانوية عامة"),
            ("bachelor", "بكالوريوس"),
            ("master", "ماجستير"),
            ("phd", "دكتوراه"),
        ],
        required=True
    )
    skills = forms.CharField(
        label="المهارات الأساسية",
        widget=forms.Textarea(attrs={"rows": 4}),
        required=True
    )