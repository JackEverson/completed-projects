# Dactyl-Manuform
running ZMK

Run commands from zmk/app directory


west build -p -d build/left -b nice_nano -- -DSHIELD=dactyl_manuform_left -DZMK_CONFIG="/home/jack/code/zmk-config/config/"
west build -p -d build/right -b nice_nano -- -DSHIELD=dactyl_manuform_right -DZMK_CONFIG="/home/jack/code/zmk-config/config/"

west build -p -d build/left -b nice_nano -- -DSHIELD=redox_left
probably need to add -p/--pristine tag
-DZMK_CONFIG="/home/jack/code/zmk-config/config/" 
-DZMK_CONFIG="C:/the/absolute/path/config" Notice that this path should point to the folder labelled config within your zmk-config folder.





