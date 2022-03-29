# Robotics project

## Forward kinematics function (FK)

## Inverse kinematics function (IK)

**Description**: Inverse kinematics is the use of kinematic equations to determine the motion of a serial manipulator to reach a desired position.  
**Input**: Robot arrangement, its DH parameter table, and the end-effector pose.  
**Output**: Joint variables.  
**Examples**:

1. **Input**:  
   Robot arrangement:  
   RR  
   DH parameter table:  
    [ 2 0 0 ]  
    [ 2 0 0 ]  
   End-effector pose:  
   Xe = 2.25, Ye = 2.94, Ze=0, Φ=0, θ=0, Ψ=0

   **Output**:  
   [{θ1: 30.323, θ2: 44.499}, {θ1: 74.823, θ2: -44.499}]

![RR IK](images/rrIK.png)

2. **Input**:  
   Robot arrangement:
   RPP  
   DH parameter table:  
   [ 0 0 0.1 ]  
   [ 0 -90 0 ]  
   [ 0 0 0 ]  
   End-effector pose:  
   Xe = -0.1 Ye = 0 Ze = 0.2

   **Output**:  
   [{θ1: 270.00, d3: -0.10000, d2: 0.10000}, {θ1: 90.000, d3: 0.10000, d2: 0.10000}]

   ![RR IK](images/rppIK.png)

## Forward jacobian function (FJ)

## Inverse jacobian function (FJ)

## Trajectory planning function (TP)
