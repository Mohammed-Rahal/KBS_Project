; ============================================
; GIFT RECOMMENDATION RULES WITH SCORING
; ============================================

; Rule 1: Match user interests to gift categories
(defrule match-interests-to-categories
  (user-query (interests $?interests))
  (interest-mapping (interest ?interest) (category ?category))
  (test (member$ ?interest ?interests))
  =>
  (assert (matching-category ?category))
)

; Rule 2: Count how many interests map to each category
(defrule count-category-matches
  (user-query (interests $?interests))
  (matching-category ?category)
  =>
  (bind ?count 0)
  (do-for-all-facts ((?im interest-mapping)) 
    (and (eq ?im:category ?category)
         (member$ ?im:interest ?interests))
    (bind ?count (+ ?count 1))
  )
  (assert (category-match-count (category ?category) (count ?count)))
)

; Rule 3: Find and score matching gifts
(defrule find-and-score-matching-gifts
  ; Get user query details
  (user-query (age ?age) 
              (budget ?budget) 
              (gender ?gender) 
              (gift_type ?gift_type))
  
  ; Get category match count
  (category-match-count (category ?category) (count ?interest_count))
  
  ; Find gifts that match
  (gift (name ?name) 
        (type ?type)
        (category ?category)
        (min_age ?min) 
        (max_age ?max) 
        (price ?price&:(<= ?price ?budget))
        (gender ?gift_gender))
  
  ; Apply all constraints
  (test (and (>= ?age ?min)
             (<= ?age ?max)
             (or (eq ?gift_type any) (eq ?type ?gift_type))
             (or (eq ?gender any) (eq ?gift_gender any) (eq ?gender ?gift_gender))))
  =>
  ; Calculate score components
  ; 1. Interest match score (0-30 points)
  (bind ?interest_score (* ?interest_count 10))
  
  ; 2. Age appropriateness score (0-30 points)
  ; Perfect score if age is in middle 50% of range
  (bind ?age_range (- ?max ?min))
  (bind ?age_middle (+ ?min (/ ?age_range 2)))
  (bind ?age_distance (abs (- ?age ?age_middle)))
  (bind ?age_score (max 0 (- 30 (* ?age_distance 3))))
  
  ; 3. Budget efficiency score (0-25 points)
  ; Higher score for better value (further under budget)
  (bind ?budget_ratio (/ ?price ?budget))
  (bind ?budget_score (integer (- 25 (* ?budget_ratio 25))))
  
  ; 4. Type match bonus (0-15 points)
  (bind ?type_score 0)
  (if (eq ?gift_type any) 
    then (bind ?type_score 10)
    else (if (eq ?type ?gift_type) 
      then (bind ?type_score 15)
    )
  )
  
  ; Calculate total score
  (bind ?total_score (+ ?interest_score ?age_score ?budget_score ?type_score))
  
  ; Assert matching gift with score
  (assert (matching-gift (name ?name) 
                        (type ?type) 
                        (category ?category) 
                        (price ?price)
                        (score ?total_score)))
  
  (printout t "✅ " ?name " - Score: " ?total_score)
  (printout t " (Interest:" ?interest_score " Age:" ?age_score)
  (printout t " Budget:" ?budget_score " Type:" ?type_score ")" crlf)
)

; Rule 4: Clean up intermediate facts (fixed syntax)
(defrule cleanup-categories
  (declare (salience -10))
  ?f <- (matching-category ?)
  =>
  (retract ?f)
)

(defrule cleanup-counts
  (declare (salience -10))
  ?f <- (category-match-count (category ?) (count ?))
  =>
  (retract ?f)
)