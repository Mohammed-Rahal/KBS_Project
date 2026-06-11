; ============================================
; COMPREHENSIVE GIFT DATABASE
; ============================================

(deffacts gift-database
  ; ==========================================
  ; CONSTRUCTION & BUILDING
  ; ==========================================
  
  ; Physical Gifts - Construction
  (gift (name "LEGO Classic Creative Box") 
        (type physical) 
        (category "construction") 
        (min_age 4) (max_age 99) 
        (price 29.99) (gender any))
  
  (gift (name "Magnetic Building Blocks 100pc") 
        (type physical) 
        (category "construction") 
        (min_age 3) (max_age 8) 
        (price 24.99) (gender any))
  
  (gift (name "LEGO Technic Sports Car") 
        (type physical) 
        (category "construction") 
        (min_age 10) (max_age 16) 
        (price 49.99) (gender male))
  
  (gift (name "Architecture Building Kit") 
        (type physical) 
        (category "construction") 
        (min_age 12) (max_age 18) 
        (price 39.99) (gender any))
  
  (gift (name "Wooden Block Set 200pc") 
        (type physical) 
        (category "construction") 
        (min_age 2) (max_age 6) 
        (price 34.99) (gender any))
  
  (gift (name "Marble Run Construction Set") 
        (type physical) 
        (category "construction") 
        (min_age 4) (max_age 12) 
        (price 42.99) (gender any))
  
  ; Experience Gifts - Construction
  (gift (name "LEGO Master Builder Workshop") 
        (type experience) 
        (category "construction") 
        (min_age 8) (max_age 14) 
        (price 35.00) (gender any))
  
  (gift (name "Architecture for Kids City Tour") 
        (type experience) 
        (category "construction") 
        (min_age 10) (max_age 18) 
        (price 25.00) (gender any))
  
  ; ==========================================
  ; ARTS & CRAFTS
  ; ==========================================
  
  ; Physical Gifts - Arts & Crafts
  (gift (name "Watercolor Paint Set Deluxe") 
        (type physical) 
        (category "arts_and_crafts") 
        (min_age 6) (max_age 16) 
        (price 19.99) (gender any))
  
  (gift (name "Kids Craft Box Monthly Subscription") 
        (type physical) 
        (category "arts_and_crafts") 
        (min_age 4) (max_age 12) 
        (price 25.00) (gender any))
  
  (gift (name "DIY Jewelry Making Kit") 
        (type physical) 
        (category "arts_and_crafts") 
        (min_age 7) (max_age 14) 
        (price 22.99) (gender female))
  
  (gift (name "Sketching Set Professional") 
        (type physical) 
        (category "arts_and_crafts") 
        (min_age 10) (max_age 18) 
        (price 27.99) (gender any))
  
  (gift (name "Tie-Dye Party Kit") 
        (type physical) 
        (category "arts_and_crafts") 
        (min_age 5) (max_age 15) 
        (price 15.99) (gender any))
  
  (gift (name "Pottery Wheel for Kids") 
        (type physical) 
        (category "arts_and_crafts") 
        (min_age 8) (max_age 16) 
        (price 44.99) (gender any))
  
  (gift (name "Origami Paper Art Set") 
        (type physical) 
        (category "arts_and_crafts") 
        (min_age 6) (max_age 14) 
        (price 12.99) (gender any))
  
  ; Experience Gifts - Arts & Crafts
  (gift (name "Art Workshop for Kids") 
        (type experience) 
        (category "arts_and_crafts") 
        (min_age 6) (max_age 14) 
        (price 30.00) (gender any))
  
  (gift (name "Pottery Class Experience") 
        (type experience) 
        (category "arts_and_crafts") 
        (min_age 10) (max_age 18) 
        (price 45.00) (gender any))
  
  ; ==========================================
  ; BOOKS & READING
  ; ==========================================
  
  ; Physical Gifts - Books
  (gift (name "Children's Science Encyclopedia") 
        (type physical) 
        (category "books") 
        (min_age 7) (max_age 14) 
        (price 22.50) (gender any))
  
  (gift (name "Adventure Book Series Set") 
        (type physical) 
        (category "books") 
        (min_age 8) (max_age 13) 
        (price 35.99) (gender any))
  
  (gift (name "Personalized Story Book") 
        (type physical) 
        (category "books") 
        (min_age 3) (max_age 10) 
        (price 29.99) (gender any))
  
  (gift (name "Comic Book Collection") 
        (type physical) 
        (category "books") 
        (min_age 7) (max_age 15) 
        (price 18.99) (gender any))
  
  (gift (name "Interactive Sound Book") 
        (type physical) 
        (category "books") 
        (min_age 1) (max_age 4) 
        (price 14.99) (gender any))
  
  ; Experience Gifts - Books
  (gift (name "Library Annual Membership") 
        (type experience) 
        (category "books") 
        (min_age 3) (max_age 18) 
        (price 10.00) (gender any))
  
  ; ==========================================
  ; TECHNOLOGY & STEM
  ; ==========================================
  
  ; Physical Gifts - Technology
  (gift (name "Kids Coding Robot Kit") 
        (type physical) 
        (category "technology") 
        (min_age 8) (max_age 15) 
        (price 49.99) (gender any))
  
  (gift (name "Microscope Science Kit") 
        (type physical) 
        (category "technology") 
        (min_age 8) (max_age 16) 
        (price 39.99) (gender any))
  
  (gift (name "Drone with Camera for Kids") 
        (type physical) 
        (category "technology") 
        (min_age 12) (max_age 18) 
        (price 59.99) (gender any))
  
  (gift (name "Circuit Building Electronics Kit") 
        (type physical) 
        (category "technology") 
        (min_age 10) (max_age 16) 
        (price 34.99) (gender any))
  
  (gift (name "Digital Drawing Tablet") 
        (type physical) 
        (category "technology") 
        (min_age 8) (max_age 18) 
        (price 45.99) (gender any))
  
  ; Experience Gifts - Technology
  (gift (name "Robotics Workshop for Kids") 
        (type experience) 
        (category "technology") 
        (min_age 10) (max_age 16) 
        (price 55.00) (gender any))
  
  (gift (name "Planetarium Star Show") 
        (type experience) 
        (category "technology") 
        (min_age 6) (max_age 15) 
        (price 20.00) (gender any))
  
  ; ==========================================
  ; SCIENCE KITS
  ; ==========================================
  
  ; Physical Gifts - Science
  (gift (name "Volcano Making Kit") 
        (type physical) 
        (category "science_kit") 
        (min_age 6) (max_age 12) 
        (price 17.99) (gender any))
  
  (gift (name "Crystal Growing Lab") 
        (type physical) 
        (category "science_kit") 
        (min_age 8) (max_age 14) 
        (price 21.99) (gender any))
  
  (gift (name "Dinosaur Fossil Dig Kit") 
        (type physical) 
        (category "science_kit") 
        (min_age 5) (max_age 10) 
        (price 16.99) (gender any))
  
  (gift (name "Chemistry Set Junior") 
        (type physical) 
        (category "science_kit") 
        (min_age 10) (max_age 16) 
        (price 42.99) (gender any))
  
  (gift (name "Telescope for Beginners") 
        (type physical) 
        (category "science_kit") 
        (min_age 8) (max_age 16) 
        (price 55.99) (gender any))
  
  ; Experience Gifts - Science
  (gift (name "Children's Science Museum Visit") 
        (type experience) 
        (category "science_kit") 
        (min_age 5) (max_age 16) 
        (price 15.00) (gender any))
  
  (gift (name "Zoo Keeper for a Day") 
        (type experience) 
        (category "science_kit") 
        (min_age 8) (max_age 16) 
        (price 65.00) (gender any))
  
  ; ==========================================
  ; ATHLETIC & SPORTS
  ; ==========================================
  
  ; Physical Gifts - Athletic
  (gift (name "Junior Soccer Goal Set") 
        (type physical) 
        (category "athletic") 
        (min_age 4) (max_age 12) 
        (price 32.99) (gender any))
  
  (gift (name "Adjustable Basketball Hoop") 
        (type physical) 
        (category "athletic") 
        (min_age 5) (max_age 15) 
        (price 45.99) (gender any))
  
  (gift (name "Swimming Kickboard and Goggles Set") 
        (type physical) 
        (category "athletic") 
        (min_age 3) (max_age 12) 
        (price 19.99) (gender any))
  
  (gift (name "Kids Yoga Mat and Cards Set") 
        (type physical) 
        (category "athletic") 
        (min_age 4) (max_age 12) 
        (price 24.99) (gender any))
  
  (gift (name "Skateboard with Safety Gear") 
        (type physical) 
        (category "athletic") 
        (min_age 8) (max_age 16) 
        (price 49.99) (gender any))
  
  ; Activity Gifts - Athletic
  (gift (name "Family Bowling Night Package") 
        (type activity) 
        (category "athletic") 
        (min_age 4) (max_age 99) 
        (price 40.00) (gender any))
  
  (gift (name "Kids Rock Climbing Adventure") 
        (type activity) 
        (category "athletic") 
        (min_age 6) (max_age 16) 
        (price 35.00) (gender any))
  
  (gift (name "Swimming Lessons Package") 
        (type activity) 
        (category "athletic") 
        (min_age 3) (max_age 14) 
        (price 55.00) (gender any))
  
  (gift (name "Gymnastics Trial Classes") 
        (type activity) 
        (category "athletic") 
        (min_age 3) (max_age 12) 
        (price 30.00) (gender any))
  
  ; Experience Gifts - Athletic
  (gift (name "Professional Sports Game Tickets") 
        (type experience) 
        (category "athletic") 
        (min_age 6) (max_age 18) 
        (price 50.00) (gender any))
  
  ; ==========================================
  ; MUSICAL
  ; ==========================================
  
  ; Physical Gifts - Musical
  (gift (name "Ukulele Starter Kit") 
        (type physical) 
        (category "musical") 
        (min_age 5) (max_age 15) 
        (price 28.99) (gender any))
  
  (gift (name "Electronic Keyboard Piano") 
        (type physical) 
        (category "musical") 
        (min_age 6) (max_age 16) 
        (price 55.99) (gender any))
  
  (gift (name "Percussion Instrument Set") 
        (type physical) 
        (category "musical") 
        (min_age 2) (max_age 7) 
        (price 22.99) (gender any))
  
  (gift (name "Karaoke Machine for Kids") 
        (type physical) 
        (category "musical") 
        (min_age 5) (max_age 14) 
        (price 42.99) (gender any))
  
  ; Experience Gifts - Musical
  (gift (name "Music Concert for Kids") 
        (type experience) 
        (category "musical") 
        (min_age 5) (max_age 16) 
        (price 35.00) (gender any))
  
  (gift (name "Music Lessons Trial Month") 
        (type experience) 
        (category "musical") 
        (min_age 5) (max_age 18) 
        (price 40.00) (gender any))
  
  ; ==========================================
  ; BOARD GAMES
  ; ==========================================
  
  ; Physical Gifts - Board Games
  (gift (name "Strategy Board Game Collection") 
        (type physical) 
        (category "board_games") 
        (min_age 8) (max_age 16) 
        (price 34.99) (gender any))
  
  (gift (name "Family Card Games Set") 
        (type physical) 
        (category "board_games") 
        (min_age 4) (max_age 99) 
        (price 15.99) (gender any))
  
  (gift (name "Chess Set for Kids") 
        (type physical) 
        (category "board_games") 
        (min_age 6) (max_age 16) 
        (price 19.99) (gender any))
  
  (gift (name "Escape Room Puzzle Game") 
        (type physical) 
        (category "board_games") 
        (min_age 10) (max_age 18) 
        (price 27.99) (gender any))
  
  ; Experience Gifts - Board Games
  (gift (name "Board Game Cafe Visit") 
        (type experience) 
        (category "board_games") 
        (min_age 8) (max_age 18) 
        (price 20.00) (gender any))
  
  ; ==========================================
  ; EDUCATIONAL
  ; ==========================================
  
  ; Physical Gifts - Educational
  (gift (name "World Map Puzzle 200pc") 
        (type physical) 
        (category "educational") 
        (min_age 5) (max_age 12) 
        (price 16.99) (gender any))
  
  (gift (name "Math Games Learning Kit") 
        (type physical) 
        (category "educational") 
        (min_age 4) (max_age 9) 
        (price 23.99) (gender any))
  
  (gift (name "Language Learning Flashcards") 
        (type physical) 
        (category "educational") 
        (min_age 3) (max_age 10) 
        (price 13.99) (gender any))
  
  ; Experience Gifts - Educational
  (gift (name "Historical Museum Tour") 
        (type experience) 
        (category "educational") 
        (min_age 7) (max_age 16) 
        (price 12.00) (gender any))
  
  ; ==========================================
  ; OUTDOOR & NATURE
  ; ==========================================
  
  ; Physical Gifts - Outdoor
  (gift (name "Butterfly Growing Kit") 
        (type physical) 
        (category "outdoor") 
        (min_age 4) (max_age 10) 
        (price 18.99) (gender any))
  
  (gift (name "Kids Gardening Tool Set") 
        (type physical) 
        (category "outdoor") 
        (min_age 4) (max_age 12) 
        (price 26.99) (gender any))
  
  (gift (name "Binoculars and Nature Explorer Kit") 
        (type physical) 
        (category "outdoor") 
        (min_age 5) (max_age 14) 
        (price 31.99) (gender any))
  
  ; Activity Gifts - Outdoor
  (gift (name "Outdoor Treasure Hunt Adventure") 
        (type activity) 
        (category "outdoor") 
        (min_age 5) (max_age 12) 
        (price 12.99) (gender any))
  
  (gift (name "Beach Day Fun Package") 
        (type activity) 
        (category "outdoor") 
        (min_age 3) (max_age 99) 
        (price 8.00) (gender any))
  
  (gift (name "Camping Trip Adventure") 
        (type activity) 
        (category "outdoor") 
        (min_age 5) (max_age 18) 
        (price 45.00) (gender any))
  
  (gift (name "Horseback Riding Lesson") 
        (type activity) 
        (category "outdoor") 
        (min_age 6) (max_age 16) 
        (price 48.00) (gender any))
  
  ; Experience Gifts - Outdoor
  (gift (name "Aquarium Visit Tickets") 
        (type experience) 
        (category "outdoor") 
        (min_age 3) (max_age 16) 
        (price 22.00) (gender any))
  
  (gift (name "Botanical Garden Family Pass") 
        (type experience) 
        (category "outdoor") 
        (min_age 3) (max_age 18) 
        (price 18.00) (gender any))
  
  ; ==========================================
  ; ADDITIONAL INTEREST MAPPINGS
  ; ==========================================
  
  ; Adding more variety to the experience/activity types
  (gift (name "Cooking Class for Kids") 
        (type experience) 
        (category "educational") 
        (min_age 6) (max_age 16) 
        (price 38.00) (gender any))
  
  (gift (name "Magic Show Tickets") 
        (type experience) 
        (category "board_games") 
        (min_age 5) (max_age 14) 
        (price 25.00) (gender any))
  
  (gift (name "Ice Skating Pass") 
        (type activity) 
        (category "athletic") 
        (min_age 4) (max_age 16) 
        (price 20.00) (gender any))
  
  (gift (name "Trampoline Park Pass") 
        (type activity) 
        (category "athletic") 
        (min_age 3) (max_age 15) 
        (price 18.00) (gender any))
)