from setuptools import find_packages, setup

package_name = 'test_tof_branch'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='schofier@oregonstate.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker_pos1 = test_tof_branch.publisher_tof1_position:main',
        	'listener_pos1 = test_tof_branch.subscriber_tof1_position:main',
            'talker_arduino = test_tof_branch.publisher_arduino:main', 
            'listener_arduino = test_tof_branch.subscriber_arduino1_position:main', 
            'talker_arduino_avg = test_tof_branch.publisher_arduino_avg:main', 
            'talker_rob_cart = test_tof_branch.publisher_robot_cart:main', 
            'down = test_tof_branch.moving_down_looking_for_branch:main', 
        ],
    },
)
