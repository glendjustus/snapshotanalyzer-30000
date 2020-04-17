from setuptools import setup

setup(
    name='snapshotanalyzer-3000',
    version='0.1',
    author="Glen Justus",
    author_email="test@test.com",
    description="SnapshotAnalyzer 3000 is a tool to manage AWS EC@ snapshots",
    license="GPLv3+",
    packaged=['shotty'],
    url="https://github.com/glendjustus/snapshotanalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
