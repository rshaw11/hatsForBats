# Hats For Bats

Excel Data:

(0)Date, (1)Team 1, (2)Team 2, (3)elo1_pre, (4)elo2_pre, (5)eloPreDiff, (6)elo_prob1, (7)elo_prob2, (8)eloProbDiff, (9)binaryEloProb1, (10)binaryEloProb2, (11)elo1_post, (12)elo2_post, (13)eloPostDiff, (14)rating1_pre, (15)rating2_pre, (16) ratingPreDiff, (17) pitcher1, (18) pitcher2, (19) pitcher1_rgs, (20)pitcher2_rgs, (21)pitcher1_adj, (22) pitcher2_adj, (23)rating_prob1, (23) rating_prob2, (24) ratingProbDiff, (25)binaryRatingProb1, (26)binaryRatingProb2, (27) rating1_post, (28) rating2_post, (29) ratingPostDiff, (30)score1, (31)score2, (32)result1, (33)result2 

 (0). date in mm/dd/yyyy  
 (1). Abbreviation for home team  
 (2). Abbreviation for away team  
 (3). Home team's Elo rating before the game  
 (4). Away team's Elo rating before the game  
 (5). =abs(elo1_pre(x)-elo2_pre(x))  
 (6). Home team's probability of winning according to Elo ratings  
 (7). Away team's probability of winning according to Elo ratings    
 (8). =abs(elo_prob1(x)-elo_prob1(x))  
 (9). =IF(elo_prob1(x)>elo_prob2(x),1,0)*  
(10). =IF(elo_prob1(x)<elo_prob2(x),1,0)*  
(11). Home team's Elo rating after the game  
(12). Away team's Elo rating after the game  
(13). =abs(elo1_post(x)-elo2_post(x))  
(14). Home team's rating before the game  
(15). Away team's rating before the game  
(16). =abs(rating1_pre(x)-rating2_pre(x))  
(17). Name of home starting pitcher  
(18). Name of away starting pitcher  
(19). Home starting pitcher's rolling game score before the game  
(20). Away starting pitcher's rolling game score before the game  
(21). Home starting pitcher's adjustment to their team's rating  
(22). Away starting pitcher's adjustment to their team's rating  
(23). Home team's probability of winning according to team ratings and starting pitchers  
(24). Away team's probability of winning according to team ratings and starting pitchers  
(25). =IF(rating_prob1(x)>rating_prob2(x),1,0)*  
(26). =IF(rating_prob1(x)<rating_prob2(x),1,0)*  
(27). Home team's rating after the game  
(28). Away team's rating after the game  
(29). =abs(rating1_post(x)-rating2_post(x))  
(30). Home team's score  
(31). Away team's score  
(32). =IF(score1(x)>score2(x),1,0)*  
(33). =IF(score1(x)<score2(x),1,0)*  

* Turns the larger number into a 1 and smaller into a 0. Useful for counters (hint...hint)

Ideas for new catagories:

eloX_pre and ratingX_pre trendlines (per team? per something else? both?): derivative?, pattern recognition?, etc

(eloProb vs ratingProb) compare 1,1 to 1,0 to 0,1 to 0,0

