import cozmo
# pip uninstall cozmoclad
# pip install https://raw.githubusercontent.com/DDLbots/cozmo-python-sdk/refs/heads/master/cozmoclad/cozmoclad-3.6.6-py3-none-any.whl

def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Hello World! I'm Cozmo and I can do many things").wait_for_completed()

    robot.drive_straight(distance=cozmo.util.distance_mm(300),
                         speed=cozmo.util.speed_mmps(100)).wait_for_completed()

    robot.turn_in_place(cozmo.util.degrees(180)).wait_for_completed()

cozmo.run_program(cozmo_program)
