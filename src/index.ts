import { loadPyodide } from 'pyodide';

const pythonCode = `
def is_point_in_simplex(vertices, point):
    import numpy as np
    from scipy.optimize import linprog

    vertices = np.array(vertices)
    point = np.array(point)
    num_vertices = vertices.shape[0]
    A = np.hstack((vertices.T, np.ones((vertices.shape[1], 1))))
    b = np.append(point, 1)
    try:
        barycentric_coords = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        return False
    return np.all(barycentric_coords >= 0) and np.isclose(barycentric_coords.sum(), 1)

# Example usage
vertices = [[0, 0], [1, 0], [0, 1]]
point_inside = [0.25, 0.25]
point_outside = [1, 1]

print(is_point_in_simplex(vertices, point_inside))  # Should return True
print(is_point_in_simplex(vertices, point_outside)) # Should return False
`;

const main = async () => {
    const pyodide = await loadPyodide();
//    await pyodide.loadPackage('numpy');
    await pyodide.loadPackage('scipy');
    pyodide.runPythonAsync(pythonCode);
};

main();
