from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name='meihua-yishu',
    version='1.0.0',
    author='silent780',
    description='梅花易数占卜系统 - 基于传统梅花易数的现代化占卜系统',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/silent780/meihua-yishu",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=requirements,
    extras_require={
        'web': ['fastapi>=0.104.1', 'uvicorn[standard]>=0.24.0'],
        'test': ['pytest>=7.4.3', 'pytest-asyncio>=0.21.1'],
        'dev': ['black>=23.11.0', 'flake8>=6.1.0']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment :: Fortune',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'meihua-server=app:main',
        ],
    },
)