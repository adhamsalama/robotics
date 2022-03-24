from forward import forward
from inverse import inverse
from jacobian import jacobian
from trajectory import trajectory


def main():
    kinematics = {1: forward, 2: inverse, 3: jacobian, 4: trajectory}
    try:
        while True:
            kinematic = int(input(
                'Choose Kinematics type:\n\
            1 = Forward\n\
            2 = Inverse\n\
            3 = Jacobian\n\
            4 = Trajectory\n'))
            if 1 <= kinematic <= 4:
                break
        kinematics[kinematic]()
    except:
        print('Error')


if __name__ == '__main__':
    main()
