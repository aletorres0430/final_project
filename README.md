
The only additional package needed to run this code is pygame. Once pygame is installed into your environment you should be able each version of the game. 

NormalGameofLife.py runs the regular Conway's Game of Life
- turn cells on by left clicking
- turn cells off by right clicking
- dragging these clicks also works to turn many cells on or off
- press spacebar to start the simluation
- the simulation can also be paused and played with spacebar
- cells can also be edited while the simulation is paused or running
- pressing the R key will randomize the grid so that 25% of cells are on
- randomizing can be done at any point in the simulation, even while its running

OurGameofLife.py allows the user to input custom rules to make their own Game of Life
- First, 6 3x3 grids are displayed: 3 on top and 3 on bottom, each with a small square underneath
- clicking on any of the shown squares will turn it on or off
- The top three grids are "live grids" and the bottom three are "kill grids"
- The simulation will follow these rules instead of the regular Game of Live rules:
    - If the surroundings of a cell match any of the live grids, it will be turned on next generation
    - If the surroundings of a cell match any of the kill grids, it will be turned off the next generation
    - If the surroundings of a cell don't match any of the rule grids, it will stay the same
- The little square under each rule grid is an on/off switch that will turn the corresponding active or inactive (only rule grids that are active will affect the simulation. this allows users to select how many rules they want)
- Press Spacebar when you have finished inputing the rules to move on to the grid
- The same instructions used in NormalGameofLife.py above apply here

