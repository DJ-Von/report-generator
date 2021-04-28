Program main;
Uses CRT;

Var
    x: Integer;
    first: Integer;
    second: Integer;
    third: Integer;
    msg: String;

Begin
    Write('Введите число: ');
    Readln(x);
    first := (x  div  100);
    second := ((x  div  10)  mod  10);
    third := (x  mod  10);
    msg := 'Сумма цифр в числе равна: ';
    Writeln(msg, ' ', first + second + third);
End.