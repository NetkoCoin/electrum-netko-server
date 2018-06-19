from setuptools import setup

setup(
    name="electrum-netko-server",
    version="1.0",
    scripts=['run_electrum_netko_server.py','electrum-netko-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumnetkoserver':'src'
        },
    py_modules=[
        'electrumnetkoserver.__init__',
        'electrumnetkoserver.utils',
        'electrumnetkoserver.storage',
        'electrumnetkoserver.deserialize',
        'electrumnetkoserver.networks',
        'electrumnetkoserver.blockchain_processor',
        'electrumnetkoserver.server_processor',
        'electrumnetkoserver.processor',
        'electrumnetkoserver.version',
        'electrumnetkoserver.ircthread',
        'electrumnetkoserver.stratum_tcp',
        'electrumnetkoserver.stratum_http'
    ],
    description="netko Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.deg",
    maintainer="netko",
    maintainer_email="support@netko.org",
    license="GNU Affero GPLv3",
    url="https://github.com/netko/electrum-netko-server/",
    long_description="""Server for the Electrum Lightweight netko Wallet"""
)


