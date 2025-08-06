import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_analysis",
    version="5.1.1",
    author="Biobb developers",
    author_email="genis.bayarri@irbbarcelona.org",
    description="Biobb_analysis is the Biobb module collection to perform analysis of molecular dynamics simulations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Bioinformatics Workflows BioExcel Compatibility",
    url="https://github.com/bioexcel/biobb_analysis",
    project_urls={
        "Documentation": "http://biobb-analysis.readthedocs.io/en/latest/",
        "Bioexcel": "https://bioexcel.eu/",
    },
    packages=setuptools.find_packages(exclude=["docs", "test"]),
    package_data={"biobb_analysis": ["py.typed"]},
    install_requires=["biobb_common==5.1.0"],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "cpptraj_average = biobb_analysis.ambertools.cpptraj_average:main",
            "cpptraj_bfactor = biobb_analysis.ambertools.cpptraj_bfactor:main",
            "cpptraj_convert = biobb_analysis.ambertools.cpptraj_convert:main",
            "cpptraj_dry = biobb_analysis.ambertools.cpptraj_dry:main",
            "cpptraj_image = biobb_analysis.ambertools.cpptraj_image:main",
            "cpptraj_mask = biobb_analysis.ambertools.cpptraj_mask:main",
            "cpptraj_rgyr = biobb_analysis.ambertools.cpptraj_rgyr:main",
            "cpptraj_rms = biobb_analysis.ambertools.cpptraj_rms:main",
            "cpptraj_rmsf = biobb_analysis.ambertools.cpptraj_rmsf:main",
            "cpptraj_slice = biobb_analysis.ambertools.cpptraj_slice:main",
            "cpptraj_snapshot = biobb_analysis.ambertools.cpptraj_snapshot:main",
            "cpptraj_strip = biobb_analysis.ambertools.cpptraj_strip:main",
            "gmx_cluster = biobb_analysis.gromacs.gmx_cluster:main",
            "gmx_energy = biobb_analysis.gromacs.gmx_energy:main",
            "gmx_image = biobb_analysis.gromacs.gmx_image:main",
            "gmx_rgyr = biobb_analysis.gromacs.gmx_rgyr:main",
            "gmx_rms = biobb_analysis.gromacs.gmx_rms:main",
            "gmx_trjconv_str_ens = biobb_analysis.gromacs.gmx_trjconv_str_ens:main",
            "gmx_trjconv_str = biobb_analysis.gromacs.gmx_trjconv_str:main",
            "gmx_trjconv_trj = biobb_analysis.gromacs.gmx_trjconv_trj:main",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
    ],
)
