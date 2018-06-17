import setuptools

cvalidator = setuptools.Extension('cvalidator', sources=['cvalidator.c'])

if __name__ == '__main__':
    setuptools.setup(
        name='CVAlidator',
        version='1.0',
        ext_modules=[cvalidator],
    )
