Program main;
Uses CRT;

Var
    x: Integer;
    first: Integer;
    second: Integer;
    third: Integer;
    msg: String;

Begin
    Write('Enter number: ');
    Readln(x);
    first := (x  div  100);
    second := ((x  div  10)  mod  10);
    third := (x  mod  10);
    msg := 'Sum is: ';
    Writeln(msg, ' ', first + second + third);
End.