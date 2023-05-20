from setuptools import setup, find_packages

setup(name='python_bot',
      python_requires='>=3.9',
      version='0.1',
      description='Python bot addressbook. Team 4 PythonCore 12 final project.',
      url='https://github.com/NightSpring1/PythonCore_FinalProject_Team4',
      author='Team 4',
      author_email='bazhenov.nikita27@gmail.com',
      license='MIT license',
      packages=find_packages(),
      install_requires=[],
      entry_points={'console_scripts': ['bot-start = python_bot:main']})
