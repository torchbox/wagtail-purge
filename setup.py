from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="wagtail-purge",
    version=0.1,
    description="Purge individual URLs from the Wagtail admin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tomdyson/wagtail-purge",
    author="Tom Dyson",
    author_email="tom+wagtailpurge@torchbox.com",
    license="MIT",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    keywords="development",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "wagtail>=2",
    ],
)