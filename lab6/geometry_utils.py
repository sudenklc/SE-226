import math

def circle_area(radius):
    try:
        radius = float(radius)
        if radius <= 0:
            raise ValueError("Dimensions must be positive.")
        return math.pi * radius * radius
    except ValueError as e:
        raise ValueError(str(e))


def circle_perimeter(radius):
    radius = float(radius)
    if radius <= 0:
        raise ValueError("Dimensions must be positive.")
    return 2 * math.pi * radius


def rectangle_area(width, height):
    width = float(width)
    height = float(height)
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive.")
    return width * height


def rectangle_perimeter(width, height):
    width = float(width)
    height = float(height)
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive.")
    return 2 * (width + height)


def triangle_area(base, height):
    base = float(base)
    height = float(height)
    if base <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive.")
    return (base * height) / 2
