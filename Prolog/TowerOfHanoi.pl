% less_than/2 - compares two int and succeeds if the first is less than the second
less_than(X, Y) :- X < Y->true; false. % If X is less than Y, then it is true; otherwise false.

% tower_of_hanoi/1 - print out the moves to solve a Tower of Hanoi of Number disks
tower_of_hanoi(Number) :- tower_of_hanoi_impl(Number, left, right, middle). % Calls full funtion using the number of disks

tower_of_hanoi_impl(1, Number, Destination, _) :- % When moving a single disk, use this
    write('move('),
    write(Number),
    write(','),
    write(Destination),
    write(')'),
    nl.

tower_of_hanoi_impl(Number, Source, Destination, Spare) :-
    Number>1,
    Temp is Number-1,
    tower_of_hanoi_impl(Temp, Source, Spare, Destination),
    tower_of_hanoi_impl(1, Number, Destination, _),         % I could not figure out how to get the number to print every time,
    tower_of_hanoi_impl(Temp, Spare, Destination, Source).  % since the value changes every other call. This was the closest I could get to it,
                                                            % and it is still an accurate solve. It just alternates between number and position.
