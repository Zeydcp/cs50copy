# Doodle-Drop
#### Video Demo:  <https://www.youtube.com/watch?v=m-ORimJ2ws4>
#### Description:
Doodle Drop is a fun and addictive game that challenges your reflexes and coordination. Instead of ascending through platforms, you'll be plummeting down through a series of increasingly faster travelling platforms. Dodge obstacles, and aim for a high score in this gravity-defying adventure.

I used Unity Game Engine for this CS50 Final Project. The main focus is the Assets folder which contains all the project files I worked on. Particularly Assets/Scripts which has all my scripts written in C# using a .NET framework.

Creating "Doodle Drop" was a journey of inspiration and innovation. Drawing inspiration from the classic "Doodle Jump" while juxtaposing its gameplay goals, I set out to create a unique gaming experience. In "Doodle Drop," players must dodge incoming obstacles as they continuously fall through a maze of platforms, moving left and right using arrow keys. The challenge lies in avoiding reaching the top of the screen due to the incoming platforms, which would result in a game over.

The development process came with its fair share of challenges, as is typical in any game project. Collision detection between the player and the platforms proved to be a persistent issue, as did synchronizing the velocities of these platforms to create a seamless gameplay experience. Making the player character bounce correctly, transitioning between game scenes, and ensuring the seamless spawning of platforms in random positions were also formidable hurdles. Despite these challenges, persevering through them served as a valuable learning experience.

Working on "Doodle Drop" was a solo endeavor, allowing me to delve deep into Unity Game Engine's capabilities. The initial learning curve was steep, but as I became more familiar with the engine, my rate of learning skyrocketed. The most rewarding part of this journey was creating a game that I genuinely enjoyed playing.

While there are no immediate plans for further improvements or expansions of the game, "Doodle Drop" stands as a testament to my first foray into game development. I hope that players find it to be a delightful and entertaining twist on the original "Doodle Jump," offering a fresh and fun perspective on the classic gameplay they know and love.


#### Script:
In my BlueCPhysics script, I handle the back and forth horizontal movement of the blue platforms.

In my CapsulePhysics script, I declare the vertical speed of all platforms.

In my CapsuleSpawner script, I handle the random spawning of the platforms, the interval between spawn times, the varying vertical velocity of the platforms and the despawning of the platforms and finally freezing the platforms at the end of game.

In my EndGame script, I handle the current score and high scores being passed on to the next scene, I also handle making the platforms disappear. This script is executed when the game is over.

In my giveValue script, this script stores the value of current score in a variable.

In my highscore script, this script stores the value of high score in a variable.

In my Jump script, I handle all player movements. The input game controls right and left arrow that control the player. The bounce of the player after collisions with the platforms. The changing sprite when player bounces or receives control input. The teleportation of player to opposite side of screen when out of bounds. The calling of a capsuleSpawner function when player reaches screen midpoint to accelerate platform speed. The calling of the EndGame function when player goes vertically out of bounds.

In my MenuAgain script, I handle the transition between game over scene and start menu scene, this includes a button animation when menu button is clicked in game over scene.

In my PauseMenu script, I handle pausing the game when pause button at top of the screen is clicked. This results in freezing the game by setting the time scale to 0. Then when resume button is clicked, I set time scale to 1e-6, do a resume button animation and then set time scale back to 1 getting out of pause.

In my PlayAgain script, I handle the transition between game over scene and playing scene, this includes a button animation when play again button is clicked in game over scene.

In my scoreKeeper script, I update the displayed score value, I do this by calling a capsuleSpawner variable which keeps track of number of capsules despawned and assign that variable to the displayed score.

In my staticData script, this acts as a global current score variable that can be used across all scenes, this helps in transferring the value from playing scene to game over scene.