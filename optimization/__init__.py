"""
Optimization Package
"""

__all__ = ["gradient_descent"]


def gradient_descent(func, grad, x0, lr=0.01, max_iter=1000, tol=1e-6):
    """Perform simple gradient descent for a scalar function.

    Args:
        func: Callable representing the objective function.
        grad: Callable representing the derivative of the objective.
        x0: Initial scalar value.
        lr: Learning rate.
        max_iter: Maximum number of iterations.
        tol: Convergence tolerance.

    Returns:
        The optimized scalar value.
    """
    x = x0
    for _ in range(max_iter):
        g = grad(x)
        x_next = x - lr * g
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    return x
