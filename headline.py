import random
#news lists
news1=["New Delhi: Indian Navy commissions INS Imphal, marking a significant milestone in indigenous shipbuilding.","Mumbai: Sensex breaches 90,000 mark for the first time, driven by banking and IT stocks."]
news2=["US Congress passes $1.7 trillion spending bill to avoid government shutdown, includes military aid for Ukraine.","Japan and South Korea express renewed concerns over North Korea’s missile program following latest provocations."]
news3=["Indian Railways introduces AI-powered safety system to detect track defects in real-time, aiming to prevent derailments.","Kolkata's iconic Howrah Bridge temporarily closed for emergency structural inspection after unusual vibrations reported by commuters."]
while True:
    random_news = random.choice([news1, news2, news3]) 
    selected = random.choice(random_news)               
    headline=f"Breaking_News: {selected}"
    print("\n" + headline)
    while True:
        cont = input("\n do you want to continue(y/n):  ").lower()
        if cont == "y":
            break  
        elif cont == "n":
            print("Thanks for reading")
            exit()
        else:
            print("Invalid input! Enter yes or no only")