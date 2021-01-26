from math import radians, sin, cos, tan

angle_in_radians: float = radians(float(input('Enter an angle: ')))

print(
    f'The sine is: {sin(angle_in_radians):.2f}\n'
    f'The cosine is: {cos(angle_in_radians):.2f}\n'
    f'The tangent is: {tan(angle_in_radians):.2f}'
)
