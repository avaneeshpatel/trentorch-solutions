import numpy as np


def conv1d(x: np.ndarray, kernel: np.ndarray, mode: str) -> np.ndarray:
    """
    1D cross-correlation ("convolution" in the deep-learning sense: the
    kernel is NOT flipped) with "valid" or "same" zero padding.

    x: shape (n,). kernel: shape (k,), k odd. mode: "valid" or "same".

    "valid": no padding, output length n - k + 1.
    "same": zero-pad x by k // 2 on each side first, output length n.

    Slide the kernel across the (possibly padded) signal without flipping
    it, taking sum(window * kernel) at each position.
    """
    # TODO: build the padded (or unpadded) signal first, then one sliding-window loop.
    if mode == "same":
        # Adding Padding first at left side and then right side
        x = np.append([0]*(len(kernel)//2),x)
        x = np.append(x,[0]*(len(kernel)//2))
    result = np.array([])
    for i in range(len(x)-len(kernel)+1):
        res = sum(x[i:i+len(kernel)]*kernel)
        result = np.append(result,round(res,6))
    return result
