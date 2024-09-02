main :: IO ()
main = do
    data <- readFile "input.txt"
    writeFile "output.txt" data
