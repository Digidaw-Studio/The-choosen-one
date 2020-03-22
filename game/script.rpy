# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define U = Character("Unknown")
define R = Character("Rangga Syahputra", who_color="#2e70ff")
define S = Character("Sarah")
define Mom = Character("Ibu Rangga", who_color="#2e70ff")
define Ruri = Character ("Ruri", who_color="#2e70ff") #adeknya rangga
define Narator = Character ("")

#Rangga = B aja, ga jelek,dan gak ganteng amat
#Sarah = rambut panjang,berkacamata

#Outfit Sarah = Sma biasa
#Outfit Rangga = Sma Biasa

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    Narator "*Mimpi Buruk"


    R "Maksud mimpi gua tadi, apa ya?"
    R "Yaudahlah, ngapain gua pusing-pusing mikirin"
    Mom "Ranggaaaaaa!!! Bangun...Sarapannya udah siap nih!"
    R "Iya mah, rangga segera turun."
    Mom "Ayo cepat diabisin makanan nya, jangan sampai telat. Ini kan hari pertama
        kamu sekolah."
    Ruri "Kak,Bareng dong!!!"

    menu :
        "Yaudah ayo":
            jump Ruri_ikut

        "Nggak ah!":
            jump Ruri_gaikut

    label Ruri_ikut:
        R "yaudah cepetan abisin makan nya dulu!"
        Ruri "Asik!!!"
        jump Ruri_ikut2

    label Ruri_gaikut:
        R "Nggak ah, kakak lagi buru-buru,kamu berangkat sama ayah aja!"
        Ruri "dasar, Kakak Jahat!!!"
        jump disekolah







    # This ends the game.

    return
