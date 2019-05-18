# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Arduino

Arduino Wiring-based Framework allows writing cross-platform software to
control devices attached to a wide range of Arduino boards to create all
kinds of creative coding, interactive objects, spaces or physical experiences.
"""

from os import listdir
from os.path import isdir, join

from SCons.Script import DefaultEnvironment

import re

env = DefaultEnvironment()
platform = env.PioPlatform()
board = env.BoardConfig()
variant = board.get("build.variant")

FRAMEWORK_DIR = platform.get_package_dir("framework-linuxduino")
assert isdir(FRAMEWORK_DIR)

CORE_DIR = join(FRAMEWORK_DIR, "src")
assert isdir(CORE_DIR)

env.Append(
    CPPPATH=[
        join(CORE_DIR, "linux_headers"),
        join(CORE_DIR, "Linuxduinoh"),
        join(CORE_DIR, "Arduinoh"),
        join(CORE_DIR),
    ],

    LINKFLAGS=[
        "-pthread"
    ],
)

libs = []

libs.append(
    env.BuildLibrary(
        join("$BUILD_DIR", "FrameworkArduinoWrapper"),
        join(CORE_DIR, "Arduinoh")))

libs.append(
    env.BuildLibrary(
        join("$BUILD_DIR", "FrameworkArduino"),
        join(CORE_DIR)))

env.Prepend(LIBS=libs)
