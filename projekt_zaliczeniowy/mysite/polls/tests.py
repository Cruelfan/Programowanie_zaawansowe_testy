import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question

# testowanie logiki pytań
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        
        # Zwraca False dla pytań, których wartość pub_date
        # jest w przyszłości.
        
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
        
        
    def test_was_published_recently_with_old_question(self):

        # Zwraca False dla pytań, których wartość pub_date
        # jest starsza niż 1 dzień
        
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):
 
        #Zwraca True dla pytań, ktoych wartość pub_date
        # zawiera się w minionym dniu
        
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    
    
# funkcja potrzebna do testowania widoków (tworzy pytania)
def create_question(question_text, days):
    
    # Tworzy pytanie z podaną nazwą "question_text" (argument) i publikuje podaną liczbę
    # "days" przesuniętych do teraz. 
    # ujemne dla pytań opublikowanych w przeszłości
    # dodatnie dla pytań które nie zostały jeszcze opublikowane
    
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


# testowanie widoku index.html
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        
        # jeśli nie istnieje żadne pytanie, wyświetl odpowiednią wiadomość
        
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        
        # Pytania z wartością przeszłą w "pub_date" są wyświetlane na stronie domyślnej (index.html)
        
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        
        # Pytania z wartością przyszłą w "pub_date" nie są wyświetlane na stronie domyślnej (index.html)
        
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        
        # Jeśli istnieją przyszłe i przeszłe pytania, aplikacja wyświetla tylko 
        # przeszłe pytania
        
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        # fail :https://stackoverflow.com/questions/42770040/trying-to-compare-non-ordered-queryset-against-more-than-one-ordered-values-djan 
        # repaired -> added ordered=False
         
        # Na stronie domyślnej (index.html) może być wyświetlanych wiele pytań
        
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [question1, question2], ordered=False
        )

# testowanie widoku "detail.html"
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):

        # widok "detail.html" pytania z przyszłą wartością "pub_date" zwraca kod "404" 
        
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        
        #  widok "detail.html" pytania z przeszłą wartością "pub_date" wyświetla
        # tekst pytania 
        
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)