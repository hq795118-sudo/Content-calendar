import os

IDEAS = {
    "restaurant": [
        ("Signature dish ki close-up photo", "{name} ka signature dish try kiya? Aaj hi aayein, {city} mein aapka intezar hai!"),
        ("Kitchen ki behind-the-scenes video", "Hamari kitchen mein roz taza khana banta hai. Dekhein kaise!"),
        ("Customer ki khushi wali photo", "Aap ki muskurahat hamari sab se badi kamyabi hai. Shukriya!"),
        ("Aaj ka special deal", "Aaj ka special: {name} par khaas offer. Dost aur family ko saath layein!"),
        ("Menu ki ek dish ka taruf", "Is dish ki khaasiyat jaanein, aur apni pasand batayein."),
        ("Staff se taruf", "Milein hamari team se jo aap ki khidmat mein hai."),
        ("Weekend family plan", "Is weekend family ke saath {name} aayein. Table book karein."),
        ("Customer se sawal", "Aap ki favourite dish kaun si hai? Comment mein batayein."),
        ("Chef ka taruf", "Milein hamare chef se, jin ke haath ka zaika {city} ko pasand hai."),
        ("Taaza ingredients ki photo", "Har dish taaze ingredients se. Mayaar par koi samjhauta nahi."),
        ("Chai ya drinks ka waqt", "Shaam ki chai ya thanda drink, sab {name} par."),
        ("Birthday ya party booking", "Birthday ya party? {name} mein booking ke liye rabta karein."),
        ("Takeaway aur delivery ki khabar", "Ghar baithe {name} ka khana mangwayein."),
        ("Customer review ka screenshot", "Aap ke pyare alfaz hamari himmat hain. Shukriya!"),
        ("Dessert ki tasveer", "Meetha na ho to khana adhura. Hamari dessert try karein."),
        ("Ramzan ya tehwar ka khaas menu", "Khaas mauqe par khaas menu. Pehle se table book karein."),
        ("Pichli raat ki rounaq", "Kal raat {name} mein kya mahaul tha, dekhein."),
        ("Do dish mein muqabla", "Biryani ya karahi? Comment mein apna vote dein."),
        ("Restaurant ke andar ki photo", "Aaram se baithein, mazedar khana khayein."),
        ("Lunch deal", "Din ka lunch deal sirf {name} par. Waqt mehdood hai."),
        ("Khaas mehmaan ya regular customer", "Hamare purane saathiyon ka shukriya."),
        ("Dish banane ki 15 second video", "Dekhein ye dish kaise banti hai."),
        ("Family size platter", "Poori family ke liye ek platter, behtareen qeemat par."),
        ("Safai ki jhalak", "Safai aur hifazat hamari pehli tarjeeh hai."),
        ("Naye menu ki khabar", "Naya menu aa gaya! Sab se pehle {name} par try karein."),
        ("Khana aur mausam", "Mausam kuch bhi ho, garam khana hamesha pasand aata hai."),
        ("Sawal jawab: aap kya jaan na chahte hain", "Hamare menu ya timing ke baare mein kuch poochna hai? Comment karein."),
        ("Team ki group photo", "Ye hai {name} ki team. Aap ki khidmat mein hazir."),
        ("Weekend special", "Weekend par {name} par khaas pakwan."),
        ("Shukriya post", "Is mahine ke liye shukriya. Aap ka saath hamari taqat hai."),
    ],
    "clinic": [
        ("Sehat ka roz ka mashwara", "Aaj ka sehat tip: roz kam az kam 8 glass pani piyein."),
        ("Doctor ka taruf", "Milein hamare doctors se. {name}, {city} mein aap ki sehat hamari zimmedari."),
        ("Mausam ki bimari se bachao", "Mausam badal raha hai, in ehtiyaat se bimari se bachein."),
        ("Clinic ke timing ki post", "Hamare timing note kar lein. Appointment ke liye rabta karein."),
        ("Aam ghalat fehmi", "Sehat ke baare mein ek aam ghalat fehmi aur sahi baat."),
        ("Saaf suthri clinic ki photo", "Safai hamari pehli tarjeeh hai."),
        ("Mareez ka mashwara (ijazat se)", "Hamare mareezon ka tajurba. Shukriya aap ke bharose ka."),
        ("Appointment ki yaad dahani", "Check-up mein der na karein. Aaj hi appointment lein."),
        ("Neend ka khayal", "Achhi neend achhi sehat ki bunyaad hai. Roz 7 se 8 ghante soyein."),
        ("Bachon ki sehat", "Bachon ke check-up aur teekon mein der na karein."),
        ("Blood pressure ki jaanch", "Blood pressure ki jaanch waqt par karwayein."),
        ("Sugar ki ehtiyaat", "Sugar ke mareez khana aur dawa waqt par lein."),
        ("Exercise ka mashwara", "Roz 30 minute chalna dil ke liye faida mand hai."),
        ("Doctor se sawal jawab", "Aap ke sehat ke sawalon ke jawab, comment mein poochein."),
        ("Clinic ki sahulaton ki list", "{name} mein kaun kaun si sahulat hai, jaan lein."),
        ("Garmi ki bimariyan", "Garmi mein pani aur saaya, loo se bachao."),
        ("Sardi ki ehtiyaat", "Sardi zukam se bachne ke asan tareeqe."),
        ("Haath dhone ki ehmiyat", "Saaf haath, kai bimariyon se hifazat."),
        ("Khoon ka test aur lab", "Lab ke tests ke liye {name} par tashreef layein."),
        ("Beemari ki alamaat jaldi pehchanein", "Alamaat ko nazar andaz na karein. Doctor se rabta karein."),
        ("Healthy nashta", "Sehatmand din ki shuruaat achhe nashte se."),
        ("Maa aur bacha", "Maa aur bachay ki sehat, hamari khaas tawajjo."),
        ("Dant ya aankh ka khayal", "Dant aur aankhon ki jaanch bhi zaroori hai."),
        ("Mareez ki kamyabi ki kahani (ijazat se)", "Sehat yaab mareezon ke saath hamara safar."),
        ("Staff se taruf", "Milein hamare staff se jo aap ki madad ke liye hai."),
        ("Mahine ka health camp", "Is mahine ka health camp, tafseel ke liye rabta karein."),
        ("Zehni sehat", "Zehni sukoon bhi sehat ka hissa hai."),
        ("Beemari se bachao ka checklist", "Ye 5 aadatein apna kar sehatmand rahein."),
        ("Emergency rabta", "Zaroorat ke waqt {name} se rabta karein."),
        ("Shukriya post", "Aap ke bharose ka shukriya."),
    ],
    "shop": [
        ("Naye maal ki photo", "{name} mein naya stock aa gaya hai! Aaj hi dekhne aayein."),
        ("Special discount", "Khaas discount sirf is hafte {name} par."),
        ("Best seller product", "Ye cheez sab se zyada pasand ki ja rahi hai. Aap ne dekhi?"),
        ("Dukaan ki photo", "{name}, {city}. Hum aap ke intezar mein hain."),
        ("Customer ki khareedari ki photo", "Hamare khush customer. Shukriya aap sab ka!"),
        ("Product ka istemal ka tareeqa", "Is cheez ko is tarah istemal karein, behtareen natija."),
        ("Home delivery ki khabar", "Ab ghar baithe order karein, delivery hamari zimmedari."),
        ("Customer se sawal", "Aap ko kaun si cheez chahiye? Comment mein batayein."),
        ("Do cheezon ka muqabla", "Aap kaun si pasand karenge? Comment mein vote dein."),
        ("Tehwar ka khaas stock", "Tehwar ke liye khaas cheezein {name} par maujood hain."),
        ("Combo offer", "Do ya zyada cheezein ek saath, behtareen qeemat par."),
        ("Quality ki jhalak", "Hum quality par koi samjhauta nahi karte."),
        ("Customer review", "Hamare customers ke pyare alfaz. Shukriya!"),
        ("Dukaan ke timing", "Hamare timing note kar lein. {name} aap ka intezar karega."),
        ("Behind-the-scenes", "Dekhein hum aap ke liye maal kaise tayyar karte hain."),
        ("Naya brand", "Naya brand ab {name} mein dastyab hai."),
        ("Budget friendly cheezein", "Kam budget mein behtareen cheezein dekhein."),
        ("Gift ideas", "Kisi ko tohfa dena hai? Hamare paas behtareen options hain."),
        ("Season sale", "Season ki sale shuru. Jaldi karein, stock mehdood hai."),
        ("Staff se taruf", "Milein hamari team se jo aap ki madad ke liye hai."),
        ("Product ka fayda", "Is cheez ka asli fayda jaanein."),
        ("Pehle aur baad ki tasveer", "Is cheez ka istemal, farq khud dekhein."),
        ("Customer ko shukriya", "Aap ke saath ka shukriya."),
        ("Aakhri pieces", "Sirf kuch pieces baqi hain. Aaj hi {name} se len."),
        ("Payment ke tareeqe", "Cash ke ilawa digital payment bhi dastyab hai."),
        ("Dukaan ki saafai aur sajawat", "Naye andaz mein sajee {name} ki dukaan."),
        ("Sawal jawab", "Kisi cheez ke baare mein poochna hai? Comment karein."),
        ("Hafte ki best deal", "Is hafte ki sab se achhi deal."),
        ("Naya arrival teaser", "Kuch naya aa raha hai. Intezar karein!"),
        ("Mahine ka shukriya", "Is mahine ke liye shukriya. {name} aap ka apna hai."),
    ],
}

TAGS = {
    "restaurant": ["#food", "#foodie", "#restaurant"],
    "clinic": ["#health", "#doctor", "#clinic"],
    "shop": ["#shopping", "#sale", "#newarrival"],
}


def make_calendar(name, btype, city):
    btype = btype.lower().strip()
    if btype not in IDEAS:
        raise ValueError("Type sirf ye ho sakti hai: restaurant, clinic, shop")
    city_tag = "#" + city.replace(" ", "")
    posts = []
    for day in range(1, 31):
        idea, caption = IDEAS[btype][(day - 1) % len(IDEAS[btype])]
        posts.append({
            "day": day,
            "idea": idea,
            "caption": caption.format(name=name, city=city),
            "hashtags": " ".join(TAGS[btype] + [city_tag]),
        })
    return posts


def save_markdown(name, btype, city, posts):
    folder = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(folder, exist_ok=True)
    filename = name.replace(" ", "_") + "_calendar.md"
    path = os.path.join(folder, filename)
    lines = ["# 30 Din ka Content Calendar (DRAFT)", "",
             f"Business: {name} | Type: {btype} | City: {city}", ""]
    for p in posts:
        lines += [f"## Din {p['day']}",
                  f"- Idea: {p['idea']}",
                  f"- Caption: {p['caption']}",
                  f"- Hashtags: {p['hashtags']}", ""]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return path


if __name__ == "__main__":
    n = input("Business ka naam: ")
    t = input("Type (restaurant/clinic/shop): ")
    c = input("City: ")
    result = make_calendar(n, t, c)
    print("Calendar save ho gaya:", save_markdown(n, t, c, result))
