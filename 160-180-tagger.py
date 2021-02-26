from get_metadata import json_read, json_write

X = """2	ענד גוברין	עסקי אוויר. אנשים ואירועים בחדשות. מפקד חיל־האוויר - דו״ח טיסה ב־15£-ק / ראיון עם ראש אכ״א, האלוף רן גורן / ראש להק כוח־אדם: ״אנו משתדלים שהקיצוצים לא יהיו מכאיבים״ / תאונות טיסה אזרחיות / שינויים במערך המזל״ט / תקיפות חיל־האוויר / החילוץ מה־״סו־אלן״
14	דרור מרום	האיש שעשה אח ה״אפאצ׳י״. לג׳ים תומפסון יש 2,000 שעות־טיסה על המסוק
19	דרור מרום	נחת על הזנב. דף בספר הטיסות
20	אייל ארליך	סיוט המלחמה של ספקטור. ״חלום בתכלת־שחור״, ספר של תא״ל (מיל׳) יפתח ספקטור
24	גיא רימון	משמעת מול אש. אליעזר פריגת, טייס מפקד - וחלוץ
30	הילי מודריק	לרוץ עם סטיגגר. טיל הכתף הטוב בעולם מאומץ ע׳׳י גדוד וולקן
33	קוני מריגקו ושרון שדה	היי־טק. מדור טכנולוגיות ותעשייה.  משה קרת, מנכ׳׳ל התעשייה האווירית: ״אנחנו לקראת ייצוא ב־2 מיליארד דולאר״ / רפא״ל ייצרה את המנוע שלב־3 של הלוויין ״אופק״ / מתקן מוטס חדש של ״ראדא״ לתחקור קרבות־אוויר / כך מתאזרחות התעשיות הבטחוניות
38	שדון שדה	מוחץ. הפרופיל המבצעי של ה״חץ״
44	דרור מרום	טייס מסוק־קרב. שני טייסי ״קוברה״ צעירים עוברים ל״אפאצ׳י״
50	אהרון לפידוח ושרון שדה	סאלון מקורקע. הסאלון האווירי ה־39 בלה־בורז׳ה
64	אהרון לפידות	״ממפיס־נל" - הסרט. 8-17 אמריקני אחד, נגד העולם
68	עודד גלוברמן	תסתכל באלבום ותראה. צילומים נדירים ממלחמת העצמאות
72	ליאורה שוסטר	לא הגיל, התרגיל. ל״סקייהוקים״ יש עדיין מה להציע
76	קרן קרפ	האח הגדול טס מלמעלה. משפחה אחת, שלושה טייסים
79	ליאורה שוסטר	ה׳׳סוחוי" של בבלי. דף בספר הטיסות
81		מדף אווירי. מדור ספרים
82	שרון שדה	באוויר העולם. 8-2 - פיקציה או קורבן להשמצות / מטוסי ההדרכה של שנות ה־90 / הטובים ל״שבשבת״, בחיל־האוויר הבלגי / מנחם שמול על טייסות מעורבות בחא״א / משבר בתעופה האזרחית העולמית
90	רוני אלרואי	נח״א רתוב. פרופ׳ יורם רוזוב לקח את עיצוב בסיסי חיל־האוויר כפרוייקט אישי
94		אנגלית."""


def main():
    num = "181"
    file = json_read(f'schemes/{num}.json')
    index = []
    try:
        for raw_line in X.splitlines():
            line = raw_line.split("\t")
            start_page = line[0].strip()
            author = line[1].strip()
            title = ""
            if len(line) > 2:
                title = " ".join(line[2:])
            index.append({"author": author, "start_page": int(start_page), "title": title, "description": ""})

    except Exception as e:
        raise e
    finally:
        file["index"] = index
        json_write(f'schemes/{num}.json', file)


if __name__ == '__main__':
    main()
