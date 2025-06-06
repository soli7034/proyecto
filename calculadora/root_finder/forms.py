from django import forms

class PolynomialForm(forms.Form):
    METHOD_CHOICES = [
        ('bisection', 'Bisección'),
        ('newton', 'Newton-Raphson'),
        ('modified_newton', 'Newton-Raphson Modificado'),
    ]
    
    polynomial = forms.CharField(
        label='Polinomio (ejemplo: x**2 - 4)',
        max_length=100,
        help_text='Ingresa un polinomio en términos de x (ejemplo: x**2 - 4)'
    )
    method = forms.ChoiceField(
        choices=METHOD_CHOICES,
        label='Método Numérico',
        widget=forms.Select(attrs={'id': 'id_method', 'class': 'form-select'})
    )
    a = forms.FloatField(
        label='Extremo inferior (a) - Solo para Bisección',
        required=False
    )
    b = forms.FloatField(
        label='Extremo superior (b) - Solo para Bisección',
        required=False
    )
    x0 = forms.FloatField(
        label='Valor inicial (x0) - Para Newton-Raphson y Modificado',
        required=False
    )
    tolerance = forms.FloatField(
        label='Tolerancia (error permitido)',
        initial=1e-6,
        min_value=0
    )
    max_iterations = forms.IntegerField(
        label='Máximo número de iteraciones',
        initial=100,
        min_value=1
    )