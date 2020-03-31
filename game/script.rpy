# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define U = Character("Unknown")
define R = Character("Rangga Syahputra", who_color="#2e70ff")
define S = Character("Sarah")
define Mom = Character("Ibu Rangga", who_color="#2e70ff")
define Ruri = Character ("Ruri", who_color="#2e70ff") #adeknya rangga
define Narator = Character ("")
define D = Character ("Deni")

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

    R "....."
    R "Maksud mimpi ku tadi, apa ya?"
    R "..."
    R "Yaudahlah, ngapain pusing-pusing mikirin mimpi."
    Mom "Ranggaaaaaa!!! Bangun...Sarapannya udah siap nih!"
    R "Iya mah, rangga segera turun."
    with fade
    Mom "Ayo cepat diabisin makanan nya, jangan sampai telat. Ini kan hari pertama
        kamu sekolah."
    R "Iya mah."
    Ruri "Kak,Bareng dong berangkatnya!!!"

    menu :
        "Yaudah ayo":
            jump Ruri_ikut

        "Nggak ah!":
            jump Ruri_gaikut

    label Ruri_ikut:
        R "yaudah, tapi buruan abisin makan nya dulu!"
        Ruri "Asik!!!"
        scene bgroom
        with fade
        Ruri "makasih ya kak, udah anter ruri!"
        R "Iya, Kamu belajar yang rajin ya!"
        Ruri "Pasti dong kak!!!"
        R "Bagus."
        R "Iyaudah, kakak berangkat dlu ya."
        Ruri "Oke kak, hati-hati di jalan ya!"
        jump disekolah

    label Ruri_gaikut:
        R "Nggak ah, kakak lagi buru-buru,kamu berangkat sama ayah aja!"
        Ruri "Iyaudah deh."
        jump disekolah

    label disekolah:
        with fade
        R "waduh gawat, udah mau dimulai nih upacara nya, aku gaboleh sampai terlambat."
        with fade
        R "hadehhh, akhirnya selesai juga..."
        R "Pidato pembukaan tadi terlalu panjang.Sampe ngantuk dengerinnya"
        with vpunch
        Narator"sfx:gedubrak!!!"
        R "eh maaf-maaf, gua ga sengaja"
        S "....."
        R "Ini buku lu, maafin gua ya!"
        S "..... (Diam tanpa sepatah kata,dan langsung pergi)"
        R "Aishhh, sombong banget itu cewe..."
        R "Gua minta maaf ga di respon sama sekali"
        R "Tapi kayak gua pernah liat tuh cewe"
        R "Ahhh udahlah, lagi-lagi gua mikirin hal yang ga penting"

        scene kelas
        with fade

        Narator "Woy Rangga!!!"
        R "Deni??? lu sekolah disini juga?"
        D "Yoi, lu duduk dimana rang?"
        R "Tuh dibelakang,sendiri"
        D "Aduh sedih banget duduknya sendiri..."
        D "Gua duduk bareng lu yak? boleh ga?"
        R "Ya Boleh lah den, santai!"
        Narator "Pelajaran pun berlangsung"
        D "Akhirnya selesai jugaaaaaa!!!"
        D "Balik yuk rang!"
        R "Ayo"

        scene rumah
        with fade
        R "Assalamualaikum..."
        Mom "Waalaikumsalam"
        Mom "Gimana rang hari pertamanya? Lancar?"
        R "Alhamdulillah lancar mah"
        R "untungnya ada si Deni temen lama aku,jadi nya aku ga sendirian deh dikelas"
        Mom "Woah,Syukur deh kalo begitu"

        Mom "Oh iya, kamu mau makan apa engga rangga? Mamah udah masak nih."
        menu :
            "Makan":
                jump rangga_makan

            "Ke Kamar":
                jump rangga_kekamar

        label rangga_makan:
            R "Boleh deh mah, rangga laper belum makan"
            Mom "Oke,mamah siapin dlu ya"
            R "Oke mah!"
            scene ruangmakan with fade
            R "Alhamdulillah kenyang."
            R "Makasih ya mah makanannya,rangga mau ke kamar dulu"
            Mom "Iya rang, jangan lupa ganti baju"
            R "Iya mah"
            jump rangga_kekamar

        label rangga_kekamar:
            with fade
            R "Hadeh,badan pada pegel-pegel banget..."
            R "Tidur dulu deh sebentar"
            with fade
        R "....."
        Narator "Wahai anak muda..."
        R "???"
        Narator "Selamatkanlah perempuan ini..."
        Narator "Selamatkan lah ia dari aura kegelapan!"
        R "Aura kegelapan?"
        Narator "Ya...Aura kegelapan yang telah menyelimuti hatinya"
        R "Apa maksudmu? Aku tidak mengerti!"
        Narator "Aura kegelapan di hati nya,terbentuk akibat kesengsaraan yang ia alami di
                 dalam hidupnya"
        Narator "Selamatkan lah dia! Buatlah ia bahagia, agar aura kegelapan di hatinya menghilang"
        Narator "Akan tetapi,jika dia tidak segera diselamatkan..."
        Narator "Kematian akan segera datang kepadanya."
        R "Huh???" with vpunch
        Narator "Kuberikan kesempatan ini pada mu!"
        Narator "Karena...kau adalah 'Orang Yang Terpilih!' "

        with fade

        R "....."
        R "Sial...lagi-lagi aku mengalami mimpi yang aneh"
        R "Apa maksud mimpi-mimpi itu?"
        R "Dan mengapa aku memimpikan wanita yang tak sengaja kutabrak kemarin?"
        R "huh…mau dipikir seperti apapun juga,mimpi tetaplah mimpi!"
        R "Dan tak akan menjadi kenyataan"
        R "hah…sepertinya ini efek kecapekan"
        R "Jadinya aku selalu mendapatkan mimpi yang aneh"
        R "Yasudahlah, lebih baik ku hiraukan"
        R "Aku harus bergegas ke sekolah!"
        with fade
        R "Semoga aman motor nya kutaruh disini."
        D "Wey rang, lu berangkat sekolah naik motor?"
        R "Iya den"
        D "Wanjay, gua kira kagak bisa bawa motor lu hahaha"
        R "Yeeee enak aja, lu kira gua bocah apa?"
        D "Hahaha…canda rang"
        R "Yaudah yuk ah ke kelas!"
        D "Yuk"
        with fade
        Scene kelas

        D "Hadehhh, hari ini pelajaran mtk lagi"
        D "Mana gua paling gabisa sama mtk"
        R "Sama ren gua jg paling kagak bisa mtk haha"
        D "Yah,berarti gue salah dong milih duduk sama lu?"
        R "Anjir lu mau duduk sama gua cmn karna ngira gua pinter mtk?"
        D "Hahahaha...ya kagaklahhh rangg,bercanda gue"
        R "Yeee awas aja lu!"
        D "Udah gitu, guru mtk nya wali kelas kita lagi…mati dah"
        R "Iya yak, pasti bakal sering nanya-nanya nih"
        D "Eh tu guru nya dah dateng…"
        R "wah iya"

        with fade
















    # This ends the game.

    return
