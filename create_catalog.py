from extension_catalog_model.model import *

# BraiAn extension
braian_version_range_104 = VersionRange(min="v0.5.0")
braian_release_104 = Release(
    name="v1.0.4",
    main_url="https://github.com/carlocastoldi/qupath-extension-braian/releases/download/v1.0.4/qupath-extension-braian-1.0.4.jar",
    version_range=braian_version_range_104
)
braian_version_range_110 = VersionRange(min="v0.6.0")
braian_release_110 = Release(
    name="v1.1.0",
    main_url="https://github.com/carlocastoldi/qupath-extension-braian/releases/download/v1.1.0/qupath-extension-braian-1.1.0.jar",
    version_range=braian_version_range_110
)
braian_extension = Extension(
    name="QuPath BraiAn extension",
    description="A collection of tools for whole-brain data quantification and extraction",
    author="Carlo Castoldi",
    homepage="https://github.com/carlocastoldi/qupath-extension-braian",
    releases=[braian_release_104, braian_release_110]
)

catalog = Catalog(
    name="BraiAn catalog",
    description="Extensions maintained by BraiAn team",
    extensions=[braian_extension]
)

# write the catalog to a file
with open("catalog.json", "w") as f:
    f.write(catalog.model_dump_json(indent=4))
