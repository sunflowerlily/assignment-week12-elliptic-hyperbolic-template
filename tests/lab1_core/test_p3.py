import numpy as np
import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lab1_core/P3_Wave_CFL')))
try:
    from p3_wave_cfl import solve_wave
except ImportError:
    pass

def test_p3_wave_stability():
    """测试不同 CFL 下的稳定性"""
    if 'solve_wave' not in globals():
        pytest.skip("p3_wave_cfl.py 未完成")
        
    n = 50
    # c=0.5 应该稳定
    u_stable = solve_wave(n=n, c=0.5, steps=50)
    assert not np.any(np.isnan(u_stable))
    assert np.max(np.abs(u_stable)) < 2.0 # 振幅不应发散
    
    # c=1.01 理论上不稳定，但数值上可能需要更多步数才爆发
    # 这里的测试重点是确保学生代码能跑通 c=0.5
    pass
