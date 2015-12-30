#' Problem 1
#'
#' If we list all the natural numbers below 10 that are multiples of 3
#' or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#'
#' Find the sum of all the multiples of 3 or 5 below 1000.

library(magrittr)
start <- Sys.time()

ans <-
  1:999 %>%
  .[. %% 3 == 0 | . %% 5 == 0] %>%
  sum()

end <- Sys.time()
paste('The answer to Problem 1 is:', ans,
      '\n<< Returned in', end - start, 'seconds >>') %>%
  cat()
