from setuptools import setup

requires = [
    'pyramid',
    'waitress',
]

setup(name='server',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = server:main
      """,
)