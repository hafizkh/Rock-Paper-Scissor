import unittest
import rpsUtils

class rock_paper_scissors_class(unittest.TestCase):
    def test_if_Result_Draw(self):
       # Arrange
        computer = str("rock")
        user = "rock"
        expectedResult = str("Reuslt is Draw")
        # Act
        result = rpsUtils.rock_paper_scissor(user,computer)
        # Assert
        self.assertEqual(result,expectedResult)

    def test_if_User_Lost(self):
        # Arrange
        computer = str("paper")
        user = "rock"
        expectedResult = str("Computer Won")
        # Act
        result = rpsUtils.rock_paper_scissor(user,computer)
        # Assert
        self.assertEqual(result,expectedResult)

    def test_if_User_Won(self):
        # Arrange
        computer = str("scissor")
        user = "rock"
        expectedResult = str("User Won")
        # Act
        result = rpsUtils.rock_paper_scissor(user,computer)
        # Assert
        self.assertEqual(result,expectedResult)
    
if __name__ == "__main__":
    unittest.main()     
