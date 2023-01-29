# Copyright 2022 antillia.com Toshiyuki Arai 
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

# ImageSharpener.py


import os
import sys
import glob

import cv2

import numpy as np
import traceback


class ImageSharpener:
  def __init__(self):
    pass

  def run(self, images_dir, output_dir):
    ks = [2, 3, 4, 5, 6]
    png_files = glob.glob(images_dir + "/*.png")
    jpg_files = glob.glob(images_dir + "/*.jpg")
    image_files = png_files + jpg_files
    for image_file in image_files:
      basename = os.path.basename(image_file)
      
      for k in ks:
        output_image_file = os.path.join(output_dir, str(k) + "_" + basename)
  
        self.sharpen(image_file, k, output_image_file)


        
  def sharpen(self, image_file, k, output_image_file):
     
    matrix = np.array([[0, -k,           0],
                        [-k, 1 + 4 * k, -k],
                        [0, -k,          0]])
 
    img_src = cv2.imread(image_file, 3)

    img_tmp = cv2.filter2D(img_src, -1, matrix)
    sharpened = cv2.convertScaleAbs(img_tmp)
    cv2.imwrite(output_image_file, sharpened)

    cv2.imshow("Show SHAPE Image", sharpened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
  input_dir  = ""
  outout_dir = ""

  try:
    if len(sys.argv) == 3:
      input_dir  = sys.argv[1]
      output_dir = sys.argv[2]
       
    if not os.path.exists(input_dir):
      raise Exception("Not found " + input_dir)
    if not os.path.exists(output_dir):
      os.makedirs(output_dir)

    sharpener = ImageSharpener()
    sharpener.run(input_dir, output_dir)
  
  except:
    traceback.print_exc()

  