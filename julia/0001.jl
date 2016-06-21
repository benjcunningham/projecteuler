# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3
# or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

start = Dates.now()

ans = sum(filter(x -> (x % 3 == 0 || x % 5 == 0), 1:999))

finish = Dates.now()

println("The answer to Problem 1 is: $ans")
println("<< Returned in $(finish - start) milliseconds >>")
