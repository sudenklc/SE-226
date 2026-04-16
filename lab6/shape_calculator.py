import geometry_utils

def main():
    operations = {
        "circle_area": geometry_utils.circle_area,
        "circle_perimeter": geometry_utils.circle_perimeter,
        "rectangle_area": geometry_utils.rectangle_area,
        "rectangle_perimeter": geometry_utils.rectangle_perimeter,
        "triangle_area": geometry_utils.triangle_area
    }

    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: _area, _perimeter")

    operation = input("Enter the operation you want to perform: ").strip().lower()

    try:
        if operation not in operations:
            raise ValueError("Invalid operation.")

        if operation == "circle_area" or operation == "circle_perimeter":
            radius = float(input("Enter radius: "))
            result = operations[operation](radius)

        elif operation == "rectangle_area" or operation == "rectangle_perimeter":
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            result = operations[operation](width, height)

        elif operation == "triangle_area":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            result = operations[operation](base, height)

        print("Result: {:.2f}".format(result))

    except ValueError as e:
        print("Input Error:", e)


