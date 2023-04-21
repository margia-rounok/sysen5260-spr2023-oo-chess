# `oo-chess`
In this assignment you will use Objected Oriented Design and Programming techniquies to implement the rules of Chess. Wikipedia 
has a pretty good summary [here](https://en.wikipedia.org/wiki/Rules_of_chess).

## What you're provided to start:
* Python container setup (docker-compose + Dockerfile);
* A few model objects:
    * Board -- Represents the chess-board;
    * Piece -- An abstract class for chess-pieces: Handles some basic identity issues.
    * Pawn -- A concrete implementation of Piece.
    * Game -- Knows the board and who's turn it is.
* A few view functions for visualizing a piece and a board in the terminal.
* A __main__.py that integrates the above pieces into a text-based app.

## What you'll need to implement
You'll need to implement the following user-stories:

As a player...
* <strike> I want to enter a move like 'e2e4' and see the piece at e2 moved to e4. (done) </strike>
* I want to receive an error if I try to... 
    *  <strike> enter an ill-formatted move -- i.e. anything not of the form `[a..h][1..8][a..h][1..8]`.
    (done)  </strike>
    * <strike> move a non-existent piece. (done) </strike>
    * <strike> move my opponent's piece. (done) </strike>
    * <strike> move my bischop to any square not on its diagonal. (done) </strike>
    * <strike> move my rook to any square not on its row or column. </strike>
    * <strike> move my queen to any square not on its row, column, or diagonal. (done) </strike>
    * <strike> move my knight to any square not 3x2 squares aware. (done) </strike>
    * <strike> move any piece other than a knight over existing pieces (path override). (done) </strike>
    * <strike> move any piece to a square occupied by another of my pieces (dest override). (done) </strike>
    * <strike> move my pawn in violation of pawn-movement rules. (done) </strike>
    * <strike> move my king in violation of king-movement rules.(done) </strike>
    * <strike> make a move that results in my king being in check. (done) </strike>
    * <strike> make any other moves prohibited by [movement rules](https://en.wikipedia.org/wiki/ Rules_of_chess#Movement) </strike>
* <strike> I want to move my king two squares towards my rook and see the rook 
also moved to complete a castle. (done)</strike>
* <strike>I want to receive an error if any of the castling conditions don't hold. </strike>
* <strike>I want to enter 'backup' and undo a move. (done) </strike>
* I want the game to complete when either player is checkmated.


# What you'll hand in
* A link to your homework group's github repository that will contain:
   * A working chess program.
   * <strike>A DESIGN.md file that explains the design of your system to a developer wishing to use or extend your system. (done) </strike>
   * <strike> A RETROSPECTIVE.md file summarizing the agile retrospective meeting you'll hold after you complete the work for this assignment. (Nuclino has a decent description of Agile Retrospectives [here](https://www.nuclino.com/articles/sprint-retrospective-meeting)) (done) </strike>

# How you'll get an A
* <strike> I can clone your repository, start the container, run `python -m chess`, and complete several moves in an interactive session. (done)</strike>
* You have written functional tests to exercise each of the user-stories outlined above.
* <strike> Your code is readable: Meaningful names, comments where apropriate, keep modules, classes, and functions small, etc.
* Your code is well organized and demonstrates good use of object oriented design principles like:
    * Separation of Concerns / Single responsibility principle.
    * Favor Cohesion / Avoid Coupling.
    * Use of design patterns. (done) </strike>
* <strike> Your code has good unit-test coverage. (done) </strike>
* <strike> All tests pass. (done) </strike>
* <strike>Your Design Document is a good piece of technical writing with sections, 
descriptive prose, etc. (done) </strike>
* <strike>Your Design Document includes UML diagrams:
      * A class-diagram documenting the classes in the system.
      * An object-diagram depicting a chess-game after several moves.
      * An interaction diagram depicting the interaction between objects when:
         *  A user enters a valid move;
         *  A user enters an invalid move; (done) </strike>
* <strike> Your retrospective describes: 
   *  A short narrative of how your team members collaborated.
   *  A summary of what your team did well.
   *  A summary of what your team could do better next time. (done) </strike>

Extra Credit:
* Set up the GitHub Actions to enable Continuous Integration for your homework group.
* Use Python's [Abstract Base Class](https://docs.python.org/3/library/abc.html) module where appropriate.
* Implement another story: I want to enter 'resign' to resign and end the game.

