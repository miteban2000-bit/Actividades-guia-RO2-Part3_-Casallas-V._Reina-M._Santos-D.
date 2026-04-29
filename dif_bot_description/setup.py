from setuptools import setup
import os
from glob import glob

package_name = 'dif_bot_description'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('activity4/launch/*.py')),
        (os.path.join('share', package_name, 'urdf'), glob('activity4/urdf/*.xacro')),
        (os.path.join('share', package_name, 'rviz'), glob('activity4/rviz/*.rviz')),
        (os.path.join('share', package_name, 'worlds'), glob('activity4/worlds/*.world')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Esteban',
    maintainer_email='esteban@example.com',
    description='Robot diferencial en URDF/Xacro',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
