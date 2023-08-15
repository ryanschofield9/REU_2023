from setuptools import find_packages, setup

package_name = 'test_fake_data'

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
    maintainer='rodan',
    maintainer_email='rodan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'talker_pos1 = test_fake_data.publisher_tof1_position:main',
        	'listener_pos1 = test_fake_data.subscriber_tof1_position:main',
        	'talker_real1 = test_fake_data.publisher_real_tof1_pos:main', 
        	'talker_arduino = test_fake_data.publisher_arduino:main', 
        	'listener_arduino = test_fake_data.subscriber_arduino1_position:main',
        	'talker_arduino_avg = test_fake_data.publisher_arduino_avg:main', 
        ],
    },
)
