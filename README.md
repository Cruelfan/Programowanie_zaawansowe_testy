Poll app
    - można dodawać pytania z panela administratora
    - mozna dodawać odpowiedzi z panela administratora
    - aplikacja zlicza głosy z przeglądarki
    - Z panelu administratora można usuwać ankiety/pytania

a. Struktura aplikacji
    Aplikacja jest napisana w frameworku Django.

    Poniżej opiszę działanie poszczególnych plików w aplikacji poll.
        admin.py - w tym pliku definiuję co ma się wyświetlić w panelu administratora
        apps.py - konfiguracja aplikacji polls
        models.py - w tym miejscu opisujemy modele logiczne/działanie aplikacji
        tests.py - w tym pliku są testy automatyczne. Uruchamiane są z poziomu linii komend.
        urls.py - W tym pliku są zdefiniowane ścieżki URL w których są odnośniki do widoków.
        views.py - tutaj są definiowane widoki aplikacji. Wyświetlają też między innymi struktury HTML
        templates/polls/index.html - wyświetla stronę startową (linki do pytań/ankiet)
        templates/polls/detail.html - wyświetla pytania z ankiet / możliwe odpowiedzi na pytanie
        templates/polls/result.html - wyświetla głosy na konkretne odpowiedzi
        templates/polls/admin/base_site.html - strona dla administratorów (z panelu administratora)
        static/polls/style.css - podpięty .CSS który formatuje widok struktur HTML
        static/polls/images/ - miejsce na obrazy/ikony

    Struktura mysite:
        settings.py - konfiguracja aplikacji na django (zdefiniowane bazy danych, podpięte aplikacje itp.)
        urls.py - linki do podpiętych aplikacji (polls, admin)

————————————————————————————————————————————————————

b. Scenariusze testów
    Testy są zawarte w pliku "polls/tests.py"
    Można je uruchomić poprzez komendę: 
        >> python manage.py test polls

    Poniżej są scenariusze testów:

    Testy logiki (modelu Question):
        1. Test pytania z publikacją w przyszłości
        2. Test pytania z publikacją w przeszłości (starsza niż 1 dzień)
        3. Test pytania które ma publikację w minionym dniu

    Testy widoku (index.html): 
        1. Jeśli nie istnieje pytanie, wyświetl odpowiednią wiadomość
        2. Wyświetlanie pytań z przeszłą wartością "pub_date"
        3. Nie-wyświetlanie pytań z przyszłą wartością "pub_date"
        4. Utwórz dwa pytania (przeszłe i przyszłe) a następnie wyświetl tylko przeszłe
        5. Wyświetlanie wielu pytań

    Testy widoku (detail.html)
        1. Zwrócenie kodu 404 przy próbie wyświetlenia pytania z przyszłą datą
        2. Zwrócenie tekstu pytania, który ma przeszłą wartość "pub_date"

————————————————————————————————————————————————————

c. Wykorzystywane narzędzia i biblioteki
    Do stworzenia aplikacji został wykorzystany framework "Django"
    Jest to framework napisany w Pythonie do pisania aplikacji webowych.

    Nic poza django nie było wykorzystywane. 

————————————————————————————————————————————————————

d. Ewentualne problemy i ich rozwiązania
    Problem był w testach -> zostal opisany w pliku "polls/tests.py"

————————————————————————————————————————————————————
