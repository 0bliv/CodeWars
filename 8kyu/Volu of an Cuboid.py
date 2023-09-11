def get_volume_of_cuboid(length, width, height):
    
    if length <= 0 or width <= 0 or height <= 0:
        return 0
    else:
        volume = length * width * height
        return volume