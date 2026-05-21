import numpy as np
import pytest
import sys
import os

# 路径修复
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lab1_core/P1_Jacobi_GS')))
try:
    from p1_jacobi_gs import solve_laplace
except ImportError:
    pass

def test_p1_convergence():
    """测试 Jacobi/GS 求解器是否收敛到合理值"""
    if 'solve_laplace' not in globals():
        pytest.skip("p1_jacobi_gs.py 未完成或导入失败")
        
    n = 20
    u, iters, duration = solve_laplace(method='jacobi', n=n, tol=1e-2)
    
    # 物理合理性检查：中心点应大于0且小于100
    assert 0 < u[n//2, n//2] < 100
    # 边界检查
    assert np.allclose(u[-1, :], 100)
    assert np.allclose(u[0, :], 0)
