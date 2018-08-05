from setuptools import setup
from pip.req import parse_requirements
install_reqs = parse_requirements("requirements.txt", session='k')

reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='EksiPack',
    version='1.0.0',
    packages=['EksiPack'],
    url='https://github.com/kemalcanbora/EksiApi',
    license='BSD',
    package_data={'': ['EksiPack/*.py']},
    author='Kemalcan Bora',
    author_email='kemalcanbora@gmail.com',
    description='Eksisözlük python api resmi olmayan versiyonu.',
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=reqs
)