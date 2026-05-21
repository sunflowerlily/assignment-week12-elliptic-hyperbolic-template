import numpy as np
import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lab1_core/P2_SOR_RedBlack')))
try:
    from p2_sor_redblack import solve_sor
except ImportError:
    pass

def test_p2_sor_convergence():
    """测试 SOR 求解器是否比 Jacobi 更快"""
    if 'solve_sor' not in globals():
        pytest.skip("p2_sor_redblack.py 未完成")
        
    n = 30
    # 测试 omega=1 (GS) 和 omega=1.5
    u1, iters1 = solve_sor(n=n, omega=1.0, tol=1e-3)
    u2, iters2 = solve_sor(n=n, omega=1.5, tol=1e-3)
    
    # 物理检查
    assert 0 < u2[n//2, n//2] < 100
    # 效率检查：omega=1.5 应该迭代更少
    assert iters2 < iters1
