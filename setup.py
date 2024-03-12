from setuptools import find_packages, setup


setup(
    name="admission-model",
    version="0.0.2",
    author="manojkumar21",
    author_email="mk.chinthakindi@gmail.com",
    install_requiress=['numpy','pandas','seaborn','matplotlib','scikit-learn','statsmodels'],
    packages=find_packages()

)