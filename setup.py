from setuptools import setup, find_packages


setup(name='cytounet',
      version="0.2.0",
      description='Deep Learning based Cell Segmentation',
      url="http://www.github.com/Nelson-Gon/cytounet",
      download_url="https://github.com/Nelson-Gon/cytounet/archive/v0.2.0.zip",
      author='Nelson Gonzabato',
      author_email='gonzabato@hotmail.com',
      license='MIT',
      keywords="keras tensorflow images image-analysis deep-learning biology",
      packages=find_packages(),
      long_description=open('README.md').read(),
      python_requires='>=3.6',
      long_description_content_type='text/markdown',
      zip_safe=False)
