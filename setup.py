from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="wagtail-purge",
    version="0.3.0",
    description="Purge individual URLs from the Wagtail admin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/torchbox/wagtail-purge",
    author="Tom Dyson",
    author_email="tom+wagtailpurge@torchbox.com",
    license="MIT",
    classifiers=[
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 4",
        "Framework :: Wagtail :: 5",
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
        "wagtail>=4.1,<6.0",
    ],
)
