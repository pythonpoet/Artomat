import motor_interface
import vision
import image_preperation


img = image_preperation.prepare_image("bbb_logo.jpeg")

app = vision.Vision(motor_interface.MotorInterface(0, 0), 100, 5, 150, spray_point_offset=(0, -25), image_to_print=img)

app.run()