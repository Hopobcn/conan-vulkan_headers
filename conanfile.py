# -*- coding: utf-8 -*-

from conans import CMake, ConanFile, tools
import os


class VulkanHeadersConan(ConanFile):
    name = "vulkan_headers"
    version = "1.1.106"
    license = "Apache-2.0"
    author = "bincrafters <bincrafters@gmail.com>"
    url = "https://github.com/bincrafters-conan-vulkan_headers"
    homepage = "https://github.com/KhronosGroup/Vulkan-Headers"
    description = "Vulkan Header files and API registry"
    topics = ("vulkan", "khronos", "ghraphics", "api", )
    no_copy_source = True
    exports = ["LICENSE.md", ]
    exports_sources = ["CMakeLists.txt", ]
    generators = "cmake", 

    _source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/KhronosGroup/Vulkan-Headers/archive/v{}.tar.gz".format(self.version)
        sha256 = "42625612d14bb920f0d88361dea01d2e839abba1c3d1515ffd3be0946d4668a4"

        tools.get(source_url, sha256=sha256)
        os.rename("Vulkan-Headers-{}".format(self.version), self._source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install(build_dir=self.build_folder)
        self.copy("LICENSE.txt", src=self._source_subfolder, dst="licenses")

    def package_info(self):
        self.user_info.VULKAN_REGISTRY_PATH = os.path.join(self.package_folder, "share", "vulkan", "registry")
