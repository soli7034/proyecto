import sympy as sp
import numpy as np

def evaluate_polynomial(expr, x_val):
    x = sp.Symbol('x')
    try:
        return float(expr.subs(x, x_val))
    except:
        return None

def bisection_method(expr, a, b, tol, max_iter):
    x = sp.Symbol('x')
    results = []
    fa = evaluate_polynomial(expr, a)
    fb = evaluate_polynomial(expr, b)
    
    if fa is None or fb is None:
        return None, "Error al evaluar el polinomio en los extremos."
    if fa * fb >= 0:
        return None, "No hay cambio de signo en el intervalo [a, b]."
    
    c = None
    for i in range(max_iter):
        c = (a + b) / 2
        fc = evaluate_polynomial(expr, c)
        if fc is None:
            return None, "Error al evaluar el polinomio en c."
        
        error = abs(b - a) / 2
        results.append({
            'iteration': i + 1,
            'a': a,
            'b': b,
            'c': c,
            'f_c': fc,
            'error': error
        })
        
        # No retornamos aquí, solo marcamos si se cumple la tolerancia
        if error < tol or fc == 0:
            # Pero seguimos iterando hasta max_iter
        
            # Si quieres marcar la fila donde se cumple la tolerancia, puedes agregar un campo extra
        
            pass
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    return c, results

def newton_raphson_method(expr, x0, tol, max_iter):
    x = sp.Symbol('x')
    f = expr
    df = sp.diff(expr, x)
    results = []
    xn = x0
    
    for i in range(max_iter):
        fx = evaluate_polynomial(f, xn)
        dfx = evaluate_polynomial(df, xn)
        
        if fx is None or dfx is None:
            return None, "Error al evaluar el polinomio o su derivada."
        if abs(dfx) < 1e-10:
            return None, "Derivada cercana a cero, método no aplicable."
        
        error = abs(fx / dfx)
        results.append({
            'iteration': i + 1,
            'x_n': xn,
            'f_x_n': fx,
            'df_x_n': dfx,
            'error': error
        })
        
        # No retornamos aquí, solo marcamos si se cumple la tolerancia
        # if error < tol:
        #     return xn, results
        
        xn = xn - fx / dfx
    
    return xn, results

def modified_newton_raphson_method(expr, x0, tol, max_iter):
    x = sp.Symbol('x')
    f = expr
    df = sp.diff(expr, x)
    d2f = sp.diff(df, x)
    results = []
    xn = x0
    
    for i in range(max_iter):
        fx = evaluate_polynomial(f, xn)
        dfx = evaluate_polynomial(df, xn)
        d2fx = evaluate_polynomial(d2f, xn)
        
        if fx is None or dfx is None or d2fx is None:
            return None, "Error al evaluar el polinomio o sus derivadas."
        if abs(dfx) < 1e-10:
            return None, "Derivada primera cercana a cero, método no aplicable."
        
        denominator = dfx**2 - fx * d2fx
        if abs(denominator) < 1e-10:
            return None, "Denominador cercano a cero, método no aplicable."
        
        error = abs(fx * dfx / denominator)
        results.append({
            'iteration': i + 1,
            'x_n': xn,
            'f_x_n': fx,
            'df_x_n': dfx,
            'd2f_x_n': d2fx,
            'error': error
        })
        
        # No retornamos aquí, solo marcamos si se cumple la tolerancia
        # if error < tol:
        #     return xn, results
        
        xn = xn - (fx * dfx) / denominator
    
    return xn, results