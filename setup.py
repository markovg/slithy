from distutils.core import setup
setup(name = "slithy", version = "slithy-hg-tip",
      packages = ["slithy"],
      package_data={'slithy': ['*.so', 'fonts/*','rst2pdf_*']})
