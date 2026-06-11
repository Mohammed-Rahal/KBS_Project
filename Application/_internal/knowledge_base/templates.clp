; Base gift template
(deftemplate gift
  (slot name (type STRING))
  (slot type (type SYMBOL) (allowed-symbols physical experience activity))
  (slot category (type STRING))
  (slot min_age (type INTEGER))
  (slot max_age (type INTEGER))
  (slot price (type FLOAT))
  (slot gender (type SYMBOL) (allowed-symbols male female any))
)

; Interest to category mapping
(deftemplate interest-mapping
  (slot interest (type STRING))
  (slot category (type STRING))
)

; User query template
(deftemplate user-query
  (slot age (type INTEGER))
  (slot budget (type FLOAT))
  (slot gender (type SYMBOL) (allowed-symbols male female any))
  (slot gift_type (type SYMBOL) (allowed-symbols physical experience activity any))
  (multislot interests (type STRING))
)

; Result template - now with score
(deftemplate matching-gift
  (slot name (type STRING))
  (slot type (type SYMBOL))
  (slot category (type STRING))
  (slot price (type FLOAT))
  (slot score (type INTEGER))
)

; Template to count interest matches per category
(deftemplate category-match-count
  (slot category (type STRING))
  (slot count (type INTEGER))
)