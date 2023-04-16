import vtk

def sierpinski_pyramid(order, scale=1.0):
    if order == 0:
        # Define the vertices of the pyramid
        vertices = [
            [-1, -1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [0, 0, 1]
        ]
        # Scale the pyramid
        for i in range(len(vertices)):
            vertices[i] = [vertices[i][j] * scale for j in range(3)]
        # Define the faces of the pyramid
        faces = [
            [0, 1, 2],
            [0, 2, 3],
            [1, 0, 4],
            [2, 1, 4],
            [3, 2, 4],
            [0, 3, 4]
        ]
        return vertices, faces

    # Recursively generate the sub-pyramids
    vertices, faces = sierpinski_pyramid(order-1, scale/2.0)
    new_vertices = []
    new_faces = []
    for face in faces:
        # Get the vertices of the current face
        v1 = vertices[face[0]]
        v2 = vertices[face[1]]
        v3 = vertices[face[2]]
        # Compute the midpoint of each edge
        mid1 = [(v1[j]+v2[j])/2.0 for j in range(3)]
        mid2 = [(v2[j]+v3[j])/2.0 for j in range(3)]
        mid3 = [(v3[j]+v1[j])/2.0 for j in range(3)]
        # Add the new vertices
        new_vertices.append(mid1)
        new_vertices.append(mid2)
        new_vertices.append(mid3)
        # Add the new faces
        index = len(vertices) + len(new_vertices) - 3
        new_faces.append([face[0], index-2, index-1])
        new_faces.append([face[1], index-1, index])
        new_faces.append([face[2], index, index-2])
    return vertices + new_vertices, new_faces

# Create a renderer and a render window
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# Create a camera and set its position and focal point
camera = vtk.vtkCamera()
camera.SetPosition(0, 0, 10)
camera.SetFocalPoint(0, 0, 0)
renderer.SetActiveCamera(camera)

# Generate the Sierpinski Pyramid
vertices, faces = sierpinski_pyramid(order=3, scale=3)

# Create a polydata object and add the vertices and faces to it
polydata = vtk.vtkPolyData()
points = vtk.vtkPoints()
for vertex in vertices:
    points.InsertNextPoint(vertex)
polydata.SetPoints(points)
triangles = vtk.vtkCellArray()
for face in faces:
    triangle = vtk.vtkTriangle()
    triangle.GetPointIds().SetId(0, face[0])
    triangle.GetPointIds().SetId(1, face[1])
    triangle.GetPointIds().SetId(2, face[2])
    triangles.InsertNextCell(triangle)
polydata.SetPolys(triangles)

# Create a mapper and an actor for the polydata object
