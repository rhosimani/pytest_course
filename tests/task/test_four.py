from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_asdict():
    t_task = Task('do something', 'Smith', True, 21)
    t_dict = t_task._asdict()
    expected = {
        'summary': 'do something',
        'owner': 'Smith',
        'done': True,
        'id': 21
    }
    assert t_dict == expected

def test_replace():
    t_before = Task('finnish book', 'Brian', False)
    t_after = t_before._replace(id=10, done=True)

    t_expected = Task('finnish book', 'Brian', True, 10)
    assert t_after == t_expected
