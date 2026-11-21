from setuptools import setup

package_name = "dogx_rl"

setup(
    name=package_name,
    version="0.1.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Jerome Graves",
    maintainer_email="you@example.com",
    description="ROS 2 node that runs a learned locomotion policy for the Dogx quadruped.",
    license="MIT",
    entry_points={
        "console_scripts": [
            "policy_node = dogx_rl.policy_node:main",
        ],
    },
)
