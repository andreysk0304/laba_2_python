from src.components.command import Command


def test_command_tokenizer_func():

    command = Command('ls hello "my bro" this/is/very cool.')

    assert command._tokens == ['ls', 'hello', 'my bro',  'this/is/very', 'cool.']


def test_command_get_command_func():

    command1 = Command('ls -l')
    command2 = Command('cd hello "my dir with probel" kf -l')

    assert command1.command == 'ls' and command2.command == 'cd'


def test_paths_get_func():

    command1 = Command('ls hello bro')
    command2 = Command('ls "русский с пробелами тоже работает!" path -l -re -rfdf -rejfdb')

    assert command1.paths == ['hello', 'bro'] and command2.paths == ['русский с пробелами тоже работает!', 'path']


def test_flags_get_func():

    command1 = Command('ls flagsTest -l')
    command2 = Command('ls -43 -43 -fd -k -r -l')

    assert command1.flags == ['-l'] and command2.flags == ['-43', '-43', '-fd', '-k', '-r', '-l']