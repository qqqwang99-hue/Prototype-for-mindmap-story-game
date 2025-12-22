#Prototype 10/7/2025
import time
import tkinter as tk

#NOTE: need to figure out how to make stats stay in 0-100 range
#NOTE: can use/implement tkinter so they can press on buttons and see health bars and stuff
'''
NOTE: Will probably combine verdant and celestial into the trial of spirit/quiz and use some of the infero/tidal/tempest
values in the trial/quiz. Close endings of the storyline before start too much on other functions'''

    
stats =  {
    "Trust_in_Gavriel":5,
        "Trust_in_Maximus":30,
        "Hope":10,
        "Love_for_Gavriel": 40,
        "Love_for_Maximus":30,
        "Willpower":50,
        "Corruption":40,
        "Guilt":70,
        "Happiness":5,
        "Intelligence":90,
        "Forgiveness":5,
    "Rage":90,
    "Heartbreak":100
}

            
def print_stats():
    print("Valeria's Current Stats: ")
    print()
    for stat, value in stats.items():
        print(f"{stat}: {value}")
    print()
    


time.sleep(1)
'''There is a strange mark on her arm. Circular, ancient, and thickly ringed with a void purple color—a color so dark it was nearly black, but laced with shifting undertones of deep amethyst, indigo, and a strange, oily shimmer that sometimes looked like stars trapped beneath the surface.
It felt like a color you could fall into—bottomless, cold, and pulsing with slow, alien energy. 
At the very center of the brand, there was a pale outline of a flame. It looked empty for now but I caught hints of silver, purple, and black waiting along edges to fill it in.
The flame was surrounded by a pentagon, and there was a symbol on each of its points, but they were faint, as if they had yet to show their color.
At the tip of the pentagon, there was a compass starburst surrounded with orbital rings around it.
To its right, there was a rune shaped like a fang with flames curling off of it.
Then an inverted spiral wave, then a circular seed pod cracked open with vines snaking out of it, and finally, ending at the left of the compass,
there was a jagged glyph with twin lightning bolts crossing to create an X.
All these symbols were connected with a thin silver line.   
With her time running out, and the deity gaining power by the day, Valeria and Maximus have finally found and retrieved the Crown.
It is an ancient magical item that has the power to cleanse the deity of her body and soul, but at a price...
She is given a choice:
Binding the deity with the Crown will kill her, and all the ones she loves
Merging with the Crown and the deity will give it unlimited power and may destroy the world
Attempting to forge a different path may condemn them all
'''

welcome = '''Welcome to the Fantasy World Building Game, where you will be roleplaying as
a character named Valeria in a fantasy world where your choices and outcomes may affected not just Valeria's world, but the universe.'''
print(welcome)
print("From this point on, you are Valeria, and will see the story through her eyes.")
print('*' * 40)
print()

#allows user to read it more easily
def slowprint(text):
    for line in text.splitlines():
        print(line)
        time.sleep(2)
    print()


#for answers that only have two choices
def decision(question):
    global choice
    while True:
        choice = input(question).lower().strip()
        if choice == 'a' or choice == 'b':
            break
        else:
            continue
    return choice

#for answers that have more than two and are formatted a list
def decision1(question, lst):
    while True:
        print(question)
        print('Your choices are: ')
        for i in range(len(lst)):
            print(lst[i])
            i += 1
        choice = input("Choose A, B, or C: ").lower().strip()
        if choice == 'a' or choice == 'b' or choice == 'c':
            break
        else:
            continue
    

def change(catagory, add):
    old = stats[catagory]
    stats[catagory] += add
    new = stats[catagory]
    print(f"You have {'gained' if new > old else 'lost'} {abs(add)} {catagory}")


#The accepting her flawed self and forgiving someone who doesn't deserve it(maybe herself, make it emotional and stuff)
#Need to figure out how to involve the player more with the trial
#Maybe a trivia maybe a choose the lesser evil that will provoke thought
    

def trial():
    print("Trial.")
    print("I was no longer mentally on the physical world.")
    print("I stood on a long path of stone that I could not see the end of. On either side, there was a steep plunge into the black clouds, and I saw many dips and rises in the rocky terrain.")
    print(' A voice spoke into my head. "Cross the terrain, cursed one. Balance the weights. Pass the tests. Only then shall we deem you worthy." ')
    print("As if on cue, steel weights attached themselves to my legs and an iron vest was placed on my chest.")
    print("Two backpack sized rocks appeared hovering above my hands. I felt the tug on my mind as they stayed aloft.")
    print('"Get to the other side without letting those rocks drop or taking any of the steel weights off," the ethereal voice whispered.')
    print("Not only did I have to keep these relatively large rocks from dropping with only my mind, I had to lug about 150 pounds of steel across dangerous rocky terrain.")
    print('"I suggest you hurry, cursed one. Your time is ticking."')
    print("A glowing yellow clock showed I had two hours to make it to the other end. I didn't even want to think of what would happen if I failed.")
    print("Taking my first step, I already felt my muscles screaming in agony and a dull ache started in the back of my head.")
    
    
    
def storyline():
    #need to close up some loose strings/endings if they choose 'b'
    print()
    print("The Celestial Court holds the Starforged Prism, but Maximus is reluctant to tell me where it is.")
    print("Although we're on better terms now, he is still occassionally very closed off about topics like this, but I don't blame him. His duty first and foremost is to protect his court.")
    print("I've been spending more time in the Celestial Court, especially after...")
    print("No---I couldn't dwell on that, or it might break me all over again. I did not care what Gavriel was doing or how he was faring. No. I needed to be productive today.")
    print("The artifact was probably somewhere either restricted or off limits and under strict security, which meant I was going to break some rules today.")
    print("Maximus was busy today, and would probably not be able to find me until late tonight.")
    decision("Should you explore the Celestial Palace(a) or stay in the areas you are allowed to go(b)?: ")
    if choice == 'a':
        print()
        change("Intelligence",2)
        print()
        print("The halls were eerily quiet as I wandered into the wings that had not been remodeled.")
        print("Then I felt the pull.")
        #trial_of_spirit()
        print()
    elif choice == 'b':
        print()
        change("Intelligence",-2)
        print()
        print("Deciding to stay within the limits of the north wing, I wandered the halls, admiring the artwork on the walls and exploring the many rooms.")
        print("I wanted to sit in on the meeting he had today, but Maximus wouldn't let me, saying it would bore me.")
        print("I think he still doesn't trust me, and it's obvious in the way he always walks behind me and keeps an eye on me whenever I'm in the room.")
        print("As I was pondering this I walked past a mirror mounted on the wall.")
        decision("Should you turn your head and look at it(a) or keep your gaze forward and quickly walk past(b)?: ")
        if choice == 'a':
            print("Turning my head, I saw my reflection in it and my control snapped.")
            print("My vision danced with black spots and the roaring in my head crescendoed.")
            print("No, no, no, no. My breath came in short, fast bursts and my ears rang high and sharp.")
            print("All I could see was the blood that decorated my face and neck. The lives that I took tainting my soul.")
            print("I could hear the screams and the pleas for mercy all over again. I could feel the stickiness of the redness that covered my hands, face, and arms.")
            print("No matter how hard I scrubbed, it never disappeared. It clung to me like a second skin.")
            print("My fingernails gouged grooves in my arms and neck.")
            print("It was almost second nature in the way my index fingers with their carefully filed to a point nails opened bleeding red lines on myself.")
            print("I watched the blood slowly drip out of the cut. Every cut was made in penance, every drop of blood another in the endless sea of red.")
            print("All the pain locked up tight in a box as dark as my soul. Yet still, the pain wasn't enough. I was spiraling deeper and deeper.")
            print("The pressure in my head mounted to painful proportions and I screamed, the sound muffled by the immenseness of the Celestial Palace.")
            print("I've spend my entire life screaming into the dark---screaming and screaming yet never heard. The sound swallowed by the darkness, the life taken by the stifling shadows..")
            print("Clutching my head with my bloody hands, I screamed and screamed and screamed...")
            print()
            change("Corruption",10)
            change("Willpower",-10)
            change("Happiness",-5)
            change("Hope",-5)
            change("Rage",10)
            change("Intelligence",-2)
            change("Forgiveness",-5)
            print()
            #time.sleep(2)
            print("I woke up in my bed, surronded by fluffy blankets and with a dim light next to me.")
            print("There were thick swatches of white bandages that covered my arms and hands, and I realized my clothes had been changed.")
            print("Maximus was sitting in an armchair in the corner, silently watching me.")
            print('At the sight of him, I immediately asked, "Did you undress me?" ')
            print(''' He responds with an insufferable answer. "Technically, no. Sylv and the healer were the ones who did that. I just made sure
you were alright." ''')
            print(' "So yes you did," I flatly said.')
            print('"What happened? Why were you covered in blood and cuts? Were you attacked?" he asked, tilting his head to study me.')
            decision("Do you tell him the truth(a) or make up a lie(b)?: ")
            if choice == 'a':#incomplete
                print("Deciding to tell him the truth, I sat up in bed and looked him in the eye.")
                print(''' "I have really bad panic attacks sometimes," I admitted in a quiet voice, unable to look him in the eye. "And sometimes
    the only way to get myself out of that state is to harm myself, because pain in the body quiets pain in the mind."''')
                print('''Maximus's gaze shuttered. "You do it often," he stated. Of course, because he was there when they had undressed and cleaned me up,
he had seen the scars that decorated my entire body---especially my arms and legs---like artwork. Most of the newer ones were self-inflicted, but the big, ugly ones were not.''')
                print("I didn't even need to say anything; he knew the answer to his question already.")
                print("I waited for the pity to come. The judgement. The belief that he could change me or heal me.")
                print("But it never did. His face remained the same, and if anything its harshness softened a bit.")
                print()
                change("Trust_in_Maximus",20)
                change("Love_for_Maximus",10) 
                change('Hope', 5)
                change('Happiness',10)
                change("Guilt",-5)
                change("Corruption",-5)
                change("Rage",-10)
                change("Forgiveness",10)
                change("Heartbreak", -20)
                print()
                print("His eyes remained locked with mine, as if waiting for me to go on.")
                print("I wanted so badly to tell him all about myself and to have someone there who knew what I was going through.")
                print('But that little voice in my head whispered, "Do not trust them. You can not trust anyone from the courts. They are all praying on your downfall." ')
                print("Instead of answering the unspoken questions in his eyes, I changed the subject.")
                print('"Did anyone else besides Sylv and the healer see me?"')
                print('"Sera did, but she will not say anything," Maximus reassured me.')
                print("Pressing my eyes closed, I sighed. What a mess.")
                
            elif choice == 'b':#incomplete
                print("I couldn't let him see that side of me.")
                print("The side that was messy, imperfect, and tainted with sins. He would look at me differently, just like all the rest of them.")
                print("He would try to fix me. He would pity me and treat me differently just because I was too broken to be left alone.")
                print("And I wanted more than anything to just live a normal life.")
                print("It was for both our sakes that I told him a lie.")
                print()
                change("Trust_in_Maximus", -10)
                change("Love_for_Maximus",-5)
                change("Hope",-5)
                change("Happiness",-3)
                change("Guilt", 5)
                change("Corruption",5)
                change("Rage",5)
                change("Forgiveness",-5)
                print()
                print(''' "Yeah, I was attacked by I think an assassin. I managed to fight them off but I don't know where they went.
Maybe you should go check," I said, trying to keep my tone even and my mask in place. ''')
                print("Maximus's eyes darkened and his voice turned dark.")
                print("I would know if anyone, especially an intruder, was in my capital or palace. There was no such thing, which means you're lying.")
                print("As quick as lightning, Maximus was next to me and he tore off the bandages that were wrapped around my left wrist.")
                print(''' "No!" I cried, desperately trying to wrench myself out of his grasp. "Please, Maximus, don't do this!" I begged. "Please don't see this side of me.
I don't want you to see me! No!" Fear lanced through me as the bandages fell away and revealed my forearm and wrist.''')
                print("They were covered with a multitude of parallel and perpendicular lines. There were a few raw and red ones among the raised, scarred ones.")
                print("But what caught my attention the most was the words carved into my skin. 'Disappointment' 'Pain' 'Rage' 'Revenge'.")
                print("I had done that with a tiny knife on one of my worst episodes. They were essentially my motto and represented everything my life had been or were built on.")
                print("On days when the storm was close to dragging me under, I would trace those words with a needle until I bled.")
                print("And on days when I was unable to stop the waves from dragging me under, I let myself bleed until I lost consciousness, just to purge the shadows and darkness that lived in my blood.")
                print("I hesitated to meet his eyes, afraid of what I would find. ")
                print(' "Valeria, look at me," Maximus commanded. In the shining blue and violet depths of his eyes, I saw understanding.')
                
        elif choice == 'b':#incomplete
            print("Averting my eyes and quickly walking past, I never saw myself in the mirror.")
            print("After I was freed from the Nightmare Palace, I was unable to look at my reflection.")
            print("Whenever I did, I saw a killer, a murderer, someone who was so tainted with blood there was no skin left to be seen.")
            print("I saw each of my demons that whispered to me I didn't deserve to live, and the world would be better off if I was gone.")
            print("Every time, I would have a panic attack, and the only way to snap myself out of it was to inflict pain. After all, pain in the body quiets pain in the mind.")
            print()
            change("Corruption",-10)
            change("Willpower",10)
            change("Happiness",5)
            change("Hope",5)
            change("Rage",-10)
            change("Intelligence",5)
            change("Forgiveness",5)
        print_stats()
    
    
prophecy = '''
    This is the story of how the fallen one plunges even further.
    Slowly, over centuries, she breaks.
    Surely, with each cruel turn, she bends.
    Painfully, she loses faith in the light.
    And even when nothing remains to take, she endures.
    But tell me—can a fallen angel ever find its wings again?

    Time ticks away on the winds of magic.
    Choose, cursed one.
    Bind, and you shall fall with all you love.
    Merge, and the world shall burn in your image.
    Defy, and doom them all.

    Only when the shuttered doors are thrust open again,
    And the dry spring fills with rich life once more.
    Not for power, nor penance, nor pain
    But for balance long denied.

    Choose, Valeria Xilliana — the world, or the only soul who dared to mend your bitter, shattered heart when all others turned away.
    '''
    

def break_crown(): #If user decides to save the world and sacrifice Valeria and Maximus
    print('''To the Crown, I said, "I choose the world. I have always been the one giving until I had nothing left, what's one more pound of flesh?
At least it'll all finally be over, and maybe I'll have finally atoned for all that I've done.
I will see you in whatever afterlife the gods condemn me to, Maximus. I love you."''')
    print('''With the Crown in one hand, Dravyn screaming in my head, a silvery purple glow emanating from my eyes, and the most powerful concoction of all the Five Courts' magic in the other,
I shook the foundation of the universe... The runes on the Crown glowed brighter and brighter as all the magic in my body overloaded the artifact.
For a moment, I felt unstoppable, filled with magic and powerful beyond belief. Dravyn screamed louder, its cries for mercy resounding on deaf ears.
With a boom that echoed off other galaxies, everything went black...''')
    print("Somewhere across that vast, bloody battlefield, Maximus Vaelis---the most powerful Fae male in history, bloodbound to Valeria, and Sovereign of the Celestial Court---landed in the trampled mud with a clink of armor.")
    print("The hordes that Dravyn had summoned all turned to ash, and the war was finally over.")
    print("Two legends, two dark tales, two long, winding paths, two broken, lost souls who found life---and love---in each other...finally at rest.")
          
def bind_entity():#if user decides to sacrifice the world and save Valeria and Maximus
    print('''To the Crown, I said, "I choose Maximus. If I lose him, I lose everything. He saved me the first time when I spiraled into that dark pit, I won't survive the second.
He is the only reason I breathe. The only reason I love. He’s the only reason I endure this miserable existence I never wanted, but can’t escape.”
I can't lose him," my voice broke as I made my decision. We were apostraphes, inverted and upside down, caught between two worlds in a life we never asked for. So small, yet without us, the worlds would collapse.
    The Crown's voice projected into my head. "You would let the world burn for a chance at saving your lover and yourself. Why?"
    "You want to know why?" I said, my heart growing steely hard. "All this world has ever done for me is break me, over and over, and kick me and shove me down whenever I tried to get back up.
You ask why I would choose a single soul over millions. Because he's the only one that ever cared about me. He's the only one who helped me back up when I had lost all hope.
I would burn the world if it meant saving him, and that's exactly what I'm doing. I've always been the one who gave and gave without limit. I sacrificed everything---my mind, my body, my soul, my heart, my life.
And when it had taken every single thing that ever mattered to me, it gave me Maximus. I was so afraid to love him, to let him in, because I knew he would be taken away too.
But I couldn't help myself, and in doing so, I condemned us both. Anything I touch dies. He isn't anything different, but I would save him every time, because he stayed when nobody else did.
So I'm sorry to all the lives I chose Maximus over. But I'm not sorry for finally taking something for myself. Through Maximus, I have learned that I don't need to bleed to fix things, and that it's ok to love myself.
The Fae entity within me only understands sacrifice and devotion through loss, and I used to be that way, but Maximus came along and I fell in love and now I have something to live for.
Dying for something is noble and heroical, but living for someone? That's the ultimate sacrifice. Changing yourself in ways you never would've without the other person sacrifices more than you would think.
Life was actually looking better for the first time in centuries, but of course, I can't have that, so I'll take the next best thing. Living out the rest of my days in the body of Dravyn, but at least I'll be with Maximus.
I'm sorry it ended this way, both for me and the world, but sometimes, you don't get to live the life of happily ever after, even if you are the hero."''')

def risk():#if user takes the risk and tries to save both. IDEA: make them pass a test or something so that this can work
    print('''To the Crown, I said, "I choose my own path, and I will take the risks of condemning both. ''')
    print('''You gave me an ultimatum, and I refuse to play by those rules. Dravyn has been whispering in my ear, but so have you.
I have spent my whole life choosing my happiness, or someone else's. I don't have to bleed to make things better, and it's not always my fault.
Maximus has shown me that I am worth it and I am enough just the way I am. I'll find a way to save Maximus and the world, even if it comes at the cost of just myself.
"''')


storyline()
print()

def choice():
    while True:
        print("What is your final choice?")
        ult_decision("Break the Crown(c), bind with Dravyn(e), or take a risk on everything(r): ")
        if ult_choice == 'c':
            break_crown()
            break
        elif ult_choice == 'e':
            bind_entity()
            break
        elif ult_choice == 'r':
            risk()
            break
        else:
            print("That is not a valid answer. Try again.")
            print()
            continue

# leaderboard = input("Would you like to post your scores on the leaderboard(y,n)?: ").strip().lower()
# leaders = []
# if leaderboard == 'y':
#     print(f"Date: {dt.date.today()}")


