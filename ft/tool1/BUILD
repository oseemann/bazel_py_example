load("@my_deps//:requirements.bzl", "requirement")

py_binary(
	name = 'tool1',
	main = 'tool.py',
	srcs = ['tool.py'],
	deps = [
		'//ft/liba',
		requirement('colored'),
		requirement('psycopg2-binary'),
	],
)
