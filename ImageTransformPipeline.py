# Copyright 2023 antillia.com Toshiyuki Arai
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

# 
# 2023/01/30 copyright (c) antillia.com
#
# class ImageWarpParallelogramer.py
# This is a very simple, primitive parallelogramer to convert a rectangle area of an image to a parallelogram.
#

import os
import sys
import glb
import shutil
import traceback

from ConfiParser import ConfigParser

from ImageWarpRotator import ImageWarpRotator
from ImageWarpTrapezoider import ImageWarpTrapezoider
from ImageWarpParallelogramer import ImageWarpParallelogramer


class ImageTransformPipeline
  def __init__(self, configs_parser):
    pass
    CONFIGS = "configs"
    self.rotator_conf         = config_parser.get(CONFIGS, "rotator_config")
    self.trapezoider_conf     = config_parser.get(CONFIGS, "trapezoider_config")
    self.parallelogramer_conf = config_parser.get(CONFIGS, "parallelogramer_config")


  def run(self, images_dir, output_dir):
     # TO DO      
     pass


if __name__ == "__main__":
  try:
    pipeline = ImageTransformPipeline()
   
  except:
    traceback.print_exc()

