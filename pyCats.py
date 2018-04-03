MAX = 100


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Work:
    def __init__(self, name="McCat's Burger Flipper", rate=11, work_id=0, exp_req=0):
        self.name = name
        self.rate = rate
        self.work_id = work_id
        self.exp_req = exp_req

    def get_name(self):
        return self.name

    def get_rate(self):
        return self.rate

    def get_work_id(self):
        return self.work_id

    def get_exp_req(self):
        return self.exp_req


job1 = Work("McCat's Burger Flipper", 11, 0, 0)
job2 = Work("Help Desk", 14, 1, 10)
job3 = Work("Junior Developer", 18, 2, 20)
job4 = Work("Senior Developer", 25, 3, 40)
job_list = [job1, job2, job3, job4]


class Condo:
    def __init__(self, name="", rate=0, price=0, condo_id=0):
        self.name = name
        self.rate = rate
        self.condo_id = condo_id
        self.price = price

    def get_name(self):
        return self.name

    def get_rate(self):
        return self.rate

    def get_condo_id(self):
        return self.condo_id

    def get_price(self):
        return self.price


condo1 = Condo("Small Box", 1, 0, 0)
condo2 = Condo("Large Box", 3, 15, 1)
condo3 = Condo("Basic Cat Condo", 6, 120, 2)
condo4 = Condo("Luxury Cat Condo", 10, 250, 3)
condo_list = [condo1, condo2, condo3, condo4]


class Human:
    def __init__(self, name="", energy=100, money=0, work=Work(), exp=0):
        self.name = name
        self.energy = energy
        self.money = money
        self.work = work
        self.exp = exp

    def set_name(self, name):
        self.name = name

    def set_energy(self, energy):
        self.energy = energy

    def set_money(self, money):
        self.money = money

    def set_work(self, work):
        self.work = work

    def set_exp(self, exp):
        self.exp = exp

    def get_name(self):
        return self.name

    def get_energy(self):
        return self.energy

    def get_money(self):
        return self.money

    def get_work(self):
        return self.work

    def get_exp(self):
        return self.exp

    def init_setup(self):
        init_name = input("    Please Enter Your Name : ")
        self.set_name(init_name)
        self.work = job1

    def __repr__(self):
        string = "    Name: {}\n" \
                 "    Energy: {}\n" \
                 "    Money: ${}\n" \
                 "    Job: {} (${} per work)\n" \
                 "    Current EXP: {}".format(self.get_name(), self.get_energy(),
                                            self.get_money(), self.get_work().get_name(),
                                            self.get_work().get_rate(), self.get_exp())
        return string


class Cat:
    def __init__(self, name="", food=100, love=0, condo=Condo()):
        self.name = name
        self.food = food
        self.love = love
        self.condo = condo

    def set_name(self, name):
        self.name = name

    def set_food(self, food):
        self.food = food

    def set_love(self, love):
        self.love = love

    def set_condo(self, condo):
        self.condo = condo

    def get_name(self):
        return self.name

    def get_food(self):
        return self.food

    def get_love(self):
        return self.love

    def get_condo(self):
        return self.condo

    def init_setup(self):
        init_name = input("    Please Enter the Cat's name : ")
        self.set_name(init_name)
        self.set_condo(condo1)

    def __repr__(self):
        string = "    Cat: {}\n" \
                 "    Food: {}\n" \
                 "    Love: {}\n" \
                 "    Condo Name: {} ({} love per play)".format(self.get_name(), self.get_food(),
                                                                self.get_love(), self.get_condo().get_name(),
                                                                self.get_condo().get_rate())
        return string


class Action:
    job1 = Work("McCat's Burger Flipper", 11, 0, 0)
    job2 = Work("Help Desk", 14, 1, 10)
    job3 = Work("Junior Developer", 18, 2, 20)
    job4 = Work("Senior Developer", 25, 3, 40)
    job_list = [job1, job2, job3, job4]
    condo1 = Condo("Small Box", 1, 0, 0)
    condo2 = Condo("Large Box", 3, 15, 1)
    condo3 = Condo("Basic Cat Condo", 6, 120, 2)
    condo4 = Condo("Luxury Cat Condo", 10, 250, 3)
    condo_list = [condo1, condo2, condo3, condo4]

    def __init__(self, human=Human(), cat=Cat(), day=0):
        self.human = human
        self.cat = cat
        self.day = day

    def play(self):
        if self.human.get_energy() >= 20:
            self.human.energy -= 20
            self.cat.love += self.cat.get_condo().get_rate()
        else:
            print("    You don't have enough energy !")

    def work(self):
        if self.human.get_energy() >= 15:
            self.human.energy -= 15
            self.human.money += self.human.get_work().get_rate()
            self.human.exp += 1
        else:
            print("    You don't have enough energy!")

    def sleep(self):
        self.human.set_energy(100)
        self.cat.food -= 30

    def feed(self):
        if self.human.money >= 5:
            self.human.money -= 5
            self.cat.food += 20
            if self.cat.food > 100:
                self.cat.set_food(MAX)
        else:
            print("    You don't have enough money!")

    def buy(self, ):
        if self.human.money >= condo.get_price():
            self.human.money -= condo.get_price()
            self.cat.set_condo(condo)
        else:
            print("    You don't have enough money!")


def welcome_message():
    print("\n                            ***Welcome to pyCats!***")
    print("""
                .+++/                                         -/+++-
               .mMMMMds/                                 -+hhNNMMMMh
               sMMmsdmMMNo:    --:+++++++++++++++++++:-+dNMNhs///NMM+
               MMM` ``-sNMMNNNNNNNMmddddddddddddddMMMMNMNho``    /MMd
              +MMs      `oNMMdyo:..```````````````../yyy-`       -MMN
              NMMd        .:.`                                   dMMs
              MMMM+                                             :mMMN+`
            `sMMms-                                              `:dMMh.
           -hMNs`                                                  `sMMm.
          +NNs.                                                      yMMm/
         +MM:      -/oo:`                        `-::-`              `oMMN.
        oNMs      yNMMMMd:                      :dNMMNd.               dMMs      -yhhhhy/.
       /MMd`      mMMMMMN+                      dMMMMMM+               oMMN     .NMmyodNMNs
       mMM+       `+ydds-      shhhhhhs         .syddy+                oMMM     oMd`   /NMM+
       MMM`              ```   +dMMMMs+   ...                          oMMM     sM+     +MMM`
       yMMs`             odmo..smMMMM+:..+NMm                         `hMMN     NM`      dMMy
       :NMMo              :hNNNNNhyhNNNNNNho`                        `dMMMs     MM-      -MMM
        -dMM/`              `---`   -----`                         `-dMMMy`     NMh       NMM:
         -NMMN-                                                  `-hMMMMy.      oMM`      +MMo
          .+dMMh+-`                                          `-/smMMMMM/        oMMd       MMo
            .+NMMMds::`                                  `::+dmMNNhhNMMm.        mMM       MMo
               /hmMMMMMds+::.`                 ```::::+sdMMMNmh/.   .hMMm+       oMM:      MMo
                  .ohmMMMMMMMMdddddddddddddddddMMMMMMMMmhyo-          sMMMo      /MMo     oMMo
                      oMMy::ooooyhhhhhhhhhhhhhhhhy:::::                :mMMm:     MMo     oMMo
                      hMM                                               .yMMM:    MMo     yMMo
                      MMm                                                 oMMM/   MMo     MMM/
                     oMM.                                                  sMMNs .MMo     MMM
                     oMM                                                    /MMMysMMo     MMM
                     oMM                                                     sMMMMMM:    `MMN
                     oMM                                                      hMMMMM     yMM+
                     oMM                                                      `sMMMM    :MMs`
                     oMM                                                       `sMMM   `NMM/
                     oMM                                                        `mMM:  sMMs
                     oMM                                                         oMMy /NMM-
                     oMM                                                         /MMM+NMMo
                     oMM             `:.   .-             +y.                     MMMMMMy`
                     oMM             +Mh  .mN             NMo                     MMMMMm`
                     oMM/            oMM  oMM             MMo                     MMMMh.
                     +MMh            oMM  oMM             MMo                    `MMMm`
                     `MMM            oMM  oMM             MMo                   `yMMs.
                      NMM/           oMM  oMM             MMo                 `:mMNs
                      -MMs           oMM  oMM`            MMo               .:hMmo:
                       NMM/          oMM  oMMs           `MMo          `./oyNMNo`
                       /MMMo`      `oNMM.`sMMM/`        -dMMy///////yyhmMMMNd/`
                        sNMMN+-``-oNMMMMNdNNMMMds/```-osNMMMMNNNNNNNNNdy++:.
                         .sNMMMMMMMMMNs/----+hmMMMMMMMMMMMd+/--------
                           ./shhhhh++.        .+shhhhhhs+/       \n\n\n""")


def main():

    game_over = False
    day, condo_counter, job_counter = 0, 0, 0

    def display_status():
        print("    ***********************************")
        print(human.__repr__())
        print("    ***********************************")
        print(cat.__repr__())
        print("    ***********************************")

    def action_selection():
        print("\n\n\n    *Energy Left : {}"
              "    *Money Left : {}".format(human.energy, human.money))
        user_input = input("    What would you like to do?\n "
                           "   (Play, Work, Sleep, Feed, Buy, Display) : ").lower()
        if user_input == "play":
            game.play()
        elif user_input == "work":
            game.work()
        elif user_input == "sleep":
            game.sleep()
        elif user_input == "feed":
            game.feed()
        elif user_input == "buy":
            game.buy()
        elif user_input == "display":
            display_status()
        else:
            print("Invalid Option!")

    welcome_message()
    while not game_over:
        human = Human()
        human.init_setup()
        cat = Cat()
        cat.init_setup()
        game = Action(human, cat)
        display_status()
        while human.energy != 0:
            action_selection()


if __name__ == '__main__':
    main()
