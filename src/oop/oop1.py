# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# class Vehicle:
#     def __init__(self, name):
#         self.name = name


# class GroundVehicle(Vehicle):
#     def __init__(self, name, typeV):
#         super().__init__(name)
#         self.typeV = typeV


# class FlightVehicle(Vehicle):
#     def __init__(self, name, typeV):
#         super().__init__(name)
#         self.typeV = typeV


# class Car(GroundVehicle):
#     def __init__(self, name, typeV, axle):
#         super().__init__(name, typeV)
#         self.axle = axle


# class MotorCycle(GroundVehicle):
#     def __init__(self, name, typeV, throttle):
#         super().__init__(name, typeV)
#         self.throttle = throttle


# class Airplane(FlightVehicle):
#     def __init__(self, name, typeV, wings):
#         super().__init__(name, typeV)
#         self.wings = wings


# class Starship(FlightVehicle):
#     def __init__(self, name, typeV, thrust):
#         super().__init__(name, typeV)
#         self.thrust = thrust

class Vehicle:
    def __init__(self):
        pass


class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass


class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass


class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass


class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass


class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass


class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass
