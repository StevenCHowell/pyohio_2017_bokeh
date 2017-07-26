mu = np.array([
        [2, 2],
        [2, -2],
        [-2, -2],
        [-2, 2],
        [0, 0],
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1],
    ])

sigma = np.array([0.01, 0.1, 0.5, 1.0, 3.0, 2.0, 0.25, 5.0, 0.05])

points = gaussian_points(mu, sigma, 1000000)

hv_points = hv.Points(
    points, label='Points',
    kdims=[
        'independent variable',
        'dependent variable'
    ])

datashade(hv_points)
