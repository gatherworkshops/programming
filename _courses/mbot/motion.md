---
layout: default
title: Basic Motion
course: workshop

slides:

  - class: title-slide

    content: |

      ![Gather Workshops Logo]([[BASE_URL]]/theme/assets/images/gw_logo.png)

      # Basic Motion
      

    notes: |

      Welcome to Programming Robots!

      This workshop is designed to introduce you to the basics of writing programs for robots.

      By the end of the workshop you will have programmed a robot to do cool things!

    
##########


  - content: |


      ## Starting Point
      ![Starting Point](assets/images/startingpoint.jpg){: height="250" width="400"}
      Always start with the _mBot Program_ block.
      Without this entry point, your program will not start.  
    notes: |

      Without the entry point, the mblock software will not know your program is an mBot program. Many different languages work this way too
      There must always be an entry point. What your mBlock program does is, it changes blocks you've placed in your editor
      and turns these blocks into C language code(see arduino mode)

    
##########

  - content: |


      ## Basic Motions
      ![Basic Motions](assets/images/basic motion1.jpg){: height="250" width="400"}
      You can go forwards, backwards, turn right, turn left. 
      You can also alter your robot's speed. 
    notes: |

      There are many other features you can add to your robot too, eg: LED lights, sensors, we will do more of this later.
      No angle option, get them thinking about how to make a perfect 90 degree angle. You can actually enter your own speed,
      every number you wish.
      With the speed you can choose from 0 - 255 or you can simply type whatever number you want.

    
##########

  - content: |


      ## Wait
      ![Basic Motions](assets/images/wait.jpg){: height="250" width="400"}
      The wait command means how long the 
      previous block will go on for. 
      
      Copy this program on your own computer.
      {:.checkpoint}

    notes: |

      Wait does not meaning stopping and waiting, it simply means that your motion will go on for a certain amount of time. 

    
##########
         
         
         
  - content: |

      ## Uploading programs to the robot

      - ![Instruction 1](assets/images/basic motion3.jpg){: height="200" width="300"}To see program code.
      - ![Instruction 2](assets/images/basic motion4.jpg){: height="200" width="300"}To upload program to mBot.
      - ![Instruction 3](assets/images/basic motion5.jpg){: height="200" width="300"}Your robot is ready to go!
      {: .flex-list}

      Upload your program to the robot.
      {:.checkpoint}


    notes: |

      Make sure your mBot is plugged in and connected through serial port before clicking on uploading.

    

##########
  - content: |

      

      ## Want to go again?
      ![Control commands](assets/images/reset.jpg){: height="250" width="400"}
      
      To repeat the same program again, 
      push the reset button on the robot. 
      

    notes: |
      This will make your program start from the beginning and repeat itself. 

    
##########
  - content: |

      

      ## Turning your robot
      
      There is no precise way of turning your robot, 
      because the length of a turn is measured in seconds. 
      
      How would you program an exact quarter turn?
      

    notes: |
      Ask students how they may figure out the angle from speed. The best way is to always keep the same speed, i would recommend
      100, before any challenges get them to make the robot turn in speed 100 and use a stopwatch to time how long it takes for 
      a full circle then divide by 4
      The correct option should be 0.8 seconds for the wait command for a 90 degree angle. 
      Make sure if you change speeds you will have to work out the angle again, as the speed affects the time taken to create an angle. 
      


##########


  - content: |

      

      ## Challenge: Perfect Squares
      
      Program your robot drive in a square using 
      the basic motions we have covered.

      Your robot should drive in an exact square.
      {:.checkpoint}
      

    notes: |
      Ok before we start, lets think about how we can make sure the robot is turning into a 90 degree angle.
      There is no angle option for the robot. Any suggestions on how you might work out the angle just from the speed?
      You will have to work out the how many seconds it takes turning at a speed of 100 until it completes a 360 degree angle then
      divide by 4. 

    


##########

  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Basic Motion: Completed
  
      
      [Take me to the next chapter!](features.html)

    notes: |

      Great! Now lets more on to the next chapter and learn more features you can add to your program. 


---