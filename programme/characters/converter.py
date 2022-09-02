from dan import dan_speak
from mr_brown import mr_brown_speak
from mike import mike_speak
from jessica import jessica_speak
from mary import mary_speak
from author import author_speak
from security import sec_speak
from security2 import sec2_speak
from cry import cry_speak


def converting():

    print('\nYou went to the toilet...')
    author_speak('<speak>Select difficulty level<break time="1s"/>(story<break time="1s"/>or hard)</speak>', 1)
    author_speak('<speak>You chose a story difficulty level.</speak>', 2)
    author_speak('<speak>Let me tell you one story in which you will take part.</speak>', 3)
    author_speak('<speak><p>One day suddenly a security guard found a dead body on the stairs of the City Center Mall.</p>'
                 '<p>The security guard was horrified when he saw that.</p><p>Frightened, he immediately called the police.</p>'
                 '<p>He was very scared and could not even speak properly in the call.</p><p>He said to the police, "Hello, come here quickly.'
                 'Somebody’s dead body is here. A corpse is in front of me."</p>'
                 '<p>Saying this, he immediately disconnected the phone and sat in a chair nearby.</p></speak>', 4)
    author_speak('<speak><p>But detective Dan Kaliny arrived faster.</p></speak>', 5)
    dan_speak('<speak><p>"Wow, what a wonderful day it is.</p>'
              '<p>I get up early this morning, had breakfast with a fresh croissant with poppy seed cream filling.</p>'
              '<p>Then I immediately go to the gym "Kalinka". It was the best training I have ever made.</p>'
              '<p>After training, I wanted to meet with my friend Mike, I haven`t seen him for a long time.</p>'
              '<p>I have to meet him at one o\'clock.</p><p>Ohh, I`m late."</p></speak>', 1)
    author_speak('<speak><p>You walked into the mall.</p></speak>', 6)
    dan_speak("<speak>What a change this mall has made, and just a month ago, it almost burned down.</speak>", 2)
    author_speak('<speak>And then you saw a crowd of people standing on the stairs and looking at something.</speak>', 7)
    author_speak(
        '<speak>What will you do first?<break time="1s"/>'
        '(go to the toilet,<break time="1s"/>'
        'call to friend to know where is he,<break time="1s"/>'
        'approach the crowd.)</speak>', 8)

    author_speak('<speak>You went to the toilet.</speak>', 9)
    dan_speak('<speak><p>"Ohh,<break time="1s"/>this is what I’ve been waiting for."</p>'
              '<p>Ooohh<break time="2s"/>aaahhh<break time="2s"/>mmmmm<break time="2s"/>well done!</p></speak>', 3)
    author_speak(
        '<speak><p>After you peed a little, you saw that the police had arrived and you won`t be able to examine the corpse.</p>'
        '<prosody rate="x-slow"><p>GAME OVER</p></prosody>!</speak>', 10)
    author_speak('<speak>You start calling Mike.</speak>', 11)
    author_speak('<speak><prosody rate="x-slow">RING.<break time="2s"/>RING.<break time="2s"/>RING.<break time="2s"/>RING</prosody>.</speak>', 12)
    dan_speak(
        '<speak><s>"Strange,<break time="1s"/>maybe he can\'t hear?</s><s>Perhaps he is among that crowd, and there he definitely won’t hear the call."</s></speak>', 4)
    author_speak('<speak><p>You approached the crowd and saw the corpse.</p>'
                 '<p>There were shouts from the crowd.</p></speak>', 13)
    cry_speak('<speak><prosody pitch="high"><s>Ohh, It can`t be.</s><s>I don`t believe it!</s></prosody></speak>', 1)
    author_speak(
        '<speak><p>You start to investigate body.</p><p>An ID card was found on the man’s shirt with his name written on it.</p>'
        '<p>His name was "Mike Williams", an employee of a company.</p></speak>', 14)
    dan_speak('<speak><s>It`s Mike, my old friend.</s><s>It`s impossible!</s></speak>', 5)
    author_speak('<speak><p>You saw fire scars on the arms.</p></speak>', 15)
    dan_speak('<speak>"Hmm,<break time="1s"/>I guess he\'s a bad cook"</speak>', 6)
    author_speak('<speak><p>After examining the body, you realized that there were non-bullet and no stab wounds.</p></speak>', 16)
    dan_speak("<speak>So he was poisoned.</speak>", 7)
    author_speak('<speak>Now you had to know who killed Mike and who left him here?</speak>', 17)
    dan_speak("<speak>I`m sure it`s not an accident, he was killed by someone.</speak>", 8)
    author_speak('<speak><p>After knowing all this, you made the decision.</p>'
                 '<p>You went to Mike’s house.</p></speak>', 18)
    author_speak(
        '<speak><s>On there way home, you told the sad news to his family.</s><s>They were deeply saddened to hear of Mike`s death.</s></speak>', 19)
    dan_speak("<speak><p>I need to ask his family if they know something.</p>"
              "<p>Have you seen how Mike burn his hands?</p></speak>", 9)
    author_speak('<speak>Suddenly the wife took you to the kitchen, locked the door and she said:</speak>', 20)
    jessica_speak('<speak><p>A month and a half ago, Mike came home from work and told me.</p></speak>', 1)
    mike_speak(
        "<speak><p>In two weeks we will be rich, pay off all our debts, move to the New Orleans and start a new life.</p></speak>", 1)
    jessica_speak('<speak>Then I ask: "What`s happening?".</speak>', 2)
    jessica_speak('<speak><p>He said.</p></speak>', 3)
    mike_speak("<speak><p>Please don`t ask me nothing, just wait.</p>"
               "<p>And one more request, do not come to the mall on June seven, I will be very busy.</p></speak>", 2)
    jessica_speak('<speak>I told, "Okay". But my thoughts were lousy.</speak>', 4)
    dan_speak('<speak>And the fire was happened on the seventh.</speak>', 10)
    jessica_speak('<speak><p>Yes.</p><p>That evening I saw in news that City Center Mall was burning,'
                  'at once I start ringing to Mike`s phone, but he didn\'t answer the phone.</p>'
                  '<p>That night he came home.</p><p>He had blisters on his hands, they were burned.</p>'
                  '<p>He said, by reason of the fire he burned his arms.</p><p>To this day, we have treated his hands.</p></speak>',
                  5)
    dan_speak('<speak>Hmm,<break time="1s"/>Okay. Today we have<break time="1s"/>July tenth and during this time you have not moved to New Orleans yet?</speak>', 11)
    jessica_speak('<speak><s>After the fire he`s not himself.</s><s>He was in conflict with his superiors every day.</s></speak>', 6)
    dan_speak('<speak>And he told you something about it?</speak>', 12)
    jessica_speak('<speak>Nope.</speak>', 7)
    dan_speak('<speak>Hmm,<break time="1s"/>thank you, miss, for your cooperation.</speak>', 13)
    author_speak('<speak><p>After inquiring thoroughly, you thought of going to Mike`s office.</p>'
                 '<p>You came to the mall again.</p></speak>', 21)
    dan_speak('<speak><p>Jeez!</p><p>How many police officers here.</p></speak>', 14)
    author_speak('<speak><p>In the corner you saw an old friend.</p><p>In childhood, you were all friends, Mike, Mary and you.</p></speak>', 22)
    author_speak('<speak>You decided to go to Mary.</speak>', 23)
    dan_speak('<speak><p>She looked terrible.</p><p>She cried non-stop.</p><p>I\'m embarrassed.</p>'
              '<p>Hi, Mary,<break time="1s"/>my regrets. I still can\'t believe it myself.</p></speak>', 15)
    mary_speak('<speak>Wow, <break time="1s"/>Dan, like I haven\'t seen you for ages.</speak>', 1)
    author_speak('<speak>She hugged you. And cried even more on your chest.</speak>', 24)
    dan_speak('<speak>Hmm, she was excessively in love with him in childhood, and maybe now.</speak>', 16)
    mary_speak('<speak>What are you doing here, Dan?</speak>', 2)
    dan_speak('<speak>I was supposed to meet Mike here.</speak>', 17)
    author_speak('<speak>You saw the recorder in her hand.</speak>', 25)
    dan_speak('<speak><p>Are you recording someone?</p><p>"I know that she`s a journalist"</p></speak>', 18)
    author_speak('<speak>She was confused.</speak>', 26)
    mary_speak('<speak>Oh, It was Mike`s recorder. He left it to me and said that he would pick it up at one o\'clock.</speak>', 3)
    dan_speak("<speak>There is something important and I need to get it.</speak>", 19)
    author_speak('<speak>You suggested to move her to an uninhabited place.</speak>', 27)
    dan_speak(
        '<speak><s>Mary,<break time="1s"/>you understand that Mike did not just leave the recorder for you, it contains a certain secret.</s>'
        '<s>And since he`s already been killed, it`s time to take advantage of it.</s></speak>', 20)
    mary_speak('<speak>Hmm.<break time="2s"/></speak>', 4)
    author_speak('<speak>She looked around, making sure no one was around. And turned on the recorder.</speak>', 28)
    dan_speak('<speak><p>After recording. Everything cleared up.</p>'
              '<p>The mall owner killed Mike.</p></speak>', 21)
    dan_speak('<speak><p>Mary, please approach the police in fifteen minutes and tell them'
              'that the owner knows some information about the victim.</p><p>In the meantime, I`ll go to Mister Brown.</p></speak>', 22)
    mary_speak('<speak><prosody pitch="high">Good luck.</prosody></speak>', 5)
    author_speak('<speak><p>You took the elevator up to the nineteenth floor.</p>'
                 '<p>When you arrived you saw a long corridor in front of the owner`s office, where a security guard was sitting.</p></speak>', 29)
    author_speak('<speak>He asked:</speak>', 30)
    sec_speak('<speak>Who are you?</speak>', 1)

    author_speak('<speak>What do you say?<break time="1s"/>("I`m a police officer"(1),<break time="1s"/>"I`m detective"(2))</speak>', 31)
    dan_speak('<speak>I`m a police officer.</speak>', 23)
    sec_speak('<speak>Ohh,<break time="1s"/>Yes,<break time="1s"/>what do you need?</speak>', 2)
    dan_speak('<speak>Can I approached to the owner`s cabinet?</speak>', 24)
    author_speak('<speak><p>He called on the phone and after a few sentences, he hung up.</p><p>He said.</p></speak>', 32)
    sec_speak('<speak>Please pass.</speak>', 3)

    dan_speak('<speak>I`m detective.</speak>', 25)
    sec_speak('<speak>Hmm,<break time="1s"/>You have the wrong floor sir.</speak>', 4)
    dan_speak('<speak>No, friend, it`s you who made a mistake.</speak>', 26)
    sec_speak('<speak><prosody pitch="x-high">Hey Bobby, I found entertainment for us.</prosody></speak>', 5)
    author_speak('<speak>Comes out a big bearded man.</speak>', 33)
    sec2_speak('<speak>I LOVE FUN, AHAHAHA.</speak>', 1)
    dan_speak('<speak><prosody pitch="high">"Ohh shit".</prosody></speak>', 27)
    author_speak('<speak><prosody pitch="x-high">BAAANG<break time="2s"/>BOOOM<break time="2s"/>BAAAM<break time="2s"/>DOOOM.</prosody></speak>', 34)
    dan_speak('<speak>It wasn\'t too easy.</speak>', 28)

    author_speak('<speak>You enter to to the owner`s cabinet.</speak>', 35)
    author_speak('<speak><p>You saw Mister Brown.</p>'
                 '<p>He was a big, beefy man with hardly any neck, although he did have a very large mustache.</p>'
                 '<p>His face was almost completely hidden by a long, shaggy mane of hair and a wild, tangled beard,'
                 'but you could make out his eyes, glinting like black beetles under all the hair.</p></speak>', 36)
    dan_speak('<speak><p>Hello, Mister Brown.</p></speak>', 29)
    mr_brown_speak('<speak>Hello, mister<break time="1s"/></speak>', 1)
    dan_speak('<speak>Kaliny.</speak>', 30)
    dan_speak('<speak><p>I have a few questions for you.</p><p>I know that you killed Mike Williams.</p>'
              '<p>I give you a chance to tell everything yourself.</p></speak>', 31)
    mr_brown_speak('<speak><p>Are you kidding me?</p><p>This is some sort of a gamble.</p><p>I didn\'t kill him.</p></speak>', 2)
    dan_speak('<speak>Let me refresh your memory.</speak>', 32)

    author_speak('<speak>Who set fire to the mall?</speak>', 37)
    author_speak('<speak>No, please think and answer again.</speak>', 38)
    dan_speak('<speak><p>It was YOU who convinced Mike to set fire to the mall.</p>'
              '<p>You insured the mall before you burned it down.'
              'But you wanted to play it safe and agreed with Mike to set fire to the building.</p>'
              '<p>You promised him twenty percent of the amount.</p></speak>', 33)
    author_speak('<speak>Mister Brown sighed nervously.</speak>', 39)

    author_speak('<speak>What body part did Mike burn?</speak>', 40)
    dan_speak('<speak><p>When Mike set fire to the center, he burned his hands.</p>'
              '<p>It`s strange, because all your personnel were evacuated and not a single one was injured.</p></speak>', 34)
    mr_brown_speak('<speak>Keep going.</speak>', 3)

    author_speak('<speak>What June did the fire happen?</speak>', 41)
    dan_speak(
        '<speak><p>After June seventh, when the fire broke out, you did not give the promised money to Mike'
        'for a whole month.</p><p>Then he began to blackmail you by recording your conversation.</p>'
        '<p>You wanted to get a voice recorder. And then.</p></speak>', 35)
    author_speak(
        '<speak>How was Mike killed?<break time="1s"/>(shoot,<break time="1s"/>stabbed<break time="1s"/>or poisoned)</speak>',
        42)
    dan_speak('<speak><p>You met with him on the pretext that you would hand over the money.</p>'
              '<p>But in the end you poisoned him! But Mike expected it.</p>'
              '<p>He left the dictaphone to the journalist.</p>'
              '<p>You will go to jail for fifteen years, do you understand that?</p></speak>', 36)
    mr_brown_speak('<speak><p>I still have time to run Mister Kaliny.</p> '
                   '<prosody pitch="high"><p>Security!</p></prosody></speak>', 4)
    dan_speak('<speak><s>It won\'t help.</s><s>Cause the police will come in three.</s></speak>', 37)
    dan_speak('<speak>two.<break time="1s"/></speak>', 38)
    dan_speak('<speak>one.<break time="1s"/></speak>', 39)
    author_speak('<speak>"Knock-Knock-Knock".</speak>', 43)
    author_speak('<speak><p>The police come in.</p>'
                 '<p>Mister Brown looks frightened, he abruptly opens the window and jumps out of it.</p></speak>', 44)
    dan_speak('<speak>"And he jumped from a height of a nineteenth-storey building, by the way"</speak>', 40)
    author_speak('<speak>One of the cops asks: What`s happening?</speak>', 45)
    dan_speak('<speak><p>He said, "His last desire was to fly".</p><p>He made it.</p></speak>', 41)
    author_speak('<speak>Conclusion<break time="2s"/>'
                 '<p>The owner of the shopping center, Mister Brown, crashed from a bird\'s eye view.</p>'
                 '<p>Miss Mary published an article about the whole situation and became '
                 'the most in-demand journalist in the USA.</p>'
                 '<p>Well, our detective Dan Kaliny will be back with a new investigation.</p><p>See you soon.</p></speak>',
                 46)

    author_speak('<speak>You chose the hard difficulty level.</speak>', 47)
    author_speak('<speak><p>At the beginning you have ten lives.</p>'
                 '<p>In this story you will play short games.'
                 'And if you do not complete the task, then every time a life is taken away.</p>'
                 '<p>Points are also deducted for incorrect answers.</p>'
                 '<p>When life ends, you will automatically lose.</p></speak>', 48)

    author_speak('<speak><p>This game named "Rock, paper, scissors".</p>'
                 '<p>The computer chooses one of the items, and you, in turn, must choose the item that defeats it.</p>'
                 '<p>Rock beats scissors,<break time="1s"/>scissors cut paper,<break time="1s"/>paper wraps rock.</p></speak>',
                 49)
    author_speak('<speak>Please choose: (rock,<break time="1s"/>paper<break time="1s"/>or scissors)</speak>', 50)
    author_speak('<speak>Draw. let\'s try again.</speak>', 51)
    author_speak('<speak>Congratulations. You win.</speak>', 52)
    author_speak('<speak>Computer wins. Health minus one.</speak>', 53)

    author_speak(
        '<speak><p>This game named "Guess the number".</p><p>The computer guessed a number from one to ten.</p></speak>',
        54)
    author_speak('<speak>Choose number (from one to ten):</speak>', 55)
    author_speak('<speak><s>You`re loose!</s><s>Minus 1 point.</s></speak>', 56)
    author_speak('<speak><s>I\'ll give you a clue.</s><s>This number is greater than five.</s></speak>', 57)
    author_speak('<speak><s>I\'ll give you one more clue.</s><s>This is odd number.</s></speak>', 58)

    author_speak('<speak><p>This game named "Dice rolling".</p>'
                 '<p>You must roll the dice and the sum of the digits must be greater than or equal to eight.</p></speak>',
                 59)
    author_speak('<speak>Please write word "throw".</speak>', 60)
    author_speak('<speak>You win.</speak>', 61)
    author_speak('<speak>Bad luck.</speak>', 62)

    author_speak(
        '<speak><p>You didn\'t enter what you asked for.</p><prosody rate="x-slow"><p>GOODBYE.</p></prosody></speak>',
        63)
    author_speak('<speak>Do you want to play again?<break time="1s"/>(yes or no)</speak>', 64)
    author_speak('<speak><p>As you wish.</p><prosody rate="x-slow"><p>Goodbye!</p></prosody></speak>', 65)
    author_speak('<speak><p>You lost all lives</p><prosody rate="x-slow"><p>LOOSER.</p></prosody></speak>', 66)
    print('=' * 50, 'Conclusion', '=' * 50)
