Program main;
Uses CRT;

Var
    a: Integer;
    b: Integer;
    msg: String;

Begin
    Write('Введите число a: ');
    Readln(a);
    Write('Введите число b: ');
    Readln(b);
    msg := 'Sum is: ';
    Writeln(msg, ' ', a + b);
End.