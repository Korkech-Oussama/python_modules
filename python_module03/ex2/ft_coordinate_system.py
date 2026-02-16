import sys
import math


def three_d_coridinates() -> None:
    print("=== Game Coordinate System ===\n")

    base_point = (0, 0, 0)
    ex_point: tuple[int, ...] = (10, 20, 5)
    dist = math.sqrt(ex_point[0]**2 + ex_point[1]**2 + ex_point[2]**2)

    print(f"Position created: {ex_point}")
    print(f"Distance between {base_point} and {ex_point}: {dist:.2f}\n")
    ac = len(sys.argv)
    if ac == 2:
        arg = sys.argv[1]
        try:
            parsed: tuple[int, ...] = tuple(int(c) for c in arg.split(','))
            dist = math.sqrt(parsed[0]**2 + parsed[1]**2 + parsed[2]**2)
        except ValueError as e:
            print(f"Parsing invalid coordinates: {arg}")
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}, {e.args}\n")
        else:
            x, y, z = parsed
            print(f"Parsing coordinates: \"{arg}\"")
            print(f"Parsed position: {parsed}")
            print(f"Distance between {base_point} and {parsed}: {dist:.2f}\n")
            print("Unpacking demonstration:")
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    three_d_coridinates()
