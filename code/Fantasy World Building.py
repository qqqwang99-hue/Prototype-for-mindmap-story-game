#Prototype 10/7/2025
import time
import datetime as dt


'''
NOTE:
Have to make sure it's depth and impressive but doesn't have to be large for it to be impressive
Focus on one chapter/one trial and maybe the ending. Can mention/continue with the others but in less depth
and mainly focus on the trial and ending because too much = overload and maybe not good as if I just do one or two things.
'''

#how Valeria starts
#Valeria's stats so far(can add or subtract to them)

class Valeria:
    def __init__(self):
        self.stats =  {
        "Trust_in_Gregory":5,
            "Trust_in_Maximus":20,
            "Hope":10,
            "Love_for_Gregory": 40,
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
        self.relics_claimed = 0
        self.Crown_claimed = False
        self.relics = {"prism":False, "crucible":False, "tear":False, "circlet":False}
        self.courts_visited = {"Celestial":False,"Inferno":False,"Tempest":False,"Tidal":False,"Verdant":False}
        self.trials_passed = {"Celestial":False, "Inferno":False,"Tempest":False,"Tidal":False,"Verdant":False}

    def print_all(self):
        print("Valeria's Current Stats: ")
        for stat, value in self.stats.items():
            print(f"{stat}: {value}")
        print()
        print("Relics Claimed.")
        for relic, claimed in self.relics.items():
            print(f"{relic}: {'claimed' if claimed else 'not claimed'}")
        print()
        print("Courts Visited.")
        for court, visit in self.courts_visited.items():
            print(f"{court} Court: {'visited' if visit else 'not visited'}")
        print()
        print("Other.")
        print(f"{self.relics_claimed} relics claimed.")
        print(f"Crown claimed = {'Yes' if self.Crown_claimed else 'No'}")
    

val=Valeria()
            
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
def try_again(question):
    while True:
        choice = input(question).lower().strip()
        if choice == 'a' or choice == 'b':
            break
        else:
            continue
    return choice

#for answers that have more than two and are formatted a list
def try_again1(question, lst):
    while True:
        print(question)
        print('Your choices are: ')
        for i in range(len(lst)):
            print(lst[i])
            i += 1
        choice = input("Choose A, B, or C: ").lower().strip()
        if choice != 'a' or 'b' or 'c':
            continue
        else:
            break
        
full = False
def gained(catagory, add):
        old = val.stats[catagory]
        val.stats[catagory] += add
        new = val.stats[catagory]
        print(f"You have {'gained' if new > old else 'lost'} {abs(add)} {catagory}")
        
def spirit_quiz():
    print("I had done my research and found that the Prism is the First Artifact, and the only one with a mind.")
    print("If I won the Prism, I would also win the ability to search for the other artifacts to unlock the Crown")
    print("Without it, I would be unable to feel the other artifacts if they were near, so it is vital to my success.")
    print("I would go through all five elemental trials here, in the Celestial Court, and the Prism would deem me worthy or not.")
    print("I steel myself for whatever this ancient artifact might throw at me.")
    print('"Answer my questions and you will suceed in obtaining the first of the five," the Prism whispered.')
    print("The last tether to your old life has left you, and your spirit is freshly broken, yet still you are here.")
    print("You saw the perfect life you had. Did you regret this life so much that you were compelled to choose the vision? And if you could, would you go back in time and fix or prevent everything?")
    answers = ["A:  Yes, I regret everything and I would go back in a heartbeat to fix all those mistakes and lost chances",
               "B: Yes, I regret some things, but without them, I wouldn't be where I am today so I'll make the best of it",
                       "C: Yes, I regret some things and I hate the world for making me this way, but I can't do anything about it"]
    answer = input("What is your answer (A, B, C)?: ").strip().lower()
    print()
    if answer == 'a' or answer == 'c':
        print("Very well.")
        print()
        gained("Hope",-3)
        gained("Intelligence",-3)
        gained("Forgiveness",-5)
        gained("Rage", 5)
        gained("Willpower", -5)
        print_stats("prism",False, "Celestial")
    elif answer == 'b':
        print("So you have learned, cursed one.")
        print()
        val.trials_passed("Celestial",True)
        gained("Willpower", 5)
        gained("Hope",5)
        gained("Intelligence", 2)
        gained("Forgiveness", 3)
        gained("Rage", -5)
        val.relics_claimed += 1
        print_stats("prism",True, "Celestial")
        full = True
    else:
        try_again1("You saw the perfect life you had. Did you regret this life so much that you were compelled to choose the vision?", answers) 
    answers1 = []
    print("My consciousness was stolen and transported to the Inferno Court.")
    print("I realized I was in the Crucible of Flame---the volcano that the Inferno Palace was built next to.")
    print("Suddenly, something materialized next to the steaming pit of lava that was the center of the volcano.")
    print("It was me...")
    #time.sleep(1)
    print("My expression was twisted in a grotesque way, and dark red flames surronded my body.")
    
    

#Celestial
def trial_of_spirit():#Tests her mental stability and she has to choose between a happy yet delusional life or the life she has now
    #Reward is that she fights back against the darkness/entity inside her for a bit longer
    print("The ancient entity within me stirred, and its soft, yet deceptive voice flowed into my head.")
    print('"It is near, do you feel that, chosen one?" it whispered softly. "Find it, we need it."')
    choice = input("Should you follow the voice in your head(a) or go back to the north wing(b)?: ").lower().strip()
    if choice == 'a':
        print("The pull was getting stronger, and I stopped in front of a heavy iron bound oak door that was, of course, locked.")
        print("Allowing my curse to rise to the surface of my skin, I stepped forward and placed my hands on the door.")
        print("The wood quickly rotted away, the corrosive darkness eating away at the entire door.")
        print("What I found behind it shocked me.")
        print("The Starforged Prism---the Celestial's symbol of power and most prized possession---was floating in a ray of starlight, slowly rotating so that the facets of the prism refracted across the room.")
        print("This chamber was different from the others. It looked like a cave carved from the side of the mountain, and there were several gems embedded in the uneven walls.")
        print("As I stepped closer to the Starforged Prism, the entity inside me hummed with glee.")
        print("What I didn't know was that the moment I opened the door, alarms and magical signatures were sent to Maximus, and he would be here soon.")
        print('"Yes the treasure entrusted to the Celestial Court. The light to counteract darkness, the fire to burn away the shadows."')
        choice = input("Do you reach up to grab the Prism(a) or quiet the voice and get out of the room(b)?: ").lower().strip()
        if choice == 'a':
            print()
            gained("Intelligence",3)
            gained("Willpower",5)
            gained("Corruption",3)
            print("At first I felt resistance and an intense burning feeling, but then the Prism seemed to recognize me, or the entity inside me, and let me in.")
            print("As soon as I touched it, I was pulled into a different dimension.")
            print("I saw myself covered in gems and crowned as people swore their fealty to me.")
            print("I saw myself as a queen, a savior, a hero, loved and worshipped by all.")
            print("I saw myself with a strong and supportive husband who loved me more than anybody ever had.")
            print("I saw myself holding a squalling child, and then the vision fast forward fifteen years ahead.")
            print("I had aged, but my family was whole. My two perfect children---a boy and girl---, my husband, my parents, my kingdom.")
            print("I had everything anybody could ever wish for. But most of all, I had a family...")
            print('A voice whispered in my head, "This could all be yours, just let it in."')
            print("It was so tempting to let go of my hold on the physical world, and let myself fall into this realm where everything was perfect.")
            print('''
        "It's the happy ending that you deserve," I argued with myself. "I had suffered enough, and maybe it was finally time to reap the rewards."''')
            print('"Let go," a voice inside me whispered. "You deserve more than this human world has to offer. Take what was always meant to be yours, become the queen you were meant to be."')
            print("Visions flew past at high speed, each showing a better life. Then it changed to something darker.")
            print("People died on a vast battlefield. I saw myself among them, just another tick on a list of casualties at the end of the day.")
            print('No family, no friends, nobody that cared for me, I died alone and desolate. "This is the fate that awaits you if you reject it," the Prism whispered.') 
            choice = input("Do you let go(a) or resist (b)?: ")
            if choice == 'b':
                if val.stats["Willpower"] >= 50:
                    print("Shaking my head vigorously, I dislodged the voices and brought myself back to the present.")
                    print("Although the visions hold everything I had ever dreamed of, I would be living a lie.")
                    print("Trapped in the Veil between the tangible and some other world, I would not really be living;it would all be in my head.")
                    print("I was flawed in many ways, but I had to embrace it, even if it meant giving away the life I had always wanted.")
                    print("As the bright light faded, I returned to the crystal chamber once again.")
                    print("The Prism was in my hand, glowing slightly with its own light. The entity inside me hummed.")
                    print('"Good, very good. One of the five have been retrived..."')
                    print("Suddenly the Prism lit up brighter in my hands, otherworldly light reflecting off its facets.")
                    print('''
            "The darkness inside you is deep, cursed one. Your spirit has been freshly broken I see, and the old scars are not healing. But my light can only reach so far.
            You have shown humility, temptation of power, and your ultimate wish for happiness, however impossible it may seem. Virtues that must be applauded, but the road ahead is still long,
            and if you are to walk it all the way to the end, you will need the power of the five. I gift you the power of my light, to guide you in the darkest nights.
            To pierce through the shadows that threaten to steal away your humanity, and to beat back the corruption that lives inside you."''')
                    print("Staring down at the artifact in my hands and processing this load of information, I was stunned.")
                    time.sleep(0.5)
                    print()
                    gained("Willpower", 10)
                    gained("Corruption",-10)
                    gained("Hope",5)
                    gained("Intelligence", 2)
                    gained("Happiness",5)
                    gained("Forgiveness",5)
                    val.relics_claimed += 1
                    full = True
                    print_stats("prism",True, "Celestial")
                else:
                    print("My will was too weak, and I didn't have the strength to suppress the vision.")
                    gained("Corruption", -5)
                    gained("Hope", 2)
                    gained("Willpower", 10)
                    gained("Intelligence", 2)
                    gained("Happiness",3)
                    gained("Forgiveness",3)
                    print("The Prism spoke into my head.")
                    print('''
            "The darkness inside you is deep, cursed one. Your spirit has been freshly broken I see, and the old scars are not healing. But even my light can only reach so far.
            Although your will was not strong enoug, you have shown humility, temptation of power, and your ultimate wish for happiness, however impossible it may seem. Virtues that must be applauded, but the road ahead is still long,
            and if you are to walk it all the way to the end, you will need the power of the five. I gift you a shard of the power of my light, to guide you in the darkest nights.
            To pierce through the shadows that threaten to steal away your humanity, and to beat back the corruption that lives inside you."''')
                    print("Because of this, I was only able to obtain half the Prism, but at least it was more than nothing.")
                    full = False
            elif choice == 'a':
                print("The pull of the visions and the desire for happiness finally overrode my rationality.")
                print("I gave in and allowed the visions to breach my mental barriers.")
                print("Caught between this dream world and the real world, I didn't realize the danger that my physical body was in.")
                print("While I was living the best life I could ever dream of, Maximus had received the alarm and swiftly appeared in the chamber, and had to tear my hands away from the Prism.")
                print("They were burned and blistered badly, and Maximus was shocked, confused, and slightly disappointed.")
                print()
                print("You did not retrieve the Starforged Prism.")
                print("But there is still redemption.")
                choice = input("Will you take the redemption path(a) or give up and go back to the life you were living(b)?: ").lower().strip()
                if choice == 'a':
                    print()
                    gained("Willpower", 5)
                    gained("Hope", 3)
                    gained("Corruption",-5)
                    gained("Intelligence",5)
                    gained("Happiness",5)
                    print()
                    print('''The next day, I snuck out of my room and went back to the chamber, even though Maximus explicitly
        told me that I was to stay away from there. Entering the chamber again, it's almost as if it welcomed me.''')
                    print("The entity inside me whispers something that I don't catch, and the Prism murmurs quietly.")
                    print("It's strange how I lived in obsolete silence for so long, and now there are constant noises that drift to my ears, even if they're not always tangible.")
                    print("Then the Prism speaks.")
                    print('''"You are back again I see. Tell me, little flame, do you believe in redemption?" the Prism asked.
        "But it doesn't matter, because if you are to gain my abilities, you must answer a quiz that will reflect your true intentions." ''')
                    spirit_quiz()
                elif choice == 'b':
                    print("The Prism had rejected me the first time, so maybe it was really time to give up.")
                    print()
                    gained("Hope",-10)
                    gained("Happiness",-5)
                    gained("Intelligence",-5)
                    gained("Corruption", 5)
                    gained("Rage", 5)
                else:
                    try_again("Will you take the redemption path(a) or give up and go back to the life you were living(b)?: ")
            else:
                try_again("Do you let go(a) or resist (b)?: ")
        elif choice == 'b': #(if the user chooses to get out of the room)
            print()
            gained("Hope",-3)
            gained("Intelligence",-5)
            gained("Corruption",5)
            gained("Guilt",5)
            gained("Happiness",-3)
            print()
            print("I decided to leave this room, as beautiful as it was, because I was technically trespassing.")
            print("And if I got caught, I would most likely be imprisoned, and I had had enough of that for several lifetimes.")
        else:
            try_again("Do you reach up to grab the Prism(a) or quiet the voice and get out of the room(b)?: ")
    elif choice == 'b':
        print()
        gained("Corruption",10)
        gained("Willpower",-5)
        gained("Hope",-5)
        gained("Intelligence",-5)
        gained("Forgiveness",-3)
        gained("Happiness",-5)
        gained("Guilt",2)
        print()
        print("I decided to turn back and stay in the north wing where my rooms were located.")
    else:
        try_again("Should you follow the voice in your head(a) or go back to the north wing(b)?: ")
def chapter1():#trial of spirit in this one
    print("Chapter 1: ")
    print()
    print("The Celestial Court holds the Starforged Prism, but Maximus is reluctant to tell me where it is.")
    print("Although we're on better terms now, he is still occassionally very closed off about topics like this, but I don't blame him. His duty first and foremost is to protect his court.")
    print("I've been spending more time in the Celestial Court, especially after...")
    print("No---I couldn't dwell on that, or it might break me all over again. I did not care what Gregory was doing or how he was faring. No. I needed to be productive today.")
    print("The artifact was probably somewhere either restricted or off limits and under strict security, which meant I was going to break some rules today.")
    print("Maximus was busy today, and would probably not be able to find me until late tonight.")
    go = input("Should you explore the Celestial Palace(a) or stay in the areas you are allowed to go(b)?: ").lower().strip()
    if go == 'a':
        print()
        gained("Intelligence",2)
        print()
        print("The halls were eerily quiet as I wandered into the wings that had not been remodeled.")
        print("Then I felt the pull.")
        trial_of_spirit()
        print()
    elif go == 'b':
        print()
        gained("Intelligence",-2)
        print()
        print("Deciding to stay within the limits of the north wing, I wandered the halls, admiring the artwork on the walls and exploring the many rooms.")
        print("I wanted to sit in on the meeting he had today, but Maximus wouldn't let me, saying it would bore me.")
        print("I think he still doesn't trust me, and it's obvious in the way he always walks behind me and keeps an eye on me whenever I'm in the room.")
        print("As I was pondering this I walked past a mirror mounted on the wall.")
        choice = input("Should you turn your head and look at it(a) or keep your gaze forward and quickly walk past(b)?: ").lower().strip()
        if choice == 'a':
            print("Turning my head, I saw my reflection in it and my control snapped.")
            print("My vision danced with black spots and the roaring in my head crescendoed.")
            print("No, no, no, no. My breath came in short, fast bursts and my ears rang high and sharp.")
            print("All I could see was the blood that decorated my face and neck. The lives that I took tainting my soul.")
            print("I could hear the screams and the pleas for mercy all over again. I could feel the stickiness of the redness that covered my hands, face, and arms.")
            print("No matter how hard I scrubbed, it never disappeared. It clung to me like a second skin.")
            print("My fingernails gouged grooves in my arms and neck and yet they left my face unharmed.")
            print("It was almost second nature in the way my index fingers with their carefully filed to a point nails opened bleeding red lines on myself.")
            print("I watched and felt the blood slowly drip out of the cut. Every cut was made in penance, every drop of blood another in the endless sea of red.")
            print("All the pain locked up tight in a box as dark as my soul. Yet still, the pain wasn't enough. I was spiraling deeper and deeper.")
            print("The pressure in my head mounted to painful proportions and I screamed, the sound swallowed by the immenseness of the Celestial Palace.")
            print("I've spend my entire life screaming into the dark---screaming and screaming yet never heard. The sound swallowed by the darkness, the life taken by the stifling shadows..")
            print("Clutching my head with my bloody hands, I screamed and screamed and screamed...")
            print()
            gained("Corruption",10)
            gained("Willpower",-10)
            gained("Happiness",-5)
            gained("Hope",-5)
            gained("Rage",10)
            gained("Intelligence",-5)
            gained("Forgiveness",-5)
            print()
            #time.sleep(2)
            print("I wake up in my bed, surronded by fluffy blankets and with a dim light next to me.")
            print("There were thick swatches of white bandages that covered my arms and hands.")
            print("Maximus was sitting in an armchair in the corner, silently watching me.")
            print(''' "You're awake," he said, his voice low and silky.
    "Yeah. Thanks for bringing me back to my room...," I said, knowing he probably saw me in the breaking down state.''')
            print('"What happened? Were you attacked?" he asked, tilting his head to study me.')
            choice = input("Do you tell him the truth(a) or make up a lie(b)?: ").lower().strip()
            if choice == 'a':
                print("Deciding to tell him the truth, I sat up in bed and looked him in the eye.")
                print(''' "I have really bad panic attacks sometimes," I admitted in a quiet voice, unable to look him in the eye. "And sometimes
    the only way to get myself out of that state is to harm myself, because pain in the body quiets pain in the mind."''')
                print('''Maximus's gaze shuttered. "You do it often," he said. He had seen the scars that decorated my entire body like artwork.
    Most of the newer ones were self-inflicted, but the big, ugly ones were not.''')
                print("I didn't even need to say anything; he knew the answer to his question already.")
                print("I waited for the pity to come. The judgement. The belief that he could change me or heal me.")
                print("But it never did. His face remained the same, and if anything it softened a bit.")
                print()
                gained("Trust_in_Maximus",10)
                gained("Love_for_Maximus",10) 
                gained('Hope', 5)
                gained('Happiness',10)
                gained("Guilt",-5)
                gained("Corruption",-5)
                gained("Rage",-10)
                gained("Forgiveness",10)
                print()
            elif choice == 'b':
                print("I couldn't let him see that side of me.")
                print("The side that was messy, imperfect, and tainted with sins. He would look at me differently, just like all the rest of them.")
                print("He would try to fix me. He would pity me and treat me differently just because I was too broken to be left alone.")
                print("And I wanted more than anything to just live a normal life.")
                print("It was for both our sakes that I told him a lie.")
                print()
                gained("Trust_in_Maximus", -10)
                gained("Love_for_Maximus",-5)
                gained("Hope",-5)
                gained("Happiness",-3)
                gained("Guilt", 5)
                gained("Corruption",5)
                gained("Rage",5)
                gained("Forgiveness",-5)
                print()
            else:
                try_again("Do you tell him the truth(a) or make up a lie(b)?: ")
        elif choice == 'b':
            print("Averting my eyes and quickly walking past, I never saw my reflection in the mirror.")
            print("After I was freed from the Nightmare Palace, I was unable to look at my reflection in the mirror.")
            print("Whenever I did, I saw a killer, a murdererr, someone who was so tainted with blood there was no skin left to be seen.")
            print("I saw each of my demons that whispered to me I didn't deserve to live, and the world would be better off if I was gone.")
            print("Every time, I would have a panic attack, and the only way to snap myself out of it was to inflict pain. After all, pain in the body quiets pain in the mind.")
            print()
            gained("Corruption",-10)
            gained("Willpower",10)
            gained("Happiness",5)
            gained("Hope",5)
            gained("Rage",-10)
            gained("Intelligence",5)
            gained("Forgiveness",5)
        else:
            try_again("Should you turn your head and look at it(a) or keep your gaze forward and quickly walk past(b)?: ")
    else:
        try_again("Should you explore the Celestial Palace(a) or stay in the areas you are allowed to go(b)?: ")
    if full == True:
        print("Congratulations, you have claimed Starforged Prism and successfully completed Chapter 1!")
    else:
        print("You did not successfully claim the full Starforged Prism, but you have obtained a shard of it.")
        print("Although this shard is powerful, it is not enough to hold the entity at bay for long.")
        print("The window for redemption has closed...for now. Perhaps the stars will give you another chance when you have learned.")
        
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
    
#This part will be in the end of the story, I have to make the trials and stuff first
def ending():
    print("I have been unable to sleep, haunted by the facts that I learned the day before.")
    print("The brand on my arm has gotten worse. Since I had found all five conduits and passed each of their tests, I had finally obtained the Crown, and the symbols were filled in with the courts' respective colors.")
    print('''But the flame was a little more than 3/4 of the way filled, the silver, purple, and blue vividly outlining it, and leaking shadowy tendrils into the thickly ringed circular shape.
    The silvery lines connecting the symbols of the courts in a pentagon shape were fracturing and disappearing in some places. Dravyn was getting stronger.
    Soon it would be able to take over my body and possibly even the world.''')
    print("The prophecy from the Crown resounded in my head over and over: ")
    print(prophecy)
    print('"No, I will find another way. There has to be," I choked out as my knees hit the cold stone floor.')
    print("The Crown only softly, yet defeatedly laughed.")
    print()
    time.sleep(0.5)
    print("Now, days later, its words still echoed in my mind.")
    print('"Little flame?" a voice asked in the dark.')
    print("I sat up, seeing Maximus's face appear in my doorway, his violet-blue eyes twin embers of worry.")
    print("I reached for him, automatically wanting his comfort especially when things get hard.")
    print("He hopped in next to me and wrapped his arms around me.")
    print('"I just got back from the meeting with my court. There have been more and more reported Dreadspawn near the borders and in less inhabited places."')
    print("I shivered at the thought of all those horrible creatures that the entity inside me could summon.")
    print('"How are you going to deal with them?" I asked.')
    print('"That is what we are all wondering, and I was hoping to ask you for some ideas," Maximus laughed.')
    print("I talked with Maximus for a bit more until he settled beneath the blankets and pulled me into his chest.")
    print('''"Enough court talk, sleep. You need it, and you don't have to worry about the nightmares, I'm here," he said gruffly.''')


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


chapter1()
print()

def choice():
    while True:
        print("What is your final choice?")
        ult_choice = input("Break the Crown(c), bind with Dravyn(e), or take a risk on everything(r): ")
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

leaderboard = input("Would you like to post your scores on the leaderboard(y,n)?: ").strip().lower()
leaders = []
if leaderboard == 'y':
    print(f"Date: {dt.date.today()}")


