#!/usr/bin/env python3
'''
    This is a demo program showing the use of the RobotDrive class,
    specifically it contains the code necessary to operate a robot with
    tank drive.
    
    WARNING: While it may look like a good choice to use for your code if
    you're inexperienced, don't. Unless you know what you are doing, complex
    code will be much more difficult under this system. Use IterativeRobot
    or Command-Based instead if you're new.
'''

import wpilib

class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
        '''Robot initialization function'''
        # object that handles basic drive operations
        self.myRobot = wpilib.RobotDrive(0, 1)
        self.myRobot.setExpiration(0.1)
        
        self.gamePad = wpilib.Joystick(0)
        
    def teleopPeriodic(self):
        '''Runs the motors with tank steering'''
        self.myRobot.setSafetyEnabled(True)
        self.myRobot.tankDrive(self.gamePad.getRawAxis(2), self.gamePad.getRawAxis(3))
        wpilib.Timer.delay(0.005) # wait for a motor update time
            
if __name__ == '__main__':
    wpilib.run(MyRobot)
