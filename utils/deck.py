import random



def create_card(rank:str,suite:str):
    card={}
    def value_finder(val):
        value_list=[{"2":2},{"3":3},{"4":4},{"5":5},{"6":6},{"7":7},{"8":8},{"9":9},{"10":10},{"j":11},{"q":12},{"K":13},{"A":14}]
        for i in value_list:
            for j in i.keys():
                if val==j:
                    return i[j] 
    card["rank"]=rank
    card["suite"]=suite
    card["value"]=value_finder(rank)
    return card    


                
      


def compare_cards(p1_card:dict, p2_card:dict) -> str:
    human=p1_card["value"]
    ai=p2_card["value"]
    if human>ai:
        return "p1"
    if ai>human:
        return "p2"
    else:
        return "WAR"



def create_deck() -> list[dict]:
   index1=random.randint(0,50)
   index2=random.randint(0,50)
   if index1==index2:
       return []

  


def shuffle(deck:list[dict]) -> list[dict]:
    return[]


