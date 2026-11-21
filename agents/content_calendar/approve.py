import os
import sys

FOLDER = os.path.join(os.path.dirname(__file__), "output")


def load_days(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    parts = text.split("## Din ")
    return ["## Din " + p.strip() for p in parts[1:] if p.strip()]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Istemal: python3 agents/content_calendar/approve.py Business_Name_calendar.md")
        raise SystemExit

    source = os.path.join(FOLDER, sys.argv[1])
    if not os.path.exists(source):
        print("File nahi mili:", source)
        raise SystemExit

    approved_path = source.replace("_calendar.md", "_approved.md")
    already = ""
    if os.path.exists(approved_path):
        with open(approved_path, "r", encoding="utf-8") as f:
            already = f.read()

    days = load_days(source)
    count = 0
    for day in days:
        if day in already:
            continue
        print("=" * 50)
        print(day)
        choice = input("Manzoor? y = haan, n = nahi, s = baad mein, q = band: ").strip().lower()
        if choice == "q":
            break
        if choice == "y":
            with open(approved_path, "a", encoding="utf-8") as f:
                f.write(day.replace("(DRAFT)", "") + "\n\n- Status: APPROVED\n\n")
            count += 1
            print("Manzoor ho gaya.")
        elif choice == "n":
            print("Radd kar diya.")
        else:
            print("Baad ke liye chhor diya.")

    print(f"\nIs baar {count} din manzoor hue.")
    print("Note: koi post ya message bheja nahi gaya. Posting aap khud karenge.")
