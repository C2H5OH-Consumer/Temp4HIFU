from setuptools import setup, find_packages

opts = setup(
    name = 'Temp4HIFU',
    version = '0.1.0',
    url='',
    author = 'Gerald Lee',
    author_email = 'gerald13@uw.edu',
    description = 'Package Description',
    packages = find_packages(),
    package_data = {'Temp4HIFU': ['Scripts/*','tests/*']}
)

if __name__ == '__main__':
    setup(**opts)