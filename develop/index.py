from ImageGoNord import NordPaletteFile, GoNord

# E.g. Replace pixel by pixel
go_nord = GoNord()
image = go_nord.open_image("E:/Personal/Github/lazy-walls-nord/develop/wallflare234.jpg")
go_nord.convert_image(image, save_path='e:/personal/github/lazy-walls-nord/develop/test.processed.jpg')

# E.g. Avg algorithm and less colors
go_nord.enable_avg_algorithm()
go_nord.reset_palette()
go_nord.add_file_to_palette(NordPaletteFile.POLAR_NIGHT)
go_nord.add_file_to_palette(NordPaletteFile.SNOW_STORM)

# You can add color also by their hex code
#go_nord.add_color_to_palette('#FF0000')

#image = go_nord.open_image("E:/Personal/Github/lazy-walls-nord/develop/wallflare234.jpg")
#go_nord.convert_image(image, save_path='E:/Per.avg.jpg')

# E.g. Quantize

image = go_nord.open_image("e:/personal/github/lazy-walls-nord/develop/wallflare234.jpg")
go_nord.reset_palette()
go_nord.set_default_nord_palette()
quantize_image = go_nord.quantize_image(image, save_path='E:/Personal/Github/lazy-walls-nord/develop/test.quantize.jpg')

# To base64
go_nord.image_to_base64(quantize_image, 'jpeg')
