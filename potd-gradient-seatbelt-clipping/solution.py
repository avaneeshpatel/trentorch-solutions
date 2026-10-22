import numpy as np


def clip_grad_norm(g: np.ndarray, tau: float) -> np.ndarray:
    """
    Global-norm gradient clipping.

    g: shape (d,). tau: the clip threshold, tau > 0.

    If ||g||_2 > tau (strict), return g * (tau / ||g||_2). Otherwise
    return g unchanged. At exact equality (||g||_2 == tau), no clipping
    happens.
    """
    # TODO: strict > decides both whether to clip and whether the division
    # ever runs.
    sum1 = 0
    for ele in g:
        sum1 += ele**2
    g_ss = (sum1)**0.5
    if g_ss > tau:
        g = np.round(g* (tau/g_ss), decimals=6)
        return g
    else:
        return g
