#TO-DO:coins rubbing sound for buying; balance, unequip
#Game overall idea: Start out almost completely barren. Black screen all the way. Unlock color and other things, simulating either birth, dream, creation.
#Gignesthai = genesis; khaos = chaos 
#First key word = Ignatio

import random #INCLUSIVE ON BOTH ENDS
import math
import nltk
import pygame
import pygame_textinput
import sys
nltk.download('wordnet')
from nltk.corpus import wordnet as wn

def health_bar (x, y, w, tot_hp, current_hp, operating_screen):
    pygame.draw.rect(operating_screen, (0, 0, 255), pygame.Rect(x, y, w, tot_hp))
    pygame.draw.rect(operating_screen, (255, 0, 0), pygame.Rect(x, y + tot_hp*(1 - (current_hp/tot_hp)),w, (current_hp/tot_hp)*tot_hp))
    
def health_bar_enemy (x, y, w, h, tot_hp, current_hp, operating_screen):
    pygame.draw.rect(operating_screen, (0, 0, 255), pygame.Rect(x, y, w, h))
    pygame.draw.rect(operating_screen, (255, 0, 0), pygame.Rect(x, y + h*(1 - (current_hp/tot_hp)),w, (current_hp/tot_hp)*h))
    

def show_text(screen, x,y, string, Ignatio): ##Show string at coordinate x,y
    text = font.render(string, True, (255, 255, 255))
    screen.blit(text, (x, y))
    if Ignatio:
        text = font.render(string, True, (0, 0, 0))
        screen.blit(text, (x, y))

def show_centertext(screen, y, string, Ignatio): ##Show string at coordinate x,y
    text = font.render(string, True, (255, 255, 255))
    centered = text.get_rect(center = (screen.get_width()//2, y))
    screen.blit(text, centered)
    if Ignatio:
        text = font.render(string, True, (0, 0, 0))
        centered = text.get_rect(center = (screen.get_width()//2, y))
        screen.blit(text, centered)


def show_coloredcentertext(screen, y, r, g, b, string): ##Show string at coordinate x,y
    text = font.render(string, True, (r, g, b))
    centered = text.get_rect(center = (screen.get_width()//2, y))
    screen.blit(text, centered)

def show_localcentertext(screen, xin, xfin, y, string, Ignatio):
    text = font.render(string, True, (255, 255, 255))
    centered = text.get_rect(center = ((xfin + xin)//2, y))
    screen.blit(text, centered)
    if Ignatio:
        text = font.render(string, True, (0, 0, 0))
        centered = text.get_rect(center = ((xfin + xin)//2, y))
        screen.blit(text, centered)


def show_bigcentertext(screen, y, string, Ignatio): ##Show string at coordinate x,y
    text = font_big.render(string, True, (255, 255, 255))
    centered = text.get_rect(center = (screen.get_width()//2, y))
    screen.blit(text, centered)
    if Ignatio:
        text = font_big.render(string, True, (0, 0, 0))
        centered = text.get_rect(center = (screen.get_width()//2, y))
        screen.blit(text, centered)

def show_smalltext(screen, x,y, string, Ignatio): ##Show string at coordinate x,y
    text = font_small.render(string, True, (255, 255, 255))
    screen.blit(text, (x, y))
    if Ignatio:
        text = font_small.render(string, True, (0, 0, 0))
        screen.blit(text, (x, y))


def show_kindasmalltext(screen, x,y, string, Ignatio): ##Show string at coordinate x,y
    text = font_kindasmall.render(string, True, (255, 255, 255))
    screen.blit(text, (x, y))
    if Ignatio:
        text = font_kindasmall.render(string, True, (0, 0, 0))
        screen.blit(text, (x, y))

def show_localsmallcentertext(screen, xin, xfin, y, string, Ignatio):
    text = font_small.render(string, True, (255, 255, 255))
    centered = text.get_rect(center = ((xfin + xin)//2, y))
    screen.blit(text, centered)
    if Ignatio:
        text = font_small.render(string, True, (0, 0, 0))
        centered = text.get_rect(center = ((xfin + xin)//2, y))
        screen.blit(text, centered)

def show_bigtext(screen, x,y, string, Ignatio): ##Show string at coordinate x,y
    text = font_big.render(string, True, (255, 255, 255))
    screen.blit(text, (x, y))
    if Ignatio:
        text = font_big.render(string, True, (0, 0, 0))
        screen.blit(text, (x, y))

def status_change(status_array, string):
    status_array.pop(0)
    status_array.append(string)

monster_types = ["Normal", "Poison", "Fire", "Ice"]
Battle_entry = ["You are now facing, the one and most likely only, probably, idk maybe, ", "OHOHOHO, YOU'RE IN FOR IT NOW, FACE OFF AGAINST ",
                "Next fight, ", "Okay, I don't have many other battle-entry line ideas... just fight ", "DASFDSAFDSAGSAGADSA ", "Can you beat THIS? ",
                "EAT POOP LOSER. jk we love you. But your next opponent is ", "NEXT STOP: ", "YARR HARR BOYO. Or girlyo. I mean, you know in case you're not a boy or like, you know what, fight ",
                "Everyone welcome the next contestant! That's right, it's ", "I once ate soup with a fork. ", "This guy didn't shower today. ew, kill ",
                "How many of these battle-entry lines do you think I made? I'm just rambling gibberish at this point lol. Well gl against ",
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley ", "If you die against this guy, you owe me $5 :) ",
                "IT'S TIME TO DU-DU D-D-D-D-D-D-DUEL ", "Remember to get good amounts of sleep! now die against ", "He's here, it's ",
                "IT'S A BIRD. NO, IT'S A PLANE. NO! IT'S A "]
all_nouns = []
for synset in wn.all_synsets('n'):
    all_nouns.extend(synset.lemma_names())
all_adjectives = []
for synset in wn.all_synsets('a'):
    all_adjectives.extend(synset.lemma_names())

def get_valid_int_input(temp_keys):
    global complaint
    breaker = 0
    try:
        int_answer = int(f"{textinput.value}")
        for idk in range (0, len(temp_keys)):
            if int_answer == idk:
                breaker = 1
        if breaker != 1:
            complaint = "THE NUMBERS ARE THERE BEFORE THE COLONS!!! PUT ONE OF THEM IN!!!"
            int_answer = ""
        else:
            complaint = ""
    except ValueError:
        complaint = "THE NUMBERS ARE THERE BEFORE THE COLONS!!! PUT ONE OF THEM IN!!!"
        int_answer = ""
    return int_answer

def get_valid_str_input(temp_keys):
  breaker = 0
  while inf_num == 1:
    str_answer = input()
    for idk in range (0, len(temp_keys)):
      if str_answer == temp_keys[idk]:
        breaker = 1
    if breaker == 1:
      break
    else:
      print("Invalid input. Either you're trying to break my game, in which case ლ(ಠ_ಠლ), but if it was just a mistake, all good :D, 'try another' ")
      continue
  return str_answer



class consumable():
    def __init__(self, consume_name, gold_cost, amount, effect, descript):
        self.name = consume_name
        self.price = gold_cost
        self.amount = amount
        self.desc = descript
        self.effect = effect

    def consum_hp(self, targ):
        targ.hp_current = targ.hp_current + self.amount
        if targ.hp_current > targ.hp_tot:
            targ.hp_current = targ.hp_tot

    def consum_def(self, targ):
        targ.con_def = targ.con_def + self.amount

    def consum_att(self, targ):
        targ.con_att = targ.con_att + self.amount

    def consum_poison(self, targ):
        targ.poison_count = targ.poison_count + self.amount

    def consum_hp_tot(self, targ):
        targ.hp_tot = targ.hp_current + self.amount

    def consum_def_tot(self, targ):
        targ.defense_tot = targ.con_def + self.amount

    def consum_att_tot(self, targ):
        targ.attack_tot = targ.con_att + self.amount

    def consum_lag(self, targ):
        targ.buff_miss_timer_array[0] = targ.buff_miss_timer_array[0] * self.amount

    def consum_full_hp(self, targ):
        targ.hp_current = targ.hp_total

    def consum_antidote(self, targ):
        targ.poison_count = 0
        targ.buff_attack_timer_array = [1, 1, 1]
        targ.buff_attack_current = 1
        targ.buff_defense_timer_array = [1, 1, 1]
        targ.buff_defense_current = 1
        targ.buff_crit_chance_timer_array = [1, 1, 1]
        targ.buff_crit_chance_current = 1
        targ.buff_crit_damage_timer_array = [1, 1, 1]
        targ.buff_crit_damage_current = 1
        targ.buff_miss_timer_array = [1, 1, 1]
        targ.buff_miss_current = 1



shop_basic_list = [
    consumable("Red Juice", 70, 20, "consum_hp", "Instant +20 hp"),
    consumable("Phoenix fart", 140, 0, "", "Revive with 20% hp"),
    consumable("Salt Water", 110, 0, "consum_antidote", "Remove all buffs/debuffs")
    ]

shop_more_fleshed = [
    consumable("Really Red Juice", 120, 40, "consum_hp", "Instant +40 hp"),
    consumable("Molotov Coketail", 90, -20, "consum_hp", "Deal 20 damage"),
    consumable("Literal Grenade", 150, -40, "consum_hp", "Deal 40 damage"),
    consumable("Cobra Blood", 100, 8, "consum_poison", "Inflict 8 poison"),
    consumable("Neurotoxin", 180, 14, "consum_poison", "Inflict 14 poison"),
    consumable("Wolverine Surgery", 200, 2, "consum_att_tot", "Perma-increase att. by 2"),
    consumable("Iron Supplements", 250, 2, "consum_def_tot", "Perma-increase def. by 2"),
    consumable("Heart Transplant", 200, 25, "consum_hp_tot", "Perma-increase max HP by 25"),
    consumable("Full-Body Transplant", 160, 0, "consum_full_hp", "Restore to full hp"),
    consumable("Kinda Red Juice", 100, 30, "consum_hp", "Instant +30 hp"),
    ]
shop_debuffs = [
    consumable("Really Smelly Poop", 50, 2, "consum_att", "Give +2 att. this fight"),
    consumable("BANKAI", 90, 4, "consum_att", "Give +4 att. this fight"),
    consumable("Metal Varnish", 75, 2, "consum_def", "Give +2 def. this fight"),
    consumable("Apple Battery Shield", 120, 4, "consum_def", "Give +4 def. this fight"),
    consumable("Flask of Salt", 60, -2, "consum_att", "Give -2 att. this fight"),
    consumable("Stare HARD", 100, -4, "consum_att", "Give -4 att. this fight"),
    consumable("Naked Elderly Human Photo", 70, -2, "consum_def", "Give -2 def. this fight"),
    consumable("Spontaneously Cry", 110, -4, "consum_def", "Give -4 def. this fight"),
    consumable("Shadow Clone Scroll", 60, 0.5, "consum_lag", "Lower accuracy by 0.5x next turn"),
    consumable("Uno Skip Card", 130, 0, "consum_lag", "0% accuracy next turn"),
    ]

def use_consumable(consumable_list, consum_number, character_list, dead_array, currently_fighting, status_array, current_move, Ignatio):
    if consumable_list[consum_number].name == "Phoenix fart":
        if len(dead_array) == 0:
            operating_screen.fill((100, 140, 230))
            if (not Ignatio):
                operating_screen.fill((0, 0, 0))
            show_centertext(operating_screen, 200, "Literally nobody's dead. What are you trying to revive? Your self-esteem? Now you lose your turn lol", Ignatio)
            pygame.display.update()
            pygame.time.delay(2000)
            return
        get_out = 0
        current_choice = 0
        while True:
            operating_screen.fill((100, 140, 230))
            if (not Ignatio):
                operating_screen.fill((0, 0, 0))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                    current_choice = (current_choice - 1)%len(dead_array)
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                    current_choice = (current_choice + 1)%len(dead_array)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    res_acquired = dead_array[current_choice]
                    get_out = 1
            
            for res_squad in range (0, len(dead_array)):
                operating_screen.blit(dead_array[res_squad].picture, (60 + 250 * res_squad, 200))
                show_localcentertext(operating_screen, 60 + 250*res_squad, 60 + 250*res_squad + 200, 180, dead_array[res_squad].name, Ignatio)

            operating_screen.blit(marker_down, (150 + 250*current_choice, 155))
            if (not Ignatio):
                operating_screen.blit(marker_down_white, (150 + 250*current_choice, 155))

            if get_out == 1:
                break
            pygame.display.update()
            clock.tick(30)
            
        status_change(status_array, current_move.name + " has used Phoenix fart on " + res_acquired.name)
        character_list.insert(0, dead_array.pop(current_choice))
        character_list[0].hp_current = character_list[0].hp_tot * 0.2
        consumable_list.pop(consum_number)
        return
    current_choice = 0
    get_out = 0
    while True:
        operating_screen.fill((100, 140, 230))
        if (not Ignatio):
            operating_screen.fill((0, 0, 0))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                current_choice = (current_choice - 1)%(len(character_list) + len(currently_fighting))
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                current_choice = (current_choice + 1)%(len(character_list) + len(currently_fighting))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if current_choice < len(character_list):
                    targ = character_list[current_choice]
                    get_out = 1
                else:
                    targ = currently_fighting[current_choice - len(character_list)]
                    get_out = 1
        for targeting_squad in range (0, len(character_list)):
            operating_screen.blit(character_list[targeting_squad].picture, (60 + 250 * targeting_squad, 200))
            show_localcentertext(operating_screen, 60 + 250*targeting_squad, 60 + 250*targeting_squad + 200, 180, character_list[targeting_squad].name, Ignatio)
        for mo_squad in range (0, len(currently_fighting)):
            operating_screen.blit(currently_fighting[mo_squad].picture, (60 + 250 * (len(character_list) + mo_squad), 200))
            show_localcentertext(operating_screen, 60 + 250 * (len(character_list) + mo_squad), 60 + 250 * (len(character_list) + mo_squad) + 200, 180, currently_fighting[mo_squad].name, Ignatio)

        operating_screen.blit(marker_down, (150 + 250*current_choice, 155))
        if (not Ignatio):
            operating_screen.blit(marker_down_white, (150 + 250*current_choice, 155))
        if get_out == 1:
            break
        pygame.display.update()
        clock.tick(30)
    getattr(consumable_list[consum_number], consumable_list[consum_number].effect)(targ)
    status_change(status_array, current_move.name + " has used " + consumable_list[consum_number].name + " on " + targ.name)
    consumable_list.pop(consum_number)
    targ.stat_change_equipment()

class item():
  def __init__(self, item_name, item_type, att_mod, def_mod, hp_mod, descript):
    self.name = item_name
    self.kind = item_type
    self.attack = att_mod
    self.defense = def_mod
    self.hp = hp_mod
    self.desc = descript
  def reset():
    self.attack = 0
    self.defense = 0
    self.hp = 0
    self.kind = "Airlol"
    self.name ="Nothing"

class artifact():
  def __init__(self, item_name, item_type, att_mod, def_mod, hp_mod, crit_chan_mod, crit_damage_mod, dodge_mod, turn_atk, turn_def, descript):
    self.name = item_name
    self.kind = item_type
    self.attack = att_mod
    self.defense = def_mod
    self.hp = hp_mod
    self.descript = descript



################################################################################################################## COMBAT CLASSES

def see_list_with_numbers(string, inventory, Ignatio):
    loop = True
    inventory_choice = len(inventory)
    chosen = 0
    sec_inven_choice = 10
    equipping_time = 0
    global in_the_benninging
    while loop:
        operating_screen.fill((50, 120, 120))
        if (not Ignatio):
            operating_screen.fill((0, 0, 0))
        if chosen == 1:
            show_text(operating_screen, 600, 300, "Back", Ignatio)
            show_text(operating_screen, 670, 300, string, Ignatio)
            show_text(operating_screen, 750, 300, "Discard", Ignatio)
            operating_screen.blit(marker, (575 + 75 * sec_inven_choice, 300))
            if (not Ignatio):
                operating_screen.blit(marker_white, (575 + 75 * sec_inven_choice, 300))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and inventory_choice == len(inventory):
                loop = False
                in_the_benninging = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and inventory_choice < len(inventory) and chosen == 0:
                chosen = 1
                sec_inven_choice = 100
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and sec_inven_choice == 0:
                chosen = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and sec_inven_choice == 1:
                equipping_time = 1
                in_the_benninging = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and sec_inven_choice == 2:
                inventory.pop(inventory_choice)
                chosen = 0
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP and chosen == 0) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and chosen == 0):
                inventory_choice = (inventory_choice - 1)%(len(inventory) + 1)
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and chosen == 0) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and chosen == 0):
                inventory_choice = (inventory_choice + 1)%(len(inventory) + 1)
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP and chosen == 1) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and chosen == 1):
                sec_inven_choice = (sec_inven_choice - 1)%3
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and chosen == 1) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and chosen == 1):
                sec_inven_choice = (sec_inven_choice + 1)%3

        show_bigtext(operating_screen, 520, 50, "Inventory", Ignatio)
        for lovely_items in range (0, len(inventory)):
            show_text(operating_screen, 110, 200+ 25*lovely_items, str(lovely_items + 1) + ". " + inventory[lovely_items].name + ": " + inventory[lovely_items].desc, Ignatio)

        show_text(operating_screen, 110, 700, "Back", Ignatio)
        operating_screen.blit(marker, (85, 700))
        if (not Ignatio):
            operating_screen.blit(marker_white, (85, 700))
        if inventory_choice < len(inventory):
            operating_screen.blit(marker, (85, 200 + 25*inventory_choice))
            if (not Ignatio):
                operating_screen.blit(marker_white, (85, 200 + 25*inventory_choice))
        if inventory_choice == len(inventory):
            operating_screen.blit(marker, (85, 700))
            if (not Ignatio):
                operating_screen.blit(marker_white, (85, 700))
        if equipping_time == 1:
            return inventory_choice

        pygame.display.update()
        clock.tick(30)
  
class attack_or_skill_move():
  def __init__(self, move_name, attack_ratio, status_applied, miss_ratio, critical_hit_modifier, critical_damage_modifier, att_red, def_red, crit_chan_red, crit_dam_red, miss_red, app_chan, app_dur, multi, PP, describe):
    self.name = move_name
    self.att_rat = attack_ratio
    self.att_red = att_red
    self.def_red = def_red
    self.crit_chan_red = crit_chan_red
    self.crit_dam_red = crit_dam_red
    self.miss_red = miss_red
    self.app_chan = app_chan
    self.app_dur = app_dur
    self.status_applied = status_applied
    self.miss_rat = miss_ratio
    self.crit_hit_mod = critical_hit_modifier
    self.crit_dam_mod = critical_damage_modifier
    self.multi = multi
    self.pp = PP
    self.desc = describe


#(self, move_name, attack_ratio, status_applied, miss_ratio, critical_hit_modifier, critical_damage_modifier, att_red, def_red, cc, cd, mis, app_chan, app_dur)
#Make all these arrays
skilldict1 = {
    "SMASH": attack_or_skill_move("SMASH", 2, "Nothing", 0.6, 1.2, 1.3, 0, 0, 0, 0, 0, 0, 0, "", 15, "2x atk, 40% hit, 1.2x crit chance, 1.3 crit dam"),
    "Shields Down!": attack_or_skill_move("Shields Down!", 0.4, "Armor penetration", 0.9, 1, 1, 1, 0.5, 1, 1, 1, 1, 2,"", 10, "0.4x atk, 90% hit, 100% chance to 0.5x def for 2 turns"),
    "Injection shot": attack_or_skill_move("Injection shot", 0.9, "Poison", 0.9, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 10, "POISON, 90% hit, 0.9x atk value is given as poison"),
    "RaRaRasputin": attack_or_skill_move("RaRaRasputin", 1, "Poison", 0.5, 0, 0, 0.5, 0.75, 1, 1, 1, 0.7, 2, "", 10, "POISON, 50% hit, 1x atk value is given as poison, ALSO 70% chance to 0.5x atk and 0.75x def for 2 turns"),
    "Ember": attack_or_skill_move("Ember", 0, "Burn", 1, 1, 1, 0.5, 0.8, 1, 1, 1, 1, 2, "", 10, "BURN, 100% hit, 100% chance to 0.5x atk and 0.8 def for 2 turns"),
    "Ice throw lol": attack_or_skill_move("Ice throw lol", 1.4, "Ice", 0.6, 1, 1, 1, 0, 1, 1, 1, 0.5, 2, "", 10,"1.4x atk, 60% hit, 50% chance to 0x def for 2 turns. LITERALLY chuck an ice 'snow'ball"),
    "Flashbang": attack_or_skill_move("Flashbang", 0.1, "Nothing", 0.9, 1, 1, 0.8, 0.8, 1, 1, 0.8, 1, 2, "", 15,"Basically no damage, 90% hit, 0.8x atk, def and lowers accuracy by 0.8x for 2 turns."),
    "Enrage": attack_or_skill_move("Enrage", 1.1, "Nothing", 1, 1, 1, 2, 1, 5, 2.5, 1, 1, 1, "", 5,"Attack a friend for 1.1x atk, 100% hit, 100% chance to 2x atk, 5x crit chance, and 2.5x crit damage for 1 turn"),
    "Eat vegetables": attack_or_skill_move("Eat vegetables", 0, "Nothing", 1, 1, 1, 1.3, 1.3, 1.3, 1.3, 1.3, 1, 3, "", 10,"No attack, 1.3x atk, def, crit chance, crit damage, hit chance for 3 turns"),
    "They don't eat vegetables :(": attack_or_skill_move("They don't eat vegetables :(", 0, "Nothing", 1, 1, 1, 0.7, 0.7, 0.7, 0.7, 0.8, 1, 3, "", 10,"No attack, 0.7 atk, def, crit chance, crit damage, hit chance (0.8x) for 3 turns"),
    "Poison Steroid": attack_or_skill_move("Poison Steroid", 1, "Poison", 1, 0, 0, 2, 2, 2, 2, 2, 1, 3, "", 5,"Attack a friend for 1x atk poison, 100% chance to 2x atk, 2x def, 2x crit chance, 2x crit damage, 2x accuracy for 2 turns"),
    "Freeze Feet": attack_or_skill_move("Freeze Feet", 0, "Ice", 1, 1, 1, 1, 1, 1, 1, 0.3, 1, 1, "", 5,"Lower Accuracy by 70% for their next turn")
,
}
skilldict2 = {
    "HULK SMASH": attack_or_skill_move("HULK SMASH", 3, "Nothing", 0.6, 2.2, 2.3, 0, 0, 0, 0, 0, 0, 0, "", 15,"3x atk, 60% hit, 2.2x crit chance, 2.3 crit dam"),
    "Russian Roulette": attack_or_skill_move("Russian Roulette", 6, "Nothing", 0.16, 10, 3, 0, 0, 0, 0, 0, 0, 0, "", 12,"6x atk, 16% hit, 10x crit chance, 3x crit damage"),
    "Lehmann Brothers": attack_or_skill_move("Lehmann Brothers", 0, "Nothing", 1, 1, 1, 10, 1, 10, 10, 0.05, 1, 2, "", 10,"10x atk buff, 10x crit chance, 10x crit damage, 5% hit chance for 2 turns"), 
    "Corrosive Acid": attack_or_skill_move("Corrosive Acid", 1.1, "Poison", 0.9, 2, 2, 0.7, 0.7, 1, 1, 1, 1, 2, "", 5,"POISON, 90% hit, 1.1x atk value is given as poison. 2x crit hit/damage, decreases attack and defense by 0.7x for 2 turns."),
    "Poison Pillar": attack_or_skill_move("RaRaRasputin", 1.6, "Poison", 0.8, 1, 1, 0, 0, 0, 0, 0, 0, 0, "", 5,"POISON, 80% hit, 2.2x atk value is given as poison."),
    "Fireball": attack_or_skill_move("Fireball", 1.5, "Burn", 1, 1, 1, 0.5, 0.8, 1, 1, 1, 1, 2, "", 10,"BURN, 100% hit, 2x atk, 100% chance to 0.5x atk and 0.8 def for 2 turns"),
    "Glacier": attack_or_skill_move("Glacier", 1, "Ice", 1, 1, 1, 1, 0, 1, 1, 0.5, 0.5, 3, "", 5,"1x atk, 100% hit, 100% chance to 0x def for 3 turns."),
    "Brazil": attack_or_skill_move("Brazil", 1, "Nothing", 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 1, "", 10,"Take someone to Brazil and... see what happens"),
    "Get Vaccinated": attack_or_skill_move("Get Vaccinated", 0.2, "Nothing", 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, "", 10,"Vaccinate someone. 3x defense for 3 turns."),
    "Heal": attack_or_skill_move("Heal", -0.2, "Heal", 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, "", 10,"No attack, 1.3x atk, def, crit chance, crit damage, hit chance for 3 turns"),
    "Cripple": attack_or_skill_move("Cripple", 0.5, "Nothing", 0.8, 1, 1, 0.5, 0.5, 0, 0, 0.7, 1, 3, "", 10,"hit for 0.5x atk, decrease their 0.5x atk, def. No more crits, 0.7x hit chance for 3 turns"),
    "Harder Better Faster Stronger": attack_or_skill_move("Harder Better Faster Stronger", 0, "Nothing", 1, 0, 0, 2, 2, 2, 2, 2, 1, 2, "", 5,"100% chance to 2x atk, 2x def, 2x crit chance, 2x crit damage, 2x accuracy for 2 turns"),
    "Imprison": attack_or_skill_move("Imprison", 0, "Nothing", 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, "", 5,"They will miss their next turn")
    #"Taunt"
}
artif_dict1 = {}
#(self, item_name, item_type, att_mod, def_mod, hp_mod)
item_dict1 = {
    "Noob Heart": item("Noob Heart", "Necklace", 0, 0, 20, "NECKLACE, +20 hp"),
    "Poop Gloves": item ("Poop Gloves", "Gloves", 2, 0, 0, "GLOVES, +2 atk"),
    "Selfie Stick": item ("Selfie Stick", "Weapon", 3, 0, 0, "WEAPON, +3 atk"),
    "Shield of Bashing": item ("Shield of Bashing", "Weapon", 2, 2, 0, "WEAPON, +2 atk, +2 def"),
    "Candy Crusher": item ("Candy Crusher", "Weapon", 2, 0, 20, "WEAPON, +2 atk, +20 hp"),
    "Rain Cloud Armor": item ("Rain Cloud Armor", "Armor", 0, 3, 0, "ARMOR, +3 def"),
    "Armor of PAIN": item ("Armor of PAIN", "Armor", 5, -1, -10, "ARMOR, +5 atk, -1 def, -10 hp"),
    "Armor of all trades, master of none": item ("Armor of all trades, master of none", "Armor", 1, 1, 10, "ARMOR, +1 atk, +1 def, +10 hp"),
    "Power Sto- I mean Ring": item ("Power Sto- I mean Ring", "Ring", 2, 0, 0, "RING, +2 atk"),
    "Literal Rock with a hole": item ("Literal Rock with a hole", "Ring", 0, 2, 0, "RING, +2 def"),
    "Wedding Ring": item ("Wedding Ring", "Ring", -2, 4, 20, "RING, -2 atk, +4 def, +20 hp")
}
item_dict2 = {
    "Lion's Pride": item("Lion's Pride", "Necklace", 5, 0, 0, "NECKLACE, +5 atk"),
    "Fighting Naked": item ("Fighting Naked", "Armor", 8, -2, 0, "ARMOR, +8 atk, -2 def"),
    "Longer Selfie Stick": item ("Longer Selfie Stick", "Weapon", 5, 0, 0, "WEAPON, +5 atk"),
    "Pillow": item ("Pillow", "Weapon", -3, +7, 0, "WEAPON, -2 atk, +7 def"),
    "Sword or all trades, master of none": item ("Sword or all trades, master of none", "Weapon", 2, 2, 20, "WEAPON, +2 atk, +20 hp"),
    "Cumulonimbus": item ("Cumulonimbus", "Armor", 0, 4, 0, "ARMOR, +4 def"),
    "Actual Chainmail": item ("Actual Chainmail", "Armor", 0, 3, 15, "ARMOR, +3 def, +15 hp"),
    "Flesh Sack": item ("Flesh Sack", "Armor", 0, 0, 40, "ARMOR, +40 hp"),
    "Donut": item ("Donut", "Ring", 0, 0, 30, "RING, +30 hp"),
    "Abstract Circle": item ("Abstract Circle", "Ring", 2, 2, 10, "RING, +2 atk, +2 def, +10 hp"),
    "Divorce Ring": item ("Divorce Ring", "Ring", +12, -2, -20, "RING, -2 atk, +4 def, +20 hp")
}

class Gold():
    def __init__(self, descript):
        self.desc = descript

strong_against_dict = {
    "Burn": "Freeze",
    "Freeze": "Poison",
    "Poison": "Normal",
    "Normal": "Burn"
}
gold_dict1 = {
    "Payout": Gold("Get the payout amount of gold"),
    "RNG": Gold("Get somewhere between 0.5x - 1.5x the payout gold"),#random.randint(scaling_gold(monster_counter)*0.5, len(monster_counter)*1.5),
    "Invest": Gold("Invest the payout so that future payouts scale by an additional (payout/30)%")
}
fightnot = ["Fight", "Shop"]

reward_dict1 = {
    "Item": item_dict1,
    "Attack/Skill": skilldict1,
    "Gold": gold_dict1
}
reward_dict2 = {
    "Item": item_dict2,
    "Attack/Skill": skilldict2
    }

##################################################################################################################################################### COMBAT
def attack(att_char, def_char, move_1, move_2, status_array):
############################## Miss calc: If miss_current LARGE, Hits easier, small = hits HARDER
  if (random.randint(1, 100)) > (att_char.movedict[move_1][move_2].miss_rat * 100  * att_char.miss_current): #Missing, if not continue to damage
    status_change(status_array, "MISSED LULULULULUL GET REKT " + att_char.name)
    status_change(status_array, "----------------------------------------")
    return
############################## Poison or heal defense ignore
  temp_defense = def_char.defense_current
  if att_char.movedict[move_1][move_2].status_applied == "Poison" or att_char.movedict[move_1][move_2].status_applied == "Heal":
    temp_defense = 0
############################## base damage w/o defense calc
  def_char.damage_taken = math.ceil(random.randint(math.ceil(att_char.attack_current * 0.85), math.ceil(att_char.attack_current * 1.1))*att_char.movedict[move_1][move_2].att_rat)
############################## CRIT CALC
  if random.randint(1, 100) <= (4 * att_char.movedict[move_1][move_2].crit_hit_mod * att_char.crit_chance_current): #Check if it's a crit.
    status_change(status_array, "IT'S A CRIIIITTTTTTT. LUCKKKYYYYYYYYYYYYYYY. You should go get a lottery ticket. Spend all your moneys :)")
    def_char.damage_taken = math.ceil(def_char.damage_taken * 1.7 * att_char.movedict[move_1][move_2].crit_dam_mod * att_char.crit_damage_current)
############################## Defense calc included
  def_char.damage_taken = math.ceil(def_char.damage_taken - temp_defense)
  if def_char.damage_taken < 0 and att_char.movedict[move_1][move_2].status_applied != "Heal":
    def_char.damage_taken = 0
############################## Status effect calc  
  stat_track = 0

  if random.randint(1,100) <= att_char.movedict[move_1][move_2].app_chan * 100:
    stat_track = 1
    def_char.buff_attack_current = def_char.buff_attack_current * att_char.movedict[move_1][move_2].att_red
    def_char.buff_defense_current = def_char.buff_defense_current * att_char.movedict[move_1][move_2].def_red
    def_char.buff_crit_chance_current = def_char.buff_crit_chance_current * att_char.movedict[move_1][move_2].crit_chan_red
    def_char.buff_crit_damage_current = def_char.buff_crit_damage_current * att_char.movedict[move_1][move_2].crit_dam_red
    def_char.buff_miss_current = def_char.buff_miss_current * att_char.movedict[move_1][move_2].miss_red
    for messiness in range(0, att_char.movedict[move_1][move_2].app_dur):
      def_char.buff_attack_timer_array[messiness] = def_char.buff_attack_timer_array[messiness] * att_char.movedict[move_1][move_2].att_red
      def_char.buff_defense_timer_array[messiness] = def_char.buff_defense_timer_array[messiness] * att_char.movedict[move_1][move_2].def_red
      def_char.buff_crit_chance_timer_array[messiness] = def_char.buff_crit_chance_timer_array[messiness] * att_char.movedict[move_1][move_2].crit_chan_red
      def_char.buff_crit_damage_timer_array[messiness] = def_char.buff_crit_damage_timer_array[messiness] * att_char.movedict[move_1][move_2].crit_dam_red
      def_char.buff_miss_timer_array[messiness] = def_char.buff_miss_timer_array[messiness] * att_char.movedict[move_1][move_2].miss_red
############################### Making sure poison conversion  
  damage_tipo = ""
  making_sure_poison_works = def_char.damage_taken

  if att_char.movedict[move_1][move_2].status_applied == "Poison":
    def_char.poison_count = def_char.poison_count + def_char.damage_taken
    damage_tipo = "Poison "
    def_char.damage_taken = 0

  status_change(status_array, att_char.name + " has used " + att_char.movedict[move_1][move_2].name + " and has dealt " + str(making_sure_poison_works) + " " + damage_tipo + "damage to " + def_char.name)
  if stat_track == 1:
    status_change(status_array, def_char.name + " has lost " + str(round(((1 - att_char.movedict[move_1][move_2].att_red)*100), 2)) + "% atk, " + str(round(((1 - att_char.movedict[move_1][move_2].def_red)*100), 2)) + "% def, " + str(round(((1 - att_char.movedict[move_1][move_2].miss_red)*100), 2)) + "% accuracy for " + str(att_char.movedict[move_1][move_2].app_dur) + " turns. ")
  status_change(status_array, "----------------------------------------")
  att_char.movedict[move_1][move_2].pp -= 1
  if att_char.movedict[move_1][move_2].pp == 0:
      att_char.movedict[move_1].pop(move_2)
  def_char.stat_change_damage()

################################################################################################################################################## CHARACTER




class character(): # self.hp is NOT a redundancy. It's the base hp for the equipment to be calculated with.
  def __init__(self, character_name, picture, small_picture):
    self.name = character_name
    self.picture = picture
    self.s_picture = small_picture
    self.hp = random.randint(60, 80)
    self.attack = random.randint(7, 11) 
    self.defense = random.randint(4, 7)
    self.buff_attack_timer_array = [1, 1, 1, 1, 1]
    self.buff_attack_current = 1
    self.buff_defense_timer_array = [1, 1, 1, 1, 1]
    self.buff_defense_current = 1
    self.buff_crit_chance_timer_array = [1, 1, 1, 1, 1]
    self.buff_crit_chance_current = 1
    self.buff_crit_damage_timer_array = [1, 1, 1, 1, 1]
    self.buff_crit_damage_current = 1
    self.buff_miss_timer_array = [1, 1, 1, 1, 1]
    self.buff_miss_current = 1
    self.poison_count = 0
    self.poison_og = 0
    self.movedict ={
      "Attack/Skill": {
                 "Basic strike": attack_or_skill_move("Basic strike", 1.2, "Nothing", 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, "", 40,"1.2x atk, 100% hit"),
                 "Jump attack": attack_or_skill_move("Jump attack", 1.5, "Nothing", 0.75, 2, 1.5, 0, 0, 0, 0, 0, 0, 0, "", 30,"1.5x atk, 75% hit, 2x crit chance, 1.5x crit dam"),
                 "Defend": attack_or_skill_move("Defend", 0, "Defend", 1, 1, 1, 1, 1.5, 1, 1, 1, 1, 2, "", 30,"A 1.5x defense buff that lasts for 2 turns"),
                 },
      "My status": {"Unequip": "lul this is just filler",
                    "Back": "lul this is just filler"},
      "Enemy status": {"Back": "lul this is just filler"},
      "Inventory": {"Equip": "lul this is just filler",
                    "Back": "lul this is just ffiililililierrerer"},
      "Consumables": {"Equip": "lul this is just filler",
                    "Back": "lul this is just ffiililililierrerer"}
      #"run" 
    }
    self.itemdict = {
      "Weapon":item("Nothing", "Airlol", 0, 0, 0, ""),
      "Ring":item("Nothing", "Airlol", 0, 0, 0, ""),
      "Boots":item("Nothing", "Airlol", 0, 0, 0, ""),
      "Armor":item("Nothing", "Airlol", 0, 0, 0, ""),
      "Gloves":item("Nothing", "Airlol", 0, 0, 0, ""),
      "Necklace":item("Nothing", "Airlol", 0, 0, 0, "")
  }
    self.damage_taken = 0
    self.hp_tot = self.hp
    self.hp_current = self.hp_tot
    self.attack_tot = self.attack
    self.attack_current = self.attack_tot
    self.defense_tot = self.defense
    self.defense_current = self.defense_tot
    self.crit_chance_current = 1
    self.crit_damage_current = 1
    self.miss_current = 1
    self.con_hp = 0
    self.con_def = 0
    self.con_att = 0

  def reset(self):
    self.attack_current = self.attack_tot
    self.defense_current = self.defense_tot
    self.buff_attack_timer_array = [1, 1, 1, 1, 1]
    self.buff_attack_current = 1
    self.buff_defense_timer_array = [1, 1, 1, 1, 1]
    self.buff_defense_current = 1
    self.buff_crit_chance_timer_array = [1, 1, 1, 1, 1]
    self.buff_crit_chance_current = 1
    self.buff_crit_damage_timer_array = [1, 1, 1, 1, 1]
    self.buff_crit_damage_current = 1
    self.buff_miss_timer_array = [1, 1, 1, 1, 1]
    self.buff_miss_current = 1
    self.crit_chance_current = 1
    self.crit_damage_current = 1
    self.miss_current = 1
    self.poison_count = self.poison_og
    self.con_hp = 0
    self.con_def = 0
    self.con_att = 0

  def stat_change_equipment(self):
    asdf = self.hp_tot
    self.hp_tot = self.hp + self.itemdict["Weapon"].hp + self.itemdict["Ring"].hp + self.itemdict["Boots"].hp + self.itemdict["Armor"].hp + self.itemdict["Gloves"].hp + self.itemdict["Necklace"].hp + self.con_hp
    self.attack_tot = self.attack + self.itemdict["Weapon"].attack + self.itemdict["Ring"].attack + self.itemdict["Boots"].attack + self.itemdict["Armor"].attack + self.itemdict["Gloves"].attack + self.itemdict["Necklace"].attack + self.con_att
    self.defense_tot = self.defense + self.itemdict["Weapon"].defense + self.itemdict["Ring"].defense + self.itemdict["Boots"].defense + self.itemdict["Armor"].defense + self.itemdict["Gloves"].defense + self.itemdict["Necklace"].defense + self.con_def
    self.hp_current = self.hp_current + (self.hp_tot - asdf) - self.damage_taken
    self.attack_current = self.attack_tot * self.buff_attack_current
    self.defense_current = self.defense_tot * self.buff_defense_current

  def stat_change_damage(self):
    self.hp_current = self.hp_current - self.damage_taken #ONLY CUMULATIVE
    self.attack_current = self.attack_tot * self.buff_attack_current
    self.defense_current = self.defense_tot * self.buff_defense_current
    self.crit_chance_current = self.buff_crit_chance_current
    self.crit_damage_current = self.buff_crit_damage_current
    self.miss_current = self.buff_miss_current
    self.damage_taken = 0

  def unequip(self, inventory, unequipping_item_type): #uneq = string
    inventory.append(self.itemdict[unequipping_item_type])
    self.itemdict[unequipping_item_type].reset
    self.stat_change_equipment()
    #show_text(operating_screen, 900, 100, "Your " + unequipping_item_type + " has been unequipped stoopid. ")   have the equipment notifications later

  def equip(self, inventory, equipping_item): #equipping_item is an integer
    if self.itemdict[inventory[equipping_item].kind].kind != "Airlol":
      self.unequip(inventory, inventory[equipping_item].kind)
    self.itemdict[inventory[equipping_item].kind] = inventory[equipping_item] #switching Item-value
    inventory.pop(equipping_item)
    self.stat_change_equipment()



  def stat_recall(self, Ignatio):
    loop = True
    while loop:
        operating_screen.fill((50, 120, 120))
        if (not Ignatio):
            operating_screen.fill((0, 0, 0))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                loop = False
                global in_the_benninging
                in_the_benninging = True
        
        
        show_bigcentertext(operating_screen, 50, "Your Stats", Ignatio)
        show_text(operating_screen, 110, 200, "Your name is: " + self.name, Ignatio)
        show_text(operating_screen, 110, 225, "Your current hp is: " + str(self.hp_current) + "/" + str(self.hp_tot), Ignatio)
        show_text(operating_screen, 110, 250, "Your current attack is: " + str(self.attack_current) + "/" + str(self.attack_tot), Ignatio)        
        show_text(operating_screen, 110, 275, "Your current defense is: " + str(self.defense_current) + "/" + str(self.defense_tot), Ignatio)         
        show_text(operating_screen, 110, 300, "Your attack buff for the following 2 turns are: TURN 1:(" + str(self.buff_attack_timer_array[0]) + ") TURN 2:(" + str(self.buff_attack_timer_array[1]) + ")", Ignatio)
        show_text(operating_screen, 110, 325, "Your defense buff for the following 2 turns are: TURN 1:(" + str(self.buff_defense_timer_array[0]) + ") TURN 2:(" + str(self.buff_defense_timer_array[1]) + ")", Ignatio)
        show_text(operating_screen, 110, 350, "Your critical chance buff for the following 2 turns are: TURN 1:(" + str(self.buff_crit_chance_timer_array[0]) + ") TURN 2:(" + str(self.buff_crit_chance_timer_array[1]) + ")", Ignatio)
        show_text(operating_screen, 110, 375, "Your critical damage buff for the following 2 turns are: TURN 1:(" + str(self.buff_crit_damage_timer_array[0]) + ") TURN 2:(" + str(self.buff_crit_damage_timer_array[1]) + ")", Ignatio)
        show_text(operating_screen, 110, 400, "Your SANIC buff for the following 2 turns are: TURN 1:(" + str(self.buff_miss_timer_array[0]) + ") TURN 2:(" + str(self.buff_miss_timer_array[1]) + ")", Ignatio)
        show_text(operating_screen, 110, 425, "Your weapon is currently: " + self.itemdict["Weapon"].name, Ignatio)
        show_text(operating_screen, 110, 450, "Your ring is currently: " + self.itemdict["Ring"].name, Ignatio)
        show_text(operating_screen, 110, 475, "Your boots are currently: " + self.itemdict["Boots"].name, Ignatio)
        show_text(operating_screen, 110, 500, "Your armor is currently: " + self.itemdict["Armor"].name, Ignatio)
        show_text(operating_screen, 110, 525, "Your gloves is currently: " + self.itemdict["Gloves"].name, Ignatio)
        show_text(operating_screen, 110, 550, "Your necklace is currently: " + self.itemdict["Necklace"].name, Ignatio)
        show_text(operating_screen, 110, 575, "Your poison counter is currently: " + str(self.poison_count), Ignatio)
        show_text(operating_screen, 110, 600, "Your current accuracy is: " + str(self.miss_current) + "/1", Ignatio) 
        show_text(operating_screen, 110, 700, "Back", Ignatio)
        operating_screen.blit(marker, (85, 700))
        if (not Ignatio):
            operating_screen.blit(marker_white, (85, 700))
        

        pygame.display.update()
        clock.tick(30)

################################################################################################################################################### MONSTER

class Monster(): #plan: make movedict number mod. keys, values as function which changes effect of att, def, hp, etc. 
  def __init__(self, enemy_name, picture, mon_type, monster_array, character_list_array):
    self.name = enemy_name
    self.picture = picture
    self.fight_counter = len(monster_array)
    self.player_num = len(character_list_array)
    self.type_mod_hp = 1
    self.type_mod_att = 1
    self.type_mod_def = 1
    self.m_type = mon_type #string, not int
    self.buff_attack_timer_array = [1, 1, 1, 1 ,1 ]
    self.buff_attack_current = 1
    self.buff_defense_timer_array = [1, 1, 1, 1, 1]
    self.buff_defense_current = 1
    self.buff_crit_chance_timer_array = [1, 1, 1, 1, 1]
    self.buff_crit_chance_current = 1
    self.buff_crit_damage_timer_array = [1, 1, 1, 1, 1]
    self.buff_crit_damage_current = 1
    self.buff_miss_timer_array = [1, 1, 1, 1, 1]
    self.buff_miss_current = 1
    self.poison_count = 0 #monster.movedict[current_move.m_type][4][move_one]
#(self, move_name, attack_ratio, status_applied, miss_ratio, critical_hit_modifier, critical_damage_modifier, att_red, def_red, app_chan, app_dur)
    self.movedict = {
      "Normal":{
          "1": attack_or_skill_move("Monster strike", 1, "Nothing", 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, "", 1000,""),
          "2": attack_or_skill_move("SMASH", 2.3, "Nothing", 0.4, 1.2, 1.3, 0, 0, 0, 0, 0, 0, 0, "", 1000,"2.3x atk, 60% hit, 1.2x crit chance, 1.3 crit dam"),
          "3": attack_or_skill_move("Shields Down!", 0.4, "Armor penetration", 0.9, 1, 1, 1, 0.5, 1, 1, 1, 1, 2, "", 1000,"0.4x atk, 90% hit, 100% chance to 0.5x def for 3 turns")
      },
      "Poison":{
          "1": attack_or_skill_move("Monster strike", 1, "Nothing", 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, "", 1000,""),
          "2": attack_or_skill_move("Injection shot", 1, "Poison", 0.9, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1000,"POISON, 90% hit, 1x atk value is given as poison"),
          "3": attack_or_skill_move("RaRaRasputin", 1.2, "Poison", 0.5, 0, 0, 0.5, 0.75, 1, 1, 1, 0.7, 2, "", 1000,"POISON, 50% hit, 1.2x atk value is given as poison, ALSO 70% chance to 0.5x atk and 0.75x def for 2 turns")
      },
      "Fire":{
          "1": attack_or_skill_move("Monster strike", 1, "Nothing", 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, "", 1000,""),
          "2": attack_or_skill_move("Ember", 0, "Burn", 1, 1, 1, 0.5, 0.8, 1, 1, 1, 1, 2, "", 1000,"BURN, 100% hit, 100% chance to 0.5x atk and 0.8 def for 2 turns"),
          "3": attack_or_skill_move("Fire punch", 1.3, "Burn", 0.8, 1.3, 1.3, 0.5, 0.8, 1, 1, 1, 0.6, 1, "", 1000,"BURN, 1.3x atk, 80% hit, 1.3x crit chance, 1.3x crit dam, 50% chance to 0.8x atk and 0.8x def for 1 turn")
      },
      "Ice":{
          "1": attack_or_skill_move("Monster strike", 1, "Nothing", 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,"", 1000,""),
          "2": attack_or_skill_move("Ice throw lol", 1.4, "Ice", 0.6, 1, 1, 1, 0.5, 1, 1, 1, 0.5, 2, "", 1000,"1.4x atk, 60% hit, 50% chance to 0.5x def for 2 turns. LITERALLY chuck an ice 'snow'ball"),
          "3": attack_or_skill_move("Blizzard", 0, "Ice", 1, 1, 1, 0.5, 0, 1, 1, 1, 0.7, 3, "", 1000,"100% hit, 70% chance to 0.5x atk and 0x def for 3 turns") #miss should 0, but is bigger
      },
      "Bomb":{
          "0": attack_or_skill_move("Charge Up", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1,"Charge Up"),
          "1": attack_or_skill_move("Charge Up", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1,"Charge Up"),
          "2": attack_or_skill_move("Charge Up", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1,"Charge Up"),
          "3": attack_or_skill_move("Charge Up", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1,"Charge Up"),
          "4": attack_or_skill_move("Charge Up", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1,"Charge Up"),
          "5": attack_or_skill_move("Charge Up", 6, "Reset", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Mass", 1,"EXPLOOOODE"),
          "6": attack_or_skill_move("Charge Up", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1,"Charge Up"),
          "7": attack_or_skill_move("Charge Up", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1,"Charge Up"),
          "8": attack_or_skill_move("Charge Up", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1,"Charge Up"),
          "9": attack_or_skill_move("Charge Up", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1,"Charge Up"),
          "10": attack_or_skill_move("Charge Up", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1,"Charge Up"),
          "11": attack_or_skill_move("Charge Up", 6, "Reset", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Mass", 1,"EXPLOOOODE"),
          "12": attack_or_skill_move("Charge Up", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1,"Charge Up"),
          "13": attack_or_skill_move("Charge Up", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1,"Charge Up"),
          "14": attack_or_skill_move("Charge Up", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1,"Charge Up"),
          "15": attack_or_skill_move("Charge Up", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1,"Charge Up"),
          "16": attack_or_skill_move("Charge Up", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1,"Charge Up"),
          "17": attack_or_skill_move("Charge Up", 6, "Reset", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Mass", 1,"EXPLOOOODE"),
    },
      "Occipitus":{
          "0": attack_or_skill_move("Eye of Pain", 1.5, "Nothing", 1.5, 1, 1, 0, 0, 0, 0, 0, 0, 0,"", 1000,"Nothing unusual occurs"),
          "1": attack_or_skill_move("Eye of Pain", 1.5, "Nothing", 1.5, 1, 1, 0, 0, 0, 0, 0, 0, 0,"", 1000,"Nothing unusual occurs"),
          "2": attack_or_skill_move("Close Eye", 0, "Own", 100, 1, 1, 1, 2, 1, 1, 1, 1, 1, "", 1000,"Occipitus' eye shuts; the Red Prong begins to shine"),
          "3": attack_or_skill_move("Ocular Charge", 0, "Own", 100, 1, 1, 1, 2, 5, 5, 5, 1, 1, "", 1000,"The Red Prong shines brightly"),
          "4": attack_or_skill_move("Eye of Oblivion", 3, "Nothing", 1.5, 1, 1, 0, 0, 0, 0, 0, 0, 0, "Mass", 1000,"Occipitus' Eye opens, emitting a devastating laser. The Red Prong no longer shines."),
          "5": attack_or_skill_move("Rest", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1000,"Occipitus rests"),
          "6": attack_or_skill_move("Eye of Exhaustion", 1, "Nothing", 1.5, 1, 1, 0.8, 0.8, 0.8, 0.8, 0.8, 1, 2, "", 1000,"Nothing unusual occurs"),
          "7": attack_or_skill_move("Eye of Exhaustion", 1, "Nothing", 1.5, 1, 1, 0.8, 0.8, 0.8, 0.8, 0.8, 1, 2, "", 1000,"Nothing unusual occurs"),
          "8": attack_or_skill_move("Close Eye", 0, "Own", 100, 1, 1, 1, 2, 1, 1, 1, 1, 1, "", 1000,"Occipitus' eye shuts; the Blue Prong begins to shine"),
          "9": attack_or_skill_move("Ocular Charge", 0, "Own", 100, 1, 1, 1, 2, 1, 1, 10, 1, 1, "", 1000,"The Blue Prong shines brightly"),
          "10": attack_or_skill_move("Eye of Despair", 1, "Nothing", 2, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.8, 1, 5, "Mass", 1000,"Occipitus' Eye opens, Draining everyone's energy. The Blue Prong no longer shines."),
          "11": attack_or_skill_move("Rest", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1000,"Occipitus rests"),
          "12": attack_or_skill_move("Eye of Healing", -1, "Own", 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, "", 1000,"Nothing unusual occurs"),
          "13": attack_or_skill_move("Eye of Healing", -1, "Own", 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, "", 1000,"Nothing unusual occurs"),
          "14": attack_or_skill_move("Close Eye", 0, "Own", 100, 1, 1, 1, 2, 1, 1, 1, 1, 1, "", 1000,"Occipitus' eye shuts; the Green Prong begins to shine"),
          "15": attack_or_skill_move("Ocular Charge", 0, "Own", 100, 1, 1, 1, 1, 1, 1, 10, 1, 1, "", 1000,"The Green Prong shines brightly"),
          "16": attack_or_skill_move("Eye of Empowerment", 0, "Own", 2, 1, 1, 3, 3, 3, 3, 3, 1, 5, "", 1000,"Occipitus' Eye opens, Massively strengthening itself. The Green Prong no longer shines."),
          "17": attack_or_skill_move("Rest", 0, "Nothing", 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 1000,"Occipitus rests"),
          }
  }
    self.typedict ={
      "Normal":[1, 1, 1, ""],
      "Poison":[0.6, 0.2, 1, "Poisonous"],
      "Fire":[0.7, 1.1, 0.8, "Burning"],
      "Ice":[0.65, 0.8, 1.1, "Freezing"],
      "Bomb":[1.5, 1, 1, "Exploding"],
      "Occipitus":[2.1, 1.5, 1, ""] 
  }
  #I think I can consolidate self.hp/a/d with self.hp/a/d_tot: NOTE: Even if it is, it must be separated in Character()
    self.itemdict = {
      "Weapon":item("Nothing", "Airlol", 0, 0, 0, ""),
      "Ring":item("Nothing", "Airlol", 0, 0, 0, ""),
      "Boots":item("Nothing", "Airlol", 0, 0, 0, ""),
      "Armor":item("Nothing", "Airlol", 0, 0, 0, ""),
      "Gloves":item("Nothing", "Airlol", 0, 0, 0, ""),
      "Necklace":item("Nothing", "Airlol", 0, 0, 0, "")
  }
    self.hp = math.ceil(random.randint(55, 70) * (((1.15 ** (self.fight_counter - 10))*(self.fight_counter/50)) + 1) * (1.2 ** self.player_num))
    self.attack = math.ceil(random.randint(5, 8) * (((1.15 ** (self.fight_counter - 10))*(self.fight_counter/50)) + 1) * (1.4 ** self.player_num))
    self.defense = math.ceil(random.randint(1, 4) * (((1.15 ** (self.fight_counter - 10))*(self.fight_counter/50)) + 1) * (1.3 ** self.player_num))
    self.damage_taken = 0
    self.hp_tot = self.hp #self.itemdict["weapon"].hp + self.itemdict["ring"].hp + self.itemdict["boots"].hp + self.itemdict["armor"].hp
    self.hp_current = self.hp_tot
    self.attack_tot = self.attack #self.itemdict["weapon"].attack + self.itemdict["ring"].attack + self.itemdict["boots"].attack + self.itemdict["armor"].attack
    self.attack_current = self.attack_tot
    self.defense_tot = self.defense #self.itemdict["weapon"].defense + self.itemdict["ring"].defense + self.itemdict["boots"].defense + self.itemdict["armor"].defense
    self.defense_current = self.defense_tot
    self.crit_chance_current = 1
    self.crit_damage_current = 1
    self.miss_current = 1
    self.con_hp = 0
    self.con_def = 0
    self.con_att = 0

  def stat_change_equipment(self):
    asdf = self.hp_tot
    self.hp_tot = self.hp + self.itemdict["Weapon"].hp + self.itemdict["Ring"].hp + self.itemdict["Boots"].hp + self.itemdict["Armor"].hp + self.itemdict["Gloves"].hp + self.itemdict["Necklace"].hp + self.con_hp
    self.attack_tot = self.attack + self.itemdict["Weapon"].attack + self.itemdict["Ring"].attack + self.itemdict["Boots"].attack + self.itemdict["Armor"].attack + self.itemdict["Gloves"].attack + self.itemdict["Necklace"].attack + self.con_att
    self.defense_tot = self.defense + self.itemdict["Weapon"].defense + self.itemdict["Ring"].defense + self.itemdict["Boots"].defense + self.itemdict["Armor"].defense + self.itemdict["Gloves"].defense + self.itemdict["Necklace"].defense + self.con_def
    self.hp_current = self.hp_current + (self.hp_tot - asdf) - self.damage_taken
    self.attack_current = self.attack_tot * self.buff_attack_current
    self.defense_current = self.defense_tot * self.buff_defense_current

    
  def type_mod (self, m_type): #only used at monster creation
    self.type_mod_hp = self.typedict[m_type][0]
    self.type_mod_att = self.typedict[m_type][1]
    self.type_mod_def = self.typedict[m_type][2]
    self.name = self.typedict[m_type][3] + self.name
    self.hp = math.ceil(self.hp * self.type_mod_hp)
    self.attack = math.ceil(self.attack * self.type_mod_att)
    self.defense = math.ceil(self.defense * self.type_mod_def)
    self.hp_tot = self.hp
    self.hp_current = self.hp_tot
    self.attack_tot = self.attack
    self.defense_tot = self.defense

  def stat_change_damage(self): #commented parts may be used if enemies have items
    self.hp_current = self.hp_current - self.damage_taken #ONLY CUMUL
    self.attack_current = self.attack_tot * self.buff_attack_current
    self.defense_current = self.defense_tot * self.buff_defense_current
    self.crit_chance_current = self.buff_crit_chance_current
    self.crit_damage_current = self.buff_crit_damage_current
    self.miss_current = self.buff_miss_current
    self.damage_taken = 0

  def reset(self):
    self.type_mod_hp = 1
    self.type_mod_att = 1
    self.type_mod_def = 1
    self.m_type = mon_type #string, not int
    self.buff_attack_timer_array = [1, 1, 1, 1 ,1 ]
    self.buff_attack_current = 1
    self.buff_defense_timer_array = [1, 1, 1, 1, 1]
    self.buff_defense_current = 1
    self.buff_crit_chance_timer_array = [1, 1, 1, 1, 1]
    self.buff_crit_chance_current = 1
    self.buff_crit_damage_timer_array = [1, 1, 1, 1, 1]
    self.buff_crit_damage_current = 1
    self.buff_miss_timer_array = [1, 1, 1, 1, 1]
    self.buff_miss_current = 1
    self.poison_count = 0 #monster.movedict[current_move.m_type][4][move_one]
    self.attack_current = self.attack_tot
    self.defense_current = self.defense_tot
      

  def monster_stat_recall(self, str_type, type_array, Ignatio):
    loop = True
    while loop:
        operating_screen.fill((50, 120, 120))
        if (not Ignatio):
            operating_screen.fill((0, 0, 0))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                loop = False
                global in_the_benninging
                in_the_benninging = True
        
        
        show_bigcentertext(operating_screen, 50, "Monster Stats", Ignatio)
        show_text(operating_screen, 110, 250, "Name: " + self.name, Ignatio)
        show_text(operating_screen, 110, 300, "Current hp: " + str(self.hp_current) + "/" + str(self.hp_tot), Ignatio)
        show_text(operating_screen, 110, 350, "Current attack: " + str(self.attack_current) + "/" + str(self.attack_tot), Ignatio)        
        show_text(operating_screen, 110, 400, "Current defense: " + str(self.defense_current) + "/" + str(self.defense_tot), Ignatio)     
        show_text(operating_screen, 110, 450, "Current poison: " + str(self.poison_count), Ignatio)
        show_text(operating_screen, 110, 500, "Type: " + str_type, Ignatio)

        show_text(operating_screen, 110, 700, "Back", Ignatio)
        operating_screen.blit(marker, (85, 700))
        if (not Ignatio):
            operating_screen.blit(marker_white, (85, 700))
        

        pygame.display.update()
        clock.tick(30)
        



    ########################################################################################################### Poison
    #if self.poison_count != 0:
      #self.damage_taken = current_move.poison_count
      #self.poison_count = current_move.poison_count - 1
      #self.stat_change_damage()





def fight(dead_char, monster_types, monster_counter, character_list, inventory, consumable_list, Happiness, Ignatio): #int, monster_type_array, monster_array, int, character_array, inv_array, inv_int
    global GET_ME_OUT
    global gold
    global investment
    currently_fighting = []
    currently_fighting.append(Happiness)
  
  # Happiness.monster_stat_recall(temp_type, monster_types)
    battle_time = 1
    victory = 0
    battle_over = 0
    tracker = 0
    temp_keys = []
    adjust = 0
    repeat = 0
    boss_move = 0
    status_array = ["", "", "", "", "", "", "", "", "", "", "", ""]
    while battle_time == 1:
        global in_the_benninging
        in_the_benninging = False
        operating_screen.fill((100, 140, 230))
        if (not Ignatio):
            operating_screen.fill((0, 0, 0))
    ########################################################################################################### Check if People are dead
        for end_pointer in range (0, len(character_list)): 
            if character_list[end_pointer - adjust].hp_current <= 0:
                show_text(operating_screen, 110, 250 + 50*adjust, character_list[end_pointer].name + " has died", Ignatio)
                pygame.display.update()
                pygame.time.delay(2000)
                operating_screen.fill((100, 140, 230))
                if (not Ignatio):
                    operating_screen.fill((0, 0, 0))
                dead_char.append(character_list.pop(end_pointer))
                adjust = adjust + 1
        adjust = 0
        for pop_pointer in range (0, len(currently_fighting)): 
            if currently_fighting[pop_pointer - adjust].hp_current <= 0:
                show_centertext(operating_screen, 450 + 50*adjust, currently_fighting[pop_pointer].name + " has died", Ignatio)
                pygame.display.update()
                pygame.time.delay(2000)
                operating_screen.fill((100, 140, 230))
                if (not Ignatio):
                    operating_screen.fill((0, 0, 0))
                monster_counter.append(currently_fighting.pop(pop_pointer))
                adjust = adjust + 1
        adjust = 0
        if len(character_list) == 0:
            battle_over = 1
        if len(currently_fighting) == 0:
            victory = 1
        if victory == 1 or battle_over == 1:
          break
        ########################################################################################################### Current_move establishment
        turn_track = tracker%(len(character_list) + len(currently_fighting))
        if turn_track <= len(character_list) - 1:
            current_move = character_list[turn_track]
        else:
            current_move = currently_fighting[turn_track - len(character_list)]
        status_change(status_array, "It is now " + current_move.name + "'s turn.")
         ########################################################################################################### Apply Buffs and Debuffs
        if repeat == 0:
            current_move.buff_attack_current = current_move.buff_attack_timer_array.pop(0)
            current_move.buff_attack_timer_array.append(1)
            current_move.buff_defense_current = current_move.buff_defense_timer_array.pop(0)
            current_move.buff_defense_timer_array.append(1)
            current_move.buff_crit_chance_current = current_move.buff_crit_chance_timer_array.pop(0)
            current_move.buff_crit_chance_timer_array.append(1)
            current_move.buff_crit_damage_current = current_move.buff_crit_damage_timer_array.pop(0)
            current_move.buff_crit_damage_timer_array.append(1)
            current_move.buff_miss_current = current_move.buff_miss_timer_array.pop(0)
            current_move.buff_miss_timer_array.append(1)
            current_move.stat_change_damage()
            if turn_track <= len(character_list) - 1:
                Att_keys = list(current_move.movedict["Attack/Skill"].keys())
                if len(Att_keys) > 3:
                    Att_keys = random.sample(Att_keys, k = 3)
        ############################################################################################################### Make the Screen Battle
        operating_screen.blit(status_box, (575, 80))
        for statuses in range (0, 12):
            show_kindasmalltext(operating_screen, 600, 100 + 25*statuses, status_array[statuses], True)
        for character_layout in range (0, len(character_list)):
            if current_move == character_list[character_layout]:
                continue
            health_bar(100 + 100*character_layout + 82, 150 - 70*math.sqrt(character_layout) + 10, 5, character_list[character_layout].hp_tot *(2/5), character_list[character_layout].hp_current *(2/5), operating_screen)
            operating_screen.blit(character_list[character_layout].s_picture, (100 + 100*character_layout, 150 - 70*math.sqrt(character_layout)))
            show_localsmallcentertext(operating_screen, 100 + 100*character_layout, 100 + 100*character_layout + 76, 140 - 70*math.sqrt(character_layout), character_list[character_layout].name, Ignatio)
        show_kindasmalltext(operating_screen, 1200, 10, "Creatures Defeated: " + str(len(monster_counter)), Ignatio)

        current_choice = 0
        operating_screen.blit(current_move.picture, (270, 260))
        health_bar(490, 270, 25, current_move.hp_tot, current_move.hp_current, operating_screen)
        show_localcentertext(operating_screen, 270, 470, 230, current_move.name, Ignatio)    
        operating_screen.blit(currently_fighting[0].picture, (1000, 500))
        health_bar_enemy(1220, 510, 25, 200, currently_fighting[0].hp_tot, currently_fighting[0].hp_current, operating_screen)
        temp_keys = list(current_move.movedict.keys())
        for first_move in range (0, len(temp_keys)):
            show_text(operating_screen, 150, 570 + 25*first_move, temp_keys[first_move], Ignatio)
        operating_screen.blit(text_box, (100, 550))
        operating_screen.blit(marker, (125, 570 + 25*current_choice))
        if (not Ignatio):
            operating_screen.blit(marker_white, (125, 570 + 25*current_choice))


        ########################################################################################################### Monster Move
        if turn_track > len(character_list) - 1:
            if current_move.m_type == "Occipitus" or current_move.m_type == "Bomb":
                move_one = boss_move%18
                boss_move += 1
                status_change(status_array, current_move.movedict[current_move.m.type][move_one].desc)
            else:
                move_one = str(random.randint(1, 3))
            #self.movedict[m_type][4][move_one]
            if current_move.movedict[current_move.m_type][move_one].status_applied == "Reset":
                current_move.reset()
            if current_move.movedict[current_move.m_type][move_one].status_applied == "Own":
                attack(current_move, current_move, current_move.m_type, move_one, status_array)
            elif current_move.movedict[current_move.m_type][move_one].multi == "Mass":
                for attack_all in range (0, len(character_list)):
                    attack(current_move, character_list[attack_all], current_move.m_type, move_one, status_array)
            else:
                player_attack = random.randint(0, len(character_list) - 1)
                attack(current_move, character_list[player_attack], current_move.m_type, move_one, status_array)
            if current_move.poison_count != 0:
                current_move.damage_taken = current_move.poison_count
                current_move.poison_count = current_move.poison_count - 1
                current_move.stat_change_damage()
            tracker += 1 
            continue
        ########################################################################################################### Actual Player inputs/Agency
        
        current_choice = 0
        second_move = ""
        continuous = True
        while continuous:
            pygame.draw.rect(operating_screen, (0, 0, 0), pygame.Rect(124, 569, 25, 125))
            operating_screen.blit(marker, (125, 570 + 25*current_choice))
            if (not Ignatio):
                operating_screen.blit(marker_white, (125, 570 + 25*current_choice))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    current_choice = (current_choice - 1)%5
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    current_choice = (current_choice + 1)%5
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    second_move = temp_keys[current_choice]
                    continuous = False
            pygame.display.update()
            clock.tick(30)

        current_choice = 0
        continuous = True
        backing = 0
        
        while second_move == "Attack/Skill":
            operating_screen.fill((100, 140, 230))
            if (not Ignatio):
                operating_screen.fill((0, 0, 0))
            show_bigcentertext(operating_screen, 50, "Time to Strike! Or Defend I guess...", Ignatio)
            time_to_strike = ""
            get_out = 0
            choosing_target = 0
            strike_target = 0
            events = pygame.event.get()
            
                    
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                    current_choice = (current_choice - 1)%(len(Att_keys) + 1)
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                    current_choice = (current_choice + 1)%(len(Att_keys) + 1)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if current_choice == 0:
                        backing = 1
                    else:
                        time_to_strike = Att_keys[current_choice - 1]
                        get_out = 1

            show_text(operating_screen, 110, 700, "Back", Ignatio)            
            for offensive_move in range (0, len(Att_keys)):
                show_text(operating_screen, 110, 195 + 25*offensive_move, Att_keys[offensive_move] + ": " + current_move.movedict["Attack/Skill"][Att_keys[offensive_move]].desc + "             | " + str(current_move.movedict["Attack/Skill"][Att_keys[offensive_move]].pp) + " LEFT", Ignatio)

            if current_choice == 0:
                operating_screen.blit(marker,(85, 700))
                if (not Ignatio):
                    operating_screen.blit(marker_white,(85, 700))
            else:
                operating_screen.blit(marker, (85, 170 + 25*current_choice))
                if (not Ignatio):
                    operating_screen.blit(marker_white, (85, 170 + 25*current_choice))
            if backing == 1:
                in_the_benninging = True
                break
            elif get_out == 1:
                break
                
            pygame.display.update()
            clock.tick(30)
        ########################################################################################################### input checking
            
        if second_move == "My status":
            current_move.stat_recall(Ignatio)
        if second_move == "Inventory":
            poopy = see_list_with_numbers("Equip", inventory, Ignatio)
            if type(poopy) == int:
                status_change(status_array, current_move.name + " has equipped " + inventory[poopy].name)
                current_move.equip(inventory, poopy)
        if second_move == "Consumables":
            poopy = see_list_with_numbers("Use", consumable_list, Ignatio)
            if type(poopy) == int:
                use_consumable(consumable_list, poopy, character_list, dead_char, currently_fighting, status_array, current_move, Ignatio)
                tracker += 1
        if second_move == "Enemy status":
            currently_fighting[0].monster_stat_recall(Happiness.m_type, monster_types, Ignatio)
        if in_the_benninging == True:
            repeat += 1
            if second_move == "Consumables":
                repeat = 0
            continue

        repeat = 0
        get_out = 0
        current_choice = 0
        while True:
            operating_screen.fill((100, 140, 230))
            if (not Ignatio):
                operating_screen.fill((0, 0, 0))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                    current_choice = (current_choice - 1)%(len(character_list) + len(currently_fighting))
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                    current_choice = (current_choice + 1)%(len(character_list) + len(currently_fighting))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if current_choice < len(character_list):
                        target_acquired = character_list[current_choice]
                        get_out = 1
                    else:
                        target_acquired = currently_fighting[current_choice - len(character_list)]
                        get_out = 1
            
            for fired_squad in range (0, len(character_list)):
                operating_screen.blit(character_list[fired_squad].picture, (60 + 250 * fired_squad, 200))
                show_localcentertext(operating_screen, 60 + 250*fired_squad, 60 + 250*fired_squad + 200, 180, character_list[fired_squad].name, Ignatio)
            for mon_squad in range (0, len(currently_fighting)):
                operating_screen.blit(currently_fighting[mon_squad].picture, (60 + 250 * (len(character_list) + mon_squad), 200))
                show_localcentertext(operating_screen, 60 + 250 * (len(character_list) + mon_squad), 60 + 250 * (len(character_list) + mon_squad) + 200, 180, currently_fighting[mon_squad].name, Ignatio)

            operating_screen.blit(marker_down, (160 + 250*current_choice, 155))
            if (not Ignatio):
                operating_screen.blit(marker_down_white, (160 + 250*current_choice, 155))
            if get_out == 1:
                break
            pygame.display.update()
            clock.tick(30)
        
        current_choice = 0
        attack(current_move, target_acquired, "Attack/Skill", time_to_strike, status_array)
        
        ########################################################################################################### Poison
        if current_move.poison_count > 0:
          current_move.damage_taken = current_move.poison_count
          current_move.poison_count = current_move.poison_count - 1
          current_move.stat_change_damage()

      
        tracker += 1
############################################################################################################### end-while
    if victory == 1:
        current_choice = 0
        get_out = 0
        if len(monster_counter) <= 5:
            temp_keys = list(reward_dict1.keys())
        if len(monster_counter) <= 10 and len(monster_counter) > 5:
            temp_keys = list(reward_dict2.keys()) #And so on
        for reward_yay in range (0, len(character_list)):
            while True:
                operating_screen.fill((48, 205, 62))
                if (not Ignatio):
                    operating_screen.fill((0, 0, 0))
                show_bigcentertext(operating_screen, 50, "REWARDS #Positive Reinforcement", Ignatio)
                show_centertext(operating_screen, 175, "YOOOOOOO, you actually did it. Nice. Have fun with the loot or whatever. Get dopamine rushed.", Ignatio)
                show_centertext(operating_screen, 200, "And yes, I actually included rewards into this game. I know right? I think this is like my 10th day programming. Crazy.", Ignatio)
                show_centertext(operating_screen, 225, "Anyways, choose one of the following " + character_list[reward_yay].name + ": ", Ignatio)
                for reward_list in range (0, len(temp_keys)):
                    show_text(operating_screen, 220 + 250*reward_list, 450, temp_keys[reward_list], Ignatio)
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                        current_choice = (current_choice - 1)%len(temp_keys)
                    if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                        current_choice = (current_choice + 1)%len(temp_keys)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        choice_reward = temp_keys[current_choice]
                        get_out = 1

                operating_screen.blit(marker, (195 + 250*current_choice, 450))
                if (not Ignatio):
                    operating_screen.blit(marker_white, (195 + 250*current_choice, 450))
                if get_out == 1:
                    break
                pygame.display.update()
                clock.tick(30)
            
            temp_keys2 = list(reward_dict1[choice_reward].keys())
            choose = random.sample(temp_keys2, k=3)
            current_choice = 0
            get_out = 0
            while True:
                operating_screen.fill((48, 205, 62))
                if (not Ignatio):
                    operating_screen.fill((0, 0, 0))
                show_text(operating_screen, 110, 100, "No Backsies! Choose what you want:", Ignatio)
                if choice_reward == "Gold":
                    payout = math.ceil(1.2**len(monster_counter)* 150 * investment)
                    show_text(operating_screen, 110, 575, "Current Gold: " + str(gold), Ignatio)
                    show_text(operating_screen, 110, 600, "Payout Value: " + str(payout), Ignatio)
                    show_text(operating_screen, 110, 625, "Investment Value: " + str(investment), Ignatio)
                for rand_opt in range (0, len(choose)):
                    show_text(operating_screen, 200, 250 +50*rand_opt, choose[rand_opt] + ": " + reward_dict1[choice_reward][choose[rand_opt]].desc, Ignatio)
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                        current_choice = (current_choice - 1)%len(choose)
                    if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                        current_choice = (current_choice + 1)%len(choose)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        actual_reward = choose[current_choice]
                        get_out = 1

                operating_screen.blit(marker, (175, 250 + 50 * current_choice))
                if (not Ignatio):
                    operating_screen.blit(marker_white, (175, 250 + 50 * current_choice))
                if get_out == 1:
                    break
                pygame.display.update()
                clock.tick(30)
            get_out = 0
            current_choice = 0
            if choice_reward == "Item":
                inventory.append(reward_dict1[choice_reward][actual_reward])
                show_text(operating_screen, 110, 450, reward_dict1[choice_reward][actual_reward].name + " Has been added to the inventory.", Ignatio)
                
            if choice_reward == "Attack/Skill":
                character_list[reward_yay].movedict["Attack/Skill"][actual_reward] = reward_dict1[choice_reward][actual_reward]
                show_text(operating_screen, 110, 450, "Congratulations, " + character_list[reward_yay].name + " has learned: " + reward_dict1[choice_reward][actual_reward].name, Ignatio)
                
            if actual_reward == "Payout":
                earnings = payout
                gold = gold + earnings
                show_text(operating_screen, 110, 450, "You have earned " + str(earnings) + " gold", Ignatio)
               
            if actual_reward == "RNG":
                earnings = random.randint(math.ceil(payout*0.5), math.ceil(payout*1.5))
                gold = gold + earnings
                show_text(operating_screen, 110, 450, "You have earned " + str(earnings) + " gold", Ignatio)
                
            if actual_reward == "Invest":
                investment = investment * (1 + payout/3000)
                show_text(operating_screen, 110, 450, "Your new investment value is " + str(investment), Ignatio)

            pygame.display.update()
            pygame.time.delay(1000)    

        temp_keys = fightnot
        current_choice = 0
        get_out = 0
        what_do_next = ""
        global gone_to_shop
        while True:
            operating_screen.fill((139, 84, 75))
            if (not Ignatio):
                operating_screen.fill((0, 0, 0))
            show_centertext(operating_screen, 250, "Soooo uhhhh, do you want to fight again? Or go to... uh, I haven't programmed it yet lol?", Ignatio)
            show_centertext(operating_screen, 300, "AHA, I have finished programming the shop lol. But you can go only once until the boss. Choose wisely.", Ignatio)
            show_centertext(operating_screen, 300, "You also heal for half of the hp you're missing at the shop. Cheers!", Ignatio)
            for pp in range (0, len(fightnot)):
              show_text(operating_screen, 110, 450 + 50 * pp, str(fightnot[pp]), Ignatio)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                    current_choice = (current_choice - 1)%len(temp_keys)
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                    current_choice = (current_choice + 1)%len(temp_keys)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    what_do_next = temp_keys[current_choice]
                    get_out = 1

            operating_screen.blit(marker, (85, 450 + 50 * current_choice))
            if (not Ignatio):
                operating_screen.blit(marker_white, (85, 450 + 50 * current_choice))
            if what_do_next == "Shop":
                if gone_to_shop == 0:
                    GET_ME_OUT = 1
                    gone_to_shop = 1
                else:
                    show_text(operating_screen, 110, 600, "Nuh uh uhhh~. You've already gone to the shop once this cycle baby.", Ignatio)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    what_do_next = ""
                    get_out = 0
            if get_out == 1:
                break
            pygame.display.update()
            clock.tick(30)

        current_choice = 0
        get_out = 0
        for resetting in range (0, len(character_list)):
          character_list[resetting].reset()
        return
    else:
        for achieve_rew in range (0, len(monster_counter)):
            print("You've earned " + str(len(monster_counter)) + " points. It was a good run. Lol no it wasn't, git gud. ")
        pygame.quit()
        sys.exit()
def shop(gold, consumable_list, Ignatio):
    global GET_ME_OUT
    choose_power_consumables = random.sample(shop_more_fleshed, k=3)
    choose_debuffs = random.sample(shop_debuffs, k=3)
    current_choice = 0
    get_out = 0
    while True:
        operating_screen.fill((79, 189, 189))
        if (not Ignatio):
            operating_screen.fill((0, 0, 0))
        show_bigcentertext(operating_screen, 50, "Memories Materialized, Haggle and I'll sew your mouth shut", Ignatio)
        show_centertext(operating_screen, 115, "Welcome to Memories Materialized, where useless memories are sold to do useful stuff. Huh, who knew.", Ignatio)
        show_centertext(operating_screen, 140, "All these items should be references or memories of some kind, because lore, but just buy what you want", Ignatio)
        show_text(operating_screen, operating_screen.get_width()//30, 700, "Press 'r' to Refresh the shop for 10 Gold", Ignatio)
        show_text(operating_screen, 24*operating_screen.get_width()//30, 700, "Press 'l' to exit the shop", Ignatio)
        

        events = pygame.event.get()
                
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                current_choice = (current_choice - 1)%9
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                current_choice = (current_choice + 3)%9
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                current_choice = (current_choice + 1)%9
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                current_choice = (current_choice - 3)%9
            if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                get_out = 1
                GET_ME_OUT = 0
                show_centertext(operating_screen, 650, "You are now leaving the shop.", Ignatio)
                pygame.display.update()
                pygame.time.delay(2000)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                if gold - 10 < 0:
                    show_centertext(operating_screen, 650, "Not enough gold losers.", Ignatio)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    continue
                gold = gold - 10
                choose_power_consumables = random.sample(shop_more_fleshed, k=3)
                choose_debuffs = random.sample(shop_debuffs, k=3)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if current_choice <= 2:
                    if gold - shop_basic_list[current_choice].price < 0:
                        show_centertext(operating_screen, 650, "Not enough gold losers.", Ignatio)
                        pygame.display.update()
                        pygame.time.delay(2000)
                        continue
                    consumable_list.append(shop_basic_list[current_choice])
                    gold = gold - shop_basic_list[current_choice].price
                    show_centertext(operating_screen, 650, "You've bought " + shop_basic_list[current_choice].name, Ignatio)
                    pygame.display.update()
                    pygame.time.delay(2000)
                if current_choice > 2 and current_choice <= 5:
                    if gold - choose_power_consumables[current_choice%3].price < 0:
                        show_centertext(operating_screen, 650, "Not enough gold losers.", Ignatio)
                        pygame.display.update()
                        pygame.time.delay(2000)
                        continue
                    consumable_list.append(choose_power_consumables[current_choice%3])
                    gold = gold - choose_power_consumables[current_choice%3].price
                    show_centertext(operating_screen, 650, "You've bought " + choose_power_consumables[current_choice%3].name, Ignatio)
                    pygame.display.update()
                    pygame.time.delay(2000)
                if current_choice > 5 and current_choice <= 8:
                    if gold - choose_debuffs[current_choice%3].price < 0:
                        show_centertext(operating_screen, 650, "Not enough gold losers.", Ignatio)
                        pygame.display.update()
                        pygame.time.delay(2000)
                        continue
                    consumable_list.append(choose_debuffs[current_choice%3])
                    gold = gold - choose_debuffs[current_choice%3].price
                    show_centertext(operating_screen, 650, "You've bought " + choose_debuffs[current_choice%3].name, Ignatio)
                    pygame.display.update()
                    pygame.time.delay(2000)
         
        for constants in range (0, 3):
            show_text(operating_screen, operating_screen.get_width()//30, 225 + 125*constants, shop_basic_list[constants].name + ":", Ignatio)
            show_text(operating_screen, operating_screen.get_width()//30, 250 + 125*constants,  shop_basic_list[constants].desc, Ignatio)
            show_kindasmalltext(operating_screen, operating_screen.get_width()//30, 275 + 125*constants, "Price: " + str(shop_basic_list[constants].price), Ignatio)
            show_text(operating_screen, 11*operating_screen.get_width()//30, 225 + 125*constants, choose_power_consumables[constants].name + ":", Ignatio)
            show_text(operating_screen, 11*operating_screen.get_width()//30, 250 + 125*constants, choose_power_consumables[constants].desc, Ignatio)
            show_kindasmalltext(operating_screen, 11*operating_screen.get_width()//30, 275 + 125*constants, "Price: " + str(choose_power_consumables[constants].price), Ignatio)
            show_text(operating_screen, 21*operating_screen.get_width()//30, 225 + 125*constants, choose_debuffs[constants].name + ":", Ignatio)
            show_text(operating_screen, 21*operating_screen.get_width()//30, 250 + 125*constants, choose_debuffs[constants].desc, Ignatio)
            show_kindasmalltext(operating_screen, 21*operating_screen.get_width()//30, 275 + 125*constants, "Price: " + str(choose_debuffs[constants].price), Ignatio)


        show_text(operating_screen, operating_screen.get_width()//30, 575, "Gold: " + str(gold), Ignatio)
        operating_screen.blit(marker, ((operating_screen.get_width()//30 + ((operating_screen.get_width()//3) * math.ceil((current_choice-2)/3))) - 25, 225 + 125*(current_choice%3)))
        if (not Ignatio):
            operating_screen.blit(marker_white, ((operating_screen.get_width()//30 + ((operating_screen.get_width()//3) * math.ceil((current_choice-2)/3))) - 25, 225 + 125*(current_choice%3)))
        
        if get_out == 1:
            break
            
        pygame.display.update()
        clock.tick(30)
    return gold
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
# Initialize all of pygame
pygame.init()


manager = pygame_textinput.TextInputManager(validator=lambda input: len(input) <= 15)


#Make the actual display screen
operating_screen = pygame.display.set_mode((1450, 800))#, pygame.FULLSCREEN)
clock = pygame.time.Clock()

pygame.display.set_caption("Gignesthai")
font = pygame.font.Font('freesansbold.ttf', 18)
font_small = pygame.font.Font('freesansbold.ttf', 9)
font_kindasmall = pygame.font.Font('freesansbold.ttf', 15)
font_big = pygame.font.Font('freesansbold.ttf', 40)

textinput = pygame_textinput.TextInputVisualizer(manager=manager, font_object=font)

Henri = pygame.image.load('BDSM_jordan.png')
Eric = pygame.image.load('Monke_Eric.png')
Reid = pygame.image.load('Queen_reid.png')
Shane = pygame.image.load('Hulk_Cag.png')
s_Henri = pygame.image.load('BDSM_jordan_small.png')
s_Eric = pygame.image.load('Monke_Eric_small.png')
s_Reid = pygame.image.load('Queen_reid_small.png')
s_Shane = pygame.image.load('Hulk_Cag_small.png')
Enemy = pygame.image.load('Enemy_filler.png')
text_box = pygame.image.load ('text_box.png')
status_box = pygame.image.load ('statusbox.png')
marker = pygame.image.load ('marker.png')
marker_white = pygame.image.load ('marker_white.png')
marker_down = pygame.image.load ('marker_up.png')
marker_down_white = pygame.image.load ('marker_up_white.png')
inf_num = 1

Ignatio = False

character_list = []
inventory = []#item("GameDev", "Weapon", 100, 100, 100, "")
consumable_list = []
gold = 0
investment = 1
monster_counter = []
dead_char = []
monster_types = ["Normal", "Poison", "Fire", "Ice"] #Do I need this again in the other one?
temp_keys = []
GET_ME_OUT = 0
gone_to_shop = 0
complaint = ""
image_array = [Eric, Reid, Shane, Henri]
s_image_array = [s_Eric, s_Reid, s_Shane, s_Henri]
i = 1
in_the_benninging = False

textinput.font_color = (255, 255, 255)
textinput.cursor_color = (255, 255, 255)

#Make the main loop

#shop(gold, consumable_list)
continuous = True
while continuous:
    operating_screen.fill((0, 0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    show_centertext(operating_screen, 100, "wElcome to the worst arena of progression ever designed. This game sucks, why are you playing it you idiot?", Ignatio)
    show_centertext(operating_screen, 125, "Essentially, you're gonna get random stats, random enemies, and random randoms. Just random. Yea. Have fun", Ignatio)
    show_centertext(operating_screen, 150, "Well, might as well try to make this as good as possible lol.", Ignatio)
    show_centertext(operating_screen, 200, "How many of you are there? It's only up to 4, so good luck.", Ignatio)
    #operating_screen.blit(Henri, (600, 300))
    #Color change
    textinput.update(events)

    operating_screen.blit(textinput.surface, (110, 450))
    if [ev for ev in events if ev.type == pygame.KEYUP and ev.key == pygame.K_RETURN]:
        try:
            player_num = int(f"{textinput.value}")
            complaint = ""
            break
        except ValueError:
            complaint = "Please just enter a valid number D:"
    show_text(operating_screen, 110, 550, complaint, Ignatio)
    pygame.display.update()
    clock.tick(30)
while i < player_num + 1:
    operating_screen.fill((0, 0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    if player_num > 1:
        show_text(operating_screen, 110, 75, "Wow, why are so many of you playing this dead game.", Ignatio)

    show_text(operating_screen, 110, 100, "So what's player " + str(i) + "'s name?", Ignatio)
    #Color change
    textinput.update(events)
    operating_screen.blit(textinput.surface, (110, 450))
    if [ev for ev in events if ev.type == pygame.KEYUP and ev.key == pygame.K_RETURN]:
        character_name = f"{textinput.value}"
        character_list.append(character(character_name, image_array[i-1], s_image_array[i-1]))
        i += 1

    if i == 2:
        show_text(operating_screen, 110, 125, "That's a really dumb name, but alright", Ignatio)
    if i == 3 or i == 4 or i == 5:
        show_text(operating_screen, 110, 125, "That's also a really dumb name.", Ignatio)
    for showtime in range (0, len(character_list)):
        operating_screen.blit(character_list[showtime].picture, (80 + 280*showtime, 240))
        show_localcentertext(operating_screen, 80 + 280*showtime, 80 + 280*showtime + 200, 215, character_list[showtime].name, Ignatio)
    pygame.display.update()
    clock.tick(30)

pygame.time.delay(1000)
i = 1 #Resetting i counter for future looping through number of players



temp_keys = [0, 1, 2, 3]
while i < player_num +1:
    operating_screen.fill((0, 0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    show_text(operating_screen, 110, 100, "Alright, so um, I wanted to make like an entire class system, but that's gonna be .", Ignatio)
    show_text(operating_screen, 110, 125, "BUT, you get to choose one piece of gear, so here ya go punk. Number = item:", Ignatio)
    show_text(operating_screen, 110, 175, "0: Cloud Armor: +2 defense; (It's literally water vapor, but it's somehow sticking to you... magic *whoosh*.)", Ignatio)
    show_text(operating_screen, 110, 200, "1: Sword of Infertility: +1 attack; (I... please don't ask, just, it's just +1 attack. ", Ignatio)
    show_text(operating_screen, 110, 225, "2: Ring of Stupidity: -10 hp, +2 attack; (As they say, the dumber they are, the dumber they are.", Ignatio)
    show_text(operating_screen, 110, 250, "3: Boots of idk: ???; (they do... something? Don't ask what.)", Ignatio)
    show_text(operating_screen, 110, 300, "So what's player " + str(i) + " going to choose?", Ignatio)
    
    #Color change
    textinput.update(events)
    operating_screen.blit(textinput.surface, (110, 450))
    if [ev for ev in events if ev.type == pygame.KEYUP and ev.key == pygame.K_RETURN]:
        equip_choice = get_valid_int_input(temp_keys)
        if equip_choice == 0:
            CA = item("Cloud Armor", "Armor", 0, 2, 0, "+2 def")
            inventory.append(CA)
            character_list[i-1].equip(inventory, 0)
            i += 1
        if equip_choice == 1:
            SoI = item("Sword of Infertility", "Weapon", 1, 0, 0, "+1 atk")
            inventory.append(SoI)
            character_list[i-1].equip(inventory, 0)
            i += 1
        if equip_choice == 2:
            RoS = item("Ring of Stupidity", "Ring", 2, 0, -10, "+2 atk, -10 hp")
            inventory.append(RoS)
            character_list[i-1].equip(inventory, 0)
            i += 1
        if equip_choice == 3:
            Boi = item("Boots of idk", "Boots", 0, 0, 0, "Equivalent of Starting at deprived lol")
            inventory.append(Boi)
            character_list[i-1].equip(inventory, 0)
            i += 1

    show_text(operating_screen, 110, 550, complaint, Ignatio)
    pygame.display.update()
    clock.tick(30)
operating_screen.fill((0, 0, 0))
show_text(operating_screen, 110, 300, "RIGHT INTO THE FIRE. LET'S GO!", Ignatio)
pygame.display.update()
pygame.time.delay(1000)

i = 1 #Reset i counter for future
while inf_num == 1:
  if GET_ME_OUT == 0:
        enemy_name = ""
        #for some_variable in range (0, len(monster_counter)):
         #  enemy_name = enemy_name + " " + all_adjectives[random.randint(0, 10000)]
        enemy_name = enemy_name + " " + all_nouns[random.randint(0, 144000)]
        temp_type = monster_types[random.randint(0,3)] #string, not int
        Happiness = Monster(enemy_name, Enemy, temp_type, monster_counter, character_list)
        Happiness.type_mod(temp_type) #Now the monster is a specific type.
        Happiness.stat_change_damage() #Change the "Current" numbers.
        operating_screen.fill((174, 170, 110))
        if (not Ignatio):
            operating_screen.fill((0, 0, 0))
        show_centertext(operating_screen, 150, Battle_entry[random.randint(0,15)] + Happiness.name + ". FIGHT ", Ignatio)
        pygame.display.update()
        pygame.time.delay(2000)
        fight(dead_char, monster_types, monster_counter, character_list, inventory, consumable_list, Happiness, Ignatio)
  else:
      gold = shop(gold, consumable_list, Ignatio)
  if len(monster_counter) == 5:
      break
boss1lines = [
    "As you continue traversing through the darkness, finding and defeating these fantastical creatures,",
    "a strange sense of familiarity begins to grow within you in every step you take,",
    "in every strike you make",
    "in every blow that aches.",
    "A Deja Vu without reason; there is not one remarkable thing around in the surrounding abyss.",
    "Yet the familiarity is evoking something within you, a feeling? No... no not completely, it's more of a... a word?",
    "I-Il? In-If-Is-Ig. Ig? IG!",
    "Suddenly, a jagged rift of white light tears open in front of you. Blinding and shimmering;",
    "upon observation, what appears to be a smooth black orb floats out of the rift and floats a bit away from you.",
    "A pause.",
    "All of a sudden, the black orb catches on white fire. 3 prongs, one of red, another of green, and another of blue, jut out.",
    "Finally, the orb peels open revealing itself to be an eye with a pupil, also swirling with colors red, green, and blue.",
    "It stares at you keenly. There is no hostility, no resentment, but somehow you know that you are meant to fight it.",
    ""
              ]
line_count = 0
while continuous:
    if line_count < 8:  
        operating_screen.fill((0, 0, 0))
    else:
        operating_screen.fill((255,255,255))
    if line_count == 14:
        break
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            line_count += 1
    boss1lines[0]
    if line_count < 8:
        for showing in range (0, line_count):
            show_coloredcentertext(operating_screen, 150 + 50*showing, 255, 255, 255, boss1lines[showing])
    else:
        for showing in range (7, line_count):
            show_coloredcentertext(operating_screen, 150 + 50*(showing - 6), 0, 0, 0, boss1lines[showing])

    pygame.display.update()
    clock.tick(30)
operating_screen.fill((255, 255, 255))
show_coloredcentertext(operating_screen, 350, 0, 0, 0, "You now face Occipitus, The Original Sight, holder of the Ocular Keyword")
pygame.display.update()
pygame.time.delay(2000)

Occipitus = Monster("Occipitus, The Original Sight", Enemy, "Occipitus", monster_counter, character_list)
fight(dead_char, monster_types, monster_counter, character_list, inventory, consumable_list, Occipitus, Ignatio)

while inf_num == 1:
  if GET_ME_OUT == 0:
        enemy_name = ""
        #for some_variable in range (0, len(monster_counter)):
         #  enemy_name = enemy_name + " " + all_adjectives[random.randint(0, 10000)]
        enemy_name = enemy_name + " " + all_nouns[random.randint(0, 144000)]
        temp_type = monster_types[random.randint(0,3)] #string, not int
        Happiness = Monster(enemy_name, Enemy, temp_type, monster_counter, character_list)
        Happiness.type_mod(temp_type) #Now the monster is a specific type.
        Happiness.stat_change_damage() #Change the "Current" numbers.
        operating_screen.fill((174, 170, 110))
        if (not Ignatio):
            operating_screen.fill((0, 0, 0))
        show_centertext(operating_screen, 150, Battle_entry[random.randint(0,15)] + Happiness.name + ". FIGHT ", Ignatio)
        pygame.display.update()
        pygame.time.delay(2000)
        fight(dead_char, monster_types, monster_counter, character_list, inventory, consumable_list, Happiness, Ignatio)
  else:
      for heal_done in range (0, len(character_list)):
          character_list[heal_done].hp_current = character_list[heal_done].hp_current + ((character_list[heal_done].hp_tot - character_list[heal_done].hp_current)/2)
      gold = shop(gold, consumable_list, Ignatio)
  if len(monster_counter) == 5:
      break



