# When trying to use the k8s module in ansible on a system without the necessary python library, the error is thrown:

An exception occurred during task execution. To see the full traceback, use -vvv. The error was: ImportError: No module named kubernetes
fatal: [127.0.0.1]: FAILED! => {"changed": false, "error": "No module named kubernetes", "msg": "Failed to import the required Python library (openshift) on clientvm.c243.internal's Python /usr/bin/python2. Please read module documentation and install in the appropriate location"}

install-packages-k8s-module.yml
