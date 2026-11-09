from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([

        # Transformação: base_footprint -> base_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_footprint_to_base_link',
            arguments=[
                '--x', '0',
                '--y', '0',
                '--z', '0.010',
                '--roll', '0',
                '--pitch', '0',
                '--yaw', '0',
                '--frame-id', 'base_footprint',
                '--child-frame-id', 'base_link',
            ],
            output='screen',
        ),

        # Transformação: base_link -> base_scan
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_link_to_base_scan',
            arguments=[
                '--x', '-0.064',
                '--y', '0',
                '--z', '0.121',
                '--roll', '0',
                '--pitch', '0',
                '--yaw', '0',
                '--frame-id', 'base_link',
                '--child-frame-id', 'base_scan',
            ],
            output='screen',
        ),

    ])
