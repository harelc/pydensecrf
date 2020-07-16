# coding: UTF-8
from setuptools import setup
import sys
# TODO:
# - Wrap learning.
# - Make LabelCompatibility, UnaryEnergy, PairwisePotential extensible? (Maybe overkill?)

from setuptools.extension import Extension

extra_compile_args = []
extra_link_args = []
if sys.platform == 'darwin':
    extra_compile_args.append("-stdlib=libc++")
    extra_link_args.append("-stdlib=libc++")
    extra_link_args.append("-mmacosx-version-min=10.9")

ext_modules = [
Extension("pydensecrf/eigen", ["pydensecrf/eigen.cpp", "pydensecrf/eigen_impl.cpp"],
          language="c++",
          include_dirs=["pydensecrf/densecrf/include"],
          extra_compile_args=extra_compile_args, extra_link_args=extra_link_args),
Extension("pydensecrf/densecrf", ["pydensecrf/densecrf.cpp", "pydensecrf/densecrf/src/densecrf.cpp",
                                  "pydensecrf/densecrf/src/unary.cpp", "pydensecrf/densecrf/src/pairwise.cpp",
                                  "pydensecrf/densecrf/src/permutohedral.cpp", "pydensecrf/densecrf/src/optimization.cpp",
                                  "pydensecrf/densecrf/src/objective.cpp", "pydensecrf/densecrf/src/labelcompatibility.cpp",
                                  "pydensecrf/densecrf/src/util.cpp", "pydensecrf/densecrf/external/liblbfgs/lib/lbfgs.c"],
          language="c++", include_dirs=["pydensecrf/densecrf/include", "pydensecrf/densecrf/external/liblbfgs/include"],
          extra_compile_args=extra_compile_args, extra_link_args=extra_link_args),
]

setup(
    name="pydensecrf",
    version="1.0rc2",
    description="A python interface to Philipp Krähenbühl's fully-connected (dense) CRF code.",
    long_description="See the README.md at http://github.com/lucasb-eyer/pydensecrf",
    author="Lucas Beyer",
    author_email="lucasb.eyer.be@gmail.com",
    url="http://github.com/lucasb-eyer/pydensecrf",
    ext_modules=ext_modules,
    packages=["pydensecrf"],
    setup_requires=['cython>=0.22'],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: C++",
        "Programming Language :: Python",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
