ros2 action send_goal /arm_controller/follow_joint_trajectory control_msgs/action/FollowJointTrajectory "{
  trajectory: {
    joint_names: [joint1, joint2, joint3, joint4, joint5, joint6],
    points: [
      { positions: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], time_from_start: { sec: 0, nanosec: 500 } },
      { positions: [0.0, 0.9, 1.17, 0.0, -0.3, 0.0], time_from_start: { sec: 3, nanosec: 500 } },
      { positions: [0.0, 1.2, 1.17, 0.0, -0.3, 0.0], time_from_start: { sec: 5, nanosec: 500 } },
    ]
  }
}"

# /gripper_controller/follow_joint_trajectory

ros2 action send_goal /gripper_controller/follow_joint_trajectory control_msgs/action/FollowJointTrajectory "{
  trajectory: {
    joint_names: [finger_joint1],
    points: [
      { positions: [0.0], time_from_start: { sec: 0, nanosec: 500 } },
      { positions: [0.1], time_from_start: { sec: 5, nanosec: 500 } },
      { positions: [0.2], time_from_start: { sec: 7, nanosec: 500 } },
      { positions: [0.3], time_from_start: { sec: 8, nanosec: 500 } }
    ]
  }
}"
