try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='ros-dependency-manager',
    version='0.0.1',
    description='Dependency Manager for ROS',
    author='Maxime St-Pierre',
    author_email='me@maximest-pierre.me',
    packages=['ros-dependency-manager'],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)