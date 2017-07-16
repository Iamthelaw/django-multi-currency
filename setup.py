from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='django_multi_currency',
      version='0.0.1',
      description='Simple multy-currency support for any Django project.',
      long_description=readme(),
      keywords='django currency',
      url='http://github.com/iamthelaw/django-multi-currency',
      author='Anton Alekseev',
      author_email='robotehnik@me.com',
      license='MIT',
      packages=['multi_currency'],
      install_requires=[
        'Django>=1.5',
      ],
      test_suite='tests',
      tests_require=[
        'tox',
        'pytest',
        'pytest-cov',
        'pytest-django'
      ],
      include_package_data=True,
      zip_safe=False)
