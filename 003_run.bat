@echo off
@if '%1'=='FULL' goto FULL
@if '%1'=='HALF' goto HALF
goto END


:FULL
poetry run python winequality.py
goto END

:HALF
poetry run python halfwinequality.py
goto END


:END
