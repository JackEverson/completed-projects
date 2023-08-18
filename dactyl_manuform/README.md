# Dactyl-Manuform
running ZMK

Run commands from zmk/app directory
west build -d build/left -b nice_nano -- -DSHIELD=kyria_left
probably need to add -p/--pristine tag
-DZMK_CONFIG="C:/the/absolute/path/config" Notice that this path should point to the folder labelled config within your zmk-config folder.
