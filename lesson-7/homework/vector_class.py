import math

class Vector:
    def __init__(self, *components):
        """
        Initialize a vector with the given components.
        """
        self.components = list(components)

    def __repr__(self):
        """
        Return a string representation of the vector.
        """
        return f"Vector({', '.join(map(str, self.components))})"

    def __add__(self, other):
        """
        Add two vectors of the same dimension.
        """
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for addition.")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        """
        Subtract two vectors of the same dimension.
        """
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for subtraction.")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        """
        Compute the dot product of two vectors or perform scalar multiplication.
        """
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimension for dot product.")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        else:
            raise TypeError("Unsupported operand type for multiplication.")

    def __rmul__(self, scalar):
        """
        Handle scalar multiplication when the scalar is on the left.
        """
        if isinstance(scalar, (int, float)):
            return self * scalar
        else:
            raise TypeError("Unsupported operand type for multiplication.")

    def magnitude(self):
        """
        Compute the magnitude (length) of the vector.
        """
        return math.sqrt(sum(a**2 for a in self.components))

    def normalize(self):
        """
        Return the normalized (unit) vector.
        """
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*[a / mag for a in self.components])

# Example Usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)          # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(v4)          # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 = 3 * v1
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)




































