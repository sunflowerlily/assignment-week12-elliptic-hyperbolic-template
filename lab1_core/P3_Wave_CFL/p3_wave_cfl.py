import numpy as np

def wave_step(u_curr, u_prev, c):
    """
    波动方程的一步显式更新
    u_curr: 当前时刻位移
    u_prev: 上一时刻位移
    c: 库朗数 (a*dt/dx)
    返回: 下一时刻位移 u_next
    """
    # TODO: 实现二阶中心差分迭代公式
    pass

def solve_wave(n=100, c=0.5, steps=200):
    """
    一维波动方程演化
    """
    u = np.zeros((steps, n))
    x = np.linspace(0, 1, n)
    
    # 初始波包 (高斯)
    u[0, :] = np.exp(-100 * (x - 0.5)**2)
    
    # TODO: 处理冷启动的第一步 (t = dt)
    # 提示：使用泰勒展开或虚拟点法，利用 v=0 的初始条件
    
    # TODO: 迭代演化
    return u
