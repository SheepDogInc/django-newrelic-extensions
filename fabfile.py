from fabric.api import local


def publish():
    print "Please do the following before publishing:"
    print "  - Update version in setup.py"
    print "  - Update version in newrelicextensions/__init__.py"
    print "  - Update the changelog"
    print "  - Tag the release in git and push the tag to Github"
    print "  - Make sure you know the PyPI credentials"
    print "Are you ready to continue? [y/n]"
    a = raw_input()
    if a != 'y':
        print 'Aboring...'
        return
    local('python setup.py register sdist upload')
