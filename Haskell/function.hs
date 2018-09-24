module Function where

    import Data.List
    import Data.Maybe
    
    binary_search :: [Int] -> Int -> Int -> Int --list, item, offset, returns an int
    binary_search list item offset
        | length list == 1 && list!!0 /= item   = (-1) --if length is 1 & it's not the item, it was not found
        | item == list!!mid                     = mid + offset --if item is at mid, return mid + offset
        | item > list!!mid                      = binary_search (drop mid list) item offset+mid --if item is above mid, return right side of list
        | otherwise                             = binary_search (take mid list) item offset --if item is below mid, return left side of list
        where
            mid = (length list) `div` 2


    split_char :: String -> Char -> [String] --Passing in a string, char, and returning a list of strings
    split_char (string:strings) char
        | string == char    = "" : remaining
        | otherwise         = (string : head remaining) : tail remaining -- I don't know if I'm allowed to use head and tail, but drop and take were giving errors
        where
            remaining = split_char strings char
