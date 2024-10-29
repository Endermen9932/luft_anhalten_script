import time 
import sys


print("WIllkommen zum Atemtraing")
Luft_anhalten = int(input("Wieviele Sekunden willst du die Luft anhalten?"))

gesamt_zeit = Luft_anhalten * 9 + 540
gesamt_zeit = gesamt_zeit / 60

print(f"Das würde {gesamt_zeit} Minuten dauern, möchtest du fortfahren? (ja/nein)")

fortfahren = input()
 
if fortfahren == "nein" :
    sys.exit()

print("Sehr gut, dann legen wir los!")
time.sleep(1)

countdown = 3

while countdown > 0 :
    print(countdown)
    time.sleep(1)
    countdown = countdown - 1


# Luft anhalten 

Luft_anhalten_countdown = Luft_anhalten 

print(f"Jetzt {Luft_anhalten} Sekunden die Luft anhalten. ")
 
time.sleep(1)

while Luft_anhalten_countdown > -1 :
    print(Luft_anhalten_countdown)
    time.sleep(1)
    Luft_anhalten_countdown = Luft_anhalten_countdown - 1

# Ausatmen 

print("Jetzt 2 Minuten Pause")
time.sleep(1)

Ausatmen = 120
Ausatmen_countdown = Ausatmen

while Ausatmen_countdown > -1 :
    print(Ausatmen_countdown)
    time.sleep(1)
    Ausatmen_countdown = Ausatmen_countdown -1


# Luft anhalten 

Luft_anhalten_countdown = Luft_anhalten 

print(f"Jetzt {Luft_anhalten} Sekunden die Luft anhalten. ")
 
time.sleep(1)

while Luft_anhalten_countdown > -1 :
    print(Luft_anhalten_countdown)
    time.sleep(1)
    Luft_anhalten_countdown = Luft_anhalten_countdown - 1

# Ausatmen 

Ausatmen = Ausatmen - 15

print(f"Jetzt {Ausatmen} Sekunden Pause")
time.sleep(1)

Ausatmen_countdown = Ausatmen

while Ausatmen_countdown > -1 :
    print(Ausatmen_countdown)
    time.sleep(1)
    Ausatmen_countdown = Ausatmen_countdown -1

while Ausatmen > 0 :
  
    # Luft anhalten

    Luft_anhalten_countdown = Luft_anhalten 

    print(f"Jetzt {Luft_anhalten} Sekunden die Luft anhalten. ")
 
    time.sleep(1)

    while Luft_anhalten_countdown > -1 :
        print(Luft_anhalten_countdown)
        time.sleep(1)
        Luft_anhalten_countdown = Luft_anhalten_countdown - 1

    # Ausatmen 
    Ausatmen = Ausatmen - 15

    print(f"Jetzt {Ausatmen} Sekunden Pause")
    time.sleep(1)

    Ausatmen_countdown = Ausatmen

    while Ausatmen_countdown > -1 :
        print(Ausatmen_countdown)
        time.sleep(1)
        Ausatmen_countdown = Ausatmen_countdown -1

  # Luft anhalten

Luft_anhalten_countdown = Luft_anhalten 

print(f"Jetzt {Luft_anhalten} Sekunden die Luft anhalten. ")
 
time.sleep(1)
while Luft_anhalten_countdown > -1 :
    print(Luft_anhalten_countdown)
    time.sleep(1)
    Luft_anhalten_countdown = Luft_anhalten_countdown - 1