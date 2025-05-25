# TODO: insert robot code here
import rev
import wpilib
from wpilib.drive import DifferentialDrive
from rev import SparkMax
from rev import SparkMaxConfig
import wpilib.drive

class Robot(wpilib.TimedRobot):
    def robotInit(self):

        self.left1 = SparkMax(1, SparkMax.MotorType.kBrushed)
        self.left2 = SparkMax(2, SparkMax.MotorType.kBrushed)
        self.right1 = SparkMax(3, SparkMax.MotorType.kBrushed)
        self.right2 = SparkMax(4, SparkMax.MotorType.kBrushed)


        cfg_left1 = SparkMaxConfig()
        self.left1.configure(cfg_left1, SparkMax.ResetMode.kNoResetSafeParameters, SparkMax.PersistMode.kNoPersistParameters)

        cfg_left2 = SparkMaxConfig()
        cfg_left2.follow(self.left1, False)
        self.left2.configure(cfg_left2, SparkMax.ResetMode.kNoResetSafeParameters, SparkMax.PersistMode.kNoPersistParameters)

        cfg_right1 = SparkMaxConfig()
        cfg_right1.inverted(True)
        self.right1.configure(cfg_right1, SparkMax.ResetMode.kNoResetSafeParameters, SparkMax.PersistMode.kNoPersistParameters)

        cfg_right2 = SparkMaxConfig()
        cfg_right2.follow(self.right1, False)
        self.right2.configure(cfg_right2, SparkMax.ResetMode.kNoResetSafeParameters, SparkMax.PersistMode.kNoPersistParameters)

          # 建立差速驅動物件
        self.drive = DifferentialDrive(self.left1, self.right1)
        self.drive.setMaxOutput(0.5)

        # 使用一個搖桿來控制（Arcade Style）

        self.stick = wpilib.XboxController(0)
    

    def applyDeadzone(self, value, deadzone=0.1):
        return 0 if abs(value) < deadzone else value

    def teleopPeriodic(self):
        # 讀取搖桿輸入，並加入 deadzone 處理
        forward = self.applyDeadzone(self.stick.getLeftY())
        turn = self.applyDeadzone(self.stick.getRightX())

        # 執行 arcadeDrive（前後 + 左右轉）
        self.drive.arcadeDrive(forward, turn)


if __name__ == "_main_":
    import wpilib
    wpilib.run(Robot)
