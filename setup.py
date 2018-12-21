from setuptools import setup

setup(
	name='if-time-at-timezone',
	version='2018.1',
	description='The funniest joke in the world',
	scripts=['bin/if-time-at-timezone'],
	url='https://github.com/elijahr/if-time-at-timezone',
	author='Elijah Shaw-Rutschman',
	author_email='elijahr+projects@gmail.com',
	license='MIT',
	install_requires=[
		'pytz>=2018.7',
	],
	zip_safe=False
)