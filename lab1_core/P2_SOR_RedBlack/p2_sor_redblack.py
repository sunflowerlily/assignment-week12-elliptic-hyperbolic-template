import numpy as np

def sor_redblack_step(u, omega, mask_red, mask_black):
    """
    红黑排序向量化 SOR 的一步更新
    u: 当前电势分布
    omega: 松弛因子
    mask_red, mask_black: 红黑格点掩码
    """
    # TODO: 利用掩码实现红黑两步更新
    # 提示：
    # 1. 更新红色格点 (依赖黑色邻点旧值)
    # 2. 更新黑色格点 (依赖红色邻点新值)
    # 3. 使用 SOR 公式: u_new = (1-omega)*u_old + omega*u_GS
    pass

def solve_sor(n=80, omega=1.5, tol=1e-4, max_iter=20000):
    """
    使用红黑 SOR 求解
    """
    u = np.zeros((n, n))
    u[-1, :] = 100
    
    # TODO: 生成红黑掩码
    # TODO: 执行迭代
    pass
