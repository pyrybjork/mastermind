import random
import time

class MasterMind():
    def __init__(self):
        self.board = []
        self.feedback = []
        self.answer = [0, 0, 0, 0]  #correct answer
        self.entry = []             #user input
        self.round = 0

    def reset(self):
        self.round = 0
        self.board = [[0 for x in range(4)] for y in range(9)]
        self.feedback = [[' ' for x in range(2)] for y in range(9)]
        self.entry = [0, 0, 0, 0]
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        for i in range(4):
            self.answer[i] = numbers.pop(random.randint(0, len(numbers)-1))

    def handle_input(self):#handle user input
        user_input = input(': ')
        if user_input.lower() == 'exit': #exit if 'exit'
            exit()
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.entry = []
        for char in user_input: #append valid characters form input to self.entry
            if char in numbers:
                self.entry.append(int(char))
        if len(self.entry) == 4: #check if self.entry is the right length
            return True
        else:
            print('Invalid input')
            return False

    def handle_entry(self):
        self.board[self.round] = self.entry
        temp_answer = [0, 0, 0, 0]
        for i in range(4):
            temp_answer[i] = self.answer[i]
        right_place = 0     #right numbers on right places
        wrong_place = 0     #right numbers on wrong places
        for i in range(4):  #check for right numbers on right places
            if self.entry[i] == temp_answer[i]:
                right_place += 1
                temp_answer[i] = 0
        for i in range(4):  #check for right numbers on wrong places
            if self.entry[i] in temp_answer:
                wrong_place += 1
        self.feedback[self.round][0] = right_place
        self.feedback[self.round][1] = wrong_place
        if right_place == 4: #if player won
            return True
        else:
            return False

    def print_board(self):
        print('')
        for i in range(9):
            print(str(self.feedback[i][0])+str(self.board[i])+str(self.feedback[i][1]))

    def next_round(self):
        self.round += 1
        if self.round == 9:
            return False
        else:
            return True

    def info(self):
        print('Welcome to MasterMind!')
        print('In this game you need to quess 4 digit code made of numbers from 1 to 8 in nine quesses')
        print('On the left side of the board is shown how many numbers you got excatly right.')
        print('On the right side of the board id shown how many of numbers you entered were right, but in the wrong place.')
        print('To exit the game type "exit".')

    def victory(self, time):
        print(f'Correct! The answer was {self.answer}.')
        print(f'It took you {self.round} rounds and {round(time)} seconds to win.')



def main():
    mastermind = MasterMind()
    mastermind.info()
    while True:
        mastermind.reset()
        game = True
        start = time.time()
        mastermind.print_board()
        while game:
            input_check = True
            while input_check:
                input_check = not mastermind.handle_input()
            if mastermind.handle_entry():
                game = False
                end = time.time()
                mastermind.victory(end-start)

            else:
                if mastermind.next_round():
                    pass
                else:
                    print('You lost!')
                    game = False
            mastermind.print_board()

        print('Do you want to play again (y/n)?')
        play_again = input(': ')
        if play_again.lower() == 'y':
            pass
        else:
            exit()


if __name__ == '__main__':
    main()
