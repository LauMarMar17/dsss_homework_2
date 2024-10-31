from setuptools import setup, find_packages

setup(
    name='math_quiz',  # Nombre de tu paquete
    version='0.1',  # Versión del paquete
    packages=find_packages(),  # Encuentra todos los paquetes en tu proyecto
    install_requires=[
        # Lista de dependencias aquí, si tienes alguna
        # Ejemplo: 'numpy', 'pandas',
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:main',  # Ajusta según tu archivo principal
        ],
    },
)