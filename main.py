from forward import forward
from inverse import inverse
from jacobian import jacobian
from trajectory import trajectory


def main():
    kinematics = {1: forward, 2: inverse, 3: jacobian, 4: trajectory}
    _input = int(input(
        ' Choose Kinematics type:\n\
        1 = Forward\n\
        2 = Inverse\n\
        3 = Jacobian\n\
        4 = Trajectory\n'))
    kinematics[_input]()


if __name__ == '__main__':
    main()
