from setuptools import setup, find_packages

setup(
    name='q2-parser',
    version='0.0.1',
    packages=find_packages(),
    author='Keegan Evans',
    author_email='KeeganEvans@nau.edu',
    url='qiime2.org',
    license='BSD-3-Clause',
    description='A general tool to streamline the process of parsing and'
                 'importing raw data into QIIME 2 formats and types',
    entry_points={
        'qiime2.plugins':
        ['q2-parser=q2_parser.plugin_setup:plugin']
    },
    package_data={
        'q2_parser.tests': [
            'data/*',
        ],
    },
    zip_safe=False,
)
