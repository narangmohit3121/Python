import tkinter
import random
import time
# print(tkinter.TkVersion)

mainwindow = tkinter.Tk()
def load_cards(card_pack):
    # cards = []
    suites = ['club', 'diamond', 'heart', 'spade']
    face_cards = ['jack', 'queen', 'king']
    image_extension = ''
    if tkinter.TkVersion >= 8.6:
        image_extension = '.png'
    else:
        image_extension = '.ppm'
    for suite in suites:
        for value in range(1, 11):
            # file_name = str(value) + '_' + suite + image_extension
            file_name = 'cards/{0}_{1}{2}'.format(value, suite, image_extension)
            # file_name = f'cards/{value}_{suite}{image_extension}'
            # print(file_name)
            card_image = tkinter.PhotoImage(file=file_name)
            card = (value, card_image)
            card_pack.append(card)

        for face_card in face_cards:
            file_name = 'cards/{0}_{1}{2}'.format(face_card, suite, image_extension)
            # print(file_name)
            card_image = tkinter.PhotoImage(file=file_name)
            card = (10, card_image)
            card_pack.append(card)

    return cards


def deal_card(current_deck, frame):
    next_card = current_deck.pop()
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    print(len(current_deck))
    return next_card


# def deal_card_to_player():
#     global deck
#     global player_ace
#     global player_hand
#     global player_score
#     current_card = deal_card(deck, player_card_frame)
#     player_hand.append(current_card)
#     card_value = current_card[0]
#     if current_card[0] == 1 and not player_ace:
#         card_value = 11
#         player_ace = True
#
#     player_score += card_value
#
#     if player_score > 21 and player_ace:
#         player_score -= 10
#     player_score_in_frame.set(player_score)
#     if player_score > 21:
#         resultText.set('Dealer Wins')
#     if player_score == 21:
#         resultText.set('Player wins')
#     print(player_score)
#     print(player_hand)


def deal_card_to_player():
    global player_score
    current_card = deal_card(deck, player_card_frame)
    player_hand.append(current_card)
    player_score = score_hand(player_hand)
    player_score_in_frame.set(player_score)
    if player_score > 21:
        resultText.set('Dealer Wins')
    if player_score == 21:
        resultText.set('Player wins')


def deal_card_to_dealer():
    global deck
    global dealer_ace
    global dealer_hand
    global dealer_score
    current_card = deal_card(deck, dealer_card_frame)
    dealer_hand.append(current_card)
    card_value = current_card[0]
    if card_value == 1 and not dealer_ace:
        card_value = 11
    dealer_score += card_value

    if dealer_score > 21 and dealer_ace:
        dealer_score -= 10
    dealer_score_in_frame.set(dealer_score)
    if dealer_score > 21:
        resultText.set('Player Wins')
    print(dealer_score)
    blackjack()


def score_hand(current_hand:list):
    hand_score = 0
    hand_ace = False
    for current_card in current_hand:
        card_val = current_card[0]
        if card_val == 1 and not hand_ace:
            card_val = 11
            hand_ace = True
        hand_score += card_val
        if hand_score > 21 and hand_ace:
            hand_score -= 10
            hand_ace = False
    return hand_score


def blackjack():
    # time.sleep(3)
    # deal_card_to_player()
    # time.sleep(3)
    # deal_card_to_dealer()
    # time.sleep(3)
    # deal_card_to_player()
    # time.sleep(3)
    # while dealer_score < 17:
    #     deal_card_to_dealer()
    #     time.sleep(3)

    if 17 <= dealer_score <= 21:
        if player_score > dealer_score:
            resultText.set('Player Wins')
        elif player_score < dealer_score:
            resultText.set('Dealer Wins')
        else:
            resultText.set('Match Drawn')
    elif dealer_score > 21:
        resultText.set('Player wins')
    else:
        resultText.set('Dealer must pick a card')


cards = []
load_cards(cards)
deck = list(cards)
random.shuffle(deck)

player_hand = []
player_ace = False
player_score = 0

dealer_hand = []
dealer_ace = []
dealer_score = 0


mainwindow.geometry('640x480')
mainwindow.title('BlackJack')

resultText = tkinter.StringVar()
tkinter.Label(mainwindow, textvariable=resultText).grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainwindow, relief='sunken', borderwidth=2, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_in_frame = tkinter.IntVar()
tkinter.Label(card_frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_in_frame, background='green', fg='white').grid(row=1, column=0)
dealer_card_frame = tkinter.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky='ew')

player_score_in_frame = tkinter.IntVar()
tkinter.Label(card_frame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_in_frame, background='green', fg='white').grid(row=3, column=0)
player_card_frame = tkinter.Frame(card_frame, background='green')
player_card_frame.grid(row=2, column=1, rowspan=2, sticky='ew')

button_frame = tkinter.Frame(mainwindow)
button_frame.grid(row=3, column=0, columnspan=3)
dealer_button = tkinter.Button(button_frame, text='dealer', command=deal_card_to_dealer)
dealer_button.grid(row=0, column=0)
player_button = tkinter.Button(button_frame, text='player', command=deal_card_to_player)
player_button.grid(row=0, column=1)

deal_card_to_player()
deal_card_to_dealer()
deal_card_to_player()

mainwindow.mainloop()


