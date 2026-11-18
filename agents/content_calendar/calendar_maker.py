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
