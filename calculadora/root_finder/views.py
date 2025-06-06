from django.shortcuts import render
from .forms import PolynomialForm
from .utils import bisection_method, newton_raphson_method, modified_newton_raphson_method
import sympy as sp
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

def evaluate_polynomial(expr, val):
    x = sp.Symbol('x')
    return float(expr.subs(x, val))

def index(request):
    result = None
    error_message = None
    plot_div = None
    table_data = None

    if request.method == 'POST':
        form = PolynomialForm(request.POST)
        if form.is_valid():
            polynomial_str = form.cleaned_data['polynomial']
            method = form.cleaned_data['method']
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            x0 = form.cleaned_data['x0']
            tolerance = form.cleaned_data['tolerance']
            max_iterations = form.cleaned_data['max_iterations']

            try:
                x = sp.Symbol('x')
                expr = sp.sympify(polynomial_str)

                if method == 'bisection':
                    if a is None or b is None:
                        error_message = "Debes proporcionar los extremos a y b para el método de Bisección."
                    else:
                        result, table_data = bisection_method(expr, a, b, tolerance, max_iterations)
                        if result is None:
                            error_message = table_data
                            table_data = None
                elif method == 'newton':
                    if x0 is None:
                        error_message = "Debes proporcionar un valor inicial x0 para Newton-Raphson."
                    else:
                        result, table_data = newton_raphson_method(expr, x0, tolerance, max_iterations)
                        if result is None:
                            error_message = table_data
                            table_data = None
                elif method == 'modified_newton':
                    if x0 is None:
                        error_message = "Debes proporcionar un valor inicial x0 para Newton-Raphson Modificado."
                    else:
                        result, table_data = modified_newton_raphson_method(expr, x0, tolerance, max_iterations)
                        if result is None:
                            error_message = table_data
                            table_data = None

                if result is not None:
                    # Generar gráfica
                    x_vals = np.linspace(result - 5, result + 5, 400)
                    y_vals = [evaluate_polynomial(expr, xi) for xi in x_vals]
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='Polinomio'))
                    fig.add_trace(go.Scatter(x=[result], y=[0], mode='markers', name='Raíz', marker=dict(size=10, color='red')))
                    fig.update_layout(
                        title='Gráfica del Polinomio y su Raíz',
                        xaxis_title='x',
                        yaxis_title='f(x)',
                        showlegend=True
                    )
                    plot_div = pio.to_html(fig, full_html=False)

            except sp.SympifyError:
                error_message = "El polinomio ingresado no es válido. Usa la sintaxis correcta, como 'x**2 - 4'."
            except Exception as e:
                error_message = f"Ocurrió un error inesperado: {str(e)}"
        else:
            error_message = "Por favor, corrige los errores del formulario."
    else:
        form = PolynomialForm()

    return render(request, 'root_finder/index.html', {
        'form': form,
        'result': result,
        'error_message': error_message,
        'plot_div': plot_div,
        'table_data': table_data
    })