from setuptools import setup, find_packages
 
setup(
    include_package_data=True,
	name="vencryption2",
	version="1.0",
	packages=find_packages(), # permet de récupérer tout les fichiers 
	description="(De)cryption softwares. Allows you to encrypt or decrypt text based on different encryption keys.",
	url="https://encryption.nexcord.pro/",
	author="V / Lou du Poitou",
	license="ISC",
	python_requires=">=3.9.7",
    install_requires=["requests"],
    requires=["requests"]
)