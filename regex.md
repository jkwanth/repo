## Single Character

\d <!-- any digit {0-9} -->
\w <!-- any word {A-Z a-z 0-9} -->
\s <!-- any whitespace {tab space} -->
\W <!-- anything not \w -->
\S <!-- anything not \s -->
\. <!-- dot -->
\( <!-- open parenthesis -->
. <!-- any character -->

## Quantifier

* <!-- zero or more -->
+ <!-- one or more -->
? <!-- zero or one -->
{n} <!-- n of it -->
{a,b} <!-- between a-b of it -->

## Position

^ beginning
$ end
\b word boundary

## Character Classes

[abc] <!-- a or b or c -->
[-.] <!-- - or . -->
[a-z] <!-- a thru z -->
[^0-5] <!-- anything not 0 thru 5 -->

## Alternation

(net | com) <!-- net or com -->

## Capturing Groups

()() <!-- $1 $2 & $0 = whole -->

## Back References
() <!-- \1 -->

.* <!-- any number of any characters -->
colou?rs? <!-- {color, colors, colour, colours} -->