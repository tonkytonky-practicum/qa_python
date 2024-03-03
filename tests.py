from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        return collector

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize(
        'name,genre',
        [
            ('Гордость и предубеждение и зомби', 'Фантастика'),
            ('Что делать, если ваш кот хочет вас убить', 'Ужасы'),
        ]
    )
    def test_set_book_genre_set_genre_from_list(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        books_genre = collector.get_books_genre()
        assert books_genre[name] == genre

    @pytest.mark.parametrize(
        'name,genre',
        [
            ('Гордость и предубеждение и зомби', 'Фантастика'),
            ('Что делать, если ваш кот хочет вас убить', 'Ужасы'),
        ]
    )
    def test_get_book_genre_get_genre_from_list(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    # def test_get_books_for_children_exclude_one_genere(self, collector, name, genre):
    #     ('Гордость и предубеждение и зомби', 'Фантастика'),
    #     ('Что делать, если ваш кот хочет вас убить', 'Ужасы'),
    #
    #     collector.set_book_genre(name, genre)
    #     collector.add_new_book('Гордость и предубеждение и зомби')
    #     collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    #
    #
    #     collector.add_new_book(name)
    #     book_for_children = 'Гордость и предубеждение и зомби'
    #
    #     books_for_children = collector.get_books_for_children()
    #     assert len(books_for_children) == 1
    #     assert books_for_children[0] == book_for_children
