#!/bin/bash

# Define variables
VERSION="0.0.1"  # Replace this with your desired version number
PROJECT_NAME="getman"  # Replace with your project name

# Function to update version in the necessary files
function update_version() {
    sed -i "s/__version__ = .*/__version__ = '${VERSION}'/" your_project_name/__init__.py
    echo "Updated version to ${VERSION}"
}

# Function to create a git tag for the release
function create_git_tag() {
    git tag -a "v${VERSION}" -m "Version ${VERSION} release"
    git push origin "v${VERSION}"
    echo "Created and pushed git tag v${VERSION}"
}

# Function to build and publish the package to PyPI
function publish_to_pypi() {
    # Activate your virtual environment (if applicable)
    source path_to_your_virtualenv/bin/activate

    # Build the distribution package
    python setup.py sdist bdist_wheel

    # Install twine (if not installed)
    pip install twine

    # Upload the package to PyPI
    twine upload dist/*

    echo "Published version ${VERSION} to PyPI"
}

# Main release process
update_version
create_git_tag
publish_to_pypi

echo "Release process completed successfully!"
