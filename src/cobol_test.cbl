IDENTIFICATION DIVISION.
PROGRAM-ID. HELLO-WORLD.

DATA DIVISION.
WORKING-STORAGE SECTION.

01 WS-MESSAGE PIC A(80) VALUE 'Hallo Welt!'.

PROCEDURE DIVISION.

MAIN-PROCEDURE.

MOVE WS-MESSAGE TO SYSOUT.

STOP RUN.