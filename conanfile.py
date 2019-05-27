# -*- coding: utf-8 -*-

from conans import CMake, ConanFile, tools
import os


class VulkanHeadersConan(ConanFile):
    name = "vulkan_headers"
    version = "1.1.107"
    license = "Apache-2.0"
    author = "bincrafters <bincrafters@gmail.com>"
    url = "https://github.com/bincrafters-conan-vulkan_headers"
    homepage = "https://github.com/KhronosGroup/Vulkan-Headers"
    description = "Vulkan Header files and API registry"
    topics = ("vulkan", "khronos", "ghraphics", "api", )
    no_copy_source = True
    exports = ["LICENSE.md", ]

    _source_subfolder = "source_subfolder"

    def source(self):
        url = "https://github.com/KhronosGroup/Vulkan-Headers/archive/v{}.tar.gz".format(self.version)
        sha256 = "7d00748f3311a89d5a92aea4b11764bb8371dae4ab6291497bcde2fa186bbd31"

        tools.get(url, sha256=sha256)
        os.rename("Vulkan-Headers-{}".format(self.version), self._source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=os.path.join(self.source_folder, self._source_subfolder))
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install(build_dir=self.build_folder)
        self.copy("LICENSE.md", dst="licenses")

    def package_info(self):
        self.user_info.VULKAN_REGISTRY_PATH = os.path.join(self.package_folder, "share", "vulkan", "registry")
