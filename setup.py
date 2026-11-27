import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_analysis",
    version="5.4.0",
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
    install_requires=["biobb_common==5.4.0"],
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "cpptraj_average = biobb_analysis.ambertools.cpptraj_average:CpptrajAverage.main",
            "cpptraj_bfactor = biobb_analysis.ambertools.cpptraj_bfactor:CpptrajBfactor.main",
            "cpptraj_cluster = biobb_analysis.ambertools.cpptraj_cluster:CpptrajCluster.main",
            "cpptraj_convert = biobb_analysis.ambertools.cpptraj_convert:CpptrajConvert.main",
            "cpptraj_dry = biobb_analysis.ambertools.cpptraj_dry:CpptrajDry.main",
            "cpptraj_image = biobb_analysis.ambertools.cpptraj_image:CpptrajImage.main",
            "cpptraj_mask = biobb_analysis.ambertools.cpptraj_mask:CpptrajMask.main",
            "cpptraj_rgyr = biobb_analysis.ambertools.cpptraj_rgyr:CpptrajRgyr.main",
            "cpptraj_rms = biobb_analysis.ambertools.cpptraj_rms:CpptrajRms.main",
            "cpptraj_rmsf = biobb_analysis.ambertools.cpptraj_rmsf:CpptrajRmsf.main",
            "cpptraj_slice = biobb_analysis.ambertools.cpptraj_slice:CpptrajSlice.main",
            "cpptraj_snapshot = biobb_analysis.ambertools.cpptraj_snapshot:CpptrajSnapshot.main",
            "cpptraj_strip = biobb_analysis.ambertools.cpptraj_strip:CpptrajStrip.main",
            "gmx_cluster = biobb_analysis.gromacs.gmx_cluster:GMXCluster.main",
            "gmx_check = biobb_analysis.gromacs.gmx_check:GMXCheck.main",
            "gmx_energy = biobb_analysis.gromacs.gmx_energy:GMXEnergy.main",
            "gmx_image = biobb_analysis.gromacs.gmx_image:GMXImage.main",
            "gmx_rgyr = biobb_analysis.gromacs.gmx_rgyr:GMXRgyr.main",
            "gmx_rms = biobb_analysis.gromacs.gmx_rms:GMXRms.main",
            "gmx_rmsf = biobb_analysis.gromacs.gmx_rmsf:GMXRmsf.main",
            "gmx_trjconv_str_ens = biobb_analysis.gromacs.gmx_trjconv_str_ens:GMXTrjConvStrEns.main",
            "gmx_trjconv_str = biobb_analysis.gromacs.gmx_trjconv_str:GMXTrjConvStr.main",
            "gmx_trjconv_trj = biobb_analysis.gromacs.gmx_trjconv_trj:GMXTrjConvTrj.main",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
    ],
)
