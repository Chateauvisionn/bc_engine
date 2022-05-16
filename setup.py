from setuptools import find_packages, setup

with open("README.md", encoding="UTF-8") as f:
    long_desc = f.read()

setup(
    name='bc_engine',
    description='An easy to use game engine/framework for python. (fork)',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    version='1.0.0',
    url='https://github.com/Chateauvisionn/bc_engine',
    author='Chateauvisionn',
    author_email='chateauvision@outlook.fr',
    license='MIT',
    keywords='game development',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'panda3d',
        'panda3d-gltf',
        'pillow',
        'screeninfo',
        'pyperclip',
    ],
    extras_require={'extras': [
        'numpy',
        'imageio',
        'psd-tools3',
        'psutil',
        ],
    },
    python_requires='>=3.7',
)
