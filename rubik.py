from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Define colors for each Rubik's cube face
face_colors = {
    "U": color.white,
    "D": color.yellow,
    "F": color.green,
    "B": color.blue,
    "L": color.orange,
    "R": color.red,
}


# Function to create a single cube with colored faces
def create_cubelet(x, y, z):
    faces = []
    cube = Entity(
        model="cube", position=(x, y, z), scale=0.95, color=color.gray, parent=scene
    )

    if y == 1:
        faces.append(
            Entity(
                model="quad",
                parent=cube,
                position=(0, 0.51, 0),
                rotation=(90, 0, 0),
                color=face_colors["U"],
                double_sided=True,
            )
        )
    if y == -1:
        faces.append(
            Entity(
                model="quad",
                parent=cube,
                position=(0, -0.51, 0),
                rotation=(-90, 0, 0),
                color=face_colors["D"],
                double_sided=True,
            )
        )
    if z == 1:
        faces.append(
            Entity(
                model="quad",
                parent=cube,
                position=(0, 0, 0.51),
                rotation=(0, 0, 0),
                color=face_colors["F"],
                double_sided=True,
            )
        )
    if z == -1:
        faces.append(
            Entity(
                model="quad",
                parent=cube,
                position=(0, 0, -0.51),
                rotation=(0, 180, 0),
                color=face_colors["B"],
                double_sided=True,
            )
        )
    if x == -1:
        faces.append(
            Entity(
                model="quad",
                parent=cube,
                position=(-0.51, 0, 0),
                rotation=(0, 90, 0),
                color=face_colors["L"],
                double_sided=True,
            )
        )
    if x == 1:
        faces.append(
            Entity(
                model="quad",
                parent=cube,
                position=(0.51, 0, 0),
                rotation=(0, -90, 0),
                color=face_colors["R"],
                double_sided=True,
            )
        )

    return cube


# Create a 3x3x3 Rubik's Cube
offset = [-1, 0, 1]
cubelets = []
for x in offset:
    for y in offset:
        for z in offset:
            cubelets.append(create_cubelet(x, y, z))

# Optional: Add a camera controller
EditorCamera()

# Rotate camera
camera.position = (-8, 4, 0)
camera.rotation = (10, 20, 0)

# Instructions
instruction_text = Text(text="Use right mouse button to rotate the view.", origin=(0, 4), scale=1.5)

def input(key):
    if key == 'right mouse down':
        instruction_text.enabled = False
        
app.run()
