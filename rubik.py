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
core_entity = None
for x in offset:
    for y in offset:
        for z in offset:
            c = create_cubelet(x, y, z)
            if x == y == z == 0:
                core_entity = c
            cubelets.append(c)

# Add a camera controller
e = EditorCamera()

# Initial view rotation
e.smoothing_helper.rotation = (20, 30, 0)
    
# Instructions
text = '''
<red>Right button:<default> rotate the view
<red>Scrolling:<default> zoom in/out
<red>Middle button:<default> camera moving'''

instruction_text = Text(text=text, origin=(-0.55, 0.55), scale=1.0, position=window.top_left, line_height=1.5)
instruction_text.create_background(padding=0.02, radius=0.01, color=color.black50)

app.run()
