from distutils.core import setup

setup(
    name="EasyConfig",
    packages=["EasyConfig"],
    version="0.1.0",
    license="MIT",
    description="An easy-to-use configuration package using YAML",
    author="Lars Eppinger",
    author_email="pypi@eppinger.dev",
    url="https://github.com/lars250698/easyconfig",
    download_url="https://github.com/lars250698/easyconfig/archive/v_0_1_0.tar.gz",
    keywords=["config", "configuration", "yaml", "easyconfig"],
    requires=["pyyaml"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ]
)