def create_2D_gaussian(mn, variance, cov, n):
    """Randomly sample points from a two-dimensional Gaussian distribution"""
    np.random.seed(128)
    return np.random.multivariate_normal(np.array([mn, mn]), np.array([variance, cov],[cov, variance]),n)
