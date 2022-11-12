from goprocam import GoProCamera, constants
gopro = GoProCamera.GoPro(constants.gpcontrol)
gopro.overview()

# gopro.stream("udp://127.0.0.1:10000", quality="medium")
gopro.take_photo()

# gopro.shoot_video(10)

# gopro.downloadLastMedia()
# gopro.downloadLastMedia("pic.JPG")

# gopro.downloadAll()