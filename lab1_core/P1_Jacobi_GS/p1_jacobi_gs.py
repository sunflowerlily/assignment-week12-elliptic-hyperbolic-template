import numpy as np
import time

def jacobi_step(u):
    """
    Jacobi 迭代的一步更新
    u: 当前电势分布
    返回: 更新后的电势分布 u_new
    """
    # TODO: 实现 Jacobi 更新逻辑 (建议使用 NumPy 向量化)
    pass

def gauss_seidel_step_naive(u):
    """
    Gauss-Seidel 迭代的一步更新 (朴素 for 循环版)
    u: 当前电势分布 (就地更新)
    """
    # TODO: 实现原生 Python 双重循环更新
    # 注意：Gauss-Seidel 使用最新可用的邻点值
    pass

def solve_laplace(method='jacobi', n=40, tol=1e-3, max_iter=10000):
    """
    求解拉普拉斯方程
    """
    u = np.zeros((n, n))
    u[-1, :] = 100 # 上边界边界条件
    
    start_time = time.time()
    iters = 0
    # TODO: 实现迭代循环，记录次数并返回结果
    
    duration = time.time() - start_time
    return u, iters, duration
