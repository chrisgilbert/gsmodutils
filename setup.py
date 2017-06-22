from setuptools import setup, find_packages


setup(
    name="gsmodutils",
    version = "0.0.1",
    description = "Utilities for the management and testing of genome scale models in  a cross platform, open manner.",
    zip_safe = False,
    author = "James Gilbert",
    author_email = "james.gilbert@nottingham.ac.uk",
    url = "",
    license = "MIT",
    packages = ["gsmodutils"],
    entry_points={
        'console_scripts': [
            'gsm_new_project=gsmodutils.gsm_project:main',
            'scrumpy_to_cobra=gsmodutils.scrumpy:scrumpy_to_cobra',
            'gsmodutils=gsmodutils.cliutils:cli',
        ],
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    include_package_data=True
)
