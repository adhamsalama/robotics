from forward.forward_kinematics import forward_kinematics
from inverse.inverse_kinematics import inverse_kinematics
from jacobian.jacobian_function import jacobian
from inverse_jacobian.inverse_jacobian_function import inverse_jacobian
from trajectory.trajectory_solver import trajectory

def main():
    kinematics = {1: forward_kinematics,
                  2: inverse_kinematics, 3: jacobian, 4: inverse_jacobian, 5: trajectory}
    try:
        while True:
            kinematic = int(input(
                'Choose Kinematics type:\n\
            1 = Forward\n\
            2 = Inverse\n\
            3 = Jacobian\n\
            4 = Inverse_jacobian\n\
            5 = Trajectory\n'))
            if 1 <= kinematic <= 5:
                break
        kinematics[kinematic]()
    except Exception as e:
        print('Error', e)


if __name__ == '__main__':
    main()
