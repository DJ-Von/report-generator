Program main;
Uses CRT;

Var
    a: array [0..6] of String;
    i: Integer;

Begin
    a[0] := 'mon';
    a[1] := 'tue';
    a[2] := 'wed';
    a[3] := 'thu';
    a[4] := 'fri';
    a[5] := 'sat';
    a[6] := 'sun';
    
    for i := 0 to 7-1 do 
    begin
        Writeln(a[i]);
    end;
End.