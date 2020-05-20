try:
    import kubernetes
    import openshift
    from openshift.dynamic import DynamicClient
    from openshift.dynamic.exceptions import ResourceNotFoundError, ResourceNotUniqueError
    print "Found it"
except ImportError:
    print "Did not find necessary libraries for ansible k8s module"
