git_repository(
    name = "io_bazel_rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    # NOT VALID!  Replace this with a Git commit SHA.
    commit = "3175797bd07aac4ff35fa711f0a82285f2005e42",
)

# Only needed for PIP support:
load("@io_bazel_rules_python//python:pip.bzl", "pip_repositories", "pip_import")
pip_import(
	name = "my_deps",
	requirements = "requirements.txt",
)

load("@my_deps//:requirements.bzl", "pip_install")
pip_install()
pip_repositories()
