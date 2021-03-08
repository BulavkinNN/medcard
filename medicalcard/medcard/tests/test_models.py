from django.test import TestCase
from medcard.models import UserAccount
from django.db.models import Q, F, Func


def create_user_account(copies, user_name='user_test', sex='male', mob_tel='+38067'):
    for i in range(copies):
        number_user = str(i)
        UserAccount.objects.create(username=user_name + number_user,
                                   password='sdsds' + number_user,
                                   first_name='f_n_user_test' + number_user,
                                   last_name='l_n_user_test' + number_user,
                                   patronymick='p_n_user_test' + number_user,
                                   date_of_birth='2021-03-01',
                                   sex=sex,
                                   email='user_test@gmail.' + number_user,
                                   mob_tel=mob_tel + number_user,
                                   city='Nikolaev')


class UserAccountTestClass(TestCase):

    @classmethod
    def setUp(cls):
        '''
        self.NEW_USERS will be as argument function create_user_account()
        :return: Create  NEW_USERS Models UserAccount
        '''
        create_user_account(99, user_name="first_", sex='male', mob_tel="+380671")
        create_user_account(101, user_name="second_", sex='female', mob_tel="+380672")

    def tearDown(self):
        # Очистка после каждого метода
        pass

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

    def test_count(self):
        users = UserAccount.objects.count()
        self.assertEqual(200, users)

    def test_count_all(self):
        users1 = UserAccount.objects.count()
        users2 = UserAccount.objects.all()
        self.assertTrue(users1 == len(users2))

    def test_filter(self):
        users = UserAccount.objects.filter(sex__iexact='male')
        self.assertEqual(99, len(users))

    def test_exclude(self):
        users = UserAccount.objects.exclude(username__startswith='first_')
        self.assertEqual(101, len(users))

    def test_filter_endswith(self):
        users = UserAccount.objects.filter(username__endswith='98')
        self.assertEqual(2, len(users))

    def test_filter_contains(self):
        users = UserAccount.objects.filter(city__contains='Niko')
        self.assertEqual(200, len(users))

    def test_filter_gt(self):
        users = UserAccount.objects.filter(date_of_birth__gt='2021-02-01')
        self.assertEqual(200, len(users))

    def test_filter_lt(self):
        users = UserAccount.objects.filter(date_of_birth__lt='2021-03-02')
        self.assertEqual(200, len(users))

    def test_delete(self):
        UserAccount.objects.all().delete()
        users = UserAccount.objects.all()
        self.assertEqual(0, len(users))

    def test_earliest(self):
        user = UserAccount.objects.earliest('pk')
        self.assertEqual(1, user.id)

    def test_latest(self):
        user = UserAccount.objects.latest('pk')
        self.assertEqual(200, user.id)

    def test_get(self):
        user = UserAccount.objects.get(pk=1)
        user.city = 'Odessa'
        users = UserAccount.objects.filter(city='Odessa')
        self.assertEqual(1, user.id)

    def test_save(self):
        user = UserAccount()
        user.username = 'new_user'
        user.password = 'sdsds'
        user.first_name = 'f_n_user_test'
        user.last_name = 'l_n_user_test'
        user.patronymick = 'p_n_user_test'
        user.date_of_birth = '2021-03-01'
        user.sex = 'female'
        user.email = 'user_test@gmail.'
        user.mob_tel = '+38067'
        user.city = 'Odessa'
        user.save()
        users = UserAccount.objects.filter(email='user_test@gmail', city='Odessa')
        self.assertEqual(201, user.id)

    def test_annotate(self):
        user = UserAccount.objects.get(pk=1)
        user.city = 'Odessa'
        users = UserAccount.objects.filter(city='Odessa')
        self.assertEqual(1, user.id)

    def test_Q(self):
        # pk = [10,11,12, ... 20]
        users = UserAccount.objects.filter(Q(pk__gte=10) & Q(pk__lte=20))
        self.assertEqual(11, len(users))

    def test_F(self):
        UserAccount.objects.filter(pk=10).update(city=F('pk')+767)
        users = UserAccount.objects.filter(city=777)
        self.assertEqual(1, len(users))

    def test_values_list_filter(self):
        filtered_list_of_tuple = UserAccount.objects.values_list('pk','username','password').filter(pk__lt=3)
        self.assertEqual([(1, 'first_0', 'sdsds0'), (2, 'first_1', 'sdsds1')], list(filtered_list_of_tuple))


    def test_Func(self):
        pass

    def test_annotate(self):
        pass